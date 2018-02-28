# coding: utf-8

"""
    StarRez API

    This is a way to connect with the StarRez API. We are not the developers of the StarRez API, we are just an organization that uses it and wanted a better way to connect to it.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: resdev@calpoly.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NoteTypeItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'note_type_id': 'int',
        'table_name': 'str',
        'description': 'str',
        'comments': 'str',
        'xml_schema': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'note_type_id': 'NoteTypeID',
        'table_name': 'TableName',
        'description': 'Description',
        'comments': 'Comments',
        'xml_schema': 'XMLSchema',
        'date_modified': 'DateModified'
    }

    def __init__(self, note_type_id=None, table_name=None, description=None, comments=None, xml_schema=None, date_modified=None):  # noqa: E501
        """NoteTypeItem - a model defined in Swagger"""  # noqa: E501

        self._note_type_id = None
        self._table_name = None
        self._description = None
        self._comments = None
        self._xml_schema = None
        self._date_modified = None
        self.discriminator = None

        if note_type_id is not None:
            self.note_type_id = note_type_id
        if table_name is not None:
            self.table_name = table_name
        if description is not None:
            self.description = description
        if comments is not None:
            self.comments = comments
        if xml_schema is not None:
            self.xml_schema = xml_schema
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def note_type_id(self):
        """Gets the note_type_id of this NoteTypeItem.  # noqa: E501

        Note Type  # noqa: E501

        :return: The note_type_id of this NoteTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._note_type_id

    @note_type_id.setter
    def note_type_id(self, note_type_id):
        """Sets the note_type_id of this NoteTypeItem.

        Note Type  # noqa: E501

        :param note_type_id: The note_type_id of this NoteTypeItem.  # noqa: E501
        :type: int
        """

        self._note_type_id = note_type_id

    @property
    def table_name(self):
        """Gets the table_name of this NoteTypeItem.  # noqa: E501

        Table Name  # noqa: E501

        :return: The table_name of this NoteTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this NoteTypeItem.

        Table Name  # noqa: E501

        :param table_name: The table_name of this NoteTypeItem.  # noqa: E501
        :type: str
        """
        if table_name is not None and len(table_name) > 100:
            raise ValueError("Invalid value for `table_name`, length must be less than or equal to `100`")  # noqa: E501

        self._table_name = table_name

    @property
    def description(self):
        """Gets the description of this NoteTypeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this NoteTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NoteTypeItem.

        Description  # noqa: E501

        :param description: The description of this NoteTypeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def comments(self):
        """Gets the comments of this NoteTypeItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this NoteTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this NoteTypeItem.

        Comments  # noqa: E501

        :param comments: The comments of this NoteTypeItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 500:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `500`")  # noqa: E501

        self._comments = comments

    @property
    def xml_schema(self):
        """Gets the xml_schema of this NoteTypeItem.  # noqa: E501

        XML Schema  # noqa: E501

        :return: The xml_schema of this NoteTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._xml_schema

    @xml_schema.setter
    def xml_schema(self, xml_schema):
        """Sets the xml_schema of this NoteTypeItem.

        XML Schema  # noqa: E501

        :param xml_schema: The xml_schema of this NoteTypeItem.  # noqa: E501
        :type: str
        """
        if xml_schema is not None and len(xml_schema) > 5000:
            raise ValueError("Invalid value for `xml_schema`, length must be less than or equal to `5000`")  # noqa: E501

        self._xml_schema = xml_schema

    @property
    def date_modified(self):
        """Gets the date_modified of this NoteTypeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this NoteTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this NoteTypeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this NoteTypeItem.  # noqa: E501
        :type: str
        """

        self._date_modified = date_modified

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NoteTypeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
