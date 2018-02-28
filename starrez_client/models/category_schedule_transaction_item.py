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


class CategoryScheduleTransactionItem(object):
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
        'category_schedule_transaction_id': 'int',
        'category_id': 'int',
        'transaction_template_id': 'int',
        'schedule_enabled_between_enum': 'str',
        'schedule_enum': 'str',
        'schedule_interval': 'int',
        'schedule_time_of_day': 'int',
        'schedule_day_in_week_enum': 'str',
        'schedule_date_start': 'str',
        'schedule_date_end': 'str',
        'schedule_date_last_start': 'str',
        'schedule_date_last_end': 'str',
        'schedule_range_start_object': 'str',
        'first_run_date': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'category_schedule_transaction_id': 'CategoryScheduleTransactionID',
        'category_id': 'CategoryID',
        'transaction_template_id': 'TransactionTemplateID',
        'schedule_enabled_between_enum': 'ScheduleEnabledBetweenEnum',
        'schedule_enum': 'ScheduleEnum',
        'schedule_interval': 'ScheduleInterval',
        'schedule_time_of_day': 'ScheduleTimeOfDay',
        'schedule_day_in_week_enum': 'Schedule_DayInWeekEnum',
        'schedule_date_start': 'ScheduleDateStart',
        'schedule_date_end': 'ScheduleDateEnd',
        'schedule_date_last_start': 'ScheduleDateLastStart',
        'schedule_date_last_end': 'ScheduleDateLastEnd',
        'schedule_range_start_object': 'ScheduleRangeStartObject',
        'first_run_date': 'FirstRunDate',
        'date_modified': 'DateModified'
    }

    def __init__(self, category_schedule_transaction_id=None, category_id=None, transaction_template_id=None, schedule_enabled_between_enum=None, schedule_enum=None, schedule_interval=None, schedule_time_of_day=None, schedule_day_in_week_enum=None, schedule_date_start=None, schedule_date_end=None, schedule_date_last_start=None, schedule_date_last_end=None, schedule_range_start_object=None, first_run_date=None, date_modified=None):  # noqa: E501
        """CategoryScheduleTransactionItem - a model defined in Swagger"""  # noqa: E501

        self._category_schedule_transaction_id = None
        self._category_id = None
        self._transaction_template_id = None
        self._schedule_enabled_between_enum = None
        self._schedule_enum = None
        self._schedule_interval = None
        self._schedule_time_of_day = None
        self._schedule_day_in_week_enum = None
        self._schedule_date_start = None
        self._schedule_date_end = None
        self._schedule_date_last_start = None
        self._schedule_date_last_end = None
        self._schedule_range_start_object = None
        self._first_run_date = None
        self._date_modified = None
        self.discriminator = None

        if category_schedule_transaction_id is not None:
            self.category_schedule_transaction_id = category_schedule_transaction_id
        if category_id is not None:
            self.category_id = category_id
        if transaction_template_id is not None:
            self.transaction_template_id = transaction_template_id
        if schedule_enabled_between_enum is not None:
            self.schedule_enabled_between_enum = schedule_enabled_between_enum
        if schedule_enum is not None:
            self.schedule_enum = schedule_enum
        if schedule_interval is not None:
            self.schedule_interval = schedule_interval
        if schedule_time_of_day is not None:
            self.schedule_time_of_day = schedule_time_of_day
        if schedule_day_in_week_enum is not None:
            self.schedule_day_in_week_enum = schedule_day_in_week_enum
        if schedule_date_start is not None:
            self.schedule_date_start = schedule_date_start
        if schedule_date_end is not None:
            self.schedule_date_end = schedule_date_end
        if schedule_date_last_start is not None:
            self.schedule_date_last_start = schedule_date_last_start
        if schedule_date_last_end is not None:
            self.schedule_date_last_end = schedule_date_last_end
        if schedule_range_start_object is not None:
            self.schedule_range_start_object = schedule_range_start_object
        if first_run_date is not None:
            self.first_run_date = first_run_date
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def category_schedule_transaction_id(self):
        """Gets the category_schedule_transaction_id of this CategoryScheduleTransactionItem.  # noqa: E501

        Category Schedule Transaction  # noqa: E501

        :return: The category_schedule_transaction_id of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._category_schedule_transaction_id

    @category_schedule_transaction_id.setter
    def category_schedule_transaction_id(self, category_schedule_transaction_id):
        """Sets the category_schedule_transaction_id of this CategoryScheduleTransactionItem.

        Category Schedule Transaction  # noqa: E501

        :param category_schedule_transaction_id: The category_schedule_transaction_id of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: int
        """

        self._category_schedule_transaction_id = category_schedule_transaction_id

    @property
    def category_id(self):
        """Gets the category_id of this CategoryScheduleTransactionItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this CategoryScheduleTransactionItem.

        Category  # noqa: E501

        :param category_id: The category_id of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def transaction_template_id(self):
        """Gets the transaction_template_id of this CategoryScheduleTransactionItem.  # noqa: E501

        Transaction Template  # noqa: E501

        :return: The transaction_template_id of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._transaction_template_id

    @transaction_template_id.setter
    def transaction_template_id(self, transaction_template_id):
        """Sets the transaction_template_id of this CategoryScheduleTransactionItem.

        Transaction Template  # noqa: E501

        :param transaction_template_id: The transaction_template_id of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: int
        """

        self._transaction_template_id = transaction_template_id

    @property
    def schedule_enabled_between_enum(self):
        """Gets the schedule_enabled_between_enum of this CategoryScheduleTransactionItem.  # noqa: E501

        Schedule Enabled Between  # noqa: E501

        :return: The schedule_enabled_between_enum of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_enabled_between_enum

    @schedule_enabled_between_enum.setter
    def schedule_enabled_between_enum(self, schedule_enabled_between_enum):
        """Sets the schedule_enabled_between_enum of this CategoryScheduleTransactionItem.

        Schedule Enabled Between  # noqa: E501

        :param schedule_enabled_between_enum: The schedule_enabled_between_enum of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: str
        """

        self._schedule_enabled_between_enum = schedule_enabled_between_enum

    @property
    def schedule_enum(self):
        """Gets the schedule_enum of this CategoryScheduleTransactionItem.  # noqa: E501

        Schedule  # noqa: E501

        :return: The schedule_enum of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_enum

    @schedule_enum.setter
    def schedule_enum(self, schedule_enum):
        """Sets the schedule_enum of this CategoryScheduleTransactionItem.

        Schedule  # noqa: E501

        :param schedule_enum: The schedule_enum of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: str
        """

        self._schedule_enum = schedule_enum

    @property
    def schedule_interval(self):
        """Gets the schedule_interval of this CategoryScheduleTransactionItem.  # noqa: E501

        Schedule Interval  # noqa: E501

        :return: The schedule_interval of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._schedule_interval

    @schedule_interval.setter
    def schedule_interval(self, schedule_interval):
        """Sets the schedule_interval of this CategoryScheduleTransactionItem.

        Schedule Interval  # noqa: E501

        :param schedule_interval: The schedule_interval of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: int
        """

        self._schedule_interval = schedule_interval

    @property
    def schedule_time_of_day(self):
        """Gets the schedule_time_of_day of this CategoryScheduleTransactionItem.  # noqa: E501

        Schedule Time Of Day  # noqa: E501

        :return: The schedule_time_of_day of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._schedule_time_of_day

    @schedule_time_of_day.setter
    def schedule_time_of_day(self, schedule_time_of_day):
        """Sets the schedule_time_of_day of this CategoryScheduleTransactionItem.

        Schedule Time Of Day  # noqa: E501

        :param schedule_time_of_day: The schedule_time_of_day of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: int
        """

        self._schedule_time_of_day = schedule_time_of_day

    @property
    def schedule_day_in_week_enum(self):
        """Gets the schedule_day_in_week_enum of this CategoryScheduleTransactionItem.  # noqa: E501

        Schedule Day In Week  # noqa: E501

        :return: The schedule_day_in_week_enum of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_day_in_week_enum

    @schedule_day_in_week_enum.setter
    def schedule_day_in_week_enum(self, schedule_day_in_week_enum):
        """Sets the schedule_day_in_week_enum of this CategoryScheduleTransactionItem.

        Schedule Day In Week  # noqa: E501

        :param schedule_day_in_week_enum: The schedule_day_in_week_enum of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: str
        """

        self._schedule_day_in_week_enum = schedule_day_in_week_enum

    @property
    def schedule_date_start(self):
        """Gets the schedule_date_start of this CategoryScheduleTransactionItem.  # noqa: E501

        Schedule Date Start  # noqa: E501

        :return: The schedule_date_start of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_date_start

    @schedule_date_start.setter
    def schedule_date_start(self, schedule_date_start):
        """Sets the schedule_date_start of this CategoryScheduleTransactionItem.

        Schedule Date Start  # noqa: E501

        :param schedule_date_start: The schedule_date_start of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: str
        """

        self._schedule_date_start = schedule_date_start

    @property
    def schedule_date_end(self):
        """Gets the schedule_date_end of this CategoryScheduleTransactionItem.  # noqa: E501

        Schedule Date End  # noqa: E501

        :return: The schedule_date_end of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_date_end

    @schedule_date_end.setter
    def schedule_date_end(self, schedule_date_end):
        """Sets the schedule_date_end of this CategoryScheduleTransactionItem.

        Schedule Date End  # noqa: E501

        :param schedule_date_end: The schedule_date_end of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: str
        """

        self._schedule_date_end = schedule_date_end

    @property
    def schedule_date_last_start(self):
        """Gets the schedule_date_last_start of this CategoryScheduleTransactionItem.  # noqa: E501

        Schedule Date Last Start  # noqa: E501

        :return: The schedule_date_last_start of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_date_last_start

    @schedule_date_last_start.setter
    def schedule_date_last_start(self, schedule_date_last_start):
        """Sets the schedule_date_last_start of this CategoryScheduleTransactionItem.

        Schedule Date Last Start  # noqa: E501

        :param schedule_date_last_start: The schedule_date_last_start of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: str
        """

        self._schedule_date_last_start = schedule_date_last_start

    @property
    def schedule_date_last_end(self):
        """Gets the schedule_date_last_end of this CategoryScheduleTransactionItem.  # noqa: E501

        Schedule Date Last End  # noqa: E501

        :return: The schedule_date_last_end of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_date_last_end

    @schedule_date_last_end.setter
    def schedule_date_last_end(self, schedule_date_last_end):
        """Sets the schedule_date_last_end of this CategoryScheduleTransactionItem.

        Schedule Date Last End  # noqa: E501

        :param schedule_date_last_end: The schedule_date_last_end of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: str
        """

        self._schedule_date_last_end = schedule_date_last_end

    @property
    def schedule_range_start_object(self):
        """Gets the schedule_range_start_object of this CategoryScheduleTransactionItem.  # noqa: E501

        Schedule Range Start Object  # noqa: E501

        :return: The schedule_range_start_object of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_range_start_object

    @schedule_range_start_object.setter
    def schedule_range_start_object(self, schedule_range_start_object):
        """Sets the schedule_range_start_object of this CategoryScheduleTransactionItem.

        Schedule Range Start Object  # noqa: E501

        :param schedule_range_start_object: The schedule_range_start_object of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: str
        """

        self._schedule_range_start_object = schedule_range_start_object

    @property
    def first_run_date(self):
        """Gets the first_run_date of this CategoryScheduleTransactionItem.  # noqa: E501

        First Run Date  # noqa: E501

        :return: The first_run_date of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._first_run_date

    @first_run_date.setter
    def first_run_date(self, first_run_date):
        """Sets the first_run_date of this CategoryScheduleTransactionItem.

        First Run Date  # noqa: E501

        :param first_run_date: The first_run_date of this CategoryScheduleTransactionItem.  # noqa: E501
        :type: str
        """

        self._first_run_date = first_run_date

    @property
    def date_modified(self):
        """Gets the date_modified of this CategoryScheduleTransactionItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this CategoryScheduleTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this CategoryScheduleTransactionItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this CategoryScheduleTransactionItem.  # noqa: E501
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
        if not isinstance(other, CategoryScheduleTransactionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
