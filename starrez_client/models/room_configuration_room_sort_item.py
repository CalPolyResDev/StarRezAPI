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


class RoomConfigurationRoomSortItem(object):
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
        'room_configuration_room_sort_id': 'int',
        'is_best_match_when_no_room_profile': 'bool',
        'room_configuration_id': 'int',
        'room_sort_profile_item_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'room_configuration_room_sort_id': 'RoomConfigurationRoomSortID',
        'is_best_match_when_no_room_profile': 'IsBestMatchWhenNoRoomProfile',
        'room_configuration_id': 'RoomConfigurationID',
        'room_sort_profile_item_id': 'RoomSortProfileItemID',
        'date_modified': 'DateModified'
    }

    def __init__(self, room_configuration_room_sort_id=None, is_best_match_when_no_room_profile=None, room_configuration_id=None, room_sort_profile_item_id=None, date_modified=None):  # noqa: E501
        """RoomConfigurationRoomSortItem - a model defined in Swagger"""  # noqa: E501

        self._room_configuration_room_sort_id = None
        self._is_best_match_when_no_room_profile = None
        self._room_configuration_id = None
        self._room_sort_profile_item_id = None
        self._date_modified = None
        self.discriminator = None

        if room_configuration_room_sort_id is not None:
            self.room_configuration_room_sort_id = room_configuration_room_sort_id
        if is_best_match_when_no_room_profile is not None:
            self.is_best_match_when_no_room_profile = is_best_match_when_no_room_profile
        if room_configuration_id is not None:
            self.room_configuration_id = room_configuration_id
        if room_sort_profile_item_id is not None:
            self.room_sort_profile_item_id = room_sort_profile_item_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def room_configuration_room_sort_id(self):
        """Gets the room_configuration_room_sort_id of this RoomConfigurationRoomSortItem.  # noqa: E501

        Room Configuration Room Sort  # noqa: E501

        :return: The room_configuration_room_sort_id of this RoomConfigurationRoomSortItem.  # noqa: E501
        :rtype: int
        """
        return self._room_configuration_room_sort_id

    @room_configuration_room_sort_id.setter
    def room_configuration_room_sort_id(self, room_configuration_room_sort_id):
        """Sets the room_configuration_room_sort_id of this RoomConfigurationRoomSortItem.

        Room Configuration Room Sort  # noqa: E501

        :param room_configuration_room_sort_id: The room_configuration_room_sort_id of this RoomConfigurationRoomSortItem.  # noqa: E501
        :type: int
        """

        self._room_configuration_room_sort_id = room_configuration_room_sort_id

    @property
    def is_best_match_when_no_room_profile(self):
        """Gets the is_best_match_when_no_room_profile of this RoomConfigurationRoomSortItem.  # noqa: E501

        Is Best Match When No Room Profile  # noqa: E501

        :return: The is_best_match_when_no_room_profile of this RoomConfigurationRoomSortItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_best_match_when_no_room_profile

    @is_best_match_when_no_room_profile.setter
    def is_best_match_when_no_room_profile(self, is_best_match_when_no_room_profile):
        """Sets the is_best_match_when_no_room_profile of this RoomConfigurationRoomSortItem.

        Is Best Match When No Room Profile  # noqa: E501

        :param is_best_match_when_no_room_profile: The is_best_match_when_no_room_profile of this RoomConfigurationRoomSortItem.  # noqa: E501
        :type: bool
        """

        self._is_best_match_when_no_room_profile = is_best_match_when_no_room_profile

    @property
    def room_configuration_id(self):
        """Gets the room_configuration_id of this RoomConfigurationRoomSortItem.  # noqa: E501

        Room Configuration  # noqa: E501

        :return: The room_configuration_id of this RoomConfigurationRoomSortItem.  # noqa: E501
        :rtype: int
        """
        return self._room_configuration_id

    @room_configuration_id.setter
    def room_configuration_id(self, room_configuration_id):
        """Sets the room_configuration_id of this RoomConfigurationRoomSortItem.

        Room Configuration  # noqa: E501

        :param room_configuration_id: The room_configuration_id of this RoomConfigurationRoomSortItem.  # noqa: E501
        :type: int
        """

        self._room_configuration_id = room_configuration_id

    @property
    def room_sort_profile_item_id(self):
        """Gets the room_sort_profile_item_id of this RoomConfigurationRoomSortItem.  # noqa: E501

        Room Sort Profile Item  # noqa: E501

        :return: The room_sort_profile_item_id of this RoomConfigurationRoomSortItem.  # noqa: E501
        :rtype: int
        """
        return self._room_sort_profile_item_id

    @room_sort_profile_item_id.setter
    def room_sort_profile_item_id(self, room_sort_profile_item_id):
        """Sets the room_sort_profile_item_id of this RoomConfigurationRoomSortItem.

        Room Sort Profile Item  # noqa: E501

        :param room_sort_profile_item_id: The room_sort_profile_item_id of this RoomConfigurationRoomSortItem.  # noqa: E501
        :type: int
        """

        self._room_sort_profile_item_id = room_sort_profile_item_id

    @property
    def date_modified(self):
        """Gets the date_modified of this RoomConfigurationRoomSortItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RoomConfigurationRoomSortItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RoomConfigurationRoomSortItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RoomConfigurationRoomSortItem.  # noqa: E501
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
        if not isinstance(other, RoomConfigurationRoomSortItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other