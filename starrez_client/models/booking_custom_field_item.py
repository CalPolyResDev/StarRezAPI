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


class BookingCustomFieldItem(object):
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
        'booking_custom_field_id': 'int',
        'booking_id': 'int',
        'custom_field_definition_id': 'int',
        'field_data_type_enum': 'str',
        'value_string': 'str',
        'value_date': 'str',
        'value_boolean': 'bool',
        'value_integer': 'int',
        'value_money': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'booking_custom_field_id': 'BookingCustomFieldID',
        'booking_id': 'BookingID',
        'custom_field_definition_id': 'CustomFieldDefinitionID',
        'field_data_type_enum': 'FieldDataTypeEnum',
        'value_string': 'ValueString',
        'value_date': 'ValueDate',
        'value_boolean': 'ValueBoolean',
        'value_integer': 'ValueInteger',
        'value_money': 'ValueMoney',
        'date_modified': 'DateModified'
    }

    def __init__(self, booking_custom_field_id=None, booking_id=None, custom_field_definition_id=None, field_data_type_enum=None, value_string=None, value_date=None, value_boolean=None, value_integer=None, value_money=None, date_modified=None):  # noqa: E501
        """BookingCustomFieldItem - a model defined in Swagger"""  # noqa: E501

        self._booking_custom_field_id = None
        self._booking_id = None
        self._custom_field_definition_id = None
        self._field_data_type_enum = None
        self._value_string = None
        self._value_date = None
        self._value_boolean = None
        self._value_integer = None
        self._value_money = None
        self._date_modified = None
        self.discriminator = None

        if booking_custom_field_id is not None:
            self.booking_custom_field_id = booking_custom_field_id
        if booking_id is not None:
            self.booking_id = booking_id
        if custom_field_definition_id is not None:
            self.custom_field_definition_id = custom_field_definition_id
        if field_data_type_enum is not None:
            self.field_data_type_enum = field_data_type_enum
        if value_string is not None:
            self.value_string = value_string
        if value_date is not None:
            self.value_date = value_date
        if value_boolean is not None:
            self.value_boolean = value_boolean
        if value_integer is not None:
            self.value_integer = value_integer
        if value_money is not None:
            self.value_money = value_money
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def booking_custom_field_id(self):
        """Gets the booking_custom_field_id of this BookingCustomFieldItem.  # noqa: E501

        Booking Custom Field  # noqa: E501

        :return: The booking_custom_field_id of this BookingCustomFieldItem.  # noqa: E501
        :rtype: int
        """
        return self._booking_custom_field_id

    @booking_custom_field_id.setter
    def booking_custom_field_id(self, booking_custom_field_id):
        """Sets the booking_custom_field_id of this BookingCustomFieldItem.

        Booking Custom Field  # noqa: E501

        :param booking_custom_field_id: The booking_custom_field_id of this BookingCustomFieldItem.  # noqa: E501
        :type: int
        """

        self._booking_custom_field_id = booking_custom_field_id

    @property
    def booking_id(self):
        """Gets the booking_id of this BookingCustomFieldItem.  # noqa: E501

        Booking  # noqa: E501

        :return: The booking_id of this BookingCustomFieldItem.  # noqa: E501
        :rtype: int
        """
        return self._booking_id

    @booking_id.setter
    def booking_id(self, booking_id):
        """Sets the booking_id of this BookingCustomFieldItem.

        Booking  # noqa: E501

        :param booking_id: The booking_id of this BookingCustomFieldItem.  # noqa: E501
        :type: int
        """

        self._booking_id = booking_id

    @property
    def custom_field_definition_id(self):
        """Gets the custom_field_definition_id of this BookingCustomFieldItem.  # noqa: E501

        Custom Field Definition  # noqa: E501

        :return: The custom_field_definition_id of this BookingCustomFieldItem.  # noqa: E501
        :rtype: int
        """
        return self._custom_field_definition_id

    @custom_field_definition_id.setter
    def custom_field_definition_id(self, custom_field_definition_id):
        """Sets the custom_field_definition_id of this BookingCustomFieldItem.

        Custom Field Definition  # noqa: E501

        :param custom_field_definition_id: The custom_field_definition_id of this BookingCustomFieldItem.  # noqa: E501
        :type: int
        """

        self._custom_field_definition_id = custom_field_definition_id

    @property
    def field_data_type_enum(self):
        """Gets the field_data_type_enum of this BookingCustomFieldItem.  # noqa: E501

        Field Data Type  # noqa: E501

        :return: The field_data_type_enum of this BookingCustomFieldItem.  # noqa: E501
        :rtype: str
        """
        return self._field_data_type_enum

    @field_data_type_enum.setter
    def field_data_type_enum(self, field_data_type_enum):
        """Sets the field_data_type_enum of this BookingCustomFieldItem.

        Field Data Type  # noqa: E501

        :param field_data_type_enum: The field_data_type_enum of this BookingCustomFieldItem.  # noqa: E501
        :type: str
        """

        self._field_data_type_enum = field_data_type_enum

    @property
    def value_string(self):
        """Gets the value_string of this BookingCustomFieldItem.  # noqa: E501

        Value String  # noqa: E501

        :return: The value_string of this BookingCustomFieldItem.  # noqa: E501
        :rtype: str
        """
        return self._value_string

    @value_string.setter
    def value_string(self, value_string):
        """Sets the value_string of this BookingCustomFieldItem.

        Value String  # noqa: E501

        :param value_string: The value_string of this BookingCustomFieldItem.  # noqa: E501
        :type: str
        """
        if value_string is not None and len(value_string) > 5000:
            raise ValueError("Invalid value for `value_string`, length must be less than or equal to `5000`")  # noqa: E501

        self._value_string = value_string

    @property
    def value_date(self):
        """Gets the value_date of this BookingCustomFieldItem.  # noqa: E501

        Value Date  # noqa: E501

        :return: The value_date of this BookingCustomFieldItem.  # noqa: E501
        :rtype: str
        """
        return self._value_date

    @value_date.setter
    def value_date(self, value_date):
        """Sets the value_date of this BookingCustomFieldItem.

        Value Date  # noqa: E501

        :param value_date: The value_date of this BookingCustomFieldItem.  # noqa: E501
        :type: str
        """

        self._value_date = value_date

    @property
    def value_boolean(self):
        """Gets the value_boolean of this BookingCustomFieldItem.  # noqa: E501

        Value Boolean  # noqa: E501

        :return: The value_boolean of this BookingCustomFieldItem.  # noqa: E501
        :rtype: bool
        """
        return self._value_boolean

    @value_boolean.setter
    def value_boolean(self, value_boolean):
        """Sets the value_boolean of this BookingCustomFieldItem.

        Value Boolean  # noqa: E501

        :param value_boolean: The value_boolean of this BookingCustomFieldItem.  # noqa: E501
        :type: bool
        """

        self._value_boolean = value_boolean

    @property
    def value_integer(self):
        """Gets the value_integer of this BookingCustomFieldItem.  # noqa: E501

        Value Integer  # noqa: E501

        :return: The value_integer of this BookingCustomFieldItem.  # noqa: E501
        :rtype: int
        """
        return self._value_integer

    @value_integer.setter
    def value_integer(self, value_integer):
        """Sets the value_integer of this BookingCustomFieldItem.

        Value Integer  # noqa: E501

        :param value_integer: The value_integer of this BookingCustomFieldItem.  # noqa: E501
        :type: int
        """

        self._value_integer = value_integer

    @property
    def value_money(self):
        """Gets the value_money of this BookingCustomFieldItem.  # noqa: E501

        Value Money  # noqa: E501

        :return: The value_money of this BookingCustomFieldItem.  # noqa: E501
        :rtype: str
        """
        return self._value_money

    @value_money.setter
    def value_money(self, value_money):
        """Sets the value_money of this BookingCustomFieldItem.

        Value Money  # noqa: E501

        :param value_money: The value_money of this BookingCustomFieldItem.  # noqa: E501
        :type: str
        """

        self._value_money = value_money

    @property
    def date_modified(self):
        """Gets the date_modified of this BookingCustomFieldItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this BookingCustomFieldItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this BookingCustomFieldItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this BookingCustomFieldItem.  # noqa: E501
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
        if not isinstance(other, BookingCustomFieldItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
