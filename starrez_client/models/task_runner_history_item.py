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


class TaskRunnerHistoryItem(object):
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
        'task_runner_history_id': 'int',
        'task_runner_history_status_enum': 'str',
        'description': 'str',
        'class_name': 'str',
        'table_name': 'str',
        'table_id': 'int',
        'run_by_security_user_id': 'int',
        'machine_name': 'str',
        'run_by_machine_name': 'str',
        'date_start': 'str',
        'date_complete': 'str',
        'last_status_update': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'task_runner_history_id': 'TaskRunnerHistoryID',
        'task_runner_history_status_enum': 'TaskRunnerHistoryStatusEnum',
        'description': 'Description',
        'class_name': 'ClassName',
        'table_name': 'TableName',
        'table_id': 'TableID',
        'run_by_security_user_id': 'RunBy_SecurityUserID',
        'machine_name': 'MachineName',
        'run_by_machine_name': 'RunBy_MachineName',
        'date_start': 'DateStart',
        'date_complete': 'DateComplete',
        'last_status_update': 'LastStatusUpdate',
        'date_modified': 'DateModified'
    }

    def __init__(self, task_runner_history_id=None, task_runner_history_status_enum=None, description=None, class_name=None, table_name=None, table_id=None, run_by_security_user_id=None, machine_name=None, run_by_machine_name=None, date_start=None, date_complete=None, last_status_update=None, date_modified=None):  # noqa: E501
        """TaskRunnerHistoryItem - a model defined in Swagger"""  # noqa: E501

        self._task_runner_history_id = None
        self._task_runner_history_status_enum = None
        self._description = None
        self._class_name = None
        self._table_name = None
        self._table_id = None
        self._run_by_security_user_id = None
        self._machine_name = None
        self._run_by_machine_name = None
        self._date_start = None
        self._date_complete = None
        self._last_status_update = None
        self._date_modified = None
        self.discriminator = None

        if task_runner_history_id is not None:
            self.task_runner_history_id = task_runner_history_id
        if task_runner_history_status_enum is not None:
            self.task_runner_history_status_enum = task_runner_history_status_enum
        if description is not None:
            self.description = description
        if class_name is not None:
            self.class_name = class_name
        if table_name is not None:
            self.table_name = table_name
        if table_id is not None:
            self.table_id = table_id
        if run_by_security_user_id is not None:
            self.run_by_security_user_id = run_by_security_user_id
        if machine_name is not None:
            self.machine_name = machine_name
        if run_by_machine_name is not None:
            self.run_by_machine_name = run_by_machine_name
        if date_start is not None:
            self.date_start = date_start
        if date_complete is not None:
            self.date_complete = date_complete
        if last_status_update is not None:
            self.last_status_update = last_status_update
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def task_runner_history_id(self):
        """Gets the task_runner_history_id of this TaskRunnerHistoryItem.  # noqa: E501

        Task Runner History  # noqa: E501

        :return: The task_runner_history_id of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._task_runner_history_id

    @task_runner_history_id.setter
    def task_runner_history_id(self, task_runner_history_id):
        """Sets the task_runner_history_id of this TaskRunnerHistoryItem.

        Task Runner History  # noqa: E501

        :param task_runner_history_id: The task_runner_history_id of this TaskRunnerHistoryItem.  # noqa: E501
        :type: int
        """

        self._task_runner_history_id = task_runner_history_id

    @property
    def task_runner_history_status_enum(self):
        """Gets the task_runner_history_status_enum of this TaskRunnerHistoryItem.  # noqa: E501

        Task Runner History Status  # noqa: E501

        :return: The task_runner_history_status_enum of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._task_runner_history_status_enum

    @task_runner_history_status_enum.setter
    def task_runner_history_status_enum(self, task_runner_history_status_enum):
        """Sets the task_runner_history_status_enum of this TaskRunnerHistoryItem.

        Task Runner History Status  # noqa: E501

        :param task_runner_history_status_enum: The task_runner_history_status_enum of this TaskRunnerHistoryItem.  # noqa: E501
        :type: str
        """

        self._task_runner_history_status_enum = task_runner_history_status_enum

    @property
    def description(self):
        """Gets the description of this TaskRunnerHistoryItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskRunnerHistoryItem.

        Description  # noqa: E501

        :param description: The description of this TaskRunnerHistoryItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def class_name(self):
        """Gets the class_name of this TaskRunnerHistoryItem.  # noqa: E501

        Class Name  # noqa: E501

        :return: The class_name of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this TaskRunnerHistoryItem.

        Class Name  # noqa: E501

        :param class_name: The class_name of this TaskRunnerHistoryItem.  # noqa: E501
        :type: str
        """
        if class_name is not None and len(class_name) > 250:
            raise ValueError("Invalid value for `class_name`, length must be less than or equal to `250`")  # noqa: E501

        self._class_name = class_name

    @property
    def table_name(self):
        """Gets the table_name of this TaskRunnerHistoryItem.  # noqa: E501

        Table Name  # noqa: E501

        :return: The table_name of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this TaskRunnerHistoryItem.

        Table Name  # noqa: E501

        :param table_name: The table_name of this TaskRunnerHistoryItem.  # noqa: E501
        :type: str
        """
        if table_name is not None and len(table_name) > 50:
            raise ValueError("Invalid value for `table_name`, length must be less than or equal to `50`")  # noqa: E501

        self._table_name = table_name

    @property
    def table_id(self):
        """Gets the table_id of this TaskRunnerHistoryItem.  # noqa: E501

        Table  # noqa: E501

        :return: The table_id of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this TaskRunnerHistoryItem.

        Table  # noqa: E501

        :param table_id: The table_id of this TaskRunnerHistoryItem.  # noqa: E501
        :type: int
        """

        self._table_id = table_id

    @property
    def run_by_security_user_id(self):
        """Gets the run_by_security_user_id of this TaskRunnerHistoryItem.  # noqa: E501

        Run By Security User  # noqa: E501

        :return: The run_by_security_user_id of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._run_by_security_user_id

    @run_by_security_user_id.setter
    def run_by_security_user_id(self, run_by_security_user_id):
        """Sets the run_by_security_user_id of this TaskRunnerHistoryItem.

        Run By Security User  # noqa: E501

        :param run_by_security_user_id: The run_by_security_user_id of this TaskRunnerHistoryItem.  # noqa: E501
        :type: int
        """

        self._run_by_security_user_id = run_by_security_user_id

    @property
    def machine_name(self):
        """Gets the machine_name of this TaskRunnerHistoryItem.  # noqa: E501

        Machine Name  # noqa: E501

        :return: The machine_name of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this TaskRunnerHistoryItem.

        Machine Name  # noqa: E501

        :param machine_name: The machine_name of this TaskRunnerHistoryItem.  # noqa: E501
        :type: str
        """
        if machine_name is not None and len(machine_name) > 30:
            raise ValueError("Invalid value for `machine_name`, length must be less than or equal to `30`")  # noqa: E501

        self._machine_name = machine_name

    @property
    def run_by_machine_name(self):
        """Gets the run_by_machine_name of this TaskRunnerHistoryItem.  # noqa: E501

        Run By Machine Name  # noqa: E501

        :return: The run_by_machine_name of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._run_by_machine_name

    @run_by_machine_name.setter
    def run_by_machine_name(self, run_by_machine_name):
        """Sets the run_by_machine_name of this TaskRunnerHistoryItem.

        Run By Machine Name  # noqa: E501

        :param run_by_machine_name: The run_by_machine_name of this TaskRunnerHistoryItem.  # noqa: E501
        :type: str
        """
        if run_by_machine_name is not None and len(run_by_machine_name) > 30:
            raise ValueError("Invalid value for `run_by_machine_name`, length must be less than or equal to `30`")  # noqa: E501

        self._run_by_machine_name = run_by_machine_name

    @property
    def date_start(self):
        """Gets the date_start of this TaskRunnerHistoryItem.  # noqa: E501

        Date Start  # noqa: E501

        :return: The date_start of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this TaskRunnerHistoryItem.

        Date Start  # noqa: E501

        :param date_start: The date_start of this TaskRunnerHistoryItem.  # noqa: E501
        :type: str
        """

        self._date_start = date_start

    @property
    def date_complete(self):
        """Gets the date_complete of this TaskRunnerHistoryItem.  # noqa: E501

        Date Complete  # noqa: E501

        :return: The date_complete of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._date_complete

    @date_complete.setter
    def date_complete(self, date_complete):
        """Sets the date_complete of this TaskRunnerHistoryItem.

        Date Complete  # noqa: E501

        :param date_complete: The date_complete of this TaskRunnerHistoryItem.  # noqa: E501
        :type: str
        """

        self._date_complete = date_complete

    @property
    def last_status_update(self):
        """Gets the last_status_update of this TaskRunnerHistoryItem.  # noqa: E501

        Last Status Update  # noqa: E501

        :return: The last_status_update of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._last_status_update

    @last_status_update.setter
    def last_status_update(self, last_status_update):
        """Sets the last_status_update of this TaskRunnerHistoryItem.

        Last Status Update  # noqa: E501

        :param last_status_update: The last_status_update of this TaskRunnerHistoryItem.  # noqa: E501
        :type: str
        """
        if last_status_update is not None and len(last_status_update) > 200:
            raise ValueError("Invalid value for `last_status_update`, length must be less than or equal to `200`")  # noqa: E501

        self._last_status_update = last_status_update

    @property
    def date_modified(self):
        """Gets the date_modified of this TaskRunnerHistoryItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this TaskRunnerHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this TaskRunnerHistoryItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this TaskRunnerHistoryItem.  # noqa: E501
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
        if not isinstance(other, TaskRunnerHistoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other