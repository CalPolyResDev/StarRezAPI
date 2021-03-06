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


class LogInterfaceItem(object):
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
        'log_interface_id': 'int',
        'interface_id': 'int',
        'interface_application_id': 'int',
        'interface_action_enum': 'str',
        'entry_id': 'int',
        'pin_number': 'int',
        'room_space_id': 'int',
        'extension_id': 'str',
        'old_room_space_id': 'int',
        'old_extension_id': 'str',
        'log_date': 'str',
        'log_actioned_date': 'str',
        'entry_name': 'str',
        'comments': 'str',
        'machine_name': 'str',
        'username': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'log_interface_id': 'LogInterfaceID',
        'interface_id': 'InterfaceID',
        'interface_application_id': 'InterfaceApplicationID',
        'interface_action_enum': 'InterfaceActionEnum',
        'entry_id': 'EntryID',
        'pin_number': 'PinNumber',
        'room_space_id': 'RoomSpaceID',
        'extension_id': 'ExtensionID',
        'old_room_space_id': 'Old_RoomSpaceID',
        'old_extension_id': 'Old_ExtensionID',
        'log_date': 'LogDate',
        'log_actioned_date': 'LogActionedDate',
        'entry_name': 'EntryName',
        'comments': 'Comments',
        'machine_name': 'MachineName',
        'username': 'Username',
        'date_modified': 'DateModified'
    }

    def __init__(self, log_interface_id=None, interface_id=None, interface_application_id=None, interface_action_enum=None, entry_id=None, pin_number=None, room_space_id=None, extension_id=None, old_room_space_id=None, old_extension_id=None, log_date=None, log_actioned_date=None, entry_name=None, comments=None, machine_name=None, username=None, date_modified=None):  # noqa: E501
        """LogInterfaceItem - a model defined in Swagger"""  # noqa: E501

        self._log_interface_id = None
        self._interface_id = None
        self._interface_application_id = None
        self._interface_action_enum = None
        self._entry_id = None
        self._pin_number = None
        self._room_space_id = None
        self._extension_id = None
        self._old_room_space_id = None
        self._old_extension_id = None
        self._log_date = None
        self._log_actioned_date = None
        self._entry_name = None
        self._comments = None
        self._machine_name = None
        self._username = None
        self._date_modified = None
        self.discriminator = None

        if log_interface_id is not None:
            self.log_interface_id = log_interface_id
        if interface_id is not None:
            self.interface_id = interface_id
        if interface_application_id is not None:
            self.interface_application_id = interface_application_id
        if interface_action_enum is not None:
            self.interface_action_enum = interface_action_enum
        if entry_id is not None:
            self.entry_id = entry_id
        if pin_number is not None:
            self.pin_number = pin_number
        if room_space_id is not None:
            self.room_space_id = room_space_id
        if extension_id is not None:
            self.extension_id = extension_id
        if old_room_space_id is not None:
            self.old_room_space_id = old_room_space_id
        if old_extension_id is not None:
            self.old_extension_id = old_extension_id
        if log_date is not None:
            self.log_date = log_date
        if log_actioned_date is not None:
            self.log_actioned_date = log_actioned_date
        if entry_name is not None:
            self.entry_name = entry_name
        if comments is not None:
            self.comments = comments
        if machine_name is not None:
            self.machine_name = machine_name
        if username is not None:
            self.username = username
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def log_interface_id(self):
        """Gets the log_interface_id of this LogInterfaceItem.  # noqa: E501

        Log Interface  # noqa: E501

        :return: The log_interface_id of this LogInterfaceItem.  # noqa: E501
        :rtype: int
        """
        return self._log_interface_id

    @log_interface_id.setter
    def log_interface_id(self, log_interface_id):
        """Sets the log_interface_id of this LogInterfaceItem.

        Log Interface  # noqa: E501

        :param log_interface_id: The log_interface_id of this LogInterfaceItem.  # noqa: E501
        :type: int
        """

        self._log_interface_id = log_interface_id

    @property
    def interface_id(self):
        """Gets the interface_id of this LogInterfaceItem.  # noqa: E501

        Interface  # noqa: E501

        :return: The interface_id of this LogInterfaceItem.  # noqa: E501
        :rtype: int
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """Sets the interface_id of this LogInterfaceItem.

        Interface  # noqa: E501

        :param interface_id: The interface_id of this LogInterfaceItem.  # noqa: E501
        :type: int
        """

        self._interface_id = interface_id

    @property
    def interface_application_id(self):
        """Gets the interface_application_id of this LogInterfaceItem.  # noqa: E501

        Interface Application  # noqa: E501

        :return: The interface_application_id of this LogInterfaceItem.  # noqa: E501
        :rtype: int
        """
        return self._interface_application_id

    @interface_application_id.setter
    def interface_application_id(self, interface_application_id):
        """Sets the interface_application_id of this LogInterfaceItem.

        Interface Application  # noqa: E501

        :param interface_application_id: The interface_application_id of this LogInterfaceItem.  # noqa: E501
        :type: int
        """

        self._interface_application_id = interface_application_id

    @property
    def interface_action_enum(self):
        """Gets the interface_action_enum of this LogInterfaceItem.  # noqa: E501

        Interface Action  # noqa: E501

        :return: The interface_action_enum of this LogInterfaceItem.  # noqa: E501
        :rtype: str
        """
        return self._interface_action_enum

    @interface_action_enum.setter
    def interface_action_enum(self, interface_action_enum):
        """Sets the interface_action_enum of this LogInterfaceItem.

        Interface Action  # noqa: E501

        :param interface_action_enum: The interface_action_enum of this LogInterfaceItem.  # noqa: E501
        :type: str
        """

        self._interface_action_enum = interface_action_enum

    @property
    def entry_id(self):
        """Gets the entry_id of this LogInterfaceItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this LogInterfaceItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this LogInterfaceItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this LogInterfaceItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def pin_number(self):
        """Gets the pin_number of this LogInterfaceItem.  # noqa: E501

        Pin Number  # noqa: E501

        :return: The pin_number of this LogInterfaceItem.  # noqa: E501
        :rtype: int
        """
        return self._pin_number

    @pin_number.setter
    def pin_number(self, pin_number):
        """Sets the pin_number of this LogInterfaceItem.

        Pin Number  # noqa: E501

        :param pin_number: The pin_number of this LogInterfaceItem.  # noqa: E501
        :type: int
        """

        self._pin_number = pin_number

    @property
    def room_space_id(self):
        """Gets the room_space_id of this LogInterfaceItem.  # noqa: E501

        Room Space  # noqa: E501

        :return: The room_space_id of this LogInterfaceItem.  # noqa: E501
        :rtype: int
        """
        return self._room_space_id

    @room_space_id.setter
    def room_space_id(self, room_space_id):
        """Sets the room_space_id of this LogInterfaceItem.

        Room Space  # noqa: E501

        :param room_space_id: The room_space_id of this LogInterfaceItem.  # noqa: E501
        :type: int
        """

        self._room_space_id = room_space_id

    @property
    def extension_id(self):
        """Gets the extension_id of this LogInterfaceItem.  # noqa: E501

        Extension  # noqa: E501

        :return: The extension_id of this LogInterfaceItem.  # noqa: E501
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this LogInterfaceItem.

        Extension  # noqa: E501

        :param extension_id: The extension_id of this LogInterfaceItem.  # noqa: E501
        :type: str
        """
        if extension_id is not None and len(extension_id) > 10:
            raise ValueError("Invalid value for `extension_id`, length must be less than or equal to `10`")  # noqa: E501

        self._extension_id = extension_id

    @property
    def old_room_space_id(self):
        """Gets the old_room_space_id of this LogInterfaceItem.  # noqa: E501

        Old Room Space  # noqa: E501

        :return: The old_room_space_id of this LogInterfaceItem.  # noqa: E501
        :rtype: int
        """
        return self._old_room_space_id

    @old_room_space_id.setter
    def old_room_space_id(self, old_room_space_id):
        """Sets the old_room_space_id of this LogInterfaceItem.

        Old Room Space  # noqa: E501

        :param old_room_space_id: The old_room_space_id of this LogInterfaceItem.  # noqa: E501
        :type: int
        """

        self._old_room_space_id = old_room_space_id

    @property
    def old_extension_id(self):
        """Gets the old_extension_id of this LogInterfaceItem.  # noqa: E501

        Old Extension  # noqa: E501

        :return: The old_extension_id of this LogInterfaceItem.  # noqa: E501
        :rtype: str
        """
        return self._old_extension_id

    @old_extension_id.setter
    def old_extension_id(self, old_extension_id):
        """Sets the old_extension_id of this LogInterfaceItem.

        Old Extension  # noqa: E501

        :param old_extension_id: The old_extension_id of this LogInterfaceItem.  # noqa: E501
        :type: str
        """
        if old_extension_id is not None and len(old_extension_id) > 10:
            raise ValueError("Invalid value for `old_extension_id`, length must be less than or equal to `10`")  # noqa: E501

        self._old_extension_id = old_extension_id

    @property
    def log_date(self):
        """Gets the log_date of this LogInterfaceItem.  # noqa: E501

        Log Date  # noqa: E501

        :return: The log_date of this LogInterfaceItem.  # noqa: E501
        :rtype: str
        """
        return self._log_date

    @log_date.setter
    def log_date(self, log_date):
        """Sets the log_date of this LogInterfaceItem.

        Log Date  # noqa: E501

        :param log_date: The log_date of this LogInterfaceItem.  # noqa: E501
        :type: str
        """

        self._log_date = log_date

    @property
    def log_actioned_date(self):
        """Gets the log_actioned_date of this LogInterfaceItem.  # noqa: E501

        Log Actioned Date  # noqa: E501

        :return: The log_actioned_date of this LogInterfaceItem.  # noqa: E501
        :rtype: str
        """
        return self._log_actioned_date

    @log_actioned_date.setter
    def log_actioned_date(self, log_actioned_date):
        """Sets the log_actioned_date of this LogInterfaceItem.

        Log Actioned Date  # noqa: E501

        :param log_actioned_date: The log_actioned_date of this LogInterfaceItem.  # noqa: E501
        :type: str
        """

        self._log_actioned_date = log_actioned_date

    @property
    def entry_name(self):
        """Gets the entry_name of this LogInterfaceItem.  # noqa: E501

        Entry Name  # noqa: E501

        :return: The entry_name of this LogInterfaceItem.  # noqa: E501
        :rtype: str
        """
        return self._entry_name

    @entry_name.setter
    def entry_name(self, entry_name):
        """Sets the entry_name of this LogInterfaceItem.

        Entry Name  # noqa: E501

        :param entry_name: The entry_name of this LogInterfaceItem.  # noqa: E501
        :type: str
        """
        if entry_name is not None and len(entry_name) > 40:
            raise ValueError("Invalid value for `entry_name`, length must be less than or equal to `40`")  # noqa: E501

        self._entry_name = entry_name

    @property
    def comments(self):
        """Gets the comments of this LogInterfaceItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this LogInterfaceItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this LogInterfaceItem.

        Comments  # noqa: E501

        :param comments: The comments of this LogInterfaceItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 500:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `500`")  # noqa: E501

        self._comments = comments

    @property
    def machine_name(self):
        """Gets the machine_name of this LogInterfaceItem.  # noqa: E501

        Machine Name  # noqa: E501

        :return: The machine_name of this LogInterfaceItem.  # noqa: E501
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this LogInterfaceItem.

        Machine Name  # noqa: E501

        :param machine_name: The machine_name of this LogInterfaceItem.  # noqa: E501
        :type: str
        """
        if machine_name is not None and len(machine_name) > 30:
            raise ValueError("Invalid value for `machine_name`, length must be less than or equal to `30`")  # noqa: E501

        self._machine_name = machine_name

    @property
    def username(self):
        """Gets the username of this LogInterfaceItem.  # noqa: E501

        Username  # noqa: E501

        :return: The username of this LogInterfaceItem.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this LogInterfaceItem.

        Username  # noqa: E501

        :param username: The username of this LogInterfaceItem.  # noqa: E501
        :type: str
        """
        if username is not None and len(username) > 30:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `30`")  # noqa: E501

        self._username = username

    @property
    def date_modified(self):
        """Gets the date_modified of this LogInterfaceItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this LogInterfaceItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this LogInterfaceItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this LogInterfaceItem.  # noqa: E501
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
        if not isinstance(other, LogInterfaceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
