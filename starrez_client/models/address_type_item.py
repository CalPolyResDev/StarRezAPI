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


class AddressTypeItem(object):
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
        'address_type_id': 'int',
        'record_type_enum': 'str',
        'description': 'str',
        'is_entry_address': 'bool',
        'comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'address_type_id': 'AddressTypeID',
        'record_type_enum': 'RecordTypeEnum',
        'description': 'Description',
        'is_entry_address': 'IsEntryAddress',
        'comments': 'Comments',
        'date_modified': 'DateModified'
    }

    def __init__(self, address_type_id=None, record_type_enum=None, description=None, is_entry_address=None, comments=None, date_modified=None):  # noqa: E501
        """AddressTypeItem - a model defined in Swagger"""  # noqa: E501

        self._address_type_id = None
        self._record_type_enum = None
        self._description = None
        self._is_entry_address = None
        self._comments = None
        self._date_modified = None
        self.discriminator = None

        if address_type_id is not None:
            self.address_type_id = address_type_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if description is not None:
            self.description = description
        if is_entry_address is not None:
            self.is_entry_address = is_entry_address
        if comments is not None:
            self.comments = comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def address_type_id(self):
        """Gets the address_type_id of this AddressTypeItem.  # noqa: E501

        Address Type  # noqa: E501

        :return: The address_type_id of this AddressTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._address_type_id

    @address_type_id.setter
    def address_type_id(self, address_type_id):
        """Sets the address_type_id of this AddressTypeItem.

        Address Type  # noqa: E501

        :param address_type_id: The address_type_id of this AddressTypeItem.  # noqa: E501
        :type: int
        """

        self._address_type_id = address_type_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this AddressTypeItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this AddressTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this AddressTypeItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this AddressTypeItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def description(self):
        """Gets the description of this AddressTypeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this AddressTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddressTypeItem.

        Description  # noqa: E501

        :param description: The description of this AddressTypeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def is_entry_address(self):
        """Gets the is_entry_address of this AddressTypeItem.  # noqa: E501

        Is Entry Address  # noqa: E501

        :return: The is_entry_address of this AddressTypeItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_entry_address

    @is_entry_address.setter
    def is_entry_address(self, is_entry_address):
        """Sets the is_entry_address of this AddressTypeItem.

        Is Entry Address  # noqa: E501

        :param is_entry_address: The is_entry_address of this AddressTypeItem.  # noqa: E501
        :type: bool
        """

        self._is_entry_address = is_entry_address

    @property
    def comments(self):
        """Gets the comments of this AddressTypeItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this AddressTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this AddressTypeItem.

        Comments  # noqa: E501

        :param comments: The comments of this AddressTypeItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 200:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `200`")  # noqa: E501

        self._comments = comments

    @property
    def date_modified(self):
        """Gets the date_modified of this AddressTypeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this AddressTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this AddressTypeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this AddressTypeItem.  # noqa: E501
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
        if not isinstance(other, AddressTypeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
