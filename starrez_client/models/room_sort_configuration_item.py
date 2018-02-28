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


class RoomSortConfigurationItem(object):
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
        'room_sort_configuration_id': 'int',
        'room_location_area_id': 'int',
        'room_location_id': 'int',
        'room_type_id': 'int',
        'profile_item_id': 'int',
        'security_user_id': 'int',
        'created_by_security_user_id': 'int',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'room_sort_configuration_id': 'RoomSortConfigurationID',
        'room_location_area_id': 'RoomLocationAreaID',
        'room_location_id': 'RoomLocationID',
        'room_type_id': 'RoomTypeID',
        'profile_item_id': 'ProfileItemID',
        'security_user_id': 'SecurityUserID',
        'created_by_security_user_id': 'CreatedBy_SecurityUserID',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, room_sort_configuration_id=None, room_location_area_id=None, room_location_id=None, room_type_id=None, profile_item_id=None, security_user_id=None, created_by_security_user_id=None, date_created=None, date_modified=None):  # noqa: E501
        """RoomSortConfigurationItem - a model defined in Swagger"""  # noqa: E501

        self._room_sort_configuration_id = None
        self._room_location_area_id = None
        self._room_location_id = None
        self._room_type_id = None
        self._profile_item_id = None
        self._security_user_id = None
        self._created_by_security_user_id = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if room_sort_configuration_id is not None:
            self.room_sort_configuration_id = room_sort_configuration_id
        if room_location_area_id is not None:
            self.room_location_area_id = room_location_area_id
        if room_location_id is not None:
            self.room_location_id = room_location_id
        if room_type_id is not None:
            self.room_type_id = room_type_id
        if profile_item_id is not None:
            self.profile_item_id = profile_item_id
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if created_by_security_user_id is not None:
            self.created_by_security_user_id = created_by_security_user_id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def room_sort_configuration_id(self):
        """Gets the room_sort_configuration_id of this RoomSortConfigurationItem.  # noqa: E501

        Room Sort Configuration  # noqa: E501

        :return: The room_sort_configuration_id of this RoomSortConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_sort_configuration_id

    @room_sort_configuration_id.setter
    def room_sort_configuration_id(self, room_sort_configuration_id):
        """Sets the room_sort_configuration_id of this RoomSortConfigurationItem.

        Room Sort Configuration  # noqa: E501

        :param room_sort_configuration_id: The room_sort_configuration_id of this RoomSortConfigurationItem.  # noqa: E501
        :type: int
        """

        self._room_sort_configuration_id = room_sort_configuration_id

    @property
    def room_location_area_id(self):
        """Gets the room_location_area_id of this RoomSortConfigurationItem.  # noqa: E501

        Room Location Area  # noqa: E501

        :return: The room_location_area_id of this RoomSortConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_location_area_id

    @room_location_area_id.setter
    def room_location_area_id(self, room_location_area_id):
        """Sets the room_location_area_id of this RoomSortConfigurationItem.

        Room Location Area  # noqa: E501

        :param room_location_area_id: The room_location_area_id of this RoomSortConfigurationItem.  # noqa: E501
        :type: int
        """

        self._room_location_area_id = room_location_area_id

    @property
    def room_location_id(self):
        """Gets the room_location_id of this RoomSortConfigurationItem.  # noqa: E501

        Room Location  # noqa: E501

        :return: The room_location_id of this RoomSortConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_location_id

    @room_location_id.setter
    def room_location_id(self, room_location_id):
        """Sets the room_location_id of this RoomSortConfigurationItem.

        Room Location  # noqa: E501

        :param room_location_id: The room_location_id of this RoomSortConfigurationItem.  # noqa: E501
        :type: int
        """

        self._room_location_id = room_location_id

    @property
    def room_type_id(self):
        """Gets the room_type_id of this RoomSortConfigurationItem.  # noqa: E501

        Room Type  # noqa: E501

        :return: The room_type_id of this RoomSortConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_type_id

    @room_type_id.setter
    def room_type_id(self, room_type_id):
        """Sets the room_type_id of this RoomSortConfigurationItem.

        Room Type  # noqa: E501

        :param room_type_id: The room_type_id of this RoomSortConfigurationItem.  # noqa: E501
        :type: int
        """

        self._room_type_id = room_type_id

    @property
    def profile_item_id(self):
        """Gets the profile_item_id of this RoomSortConfigurationItem.  # noqa: E501

        Profile Item  # noqa: E501

        :return: The profile_item_id of this RoomSortConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._profile_item_id

    @profile_item_id.setter
    def profile_item_id(self, profile_item_id):
        """Sets the profile_item_id of this RoomSortConfigurationItem.

        Profile Item  # noqa: E501

        :param profile_item_id: The profile_item_id of this RoomSortConfigurationItem.  # noqa: E501
        :type: int
        """

        self._profile_item_id = profile_item_id

    @property
    def security_user_id(self):
        """Gets the security_user_id of this RoomSortConfigurationItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this RoomSortConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this RoomSortConfigurationItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this RoomSortConfigurationItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def created_by_security_user_id(self):
        """Gets the created_by_security_user_id of this RoomSortConfigurationItem.  # noqa: E501

        Created By Security User  # noqa: E501

        :return: The created_by_security_user_id of this RoomSortConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._created_by_security_user_id

    @created_by_security_user_id.setter
    def created_by_security_user_id(self, created_by_security_user_id):
        """Sets the created_by_security_user_id of this RoomSortConfigurationItem.

        Created By Security User  # noqa: E501

        :param created_by_security_user_id: The created_by_security_user_id of this RoomSortConfigurationItem.  # noqa: E501
        :type: int
        """

        self._created_by_security_user_id = created_by_security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this RoomSortConfigurationItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this RoomSortConfigurationItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this RoomSortConfigurationItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this RoomSortConfigurationItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this RoomSortConfigurationItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RoomSortConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RoomSortConfigurationItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RoomSortConfigurationItem.  # noqa: E501
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
        if not isinstance(other, RoomSortConfigurationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other