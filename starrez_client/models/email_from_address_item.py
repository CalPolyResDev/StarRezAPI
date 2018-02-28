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


class EmailFromAddressItem(object):
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
        'email_from_address_id': 'int',
        'description': 'str',
        'from_address': 'str',
        'from_name': 'str',
        'smtp_username': 'str',
        'module': 'str',
        'comments': 'str',
        'record_type_enum': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'email_from_address_id': 'EmailFromAddressID',
        'description': 'Description',
        'from_address': 'FromAddress',
        'from_name': 'FromName',
        'smtp_username': 'SmtpUsername',
        'module': 'Module',
        'comments': 'Comments',
        'record_type_enum': 'RecordTypeEnum',
        'date_modified': 'DateModified'
    }

    def __init__(self, email_from_address_id=None, description=None, from_address=None, from_name=None, smtp_username=None, module=None, comments=None, record_type_enum=None, date_modified=None):  # noqa: E501
        """EmailFromAddressItem - a model defined in Swagger"""  # noqa: E501

        self._email_from_address_id = None
        self._description = None
        self._from_address = None
        self._from_name = None
        self._smtp_username = None
        self._module = None
        self._comments = None
        self._record_type_enum = None
        self._date_modified = None
        self.discriminator = None

        if email_from_address_id is not None:
            self.email_from_address_id = email_from_address_id
        if description is not None:
            self.description = description
        if from_address is not None:
            self.from_address = from_address
        if from_name is not None:
            self.from_name = from_name
        if smtp_username is not None:
            self.smtp_username = smtp_username
        if module is not None:
            self.module = module
        if comments is not None:
            self.comments = comments
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def email_from_address_id(self):
        """Gets the email_from_address_id of this EmailFromAddressItem.  # noqa: E501

        Email From Address  # noqa: E501

        :return: The email_from_address_id of this EmailFromAddressItem.  # noqa: E501
        :rtype: int
        """
        return self._email_from_address_id

    @email_from_address_id.setter
    def email_from_address_id(self, email_from_address_id):
        """Sets the email_from_address_id of this EmailFromAddressItem.

        Email From Address  # noqa: E501

        :param email_from_address_id: The email_from_address_id of this EmailFromAddressItem.  # noqa: E501
        :type: int
        """

        self._email_from_address_id = email_from_address_id

    @property
    def description(self):
        """Gets the description of this EmailFromAddressItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this EmailFromAddressItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EmailFromAddressItem.

        Description  # noqa: E501

        :param description: The description of this EmailFromAddressItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def from_address(self):
        """Gets the from_address of this EmailFromAddressItem.  # noqa: E501

        From Address  # noqa: E501

        :return: The from_address of this EmailFromAddressItem.  # noqa: E501
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this EmailFromAddressItem.

        From Address  # noqa: E501

        :param from_address: The from_address of this EmailFromAddressItem.  # noqa: E501
        :type: str
        """
        if from_address is not None and len(from_address) > 200:
            raise ValueError("Invalid value for `from_address`, length must be less than or equal to `200`")  # noqa: E501

        self._from_address = from_address

    @property
    def from_name(self):
        """Gets the from_name of this EmailFromAddressItem.  # noqa: E501

        From Name  # noqa: E501

        :return: The from_name of this EmailFromAddressItem.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this EmailFromAddressItem.

        From Name  # noqa: E501

        :param from_name: The from_name of this EmailFromAddressItem.  # noqa: E501
        :type: str
        """
        if from_name is not None and len(from_name) > 200:
            raise ValueError("Invalid value for `from_name`, length must be less than or equal to `200`")  # noqa: E501

        self._from_name = from_name

    @property
    def smtp_username(self):
        """Gets the smtp_username of this EmailFromAddressItem.  # noqa: E501

        Smtp Username  # noqa: E501

        :return: The smtp_username of this EmailFromAddressItem.  # noqa: E501
        :rtype: str
        """
        return self._smtp_username

    @smtp_username.setter
    def smtp_username(self, smtp_username):
        """Sets the smtp_username of this EmailFromAddressItem.

        Smtp Username  # noqa: E501

        :param smtp_username: The smtp_username of this EmailFromAddressItem.  # noqa: E501
        :type: str
        """
        if smtp_username is not None and len(smtp_username) > 50:
            raise ValueError("Invalid value for `smtp_username`, length must be less than or equal to `50`")  # noqa: E501

        self._smtp_username = smtp_username

    @property
    def module(self):
        """Gets the module of this EmailFromAddressItem.  # noqa: E501

        Module  # noqa: E501

        :return: The module of this EmailFromAddressItem.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this EmailFromAddressItem.

        Module  # noqa: E501

        :param module: The module of this EmailFromAddressItem.  # noqa: E501
        :type: str
        """
        if module is not None and len(module) > 50:
            raise ValueError("Invalid value for `module`, length must be less than or equal to `50`")  # noqa: E501

        self._module = module

    @property
    def comments(self):
        """Gets the comments of this EmailFromAddressItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this EmailFromAddressItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this EmailFromAddressItem.

        Comments  # noqa: E501

        :param comments: The comments of this EmailFromAddressItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 1000:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `1000`")  # noqa: E501

        self._comments = comments

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this EmailFromAddressItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this EmailFromAddressItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this EmailFromAddressItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this EmailFromAddressItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def date_modified(self):
        """Gets the date_modified of this EmailFromAddressItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this EmailFromAddressItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this EmailFromAddressItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this EmailFromAddressItem.  # noqa: E501
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
        if not isinstance(other, EmailFromAddressItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other