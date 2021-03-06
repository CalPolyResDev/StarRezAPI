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


class TotalItem(object):
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
        'total_id': 'int',
        'entry_id': 'int',
        'charge_group_id': 'int',
        'total_count': 'int',
        'total_amount': 'str',
        'total_tax_amount': 'str',
        'total_tax_amount2': 'str',
        'total_tax_amount3': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'total_id': 'TotalID',
        'entry_id': 'EntryID',
        'charge_group_id': 'ChargeGroupID',
        'total_count': 'TotalCount',
        'total_amount': 'TotalAmount',
        'total_tax_amount': 'TotalTaxAmount',
        'total_tax_amount2': 'TotalTaxAmount2',
        'total_tax_amount3': 'TotalTaxAmount3',
        'date_modified': 'DateModified'
    }

    def __init__(self, total_id=None, entry_id=None, charge_group_id=None, total_count=None, total_amount=None, total_tax_amount=None, total_tax_amount2=None, total_tax_amount3=None, date_modified=None):  # noqa: E501
        """TotalItem - a model defined in Swagger"""  # noqa: E501

        self._total_id = None
        self._entry_id = None
        self._charge_group_id = None
        self._total_count = None
        self._total_amount = None
        self._total_tax_amount = None
        self._total_tax_amount2 = None
        self._total_tax_amount3 = None
        self._date_modified = None
        self.discriminator = None

        if total_id is not None:
            self.total_id = total_id
        if entry_id is not None:
            self.entry_id = entry_id
        if charge_group_id is not None:
            self.charge_group_id = charge_group_id
        if total_count is not None:
            self.total_count = total_count
        if total_amount is not None:
            self.total_amount = total_amount
        if total_tax_amount is not None:
            self.total_tax_amount = total_tax_amount
        if total_tax_amount2 is not None:
            self.total_tax_amount2 = total_tax_amount2
        if total_tax_amount3 is not None:
            self.total_tax_amount3 = total_tax_amount3
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def total_id(self):
        """Gets the total_id of this TotalItem.  # noqa: E501

        Total  # noqa: E501

        :return: The total_id of this TotalItem.  # noqa: E501
        :rtype: int
        """
        return self._total_id

    @total_id.setter
    def total_id(self, total_id):
        """Sets the total_id of this TotalItem.

        Total  # noqa: E501

        :param total_id: The total_id of this TotalItem.  # noqa: E501
        :type: int
        """

        self._total_id = total_id

    @property
    def entry_id(self):
        """Gets the entry_id of this TotalItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this TotalItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this TotalItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this TotalItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def charge_group_id(self):
        """Gets the charge_group_id of this TotalItem.  # noqa: E501

        Charge Group  # noqa: E501

        :return: The charge_group_id of this TotalItem.  # noqa: E501
        :rtype: int
        """
        return self._charge_group_id

    @charge_group_id.setter
    def charge_group_id(self, charge_group_id):
        """Sets the charge_group_id of this TotalItem.

        Charge Group  # noqa: E501

        :param charge_group_id: The charge_group_id of this TotalItem.  # noqa: E501
        :type: int
        """

        self._charge_group_id = charge_group_id

    @property
    def total_count(self):
        """Gets the total_count of this TotalItem.  # noqa: E501

        Total Count  # noqa: E501

        :return: The total_count of this TotalItem.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this TotalItem.

        Total Count  # noqa: E501

        :param total_count: The total_count of this TotalItem.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def total_amount(self):
        """Gets the total_amount of this TotalItem.  # noqa: E501

        Total Amount  # noqa: E501

        :return: The total_amount of this TotalItem.  # noqa: E501
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this TotalItem.

        Total Amount  # noqa: E501

        :param total_amount: The total_amount of this TotalItem.  # noqa: E501
        :type: str
        """

        self._total_amount = total_amount

    @property
    def total_tax_amount(self):
        """Gets the total_tax_amount of this TotalItem.  # noqa: E501

        Total Tax Amount  # noqa: E501

        :return: The total_tax_amount of this TotalItem.  # noqa: E501
        :rtype: str
        """
        return self._total_tax_amount

    @total_tax_amount.setter
    def total_tax_amount(self, total_tax_amount):
        """Sets the total_tax_amount of this TotalItem.

        Total Tax Amount  # noqa: E501

        :param total_tax_amount: The total_tax_amount of this TotalItem.  # noqa: E501
        :type: str
        """

        self._total_tax_amount = total_tax_amount

    @property
    def total_tax_amount2(self):
        """Gets the total_tax_amount2 of this TotalItem.  # noqa: E501

        Total Tax Amount 2  # noqa: E501

        :return: The total_tax_amount2 of this TotalItem.  # noqa: E501
        :rtype: str
        """
        return self._total_tax_amount2

    @total_tax_amount2.setter
    def total_tax_amount2(self, total_tax_amount2):
        """Sets the total_tax_amount2 of this TotalItem.

        Total Tax Amount 2  # noqa: E501

        :param total_tax_amount2: The total_tax_amount2 of this TotalItem.  # noqa: E501
        :type: str
        """

        self._total_tax_amount2 = total_tax_amount2

    @property
    def total_tax_amount3(self):
        """Gets the total_tax_amount3 of this TotalItem.  # noqa: E501

        Total Tax Amount 3  # noqa: E501

        :return: The total_tax_amount3 of this TotalItem.  # noqa: E501
        :rtype: str
        """
        return self._total_tax_amount3

    @total_tax_amount3.setter
    def total_tax_amount3(self, total_tax_amount3):
        """Sets the total_tax_amount3 of this TotalItem.

        Total Tax Amount 3  # noqa: E501

        :param total_tax_amount3: The total_tax_amount3 of this TotalItem.  # noqa: E501
        :type: str
        """

        self._total_tax_amount3 = total_tax_amount3

    @property
    def date_modified(self):
        """Gets the date_modified of this TotalItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this TotalItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this TotalItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this TotalItem.  # noqa: E501
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
        if not isinstance(other, TotalItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
