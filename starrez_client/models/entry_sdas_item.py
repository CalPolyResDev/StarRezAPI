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


class EntrySDASItem(object):
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
        'entry_sdasid': 'int',
        'entry_id': 'int',
        'sdas_charge_rate_id': 'int',
        'enabled': 'bool',
        'user_name': 'str',
        'access_level': 'str',
        'machine_description': 'str',
        'machine_type': 'str',
        'ip_address': 'str',
        'mac_address': 'str',
        'operating_system': 'str',
        'date_enabled': 'datetime',
        'date_last_reset': 'datetime',
        'monthly_allowance': 'str',
        'comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'entry_sdasid': 'EntrySDASID',
        'entry_id': 'EntryID',
        'sdas_charge_rate_id': 'SDASChargeRateID',
        'enabled': 'Enabled',
        'user_name': 'UserName',
        'access_level': 'AccessLevel',
        'machine_description': 'MachineDescription',
        'machine_type': 'MachineType',
        'ip_address': 'IPAddress',
        'mac_address': 'MACAddress',
        'operating_system': 'OperatingSystem',
        'date_enabled': 'DateEnabled',
        'date_last_reset': 'DateLastReset',
        'monthly_allowance': 'MonthlyAllowance',
        'comments': 'Comments',
        'date_modified': 'DateModified'
    }

    def __init__(self, entry_sdasid=None, entry_id=None, sdas_charge_rate_id=None, enabled=None, user_name=None, access_level=None, machine_description=None, machine_type=None, ip_address=None, mac_address=None, operating_system=None, date_enabled=None, date_last_reset=None, monthly_allowance=None, comments=None, date_modified=None):  # noqa: E501
        """EntrySDASItem - a model defined in Swagger"""  # noqa: E501

        self._entry_sdasid = None
        self._entry_id = None
        self._sdas_charge_rate_id = None
        self._enabled = None
        self._user_name = None
        self._access_level = None
        self._machine_description = None
        self._machine_type = None
        self._ip_address = None
        self._mac_address = None
        self._operating_system = None
        self._date_enabled = None
        self._date_last_reset = None
        self._monthly_allowance = None
        self._comments = None
        self._date_modified = None
        self.discriminator = None

        if entry_sdasid is not None:
            self.entry_sdasid = entry_sdasid
        if entry_id is not None:
            self.entry_id = entry_id
        if sdas_charge_rate_id is not None:
            self.sdas_charge_rate_id = sdas_charge_rate_id
        if enabled is not None:
            self.enabled = enabled
        if user_name is not None:
            self.user_name = user_name
        if access_level is not None:
            self.access_level = access_level
        if machine_description is not None:
            self.machine_description = machine_description
        if machine_type is not None:
            self.machine_type = machine_type
        if ip_address is not None:
            self.ip_address = ip_address
        if mac_address is not None:
            self.mac_address = mac_address
        if operating_system is not None:
            self.operating_system = operating_system
        if date_enabled is not None:
            self.date_enabled = date_enabled
        if date_last_reset is not None:
            self.date_last_reset = date_last_reset
        if monthly_allowance is not None:
            self.monthly_allowance = monthly_allowance
        if comments is not None:
            self.comments = comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def entry_sdasid(self):
        """Gets the entry_sdasid of this EntrySDASItem.  # noqa: E501

        Entry SDAS  # noqa: E501

        :return: The entry_sdasid of this EntrySDASItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_sdasid

    @entry_sdasid.setter
    def entry_sdasid(self, entry_sdasid):
        """Sets the entry_sdasid of this EntrySDASItem.

        Entry SDAS  # noqa: E501

        :param entry_sdasid: The entry_sdasid of this EntrySDASItem.  # noqa: E501
        :type: int
        """

        self._entry_sdasid = entry_sdasid

    @property
    def entry_id(self):
        """Gets the entry_id of this EntrySDASItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this EntrySDASItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this EntrySDASItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this EntrySDASItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def sdas_charge_rate_id(self):
        """Gets the sdas_charge_rate_id of this EntrySDASItem.  # noqa: E501

        SDAS Charge Rate  # noqa: E501

        :return: The sdas_charge_rate_id of this EntrySDASItem.  # noqa: E501
        :rtype: int
        """
        return self._sdas_charge_rate_id

    @sdas_charge_rate_id.setter
    def sdas_charge_rate_id(self, sdas_charge_rate_id):
        """Sets the sdas_charge_rate_id of this EntrySDASItem.

        SDAS Charge Rate  # noqa: E501

        :param sdas_charge_rate_id: The sdas_charge_rate_id of this EntrySDASItem.  # noqa: E501
        :type: int
        """

        self._sdas_charge_rate_id = sdas_charge_rate_id

    @property
    def enabled(self):
        """Gets the enabled of this EntrySDASItem.  # noqa: E501

        Enabled  # noqa: E501

        :return: The enabled of this EntrySDASItem.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this EntrySDASItem.

        Enabled  # noqa: E501

        :param enabled: The enabled of this EntrySDASItem.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def user_name(self):
        """Gets the user_name of this EntrySDASItem.  # noqa: E501

        User Name  # noqa: E501

        :return: The user_name of this EntrySDASItem.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this EntrySDASItem.

        User Name  # noqa: E501

        :param user_name: The user_name of this EntrySDASItem.  # noqa: E501
        :type: str
        """
        if user_name is not None and len(user_name) > 30:
            raise ValueError("Invalid value for `user_name`, length must be less than or equal to `30`")  # noqa: E501

        self._user_name = user_name

    @property
    def access_level(self):
        """Gets the access_level of this EntrySDASItem.  # noqa: E501

        Access Level  # noqa: E501

        :return: The access_level of this EntrySDASItem.  # noqa: E501
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this EntrySDASItem.

        Access Level  # noqa: E501

        :param access_level: The access_level of this EntrySDASItem.  # noqa: E501
        :type: str
        """

        self._access_level = access_level

    @property
    def machine_description(self):
        """Gets the machine_description of this EntrySDASItem.  # noqa: E501

        Machine Description  # noqa: E501

        :return: The machine_description of this EntrySDASItem.  # noqa: E501
        :rtype: str
        """
        return self._machine_description

    @machine_description.setter
    def machine_description(self, machine_description):
        """Sets the machine_description of this EntrySDASItem.

        Machine Description  # noqa: E501

        :param machine_description: The machine_description of this EntrySDASItem.  # noqa: E501
        :type: str
        """
        if machine_description is not None and len(machine_description) > 20:
            raise ValueError("Invalid value for `machine_description`, length must be less than or equal to `20`")  # noqa: E501

        self._machine_description = machine_description

    @property
    def machine_type(self):
        """Gets the machine_type of this EntrySDASItem.  # noqa: E501

        Machine Type  # noqa: E501

        :return: The machine_type of this EntrySDASItem.  # noqa: E501
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this EntrySDASItem.

        Machine Type  # noqa: E501

        :param machine_type: The machine_type of this EntrySDASItem.  # noqa: E501
        :type: str
        """
        if machine_type is not None and len(machine_type) > 20:
            raise ValueError("Invalid value for `machine_type`, length must be less than or equal to `20`")  # noqa: E501

        self._machine_type = machine_type

    @property
    def ip_address(self):
        """Gets the ip_address of this EntrySDASItem.  # noqa: E501

        IP Address  # noqa: E501

        :return: The ip_address of this EntrySDASItem.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this EntrySDASItem.

        IP Address  # noqa: E501

        :param ip_address: The ip_address of this EntrySDASItem.  # noqa: E501
        :type: str
        """
        if ip_address is not None and len(ip_address) > 20:
            raise ValueError("Invalid value for `ip_address`, length must be less than or equal to `20`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this EntrySDASItem.  # noqa: E501

        MAC Address  # noqa: E501

        :return: The mac_address of this EntrySDASItem.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this EntrySDASItem.

        MAC Address  # noqa: E501

        :param mac_address: The mac_address of this EntrySDASItem.  # noqa: E501
        :type: str
        """
        if mac_address is not None and len(mac_address) > 30:
            raise ValueError("Invalid value for `mac_address`, length must be less than or equal to `30`")  # noqa: E501

        self._mac_address = mac_address

    @property
    def operating_system(self):
        """Gets the operating_system of this EntrySDASItem.  # noqa: E501

        Operating System  # noqa: E501

        :return: The operating_system of this EntrySDASItem.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this EntrySDASItem.

        Operating System  # noqa: E501

        :param operating_system: The operating_system of this EntrySDASItem.  # noqa: E501
        :type: str
        """
        if operating_system is not None and len(operating_system) > 20:
            raise ValueError("Invalid value for `operating_system`, length must be less than or equal to `20`")  # noqa: E501

        self._operating_system = operating_system

    @property
    def date_enabled(self):
        """Gets the date_enabled of this EntrySDASItem.  # noqa: E501

        Date Enabled  # noqa: E501

        :return: The date_enabled of this EntrySDASItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_enabled

    @date_enabled.setter
    def date_enabled(self, date_enabled):
        """Sets the date_enabled of this EntrySDASItem.

        Date Enabled  # noqa: E501

        :param date_enabled: The date_enabled of this EntrySDASItem.  # noqa: E501
        :type: datetime
        """

        self._date_enabled = date_enabled

    @property
    def date_last_reset(self):
        """Gets the date_last_reset of this EntrySDASItem.  # noqa: E501

        Date Last Reset  # noqa: E501

        :return: The date_last_reset of this EntrySDASItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_last_reset

    @date_last_reset.setter
    def date_last_reset(self, date_last_reset):
        """Sets the date_last_reset of this EntrySDASItem.

        Date Last Reset  # noqa: E501

        :param date_last_reset: The date_last_reset of this EntrySDASItem.  # noqa: E501
        :type: datetime
        """

        self._date_last_reset = date_last_reset

    @property
    def monthly_allowance(self):
        """Gets the monthly_allowance of this EntrySDASItem.  # noqa: E501

        Monthly Allowance  # noqa: E501

        :return: The monthly_allowance of this EntrySDASItem.  # noqa: E501
        :rtype: str
        """
        return self._monthly_allowance

    @monthly_allowance.setter
    def monthly_allowance(self, monthly_allowance):
        """Sets the monthly_allowance of this EntrySDASItem.

        Monthly Allowance  # noqa: E501

        :param monthly_allowance: The monthly_allowance of this EntrySDASItem.  # noqa: E501
        :type: str
        """

        self._monthly_allowance = monthly_allowance

    @property
    def comments(self):
        """Gets the comments of this EntrySDASItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this EntrySDASItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this EntrySDASItem.

        Comments  # noqa: E501

        :param comments: The comments of this EntrySDASItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 100:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `100`")  # noqa: E501

        self._comments = comments

    @property
    def date_modified(self):
        """Gets the date_modified of this EntrySDASItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this EntrySDASItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this EntrySDASItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this EntrySDASItem.  # noqa: E501
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
        if not isinstance(other, EntrySDASItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
