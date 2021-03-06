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


class RoomSpaceInventoryConditionItem(object):
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
        'room_space_inventory_condition_id': 'int',
        'record_type_enum': 'str',
        'room_space_inventory_type_id': 'int',
        'condition_order': 'str',
        'description': 'str',
        'comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'room_space_inventory_condition_id': 'RoomSpaceInventoryConditionID',
        'record_type_enum': 'RecordTypeEnum',
        'room_space_inventory_type_id': 'RoomSpaceInventoryTypeID',
        'condition_order': 'ConditionOrder',
        'description': 'Description',
        'comments': 'Comments',
        'date_modified': 'DateModified'
    }

    def __init__(self, room_space_inventory_condition_id=None, record_type_enum=None, room_space_inventory_type_id=None, condition_order=None, description=None, comments=None, date_modified=None):  # noqa: E501
        """RoomSpaceInventoryConditionItem - a model defined in Swagger"""  # noqa: E501

        self._room_space_inventory_condition_id = None
        self._record_type_enum = None
        self._room_space_inventory_type_id = None
        self._condition_order = None
        self._description = None
        self._comments = None
        self._date_modified = None
        self.discriminator = None

        if room_space_inventory_condition_id is not None:
            self.room_space_inventory_condition_id = room_space_inventory_condition_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if room_space_inventory_type_id is not None:
            self.room_space_inventory_type_id = room_space_inventory_type_id
        if condition_order is not None:
            self.condition_order = condition_order
        if description is not None:
            self.description = description
        if comments is not None:
            self.comments = comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def room_space_inventory_condition_id(self):
        """Gets the room_space_inventory_condition_id of this RoomSpaceInventoryConditionItem.  # noqa: E501

        Room Space Inventory Condition  # noqa: E501

        :return: The room_space_inventory_condition_id of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :rtype: int
        """
        return self._room_space_inventory_condition_id

    @room_space_inventory_condition_id.setter
    def room_space_inventory_condition_id(self, room_space_inventory_condition_id):
        """Sets the room_space_inventory_condition_id of this RoomSpaceInventoryConditionItem.

        Room Space Inventory Condition  # noqa: E501

        :param room_space_inventory_condition_id: The room_space_inventory_condition_id of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :type: int
        """

        self._room_space_inventory_condition_id = room_space_inventory_condition_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this RoomSpaceInventoryConditionItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this RoomSpaceInventoryConditionItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def room_space_inventory_type_id(self):
        """Gets the room_space_inventory_type_id of this RoomSpaceInventoryConditionItem.  # noqa: E501

        Room Space Inventory Type  # noqa: E501

        :return: The room_space_inventory_type_id of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :rtype: int
        """
        return self._room_space_inventory_type_id

    @room_space_inventory_type_id.setter
    def room_space_inventory_type_id(self, room_space_inventory_type_id):
        """Sets the room_space_inventory_type_id of this RoomSpaceInventoryConditionItem.

        Room Space Inventory Type  # noqa: E501

        :param room_space_inventory_type_id: The room_space_inventory_type_id of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :type: int
        """

        self._room_space_inventory_type_id = room_space_inventory_type_id

    @property
    def condition_order(self):
        """Gets the condition_order of this RoomSpaceInventoryConditionItem.  # noqa: E501

        Condition Order  # noqa: E501

        :return: The condition_order of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :rtype: str
        """
        return self._condition_order

    @condition_order.setter
    def condition_order(self, condition_order):
        """Sets the condition_order of this RoomSpaceInventoryConditionItem.

        Condition Order  # noqa: E501

        :param condition_order: The condition_order of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :type: str
        """

        self._condition_order = condition_order

    @property
    def description(self):
        """Gets the description of this RoomSpaceInventoryConditionItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoomSpaceInventoryConditionItem.

        Description  # noqa: E501

        :param description: The description of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 25:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `25`")  # noqa: E501

        self._description = description

    @property
    def comments(self):
        """Gets the comments of this RoomSpaceInventoryConditionItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this RoomSpaceInventoryConditionItem.

        Comments  # noqa: E501

        :param comments: The comments of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 100:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `100`")  # noqa: E501

        self._comments = comments

    @property
    def date_modified(self):
        """Gets the date_modified of this RoomSpaceInventoryConditionItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RoomSpaceInventoryConditionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RoomSpaceInventoryConditionItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RoomSpaceInventoryConditionItem.  # noqa: E501
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
        if not isinstance(other, RoomSpaceInventoryConditionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
