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


class RoomSpaceMaintenanceMaterialsItem(object):
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
        'room_space_maintenance_materials_id': 'int',
        'room_space_maintenance_id': 'int',
        'type': 'str',
        'description': 'str',
        'quantity': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'room_space_maintenance_materials_id': 'RoomSpaceMaintenanceMaterialsID',
        'room_space_maintenance_id': 'RoomSpaceMaintenanceID',
        'type': 'Type',
        'description': 'Description',
        'quantity': 'Quantity',
        'date_modified': 'DateModified'
    }

    def __init__(self, room_space_maintenance_materials_id=None, room_space_maintenance_id=None, type=None, description=None, quantity=None, date_modified=None):  # noqa: E501
        """RoomSpaceMaintenanceMaterialsItem - a model defined in Swagger"""  # noqa: E501

        self._room_space_maintenance_materials_id = None
        self._room_space_maintenance_id = None
        self._type = None
        self._description = None
        self._quantity = None
        self._date_modified = None
        self.discriminator = None

        if room_space_maintenance_materials_id is not None:
            self.room_space_maintenance_materials_id = room_space_maintenance_materials_id
        if room_space_maintenance_id is not None:
            self.room_space_maintenance_id = room_space_maintenance_id
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if quantity is not None:
            self.quantity = quantity
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def room_space_maintenance_materials_id(self):
        """Gets the room_space_maintenance_materials_id of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501

        Room Space Maintenance Materials  # noqa: E501

        :return: The room_space_maintenance_materials_id of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :rtype: int
        """
        return self._room_space_maintenance_materials_id

    @room_space_maintenance_materials_id.setter
    def room_space_maintenance_materials_id(self, room_space_maintenance_materials_id):
        """Sets the room_space_maintenance_materials_id of this RoomSpaceMaintenanceMaterialsItem.

        Room Space Maintenance Materials  # noqa: E501

        :param room_space_maintenance_materials_id: The room_space_maintenance_materials_id of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :type: int
        """

        self._room_space_maintenance_materials_id = room_space_maintenance_materials_id

    @property
    def room_space_maintenance_id(self):
        """Gets the room_space_maintenance_id of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501

        Room Space Maintenance  # noqa: E501

        :return: The room_space_maintenance_id of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :rtype: int
        """
        return self._room_space_maintenance_id

    @room_space_maintenance_id.setter
    def room_space_maintenance_id(self, room_space_maintenance_id):
        """Sets the room_space_maintenance_id of this RoomSpaceMaintenanceMaterialsItem.

        Room Space Maintenance  # noqa: E501

        :param room_space_maintenance_id: The room_space_maintenance_id of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :type: int
        """

        self._room_space_maintenance_id = room_space_maintenance_id

    @property
    def type(self):
        """Gets the type of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501

        Type  # noqa: E501

        :return: The type of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RoomSpaceMaintenanceMaterialsItem.

        Type  # noqa: E501

        :param type: The type of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :type: str
        """
        if type is not None and len(type) > 100:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `100`")  # noqa: E501

        self._type = type

    @property
    def description(self):
        """Gets the description of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoomSpaceMaintenanceMaterialsItem.

        Description  # noqa: E501

        :param description: The description of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501

        self._description = description

    @property
    def quantity(self):
        """Gets the quantity of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501

        Quantity  # noqa: E501

        :return: The quantity of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this RoomSpaceMaintenanceMaterialsItem.

        Quantity  # noqa: E501

        :param quantity: The quantity of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def date_modified(self):
        """Gets the date_modified of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RoomSpaceMaintenanceMaterialsItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RoomSpaceMaintenanceMaterialsItem.  # noqa: E501
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
        if not isinstance(other, RoomSpaceMaintenanceMaterialsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
