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


class PortalThemeItem(object):
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
        'portal_theme_id': 'int',
        'description': 'str',
        'theme_layout': 'str',
        'allow_in_url': 'bool',
        'record_type_enum': 'str',
        'date_created': 'datetime',
        'security_user_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'portal_theme_id': 'PortalThemeID',
        'description': 'Description',
        'theme_layout': 'ThemeLayout',
        'allow_in_url': 'AllowInUrl',
        'record_type_enum': 'RecordTypeEnum',
        'date_created': 'DateCreated',
        'security_user_id': 'SecurityUserID',
        'date_modified': 'DateModified'
    }

    def __init__(self, portal_theme_id=None, description=None, theme_layout=None, allow_in_url=None, record_type_enum=None, date_created=None, security_user_id=None, date_modified=None):  # noqa: E501
        """PortalThemeItem - a model defined in Swagger"""  # noqa: E501

        self._portal_theme_id = None
        self._description = None
        self._theme_layout = None
        self._allow_in_url = None
        self._record_type_enum = None
        self._date_created = None
        self._security_user_id = None
        self._date_modified = None
        self.discriminator = None

        if portal_theme_id is not None:
            self.portal_theme_id = portal_theme_id
        if description is not None:
            self.description = description
        if theme_layout is not None:
            self.theme_layout = theme_layout
        if allow_in_url is not None:
            self.allow_in_url = allow_in_url
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if date_created is not None:
            self.date_created = date_created
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def portal_theme_id(self):
        """Gets the portal_theme_id of this PortalThemeItem.  # noqa: E501

        Portal Theme  # noqa: E501

        :return: The portal_theme_id of this PortalThemeItem.  # noqa: E501
        :rtype: int
        """
        return self._portal_theme_id

    @portal_theme_id.setter
    def portal_theme_id(self, portal_theme_id):
        """Sets the portal_theme_id of this PortalThemeItem.

        Portal Theme  # noqa: E501

        :param portal_theme_id: The portal_theme_id of this PortalThemeItem.  # noqa: E501
        :type: int
        """

        self._portal_theme_id = portal_theme_id

    @property
    def description(self):
        """Gets the description of this PortalThemeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this PortalThemeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortalThemeItem.

        Description  # noqa: E501

        :param description: The description of this PortalThemeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def theme_layout(self):
        """Gets the theme_layout of this PortalThemeItem.  # noqa: E501

        Theme Layout  # noqa: E501

        :return: The theme_layout of this PortalThemeItem.  # noqa: E501
        :rtype: str
        """
        return self._theme_layout

    @theme_layout.setter
    def theme_layout(self, theme_layout):
        """Sets the theme_layout of this PortalThemeItem.

        Theme Layout  # noqa: E501

        :param theme_layout: The theme_layout of this PortalThemeItem.  # noqa: E501
        :type: str
        """
        if theme_layout is not None and len(theme_layout) > 50:
            raise ValueError("Invalid value for `theme_layout`, length must be less than or equal to `50`")  # noqa: E501

        self._theme_layout = theme_layout

    @property
    def allow_in_url(self):
        """Gets the allow_in_url of this PortalThemeItem.  # noqa: E501

        Allow In Url  # noqa: E501

        :return: The allow_in_url of this PortalThemeItem.  # noqa: E501
        :rtype: bool
        """
        return self._allow_in_url

    @allow_in_url.setter
    def allow_in_url(self, allow_in_url):
        """Sets the allow_in_url of this PortalThemeItem.

        Allow In Url  # noqa: E501

        :param allow_in_url: The allow_in_url of this PortalThemeItem.  # noqa: E501
        :type: bool
        """

        self._allow_in_url = allow_in_url

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this PortalThemeItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this PortalThemeItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this PortalThemeItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this PortalThemeItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def date_created(self):
        """Gets the date_created of this PortalThemeItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this PortalThemeItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this PortalThemeItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this PortalThemeItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def security_user_id(self):
        """Gets the security_user_id of this PortalThemeItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this PortalThemeItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this PortalThemeItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this PortalThemeItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_modified(self):
        """Gets the date_modified of this PortalThemeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this PortalThemeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this PortalThemeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this PortalThemeItem.  # noqa: E501
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
        if not isinstance(other, PortalThemeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
