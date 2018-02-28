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


class TemplatePermissionItem(object):
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
        'template_permission_id': 'int',
        'template_id': 'int',
        'access_type_enum': 'str',
        'security_group_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'template_permission_id': 'TemplatePermissionID',
        'template_id': 'TemplateID',
        'access_type_enum': 'AccessTypeEnum',
        'security_group_id': 'SecurityGroupID',
        'date_modified': 'DateModified'
    }

    def __init__(self, template_permission_id=None, template_id=None, access_type_enum=None, security_group_id=None, date_modified=None):  # noqa: E501
        """TemplatePermissionItem - a model defined in Swagger"""  # noqa: E501

        self._template_permission_id = None
        self._template_id = None
        self._access_type_enum = None
        self._security_group_id = None
        self._date_modified = None
        self.discriminator = None

        if template_permission_id is not None:
            self.template_permission_id = template_permission_id
        if template_id is not None:
            self.template_id = template_id
        if access_type_enum is not None:
            self.access_type_enum = access_type_enum
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def template_permission_id(self):
        """Gets the template_permission_id of this TemplatePermissionItem.  # noqa: E501

        Template Permission  # noqa: E501

        :return: The template_permission_id of this TemplatePermissionItem.  # noqa: E501
        :rtype: int
        """
        return self._template_permission_id

    @template_permission_id.setter
    def template_permission_id(self, template_permission_id):
        """Sets the template_permission_id of this TemplatePermissionItem.

        Template Permission  # noqa: E501

        :param template_permission_id: The template_permission_id of this TemplatePermissionItem.  # noqa: E501
        :type: int
        """

        self._template_permission_id = template_permission_id

    @property
    def template_id(self):
        """Gets the template_id of this TemplatePermissionItem.  # noqa: E501

        Template  # noqa: E501

        :return: The template_id of this TemplatePermissionItem.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TemplatePermissionItem.

        Template  # noqa: E501

        :param template_id: The template_id of this TemplatePermissionItem.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def access_type_enum(self):
        """Gets the access_type_enum of this TemplatePermissionItem.  # noqa: E501

        Access Type  # noqa: E501

        :return: The access_type_enum of this TemplatePermissionItem.  # noqa: E501
        :rtype: str
        """
        return self._access_type_enum

    @access_type_enum.setter
    def access_type_enum(self, access_type_enum):
        """Sets the access_type_enum of this TemplatePermissionItem.

        Access Type  # noqa: E501

        :param access_type_enum: The access_type_enum of this TemplatePermissionItem.  # noqa: E501
        :type: str
        """

        self._access_type_enum = access_type_enum

    @property
    def security_group_id(self):
        """Gets the security_group_id of this TemplatePermissionItem.  # noqa: E501

        Security Group  # noqa: E501

        :return: The security_group_id of this TemplatePermissionItem.  # noqa: E501
        :rtype: int
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this TemplatePermissionItem.

        Security Group  # noqa: E501

        :param security_group_id: The security_group_id of this TemplatePermissionItem.  # noqa: E501
        :type: int
        """

        self._security_group_id = security_group_id

    @property
    def date_modified(self):
        """Gets the date_modified of this TemplatePermissionItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this TemplatePermissionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this TemplatePermissionItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this TemplatePermissionItem.  # noqa: E501
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
        if not isinstance(other, TemplatePermissionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
