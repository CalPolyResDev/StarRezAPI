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


class SavedListItem(object):
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
        'saved_list_id': 'int',
        'description': 'str',
        'parent_id': 'int',
        'folder': 'bool',
        'comments': 'str',
        'table_name': 'str',
        'security_user_id': 'int',
        'record_type_enum': 'str',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'saved_list_id': 'SavedListID',
        'description': 'Description',
        'parent_id': 'ParentID',
        'folder': 'Folder',
        'comments': 'Comments',
        'table_name': 'TableName',
        'security_user_id': 'SecurityUserID',
        'record_type_enum': 'RecordTypeEnum',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, saved_list_id=None, description=None, parent_id=None, folder=None, comments=None, table_name=None, security_user_id=None, record_type_enum=None, date_created=None, date_modified=None):  # noqa: E501
        """SavedListItem - a model defined in Swagger"""  # noqa: E501

        self._saved_list_id = None
        self._description = None
        self._parent_id = None
        self._folder = None
        self._comments = None
        self._table_name = None
        self._security_user_id = None
        self._record_type_enum = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if saved_list_id is not None:
            self.saved_list_id = saved_list_id
        if description is not None:
            self.description = description
        if parent_id is not None:
            self.parent_id = parent_id
        if folder is not None:
            self.folder = folder
        if comments is not None:
            self.comments = comments
        if table_name is not None:
            self.table_name = table_name
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def saved_list_id(self):
        """Gets the saved_list_id of this SavedListItem.  # noqa: E501

        Saved List  # noqa: E501

        :return: The saved_list_id of this SavedListItem.  # noqa: E501
        :rtype: int
        """
        return self._saved_list_id

    @saved_list_id.setter
    def saved_list_id(self, saved_list_id):
        """Sets the saved_list_id of this SavedListItem.

        Saved List  # noqa: E501

        :param saved_list_id: The saved_list_id of this SavedListItem.  # noqa: E501
        :type: int
        """

        self._saved_list_id = saved_list_id

    @property
    def description(self):
        """Gets the description of this SavedListItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this SavedListItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SavedListItem.

        Description  # noqa: E501

        :param description: The description of this SavedListItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def parent_id(self):
        """Gets the parent_id of this SavedListItem.  # noqa: E501

        Parent  # noqa: E501

        :return: The parent_id of this SavedListItem.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this SavedListItem.

        Parent  # noqa: E501

        :param parent_id: The parent_id of this SavedListItem.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def folder(self):
        """Gets the folder of this SavedListItem.  # noqa: E501

        Folder  # noqa: E501

        :return: The folder of this SavedListItem.  # noqa: E501
        :rtype: bool
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this SavedListItem.

        Folder  # noqa: E501

        :param folder: The folder of this SavedListItem.  # noqa: E501
        :type: bool
        """

        self._folder = folder

    @property
    def comments(self):
        """Gets the comments of this SavedListItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this SavedListItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this SavedListItem.

        Comments  # noqa: E501

        :param comments: The comments of this SavedListItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 250:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `250`")  # noqa: E501

        self._comments = comments

    @property
    def table_name(self):
        """Gets the table_name of this SavedListItem.  # noqa: E501

        Table Name  # noqa: E501

        :return: The table_name of this SavedListItem.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this SavedListItem.

        Table Name  # noqa: E501

        :param table_name: The table_name of this SavedListItem.  # noqa: E501
        :type: str
        """
        if table_name is not None and len(table_name) > 50:
            raise ValueError("Invalid value for `table_name`, length must be less than or equal to `50`")  # noqa: E501

        self._table_name = table_name

    @property
    def security_user_id(self):
        """Gets the security_user_id of this SavedListItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this SavedListItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this SavedListItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this SavedListItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this SavedListItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this SavedListItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this SavedListItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this SavedListItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def date_created(self):
        """Gets the date_created of this SavedListItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this SavedListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SavedListItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this SavedListItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SavedListItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this SavedListItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SavedListItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this SavedListItem.  # noqa: E501
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
        if not isinstance(other, SavedListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
