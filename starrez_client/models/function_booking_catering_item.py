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


class FunctionBookingCateringItem(object):
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
        'function_booking_catering_id': 'int',
        'function_booking_id': 'int',
        'catering_id': 'int',
        'function_charge_type_enum': 'str',
        'charge_to_entry': 'bool',
        'per_entry': 'bool',
        'description': 'str',
        'catering_description': 'str',
        'serving_time': 'datetime',
        'serving_duration': 'str',
        'location': 'str',
        'function_room_id': 'int',
        'amount': 'str',
        'amount_cost': 'str',
        'charge_item_id': 'int',
        'comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'function_booking_catering_id': 'FunctionBookingCateringID',
        'function_booking_id': 'FunctionBookingID',
        'catering_id': 'CateringID',
        'function_charge_type_enum': 'FunctionChargeTypeEnum',
        'charge_to_entry': 'ChargeToEntry',
        'per_entry': 'PerEntry',
        'description': 'Description',
        'catering_description': 'CateringDescription',
        'serving_time': 'ServingTime',
        'serving_duration': 'ServingDuration',
        'location': 'Location',
        'function_room_id': 'FunctionRoomID',
        'amount': 'Amount',
        'amount_cost': 'AmountCost',
        'charge_item_id': 'ChargeItemID',
        'comments': 'Comments',
        'date_modified': 'DateModified'
    }

    def __init__(self, function_booking_catering_id=None, function_booking_id=None, catering_id=None, function_charge_type_enum=None, charge_to_entry=None, per_entry=None, description=None, catering_description=None, serving_time=None, serving_duration=None, location=None, function_room_id=None, amount=None, amount_cost=None, charge_item_id=None, comments=None, date_modified=None):  # noqa: E501
        """FunctionBookingCateringItem - a model defined in Swagger"""  # noqa: E501

        self._function_booking_catering_id = None
        self._function_booking_id = None
        self._catering_id = None
        self._function_charge_type_enum = None
        self._charge_to_entry = None
        self._per_entry = None
        self._description = None
        self._catering_description = None
        self._serving_time = None
        self._serving_duration = None
        self._location = None
        self._function_room_id = None
        self._amount = None
        self._amount_cost = None
        self._charge_item_id = None
        self._comments = None
        self._date_modified = None
        self.discriminator = None

        if function_booking_catering_id is not None:
            self.function_booking_catering_id = function_booking_catering_id
        if function_booking_id is not None:
            self.function_booking_id = function_booking_id
        if catering_id is not None:
            self.catering_id = catering_id
        if function_charge_type_enum is not None:
            self.function_charge_type_enum = function_charge_type_enum
        if charge_to_entry is not None:
            self.charge_to_entry = charge_to_entry
        if per_entry is not None:
            self.per_entry = per_entry
        if description is not None:
            self.description = description
        if catering_description is not None:
            self.catering_description = catering_description
        if serving_time is not None:
            self.serving_time = serving_time
        if serving_duration is not None:
            self.serving_duration = serving_duration
        if location is not None:
            self.location = location
        if function_room_id is not None:
            self.function_room_id = function_room_id
        if amount is not None:
            self.amount = amount
        if amount_cost is not None:
            self.amount_cost = amount_cost
        if charge_item_id is not None:
            self.charge_item_id = charge_item_id
        if comments is not None:
            self.comments = comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def function_booking_catering_id(self):
        """Gets the function_booking_catering_id of this FunctionBookingCateringItem.  # noqa: E501

        Function Booking Catering  # noqa: E501

        :return: The function_booking_catering_id of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: int
        """
        return self._function_booking_catering_id

    @function_booking_catering_id.setter
    def function_booking_catering_id(self, function_booking_catering_id):
        """Sets the function_booking_catering_id of this FunctionBookingCateringItem.

        Function Booking Catering  # noqa: E501

        :param function_booking_catering_id: The function_booking_catering_id of this FunctionBookingCateringItem.  # noqa: E501
        :type: int
        """

        self._function_booking_catering_id = function_booking_catering_id

    @property
    def function_booking_id(self):
        """Gets the function_booking_id of this FunctionBookingCateringItem.  # noqa: E501

        Function Booking  # noqa: E501

        :return: The function_booking_id of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: int
        """
        return self._function_booking_id

    @function_booking_id.setter
    def function_booking_id(self, function_booking_id):
        """Sets the function_booking_id of this FunctionBookingCateringItem.

        Function Booking  # noqa: E501

        :param function_booking_id: The function_booking_id of this FunctionBookingCateringItem.  # noqa: E501
        :type: int
        """

        self._function_booking_id = function_booking_id

    @property
    def catering_id(self):
        """Gets the catering_id of this FunctionBookingCateringItem.  # noqa: E501

        Catering  # noqa: E501

        :return: The catering_id of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: int
        """
        return self._catering_id

    @catering_id.setter
    def catering_id(self, catering_id):
        """Sets the catering_id of this FunctionBookingCateringItem.

        Catering  # noqa: E501

        :param catering_id: The catering_id of this FunctionBookingCateringItem.  # noqa: E501
        :type: int
        """

        self._catering_id = catering_id

    @property
    def function_charge_type_enum(self):
        """Gets the function_charge_type_enum of this FunctionBookingCateringItem.  # noqa: E501

        Function Charge Type  # noqa: E501

        :return: The function_charge_type_enum of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: str
        """
        return self._function_charge_type_enum

    @function_charge_type_enum.setter
    def function_charge_type_enum(self, function_charge_type_enum):
        """Sets the function_charge_type_enum of this FunctionBookingCateringItem.

        Function Charge Type  # noqa: E501

        :param function_charge_type_enum: The function_charge_type_enum of this FunctionBookingCateringItem.  # noqa: E501
        :type: str
        """

        self._function_charge_type_enum = function_charge_type_enum

    @property
    def charge_to_entry(self):
        """Gets the charge_to_entry of this FunctionBookingCateringItem.  # noqa: E501

        Charge To Entry  # noqa: E501

        :return: The charge_to_entry of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: bool
        """
        return self._charge_to_entry

    @charge_to_entry.setter
    def charge_to_entry(self, charge_to_entry):
        """Sets the charge_to_entry of this FunctionBookingCateringItem.

        Charge To Entry  # noqa: E501

        :param charge_to_entry: The charge_to_entry of this FunctionBookingCateringItem.  # noqa: E501
        :type: bool
        """

        self._charge_to_entry = charge_to_entry

    @property
    def per_entry(self):
        """Gets the per_entry of this FunctionBookingCateringItem.  # noqa: E501

        Per Entry  # noqa: E501

        :return: The per_entry of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: bool
        """
        return self._per_entry

    @per_entry.setter
    def per_entry(self, per_entry):
        """Sets the per_entry of this FunctionBookingCateringItem.

        Per Entry  # noqa: E501

        :param per_entry: The per_entry of this FunctionBookingCateringItem.  # noqa: E501
        :type: bool
        """

        self._per_entry = per_entry

    @property
    def description(self):
        """Gets the description of this FunctionBookingCateringItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FunctionBookingCateringItem.

        Description  # noqa: E501

        :param description: The description of this FunctionBookingCateringItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def catering_description(self):
        """Gets the catering_description of this FunctionBookingCateringItem.  # noqa: E501

        Catering Description  # noqa: E501

        :return: The catering_description of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: str
        """
        return self._catering_description

    @catering_description.setter
    def catering_description(self, catering_description):
        """Sets the catering_description of this FunctionBookingCateringItem.

        Catering Description  # noqa: E501

        :param catering_description: The catering_description of this FunctionBookingCateringItem.  # noqa: E501
        :type: str
        """
        if catering_description is not None and len(catering_description) > 2000:
            raise ValueError("Invalid value for `catering_description`, length must be less than or equal to `2000`")  # noqa: E501

        self._catering_description = catering_description

    @property
    def serving_time(self):
        """Gets the serving_time of this FunctionBookingCateringItem.  # noqa: E501

        Serving Time  # noqa: E501

        :return: The serving_time of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: datetime
        """
        return self._serving_time

    @serving_time.setter
    def serving_time(self, serving_time):
        """Sets the serving_time of this FunctionBookingCateringItem.

        Serving Time  # noqa: E501

        :param serving_time: The serving_time of this FunctionBookingCateringItem.  # noqa: E501
        :type: datetime
        """

        self._serving_time = serving_time

    @property
    def serving_duration(self):
        """Gets the serving_duration of this FunctionBookingCateringItem.  # noqa: E501

        Serving Duration  # noqa: E501

        :return: The serving_duration of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: str
        """
        return self._serving_duration

    @serving_duration.setter
    def serving_duration(self, serving_duration):
        """Sets the serving_duration of this FunctionBookingCateringItem.

        Serving Duration  # noqa: E501

        :param serving_duration: The serving_duration of this FunctionBookingCateringItem.  # noqa: E501
        :type: str
        """

        self._serving_duration = serving_duration

    @property
    def location(self):
        """Gets the location of this FunctionBookingCateringItem.  # noqa: E501

        Location  # noqa: E501

        :return: The location of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this FunctionBookingCateringItem.

        Location  # noqa: E501

        :param location: The location of this FunctionBookingCateringItem.  # noqa: E501
        :type: str
        """
        if location is not None and len(location) > 100:
            raise ValueError("Invalid value for `location`, length must be less than or equal to `100`")  # noqa: E501

        self._location = location

    @property
    def function_room_id(self):
        """Gets the function_room_id of this FunctionBookingCateringItem.  # noqa: E501

        Function Room  # noqa: E501

        :return: The function_room_id of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: int
        """
        return self._function_room_id

    @function_room_id.setter
    def function_room_id(self, function_room_id):
        """Sets the function_room_id of this FunctionBookingCateringItem.

        Function Room  # noqa: E501

        :param function_room_id: The function_room_id of this FunctionBookingCateringItem.  # noqa: E501
        :type: int
        """

        self._function_room_id = function_room_id

    @property
    def amount(self):
        """Gets the amount of this FunctionBookingCateringItem.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FunctionBookingCateringItem.

        Amount  # noqa: E501

        :param amount: The amount of this FunctionBookingCateringItem.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def amount_cost(self):
        """Gets the amount_cost of this FunctionBookingCateringItem.  # noqa: E501

        Amount Cost  # noqa: E501

        :return: The amount_cost of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: str
        """
        return self._amount_cost

    @amount_cost.setter
    def amount_cost(self, amount_cost):
        """Sets the amount_cost of this FunctionBookingCateringItem.

        Amount Cost  # noqa: E501

        :param amount_cost: The amount_cost of this FunctionBookingCateringItem.  # noqa: E501
        :type: str
        """

        self._amount_cost = amount_cost

    @property
    def charge_item_id(self):
        """Gets the charge_item_id of this FunctionBookingCateringItem.  # noqa: E501

        Charge Item  # noqa: E501

        :return: The charge_item_id of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: int
        """
        return self._charge_item_id

    @charge_item_id.setter
    def charge_item_id(self, charge_item_id):
        """Sets the charge_item_id of this FunctionBookingCateringItem.

        Charge Item  # noqa: E501

        :param charge_item_id: The charge_item_id of this FunctionBookingCateringItem.  # noqa: E501
        :type: int
        """

        self._charge_item_id = charge_item_id

    @property
    def comments(self):
        """Gets the comments of this FunctionBookingCateringItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this FunctionBookingCateringItem.

        Comments  # noqa: E501

        :param comments: The comments of this FunctionBookingCateringItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 2000:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `2000`")  # noqa: E501

        self._comments = comments

    @property
    def date_modified(self):
        """Gets the date_modified of this FunctionBookingCateringItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this FunctionBookingCateringItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this FunctionBookingCateringItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this FunctionBookingCateringItem.  # noqa: E501
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
        if not isinstance(other, FunctionBookingCateringItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other