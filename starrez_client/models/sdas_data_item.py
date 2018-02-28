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


class SDASDataItem(object):
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
        'sdas_data_id': 'int',
        'sdas_data_date': 'str',
        'ip_address': 'str',
        'entry_id': 'int',
        'duration': 'int',
        'megabyte': 'str',
        'charge': 'str',
        'allowance': 'str',
        'plan_allowance': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'sdas_data_id': 'SDASDataID',
        'sdas_data_date': 'SDASDataDate',
        'ip_address': 'IPAddress',
        'entry_id': 'EntryID',
        'duration': 'Duration',
        'megabyte': 'Megabyte',
        'charge': 'Charge',
        'allowance': 'Allowance',
        'plan_allowance': 'PlanAllowance',
        'date_modified': 'DateModified'
    }

    def __init__(self, sdas_data_id=None, sdas_data_date=None, ip_address=None, entry_id=None, duration=None, megabyte=None, charge=None, allowance=None, plan_allowance=None, date_modified=None):  # noqa: E501
        """SDASDataItem - a model defined in Swagger"""  # noqa: E501

        self._sdas_data_id = None
        self._sdas_data_date = None
        self._ip_address = None
        self._entry_id = None
        self._duration = None
        self._megabyte = None
        self._charge = None
        self._allowance = None
        self._plan_allowance = None
        self._date_modified = None
        self.discriminator = None

        if sdas_data_id is not None:
            self.sdas_data_id = sdas_data_id
        if sdas_data_date is not None:
            self.sdas_data_date = sdas_data_date
        if ip_address is not None:
            self.ip_address = ip_address
        if entry_id is not None:
            self.entry_id = entry_id
        if duration is not None:
            self.duration = duration
        if megabyte is not None:
            self.megabyte = megabyte
        if charge is not None:
            self.charge = charge
        if allowance is not None:
            self.allowance = allowance
        if plan_allowance is not None:
            self.plan_allowance = plan_allowance
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def sdas_data_id(self):
        """Gets the sdas_data_id of this SDASDataItem.  # noqa: E501

        SDAS Data  # noqa: E501

        :return: The sdas_data_id of this SDASDataItem.  # noqa: E501
        :rtype: int
        """
        return self._sdas_data_id

    @sdas_data_id.setter
    def sdas_data_id(self, sdas_data_id):
        """Sets the sdas_data_id of this SDASDataItem.

        SDAS Data  # noqa: E501

        :param sdas_data_id: The sdas_data_id of this SDASDataItem.  # noqa: E501
        :type: int
        """

        self._sdas_data_id = sdas_data_id

    @property
    def sdas_data_date(self):
        """Gets the sdas_data_date of this SDASDataItem.  # noqa: E501

        SDAS Data Date  # noqa: E501

        :return: The sdas_data_date of this SDASDataItem.  # noqa: E501
        :rtype: str
        """
        return self._sdas_data_date

    @sdas_data_date.setter
    def sdas_data_date(self, sdas_data_date):
        """Sets the sdas_data_date of this SDASDataItem.

        SDAS Data Date  # noqa: E501

        :param sdas_data_date: The sdas_data_date of this SDASDataItem.  # noqa: E501
        :type: str
        """

        self._sdas_data_date = sdas_data_date

    @property
    def ip_address(self):
        """Gets the ip_address of this SDASDataItem.  # noqa: E501

        IP Address  # noqa: E501

        :return: The ip_address of this SDASDataItem.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this SDASDataItem.

        IP Address  # noqa: E501

        :param ip_address: The ip_address of this SDASDataItem.  # noqa: E501
        :type: str
        """
        if ip_address is not None and len(ip_address) > 15:
            raise ValueError("Invalid value for `ip_address`, length must be less than or equal to `15`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def entry_id(self):
        """Gets the entry_id of this SDASDataItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this SDASDataItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this SDASDataItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this SDASDataItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def duration(self):
        """Gets the duration of this SDASDataItem.  # noqa: E501

        Duration  # noqa: E501

        :return: The duration of this SDASDataItem.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SDASDataItem.

        Duration  # noqa: E501

        :param duration: The duration of this SDASDataItem.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def megabyte(self):
        """Gets the megabyte of this SDASDataItem.  # noqa: E501

        Megabyte  # noqa: E501

        :return: The megabyte of this SDASDataItem.  # noqa: E501
        :rtype: str
        """
        return self._megabyte

    @megabyte.setter
    def megabyte(self, megabyte):
        """Sets the megabyte of this SDASDataItem.

        Megabyte  # noqa: E501

        :param megabyte: The megabyte of this SDASDataItem.  # noqa: E501
        :type: str
        """

        self._megabyte = megabyte

    @property
    def charge(self):
        """Gets the charge of this SDASDataItem.  # noqa: E501

        Charge  # noqa: E501

        :return: The charge of this SDASDataItem.  # noqa: E501
        :rtype: str
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this SDASDataItem.

        Charge  # noqa: E501

        :param charge: The charge of this SDASDataItem.  # noqa: E501
        :type: str
        """

        self._charge = charge

    @property
    def allowance(self):
        """Gets the allowance of this SDASDataItem.  # noqa: E501

        Allowance  # noqa: E501

        :return: The allowance of this SDASDataItem.  # noqa: E501
        :rtype: str
        """
        return self._allowance

    @allowance.setter
    def allowance(self, allowance):
        """Sets the allowance of this SDASDataItem.

        Allowance  # noqa: E501

        :param allowance: The allowance of this SDASDataItem.  # noqa: E501
        :type: str
        """

        self._allowance = allowance

    @property
    def plan_allowance(self):
        """Gets the plan_allowance of this SDASDataItem.  # noqa: E501

        Plan Allowance  # noqa: E501

        :return: The plan_allowance of this SDASDataItem.  # noqa: E501
        :rtype: str
        """
        return self._plan_allowance

    @plan_allowance.setter
    def plan_allowance(self, plan_allowance):
        """Sets the plan_allowance of this SDASDataItem.

        Plan Allowance  # noqa: E501

        :param plan_allowance: The plan_allowance of this SDASDataItem.  # noqa: E501
        :type: str
        """

        self._plan_allowance = plan_allowance

    @property
    def date_modified(self):
        """Gets the date_modified of this SDASDataItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this SDASDataItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SDASDataItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this SDASDataItem.  # noqa: E501
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
        if not isinstance(other, SDASDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other