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


class SystemActivityItem(object):
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
        'system_activity_id': 'int',
        'client': 'str',
        'tracking': 'str',
        'activity_key': 'str',
        'instance': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'system_activity_id': 'SystemActivityID',
        'client': 'Client',
        'tracking': 'Tracking',
        'activity_key': 'ActivityKey',
        'instance': 'Instance',
        'date_modified': 'DateModified'
    }

    def __init__(self, system_activity_id=None, client=None, tracking=None, activity_key=None, instance=None, date_modified=None):  # noqa: E501
        """SystemActivityItem - a model defined in Swagger"""  # noqa: E501

        self._system_activity_id = None
        self._client = None
        self._tracking = None
        self._activity_key = None
        self._instance = None
        self._date_modified = None
        self.discriminator = None

        if system_activity_id is not None:
            self.system_activity_id = system_activity_id
        if client is not None:
            self.client = client
        if tracking is not None:
            self.tracking = tracking
        if activity_key is not None:
            self.activity_key = activity_key
        if instance is not None:
            self.instance = instance
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def system_activity_id(self):
        """Gets the system_activity_id of this SystemActivityItem.  # noqa: E501

        System Activity  # noqa: E501

        :return: The system_activity_id of this SystemActivityItem.  # noqa: E501
        :rtype: int
        """
        return self._system_activity_id

    @system_activity_id.setter
    def system_activity_id(self, system_activity_id):
        """Sets the system_activity_id of this SystemActivityItem.

        System Activity  # noqa: E501

        :param system_activity_id: The system_activity_id of this SystemActivityItem.  # noqa: E501
        :type: int
        """

        self._system_activity_id = system_activity_id

    @property
    def client(self):
        """Gets the client of this SystemActivityItem.  # noqa: E501

        Client  # noqa: E501

        :return: The client of this SystemActivityItem.  # noqa: E501
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this SystemActivityItem.

        Client  # noqa: E501

        :param client: The client of this SystemActivityItem.  # noqa: E501
        :type: str
        """

        self._client = client

    @property
    def tracking(self):
        """Gets the tracking of this SystemActivityItem.  # noqa: E501

        Tracking  # noqa: E501

        :return: The tracking of this SystemActivityItem.  # noqa: E501
        :rtype: str
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this SystemActivityItem.

        Tracking  # noqa: E501

        :param tracking: The tracking of this SystemActivityItem.  # noqa: E501
        :type: str
        """

        self._tracking = tracking

    @property
    def activity_key(self):
        """Gets the activity_key of this SystemActivityItem.  # noqa: E501

        Activity Key  # noqa: E501

        :return: The activity_key of this SystemActivityItem.  # noqa: E501
        :rtype: str
        """
        return self._activity_key

    @activity_key.setter
    def activity_key(self, activity_key):
        """Sets the activity_key of this SystemActivityItem.

        Activity Key  # noqa: E501

        :param activity_key: The activity_key of this SystemActivityItem.  # noqa: E501
        :type: str
        """

        self._activity_key = activity_key

    @property
    def instance(self):
        """Gets the instance of this SystemActivityItem.  # noqa: E501

        Instance  # noqa: E501

        :return: The instance of this SystemActivityItem.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this SystemActivityItem.

        Instance  # noqa: E501

        :param instance: The instance of this SystemActivityItem.  # noqa: E501
        :type: str
        """

        self._instance = instance

    @property
    def date_modified(self):
        """Gets the date_modified of this SystemActivityItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this SystemActivityItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SystemActivityItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this SystemActivityItem.  # noqa: E501
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
        if not isinstance(other, SystemActivityItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
