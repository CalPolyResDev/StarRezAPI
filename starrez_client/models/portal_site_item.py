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


class PortalSiteItem(object):
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
        'portal_site_id': 'int',
        'description': 'str',
        'title': 'str',
        'url': 'str',
        'portal_theme_id': 'int',
        'record_type_enum': 'str',
        'date_created': 'datetime',
        'security_user_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'portal_site_id': 'PortalSiteID',
        'description': 'Description',
        'title': 'Title',
        'url': 'Url',
        'portal_theme_id': 'PortalThemeID',
        'record_type_enum': 'RecordTypeEnum',
        'date_created': 'DateCreated',
        'security_user_id': 'SecurityUserID',
        'date_modified': 'DateModified'
    }

    def __init__(self, portal_site_id=None, description=None, title=None, url=None, portal_theme_id=None, record_type_enum=None, date_created=None, security_user_id=None, date_modified=None):  # noqa: E501
        """PortalSiteItem - a model defined in Swagger"""  # noqa: E501

        self._portal_site_id = None
        self._description = None
        self._title = None
        self._url = None
        self._portal_theme_id = None
        self._record_type_enum = None
        self._date_created = None
        self._security_user_id = None
        self._date_modified = None
        self.discriminator = None

        if portal_site_id is not None:
            self.portal_site_id = portal_site_id
        if description is not None:
            self.description = description
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if portal_theme_id is not None:
            self.portal_theme_id = portal_theme_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if date_created is not None:
            self.date_created = date_created
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def portal_site_id(self):
        """Gets the portal_site_id of this PortalSiteItem.  # noqa: E501

        Portal Site  # noqa: E501

        :return: The portal_site_id of this PortalSiteItem.  # noqa: E501
        :rtype: int
        """
        return self._portal_site_id

    @portal_site_id.setter
    def portal_site_id(self, portal_site_id):
        """Sets the portal_site_id of this PortalSiteItem.

        Portal Site  # noqa: E501

        :param portal_site_id: The portal_site_id of this PortalSiteItem.  # noqa: E501
        :type: int
        """

        self._portal_site_id = portal_site_id

    @property
    def description(self):
        """Gets the description of this PortalSiteItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this PortalSiteItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortalSiteItem.

        Description  # noqa: E501

        :param description: The description of this PortalSiteItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def title(self):
        """Gets the title of this PortalSiteItem.  # noqa: E501

        Title  # noqa: E501

        :return: The title of this PortalSiteItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PortalSiteItem.

        Title  # noqa: E501

        :param title: The title of this PortalSiteItem.  # noqa: E501
        :type: str
        """
        if title is not None and len(title) > 100:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `100`")  # noqa: E501

        self._title = title

    @property
    def url(self):
        """Gets the url of this PortalSiteItem.  # noqa: E501

        Url  # noqa: E501

        :return: The url of this PortalSiteItem.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PortalSiteItem.

        Url  # noqa: E501

        :param url: The url of this PortalSiteItem.  # noqa: E501
        :type: str
        """
        if url is not None and len(url) > 500:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `500`")  # noqa: E501

        self._url = url

    @property
    def portal_theme_id(self):
        """Gets the portal_theme_id of this PortalSiteItem.  # noqa: E501

        Portal Theme  # noqa: E501

        :return: The portal_theme_id of this PortalSiteItem.  # noqa: E501
        :rtype: int
        """
        return self._portal_theme_id

    @portal_theme_id.setter
    def portal_theme_id(self, portal_theme_id):
        """Sets the portal_theme_id of this PortalSiteItem.

        Portal Theme  # noqa: E501

        :param portal_theme_id: The portal_theme_id of this PortalSiteItem.  # noqa: E501
        :type: int
        """

        self._portal_theme_id = portal_theme_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this PortalSiteItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this PortalSiteItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this PortalSiteItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this PortalSiteItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def date_created(self):
        """Gets the date_created of this PortalSiteItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this PortalSiteItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this PortalSiteItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this PortalSiteItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def security_user_id(self):
        """Gets the security_user_id of this PortalSiteItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this PortalSiteItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this PortalSiteItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this PortalSiteItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_modified(self):
        """Gets the date_modified of this PortalSiteItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this PortalSiteItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this PortalSiteItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this PortalSiteItem.  # noqa: E501
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
        if not isinstance(other, PortalSiteItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other