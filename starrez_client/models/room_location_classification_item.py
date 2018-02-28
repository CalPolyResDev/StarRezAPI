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


class RoomLocationClassificationItem(object):
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
        'room_location_classification_id': 'int',
        'room_location_id': 'int',
        'classification_id': 'int',
        'maximum_bookings': 'int',
        'room_spaces_used': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'room_location_classification_id': 'RoomLocationClassificationID',
        'room_location_id': 'RoomLocationID',
        'classification_id': 'ClassificationID',
        'maximum_bookings': 'MaximumBookings',
        'room_spaces_used': 'RoomSpacesUsed',
        'date_modified': 'DateModified'
    }

    def __init__(self, room_location_classification_id=None, room_location_id=None, classification_id=None, maximum_bookings=None, room_spaces_used=None, date_modified=None):  # noqa: E501
        """RoomLocationClassificationItem - a model defined in Swagger"""  # noqa: E501

        self._room_location_classification_id = None
        self._room_location_id = None
        self._classification_id = None
        self._maximum_bookings = None
        self._room_spaces_used = None
        self._date_modified = None
        self.discriminator = None

        if room_location_classification_id is not None:
            self.room_location_classification_id = room_location_classification_id
        if room_location_id is not None:
            self.room_location_id = room_location_id
        if classification_id is not None:
            self.classification_id = classification_id
        if maximum_bookings is not None:
            self.maximum_bookings = maximum_bookings
        if room_spaces_used is not None:
            self.room_spaces_used = room_spaces_used
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def room_location_classification_id(self):
        """Gets the room_location_classification_id of this RoomLocationClassificationItem.  # noqa: E501

        Room Location Classification  # noqa: E501

        :return: The room_location_classification_id of this RoomLocationClassificationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_location_classification_id

    @room_location_classification_id.setter
    def room_location_classification_id(self, room_location_classification_id):
        """Sets the room_location_classification_id of this RoomLocationClassificationItem.

        Room Location Classification  # noqa: E501

        :param room_location_classification_id: The room_location_classification_id of this RoomLocationClassificationItem.  # noqa: E501
        :type: int
        """

        self._room_location_classification_id = room_location_classification_id

    @property
    def room_location_id(self):
        """Gets the room_location_id of this RoomLocationClassificationItem.  # noqa: E501

        Room Location  # noqa: E501

        :return: The room_location_id of this RoomLocationClassificationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_location_id

    @room_location_id.setter
    def room_location_id(self, room_location_id):
        """Sets the room_location_id of this RoomLocationClassificationItem.

        Room Location  # noqa: E501

        :param room_location_id: The room_location_id of this RoomLocationClassificationItem.  # noqa: E501
        :type: int
        """

        self._room_location_id = room_location_id

    @property
    def classification_id(self):
        """Gets the classification_id of this RoomLocationClassificationItem.  # noqa: E501

        Classification  # noqa: E501

        :return: The classification_id of this RoomLocationClassificationItem.  # noqa: E501
        :rtype: int
        """
        return self._classification_id

    @classification_id.setter
    def classification_id(self, classification_id):
        """Sets the classification_id of this RoomLocationClassificationItem.

        Classification  # noqa: E501

        :param classification_id: The classification_id of this RoomLocationClassificationItem.  # noqa: E501
        :type: int
        """

        self._classification_id = classification_id

    @property
    def maximum_bookings(self):
        """Gets the maximum_bookings of this RoomLocationClassificationItem.  # noqa: E501

        Maximum Bookings  # noqa: E501

        :return: The maximum_bookings of this RoomLocationClassificationItem.  # noqa: E501
        :rtype: int
        """
        return self._maximum_bookings

    @maximum_bookings.setter
    def maximum_bookings(self, maximum_bookings):
        """Sets the maximum_bookings of this RoomLocationClassificationItem.

        Maximum Bookings  # noqa: E501

        :param maximum_bookings: The maximum_bookings of this RoomLocationClassificationItem.  # noqa: E501
        :type: int
        """

        self._maximum_bookings = maximum_bookings

    @property
    def room_spaces_used(self):
        """Gets the room_spaces_used of this RoomLocationClassificationItem.  # noqa: E501

        Room Spaces Used  # noqa: E501

        :return: The room_spaces_used of this RoomLocationClassificationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_spaces_used

    @room_spaces_used.setter
    def room_spaces_used(self, room_spaces_used):
        """Sets the room_spaces_used of this RoomLocationClassificationItem.

        Room Spaces Used  # noqa: E501

        :param room_spaces_used: The room_spaces_used of this RoomLocationClassificationItem.  # noqa: E501
        :type: int
        """

        self._room_spaces_used = room_spaces_used

    @property
    def date_modified(self):
        """Gets the date_modified of this RoomLocationClassificationItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RoomLocationClassificationItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RoomLocationClassificationItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RoomLocationClassificationItem.  # noqa: E501
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
        if not isinstance(other, RoomLocationClassificationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other