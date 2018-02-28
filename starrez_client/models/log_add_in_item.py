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


class LogAddInItem(object):
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
        'log_add_in_id': 'int',
        'log_date': 'str',
        'session_tag': 'int',
        'addin_filename': 'str',
        'log_event_type': 'str',
        'machine': 'str',
        'user_name': 'str',
        'method_name': 'str',
        'description': 'str',
        'table_name': 'str',
        'table_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'log_add_in_id': 'LogAddInID',
        'log_date': 'LogDate',
        'session_tag': 'SessionTag',
        'addin_filename': 'AddinFilename',
        'log_event_type': 'LogEventType',
        'machine': 'Machine',
        'user_name': 'UserName',
        'method_name': 'MethodName',
        'description': 'Description',
        'table_name': 'TableName',
        'table_id': 'TableID',
        'date_modified': 'DateModified'
    }

    def __init__(self, log_add_in_id=None, log_date=None, session_tag=None, addin_filename=None, log_event_type=None, machine=None, user_name=None, method_name=None, description=None, table_name=None, table_id=None, date_modified=None):  # noqa: E501
        """LogAddInItem - a model defined in Swagger"""  # noqa: E501

        self._log_add_in_id = None
        self._log_date = None
        self._session_tag = None
        self._addin_filename = None
        self._log_event_type = None
        self._machine = None
        self._user_name = None
        self._method_name = None
        self._description = None
        self._table_name = None
        self._table_id = None
        self._date_modified = None
        self.discriminator = None

        if log_add_in_id is not None:
            self.log_add_in_id = log_add_in_id
        if log_date is not None:
            self.log_date = log_date
        if session_tag is not None:
            self.session_tag = session_tag
        if addin_filename is not None:
            self.addin_filename = addin_filename
        if log_event_type is not None:
            self.log_event_type = log_event_type
        if machine is not None:
            self.machine = machine
        if user_name is not None:
            self.user_name = user_name
        if method_name is not None:
            self.method_name = method_name
        if description is not None:
            self.description = description
        if table_name is not None:
            self.table_name = table_name
        if table_id is not None:
            self.table_id = table_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def log_add_in_id(self):
        """Gets the log_add_in_id of this LogAddInItem.  # noqa: E501

        Log Add In  # noqa: E501

        :return: The log_add_in_id of this LogAddInItem.  # noqa: E501
        :rtype: int
        """
        return self._log_add_in_id

    @log_add_in_id.setter
    def log_add_in_id(self, log_add_in_id):
        """Sets the log_add_in_id of this LogAddInItem.

        Log Add In  # noqa: E501

        :param log_add_in_id: The log_add_in_id of this LogAddInItem.  # noqa: E501
        :type: int
        """

        self._log_add_in_id = log_add_in_id

    @property
    def log_date(self):
        """Gets the log_date of this LogAddInItem.  # noqa: E501

        Log Date  # noqa: E501

        :return: The log_date of this LogAddInItem.  # noqa: E501
        :rtype: str
        """
        return self._log_date

    @log_date.setter
    def log_date(self, log_date):
        """Sets the log_date of this LogAddInItem.

        Log Date  # noqa: E501

        :param log_date: The log_date of this LogAddInItem.  # noqa: E501
        :type: str
        """

        self._log_date = log_date

    @property
    def session_tag(self):
        """Gets the session_tag of this LogAddInItem.  # noqa: E501

        Session Tag  # noqa: E501

        :return: The session_tag of this LogAddInItem.  # noqa: E501
        :rtype: int
        """
        return self._session_tag

    @session_tag.setter
    def session_tag(self, session_tag):
        """Sets the session_tag of this LogAddInItem.

        Session Tag  # noqa: E501

        :param session_tag: The session_tag of this LogAddInItem.  # noqa: E501
        :type: int
        """

        self._session_tag = session_tag

    @property
    def addin_filename(self):
        """Gets the addin_filename of this LogAddInItem.  # noqa: E501

        Addin Filename  # noqa: E501

        :return: The addin_filename of this LogAddInItem.  # noqa: E501
        :rtype: str
        """
        return self._addin_filename

    @addin_filename.setter
    def addin_filename(self, addin_filename):
        """Sets the addin_filename of this LogAddInItem.

        Addin Filename  # noqa: E501

        :param addin_filename: The addin_filename of this LogAddInItem.  # noqa: E501
        :type: str
        """
        if addin_filename is not None and len(addin_filename) > 100:
            raise ValueError("Invalid value for `addin_filename`, length must be less than or equal to `100`")  # noqa: E501

        self._addin_filename = addin_filename

    @property
    def log_event_type(self):
        """Gets the log_event_type of this LogAddInItem.  # noqa: E501

        Log Event Type  # noqa: E501

        :return: The log_event_type of this LogAddInItem.  # noqa: E501
        :rtype: str
        """
        return self._log_event_type

    @log_event_type.setter
    def log_event_type(self, log_event_type):
        """Sets the log_event_type of this LogAddInItem.

        Log Event Type  # noqa: E501

        :param log_event_type: The log_event_type of this LogAddInItem.  # noqa: E501
        :type: str
        """
        if log_event_type is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', log_event_type):  # noqa: E501
            raise ValueError("Invalid value for `log_event_type`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._log_event_type = log_event_type

    @property
    def machine(self):
        """Gets the machine of this LogAddInItem.  # noqa: E501

        Machine  # noqa: E501

        :return: The machine of this LogAddInItem.  # noqa: E501
        :rtype: str
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """Sets the machine of this LogAddInItem.

        Machine  # noqa: E501

        :param machine: The machine of this LogAddInItem.  # noqa: E501
        :type: str
        """
        if machine is not None and len(machine) > 50:
            raise ValueError("Invalid value for `machine`, length must be less than or equal to `50`")  # noqa: E501

        self._machine = machine

    @property
    def user_name(self):
        """Gets the user_name of this LogAddInItem.  # noqa: E501

        User Name  # noqa: E501

        :return: The user_name of this LogAddInItem.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this LogAddInItem.

        User Name  # noqa: E501

        :param user_name: The user_name of this LogAddInItem.  # noqa: E501
        :type: str
        """
        if user_name is not None and len(user_name) > 30:
            raise ValueError("Invalid value for `user_name`, length must be less than or equal to `30`")  # noqa: E501

        self._user_name = user_name

    @property
    def method_name(self):
        """Gets the method_name of this LogAddInItem.  # noqa: E501

        Method Name  # noqa: E501

        :return: The method_name of this LogAddInItem.  # noqa: E501
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name):
        """Sets the method_name of this LogAddInItem.

        Method Name  # noqa: E501

        :param method_name: The method_name of this LogAddInItem.  # noqa: E501
        :type: str
        """
        if method_name is not None and len(method_name) > 100:
            raise ValueError("Invalid value for `method_name`, length must be less than or equal to `100`")  # noqa: E501

        self._method_name = method_name

    @property
    def description(self):
        """Gets the description of this LogAddInItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this LogAddInItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LogAddInItem.

        Description  # noqa: E501

        :param description: The description of this LogAddInItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 5000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `5000`")  # noqa: E501

        self._description = description

    @property
    def table_name(self):
        """Gets the table_name of this LogAddInItem.  # noqa: E501

        Table Name  # noqa: E501

        :return: The table_name of this LogAddInItem.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this LogAddInItem.

        Table Name  # noqa: E501

        :param table_name: The table_name of this LogAddInItem.  # noqa: E501
        :type: str
        """
        if table_name is not None and len(table_name) > 50:
            raise ValueError("Invalid value for `table_name`, length must be less than or equal to `50`")  # noqa: E501

        self._table_name = table_name

    @property
    def table_id(self):
        """Gets the table_id of this LogAddInItem.  # noqa: E501

        Table  # noqa: E501

        :return: The table_id of this LogAddInItem.  # noqa: E501
        :rtype: int
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this LogAddInItem.

        Table  # noqa: E501

        :param table_id: The table_id of this LogAddInItem.  # noqa: E501
        :type: int
        """

        self._table_id = table_id

    @property
    def date_modified(self):
        """Gets the date_modified of this LogAddInItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this LogAddInItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this LogAddInItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this LogAddInItem.  # noqa: E501
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
        if not isinstance(other, LogAddInItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other