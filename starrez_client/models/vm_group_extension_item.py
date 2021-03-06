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


class VMGroupExtensionItem(object):
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
        'vm_group_extension_id': 'int',
        'vm_group_id': 'int',
        'extension_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'vm_group_extension_id': 'VMGroupExtensionID',
        'vm_group_id': 'VMGroupID',
        'extension_id': 'ExtensionID',
        'date_modified': 'DateModified'
    }

    def __init__(self, vm_group_extension_id=None, vm_group_id=None, extension_id=None, date_modified=None):  # noqa: E501
        """VMGroupExtensionItem - a model defined in Swagger"""  # noqa: E501

        self._vm_group_extension_id = None
        self._vm_group_id = None
        self._extension_id = None
        self._date_modified = None
        self.discriminator = None

        if vm_group_extension_id is not None:
            self.vm_group_extension_id = vm_group_extension_id
        if vm_group_id is not None:
            self.vm_group_id = vm_group_id
        if extension_id is not None:
            self.extension_id = extension_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def vm_group_extension_id(self):
        """Gets the vm_group_extension_id of this VMGroupExtensionItem.  # noqa: E501

        VM Group Extension  # noqa: E501

        :return: The vm_group_extension_id of this VMGroupExtensionItem.  # noqa: E501
        :rtype: int
        """
        return self._vm_group_extension_id

    @vm_group_extension_id.setter
    def vm_group_extension_id(self, vm_group_extension_id):
        """Sets the vm_group_extension_id of this VMGroupExtensionItem.

        VM Group Extension  # noqa: E501

        :param vm_group_extension_id: The vm_group_extension_id of this VMGroupExtensionItem.  # noqa: E501
        :type: int
        """

        self._vm_group_extension_id = vm_group_extension_id

    @property
    def vm_group_id(self):
        """Gets the vm_group_id of this VMGroupExtensionItem.  # noqa: E501

        VM Group  # noqa: E501

        :return: The vm_group_id of this VMGroupExtensionItem.  # noqa: E501
        :rtype: int
        """
        return self._vm_group_id

    @vm_group_id.setter
    def vm_group_id(self, vm_group_id):
        """Sets the vm_group_id of this VMGroupExtensionItem.

        VM Group  # noqa: E501

        :param vm_group_id: The vm_group_id of this VMGroupExtensionItem.  # noqa: E501
        :type: int
        """

        self._vm_group_id = vm_group_id

    @property
    def extension_id(self):
        """Gets the extension_id of this VMGroupExtensionItem.  # noqa: E501

        Extension  # noqa: E501

        :return: The extension_id of this VMGroupExtensionItem.  # noqa: E501
        :rtype: int
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this VMGroupExtensionItem.

        Extension  # noqa: E501

        :param extension_id: The extension_id of this VMGroupExtensionItem.  # noqa: E501
        :type: int
        """

        self._extension_id = extension_id

    @property
    def date_modified(self):
        """Gets the date_modified of this VMGroupExtensionItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this VMGroupExtensionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this VMGroupExtensionItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this VMGroupExtensionItem.  # noqa: E501
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
        if not isinstance(other, VMGroupExtensionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
