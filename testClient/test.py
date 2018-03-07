import os
import starrez_client
import xml.etree.ElementTree as ET

from dotenv import find_dotenv, load_dotenv
from starrez_client.rest import ApiException

# In order for this to work a .env file must be in project root
load_dotenv(find_dotenv())

configuration = starrez_client.Configuration()
configuration.username = os.environ.get("USERNAME")
configuration.password = os.environ.get("PASSWORD")
configuration.host = os.environ.get("HOST")
api_instance = starrez_client.DefaultApi(starrez_client.ApiClient(configuration))

entry_id = 51431
name_web = 'test@calpoly.edu'

entry_item = starrez_client.EntryItem()
entry_item.name_web = name_web

# api_instance.update_entry(entry_id, entry_item)
try:
    test = api_instance.search_entry(name_last="Reis")
    # print(test)
except ApiException as e:
    if e.body:
        print(e.body)
    else:
        print(e)

try:
    entry = ET.Element('Entry')
    fname = ET.SubElement(entry, 'NameFirst')
    fname.text = "Kyle"
    lname = ET.SubElement(entry, 'NameLast')
    lname.text = "Reis"
    test = api_instance.search_entry_xml(ET.tostring(entry, encoding="unicode"))
    # print(test)
except ApiException as e:
    if e.body:
        print(e.body)
    else:
        print(e)

try:
    entry_xml = """<Entry>
                        <NameLast>Reis</NameLast>
                        <NameFirst>Kyle</NameFirst>
                   </Entry>"""
    test = api_instance.search_entry_xml(entry_xml)
    # print(test)
except ApiException as e:
    if e.body:
        print(e.body)
    else:
        print(e)

try:
    api_instance.search_entry()
except ApiException as e:
    if e.body:
        print(e.body)
    else:
        print(e)