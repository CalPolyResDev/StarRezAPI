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


class PortalActivityItem(object):
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
        'portal_activity_id': 'int',
        'portal_site_id': 'int',
        'web_server_name': 'str',
        'date_created': 'datetime',
        'logged_in_users': 'int',
        'active_users': 'int',
        'total_portal_activity_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'portal_activity_id': 'PortalActivityID',
        'portal_site_id': 'PortalSiteID',
        'web_server_name': 'WebServerName',
        'date_created': 'DateCreated',
        'logged_in_users': 'LoggedInUsers',
        'active_users': 'ActiveUsers',
        'total_portal_activity_id': 'Total_PortalActivityID',
        'date_modified': 'DateModified'
    }

    def __init__(self, portal_activity_id=None, portal_site_id=None, web_server_name=None, date_created=None, logged_in_users=None, active_users=None, total_portal_activity_id=None, date_modified=None):  # noqa: E501
        """PortalActivityItem - a model defined in Swagger"""  # noqa: E501

        self._portal_activity_id = None
        self._portal_site_id = None
        self._web_server_name = None
        self._date_created = None
        self._logged_in_users = None
        self._active_users = None
        self._total_portal_activity_id = None
        self._date_modified = None
        self.discriminator = None

        if portal_activity_id is not None:
            self.portal_activity_id = portal_activity_id
        if portal_site_id is not None:
            self.portal_site_id = portal_site_id
        if web_server_name is not None:
            self.web_server_name = web_server_name
        if date_created is not None:
            self.date_created = date_created
        if logged_in_users is not None:
            self.logged_in_users = logged_in_users
        if active_users is not None:
            self.active_users = active_users
        if total_portal_activity_id is not None:
            self.total_portal_activity_id = total_portal_activity_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def portal_activity_id(self):
        """Gets the portal_activity_id of this PortalActivityItem.  # noqa: E501

        Portal Activity  # noqa: E501

        :return: The portal_activity_id of this PortalActivityItem.  # noqa: E501
        :rtype: int
        """
        return self._portal_activity_id

    @portal_activity_id.setter
    def portal_activity_id(self, portal_activity_id):
        """Sets the portal_activity_id of this PortalActivityItem.

        Portal Activity  # noqa: E501

        :param portal_activity_id: The portal_activity_id of this PortalActivityItem.  # noqa: E501
        :type: int
        """

        self._portal_activity_id = portal_activity_id

    @property
    def portal_site_id(self):
        """Gets the portal_site_id of this PortalActivityItem.  # noqa: E501

        Portal Site  # noqa: E501

        :return: The portal_site_id of this PortalActivityItem.  # noqa: E501
        :rtype: int
        """
        return self._portal_site_id

    @portal_site_id.setter
    def portal_site_id(self, portal_site_id):
        """Sets the portal_site_id of this PortalActivityItem.

        Portal Site  # noqa: E501

        :param portal_site_id: The portal_site_id of this PortalActivityItem.  # noqa: E501
        :type: int
        """

        self._portal_site_id = portal_site_id

    @property
    def web_server_name(self):
        """Gets the web_server_name of this PortalActivityItem.  # noqa: E501

        Web Server Name  # noqa: E501

        :return: The web_server_name of this PortalActivityItem.  # noqa: E501
        :rtype: str
        """
        return self._web_server_name

    @web_server_name.setter
    def web_server_name(self, web_server_name):
        """Sets the web_server_name of this PortalActivityItem.

        Web Server Name  # noqa: E501

        :param web_server_name: The web_server_name of this PortalActivityItem.  # noqa: E501
        :type: str
        """
        if web_server_name is not None and len(web_server_name) > 250:
            raise ValueError("Invalid value for `web_server_name`, length must be less than or equal to `250`")  # noqa: E501

        self._web_server_name = web_server_name

    @property
    def date_created(self):
        """Gets the date_created of this PortalActivityItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this PortalActivityItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this PortalActivityItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this PortalActivityItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def logged_in_users(self):
        """Gets the logged_in_users of this PortalActivityItem.  # noqa: E501

        Logged In Users  # noqa: E501

        :return: The logged_in_users of this PortalActivityItem.  # noqa: E501
        :rtype: int
        """
        return self._logged_in_users

    @logged_in_users.setter
    def logged_in_users(self, logged_in_users):
        """Sets the logged_in_users of this PortalActivityItem.

        Logged In Users  # noqa: E501

        :param logged_in_users: The logged_in_users of this PortalActivityItem.  # noqa: E501
        :type: int
        """

        self._logged_in_users = logged_in_users

    @property
    def active_users(self):
        """Gets the active_users of this PortalActivityItem.  # noqa: E501

        Active Users  # noqa: E501

        :return: The active_users of this PortalActivityItem.  # noqa: E501
        :rtype: int
        """
        return self._active_users

    @active_users.setter
    def active_users(self, active_users):
        """Sets the active_users of this PortalActivityItem.

        Active Users  # noqa: E501

        :param active_users: The active_users of this PortalActivityItem.  # noqa: E501
        :type: int
        """

        self._active_users = active_users

    @property
    def total_portal_activity_id(self):
        """Gets the total_portal_activity_id of this PortalActivityItem.  # noqa: E501

        Total Portal Activity  # noqa: E501

        :return: The total_portal_activity_id of this PortalActivityItem.  # noqa: E501
        :rtype: int
        """
        return self._total_portal_activity_id

    @total_portal_activity_id.setter
    def total_portal_activity_id(self, total_portal_activity_id):
        """Sets the total_portal_activity_id of this PortalActivityItem.

        Total Portal Activity  # noqa: E501

        :param total_portal_activity_id: The total_portal_activity_id of this PortalActivityItem.  # noqa: E501
        :type: int
        """

        self._total_portal_activity_id = total_portal_activity_id

    @property
    def date_modified(self):
        """Gets the date_modified of this PortalActivityItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this PortalActivityItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this PortalActivityItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this PortalActivityItem.  # noqa: E501
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
        if not isinstance(other, PortalActivityItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
