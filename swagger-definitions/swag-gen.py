import os
import starrez_client
import xml.etree.ElementTree as ET
from dotenv import find_dotenv, load_dotenv

VALID_TYPES = {"integer": {"type": "integer", "format": "int32"},
               "long": {"type": "integer", "format": "int64"},
               "float": {"type": "number", "format": "float"},
               "double": {"type": "number", "format": "double"},
               "string": {"type": "string", "format": ""},
               "byte": {"type": "string", "format": "byte"},
               "binary": {"type": "string", "format": "binary"},
               "boolean": {"type": "boolean", "format": ""},
               "date": {"type": "string", "format": "date"},
               "datetime": {"type": "string", "format": "date-time"},
               "password": {"type": "string", "format": "password"}}


class Column:
    def __init__(self, name, attr):
        self.name = name
        self.raw_attr = attr
        c_type = attr["type"].lower()
        if "enum" in name.lower():
            self.type = "string"
            self.format = "enum"
        elif c_type in VALID_TYPES:
            self.type = VALID_TYPES[c_type]["type"]
            self.format = VALID_TYPES[c_type]["format"]
        else:
            self.type = "string"
            self.format = attr["type"].lower()
        self.desc = attr["friendlyName"]
        self.req = attr["required"] == "true"
        self.null = attr["allowNull"] == "true"
        self.size = int(attr["size"])


class Table:
    def __init__(self, name):
        self.name = name
        self.columns = []

    def addColumn(self, column):
        self.columns.append(column)


def init():
    # In order for this to work a .env file must be in project root
    load_dotenv(find_dotenv())

    configuration = starrez_client.Configuration()
    configuration.username = os.environ.get("USERNAME")
    configuration.password = os.environ.get("PASSWORD")
    configuration.host = os.environ.get("HOST")
    api_instance = starrez_client.DefaultApi(starrez_client.ApiClient(configuration))
    return api_instance


def getTables(api_instance):
    name_spaces = ['{http://www.w3.org/2005/Atom}entry',
                   '{http://www.w3.org/2005/Atom}content',
                   '{http://www.w3.org/2005/Atom}Tables']
    table_list = []

    response = api_instance.get_tables()
    root = ET.fromstring(response)

    element = root.findall(name_spaces[0])[0]
    element = element.findall(name_spaces[1])[0]
    element = element.findall(name_spaces[2])[0]
    tables = element.findall('./')

    for table in tables:
        table_name = table.tag.split('}')[1]
        tab = Table(table_name)
        table_list.append(tab)

    return table_list


def getTableInfo(api_instance, table):
    name_spaces = ['{http://www.w3.org/2005/Atom}entry',
                   '{http://www.w3.org/2005/Atom}content',
                   '{http://www.w3.org/2005/Atom}']

    response = api_instance.get_columns(table.name)
    root = ET.fromstring(response)

    element = root.findall(name_spaces[0])[0]
    element = element.findall(name_spaces[1])[0]
    element = element.findall(name_spaces[2] + table.name)[0]
    columns = element.findall('./')

    for column in columns:
        column_name = column.tag.split('}')[1]
        column_attr = column.attrib
        col = Column(column_name, column_attr)
        table.addColumn(col)


def checkFileLock(file_path):
    try:
        # Checks if the file is flagged as being locked for editing
        f = open(file_path, "r")
        if f.readline().strip().lower() == "# locked":
            f.close()
            return True
        f.close()
        return False
    except:
        # File doesn't exist, so it can't be locked
        return False


def cleanIndex(index_path):
    f = open(index_path, "r+")
    lines = f.readlines()
    manualItems = ""
    for line in lines:
        
        if line.strip() == "# Generated":
            manualItems += line.strip() + "\n"
            break
        else:
            manualItems += line
    f = open(index_path, "w+")
    f.write(manualItems)
    f.close()


def registerPath(table_name, reqType):
    f = open("./paths/index.yaml", "a")
    if reqType == "update":
        f.write("update/" + table_name + "/{" + table_name + "ID}:\n")
    else:
        f.write(reqType + "/" + table_name + ":\n")
    f.write("  $ref: ./" + reqType + "/" + table_name.lower() + ".yaml\n")
    f.close()


def registerDef(def_name):
    f = open("./definitions/index.yaml", "a")
    f.write(def_name + ":\n")
    f.write("  $ref: " + def_name + ".yaml\n")
    f.close()


def writeDefinition(table):
    def_name = table.name + "Item"
    file_path = "./definitions/" + def_name + ".yaml"
    if not checkFileLock(file_path):
        f = open(file_path, "w+")
        f.write("type: object\n")
        f.write("#required:\n")
        for col in table.columns:
            if col.req:
                f.write("#  - " + col.name + "\n")
        f.write("properties:\n")
        for col in table.columns:
            if "password" not in col.name.lower():
                f.write("  " + col.name + ":\n")
                f.write("    type: " + col.type + "\n")
                if col.format != "" and not col.null:
                    f.write("    format: " + col.format + "\n")
                if col.size > 0 and col.type == "string":
                    f.write("    maxLength: " + str(col.size) + "\n")
                f.write("    description: " + col.desc + "\n")
        f.close()
    registerDef(def_name)


# Currently the reqType is either select (GET) or update (POST)
def writePaths(table, reqType):
    name = table.name
    file_path = "./paths/" + reqType + "/" + name.lower() + ".yaml"
    if not checkFileLock(file_path):
        f = open(file_path, "w+")
        if reqType == "update":
            f.write("post:\n")
        else:
            f.write("get:\n")
        f.write('  summary: ""\n')
        f.write("  operationId: ")
        if reqType == "update":
            f.write("update" + name + "\n")
            f.write("  description: Updates an " + name + " in the system\n")
        else:
            f.write("search" + name + "\n")
            f.write("  description: By passing in the appropriate options, " +
                    "you can search for a " + name + " in the system\n")
        f.write("  consumes:\n")
        f.write("    - application/json\n")
        f.write("    - application/xml\n")
        f.write("  produces:\n")
        f.write("    - application/json\n")

        f.write("  parameters:\n")
        if reqType == "update":
            f.write("    - in: path\n")
            f.write("      name: " + name + "ID\n")
            f.write("      type: integer\n")
            f.write("      required: true\n")
            f.write("      description: Numeric value of the " + name.lower() + "ID\n")
            f.write("    - in: body\n")
            f.write("      name: " + name + "Item\n")
            f.write("      required: true\n")
            f.write("      description: " + name + " to update\n")
            f.write("      schema:\n")
            f.write("        $ref: '#/definitions/" + name + "Item'\n")
        else:
            f.write("    - in: query\n")
            f.write("      name: " + name + "ID\n")
            f.write("      description: ID of the " + name + " you want to look up\n")
            f.write("      required: false\n")
            f.write("      type: integer\n")

        f.write("  responses:\n")
        f.write("    200:\n")
        desc = "Updated Item" if reqType == "update" else "Search results matching criteria."
        f.write("      description: " + desc + "\n")
        f.write("      schema:\n")
        f.write("        type: array\n")
        f.write("        items:\n")
        f.write("          $ref: '#/definitions/" + name + "Item'\n")
        f.write("    400:\n")
        error = "Invalid Input, Object Invalid." if reqType == "update" else "Bad Request"
        f.write("      description: " + error)

        f.close()
    registerPath(name, reqType)


def generateSwagger():
    api_instance = init()
    table_list = getTables(api_instance)
    cleanIndex("./paths/index.yaml")
    cleanIndex("./definitions/index.yaml")
    for table in table_list:
        getTableInfo(api_instance, table)
        writeDefinition(table)
        writePaths(table, "select")
        writePaths(table, "update")

generateSwagger()


def testGen():
    api_instance = init()
    table = Table("Entry")
    cleanIndex("./paths/index.yaml")
    cleanIndex("./definitions/index.yaml")
    getTableInfo(api_instance, table)
    writeDefinition(table)
    writePaths(table, "select")
    writePaths(table, "update")
