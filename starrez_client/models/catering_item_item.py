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


class CateringItemItem(object):
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
        'catering_item_id': 'int',
        'catering_id': 'int',
        'record_type_enum': 'str',
        'description': 'str',
        'serving_order': 'str',
        'optional': 'bool',
        'quantity_default_is_percentage': 'bool',
        'quantity_default': 'str',
        'charge_fixed': 'bool',
        'amount_cost': 'str',
        'amount': 'str',
        'comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'catering_item_id': 'CateringItemID',
        'catering_id': 'CateringID',
        'record_type_enum': 'RecordTypeEnum',
        'description': 'Description',
        'serving_order': 'ServingOrder',
        'optional': 'Optional',
        'quantity_default_is_percentage': 'QuantityDefaultIsPercentage',
        'quantity_default': 'QuantityDefault',
        'charge_fixed': 'ChargeFixed',
        'amount_cost': 'AmountCost',
        'amount': 'Amount',
        'comments': 'Comments',
        'date_modified': 'DateModified'
    }

    def __init__(self, catering_item_id=None, catering_id=None, record_type_enum=None, description=None, serving_order=None, optional=None, quantity_default_is_percentage=None, quantity_default=None, charge_fixed=None, amount_cost=None, amount=None, comments=None, date_modified=None):  # noqa: E501
        """CateringItemItem - a model defined in Swagger"""  # noqa: E501

        self._catering_item_id = None
        self._catering_id = None
        self._record_type_enum = None
        self._description = None
        self._serving_order = None
        self._optional = None
        self._quantity_default_is_percentage = None
        self._quantity_default = None
        self._charge_fixed = None
        self._amount_cost = None
        self._amount = None
        self._comments = None
        self._date_modified = None
        self.discriminator = None

        if catering_item_id is not None:
            self.catering_item_id = catering_item_id
        if catering_id is not None:
            self.catering_id = catering_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if description is not None:
            self.description = description
        if serving_order is not None:
            self.serving_order = serving_order
        if optional is not None:
            self.optional = optional
        if quantity_default_is_percentage is not None:
            self.quantity_default_is_percentage = quantity_default_is_percentage
        if quantity_default is not None:
            self.quantity_default = quantity_default
        if charge_fixed is not None:
            self.charge_fixed = charge_fixed
        if amount_cost is not None:
            self.amount_cost = amount_cost
        if amount is not None:
            self.amount = amount
        if comments is not None:
            self.comments = comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def catering_item_id(self):
        """Gets the catering_item_id of this CateringItemItem.  # noqa: E501

        Catering Item  # noqa: E501

        :return: The catering_item_id of this CateringItemItem.  # noqa: E501
        :rtype: int
        """
        return self._catering_item_id

    @catering_item_id.setter
    def catering_item_id(self, catering_item_id):
        """Sets the catering_item_id of this CateringItemItem.

        Catering Item  # noqa: E501

        :param catering_item_id: The catering_item_id of this CateringItemItem.  # noqa: E501
        :type: int
        """

        self._catering_item_id = catering_item_id

    @property
    def catering_id(self):
        """Gets the catering_id of this CateringItemItem.  # noqa: E501

        Catering  # noqa: E501

        :return: The catering_id of this CateringItemItem.  # noqa: E501
        :rtype: int
        """
        return self._catering_id

    @catering_id.setter
    def catering_id(self, catering_id):
        """Sets the catering_id of this CateringItemItem.

        Catering  # noqa: E501

        :param catering_id: The catering_id of this CateringItemItem.  # noqa: E501
        :type: int
        """

        self._catering_id = catering_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this CateringItemItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this CateringItemItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this CateringItemItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this CateringItemItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def description(self):
        """Gets the description of this CateringItemItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this CateringItemItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CateringItemItem.

        Description  # noqa: E501

        :param description: The description of this CateringItemItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def serving_order(self):
        """Gets the serving_order of this CateringItemItem.  # noqa: E501

        Serving Order  # noqa: E501

        :return: The serving_order of this CateringItemItem.  # noqa: E501
        :rtype: str
        """
        return self._serving_order

    @serving_order.setter
    def serving_order(self, serving_order):
        """Sets the serving_order of this CateringItemItem.

        Serving Order  # noqa: E501

        :param serving_order: The serving_order of this CateringItemItem.  # noqa: E501
        :type: str
        """

        self._serving_order = serving_order

    @property
    def optional(self):
        """Gets the optional of this CateringItemItem.  # noqa: E501

        Optional  # noqa: E501

        :return: The optional of this CateringItemItem.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this CateringItemItem.

        Optional  # noqa: E501

        :param optional: The optional of this CateringItemItem.  # noqa: E501
        :type: bool
        """

        self._optional = optional

    @property
    def quantity_default_is_percentage(self):
        """Gets the quantity_default_is_percentage of this CateringItemItem.  # noqa: E501

        Quantity Default Is Percentage  # noqa: E501

        :return: The quantity_default_is_percentage of this CateringItemItem.  # noqa: E501
        :rtype: bool
        """
        return self._quantity_default_is_percentage

    @quantity_default_is_percentage.setter
    def quantity_default_is_percentage(self, quantity_default_is_percentage):
        """Sets the quantity_default_is_percentage of this CateringItemItem.

        Quantity Default Is Percentage  # noqa: E501

        :param quantity_default_is_percentage: The quantity_default_is_percentage of this CateringItemItem.  # noqa: E501
        :type: bool
        """

        self._quantity_default_is_percentage = quantity_default_is_percentage

    @property
    def quantity_default(self):
        """Gets the quantity_default of this CateringItemItem.  # noqa: E501

        Quantity Default  # noqa: E501

        :return: The quantity_default of this CateringItemItem.  # noqa: E501
        :rtype: str
        """
        return self._quantity_default

    @quantity_default.setter
    def quantity_default(self, quantity_default):
        """Sets the quantity_default of this CateringItemItem.

        Quantity Default  # noqa: E501

        :param quantity_default: The quantity_default of this CateringItemItem.  # noqa: E501
        :type: str
        """

        self._quantity_default = quantity_default

    @property
    def charge_fixed(self):
        """Gets the charge_fixed of this CateringItemItem.  # noqa: E501

        Charge Fixed  # noqa: E501

        :return: The charge_fixed of this CateringItemItem.  # noqa: E501
        :rtype: bool
        """
        return self._charge_fixed

    @charge_fixed.setter
    def charge_fixed(self, charge_fixed):
        """Sets the charge_fixed of this CateringItemItem.

        Charge Fixed  # noqa: E501

        :param charge_fixed: The charge_fixed of this CateringItemItem.  # noqa: E501
        :type: bool
        """

        self._charge_fixed = charge_fixed

    @property
    def amount_cost(self):
        """Gets the amount_cost of this CateringItemItem.  # noqa: E501

        Amount Cost  # noqa: E501

        :return: The amount_cost of this CateringItemItem.  # noqa: E501
        :rtype: str
        """
        return self._amount_cost

    @amount_cost.setter
    def amount_cost(self, amount_cost):
        """Sets the amount_cost of this CateringItemItem.

        Amount Cost  # noqa: E501

        :param amount_cost: The amount_cost of this CateringItemItem.  # noqa: E501
        :type: str
        """

        self._amount_cost = amount_cost

    @property
    def amount(self):
        """Gets the amount of this CateringItemItem.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this CateringItemItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CateringItemItem.

        Amount  # noqa: E501

        :param amount: The amount of this CateringItemItem.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def comments(self):
        """Gets the comments of this CateringItemItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this CateringItemItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this CateringItemItem.

        Comments  # noqa: E501

        :param comments: The comments of this CateringItemItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 2000:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `2000`")  # noqa: E501

        self._comments = comments

    @property
    def date_modified(self):
        """Gets the date_modified of this CateringItemItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this CateringItemItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this CateringItemItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this CateringItemItem.  # noqa: E501
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
        if not isinstance(other, CateringItemItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
