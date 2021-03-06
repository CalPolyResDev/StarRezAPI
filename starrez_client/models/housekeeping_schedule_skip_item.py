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


class HousekeepingScheduleSkipItem(object):
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
        'housekeeping_schedule_skip_id': 'int',
        'housekeeping_id': 'int',
        'room_service_level': 'int',
        'schedule_enum': 'str',
        'schedule_interval': 'int',
        'schedule_day_in_week_enum': 'str',
        'skip_days': 'int',
        'comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'housekeeping_schedule_skip_id': 'HousekeepingScheduleSkipID',
        'housekeeping_id': 'HousekeepingID',
        'room_service_level': 'RoomServiceLevel',
        'schedule_enum': 'ScheduleEnum',
        'schedule_interval': 'ScheduleInterval',
        'schedule_day_in_week_enum': 'Schedule_DayInWeekEnum',
        'skip_days': 'SkipDays',
        'comments': 'Comments',
        'date_modified': 'DateModified'
    }

    def __init__(self, housekeeping_schedule_skip_id=None, housekeeping_id=None, room_service_level=None, schedule_enum=None, schedule_interval=None, schedule_day_in_week_enum=None, skip_days=None, comments=None, date_modified=None):  # noqa: E501
        """HousekeepingScheduleSkipItem - a model defined in Swagger"""  # noqa: E501

        self._housekeeping_schedule_skip_id = None
        self._housekeeping_id = None
        self._room_service_level = None
        self._schedule_enum = None
        self._schedule_interval = None
        self._schedule_day_in_week_enum = None
        self._skip_days = None
        self._comments = None
        self._date_modified = None
        self.discriminator = None

        if housekeeping_schedule_skip_id is not None:
            self.housekeeping_schedule_skip_id = housekeeping_schedule_skip_id
        if housekeeping_id is not None:
            self.housekeeping_id = housekeeping_id
        if room_service_level is not None:
            self.room_service_level = room_service_level
        if schedule_enum is not None:
            self.schedule_enum = schedule_enum
        if schedule_interval is not None:
            self.schedule_interval = schedule_interval
        if schedule_day_in_week_enum is not None:
            self.schedule_day_in_week_enum = schedule_day_in_week_enum
        if skip_days is not None:
            self.skip_days = skip_days
        if comments is not None:
            self.comments = comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def housekeeping_schedule_skip_id(self):
        """Gets the housekeeping_schedule_skip_id of this HousekeepingScheduleSkipItem.  # noqa: E501

        Housekeeping Schedule Skip  # noqa: E501

        :return: The housekeeping_schedule_skip_id of this HousekeepingScheduleSkipItem.  # noqa: E501
        :rtype: int
        """
        return self._housekeeping_schedule_skip_id

    @housekeeping_schedule_skip_id.setter
    def housekeeping_schedule_skip_id(self, housekeeping_schedule_skip_id):
        """Sets the housekeeping_schedule_skip_id of this HousekeepingScheduleSkipItem.

        Housekeeping Schedule Skip  # noqa: E501

        :param housekeeping_schedule_skip_id: The housekeeping_schedule_skip_id of this HousekeepingScheduleSkipItem.  # noqa: E501
        :type: int
        """

        self._housekeeping_schedule_skip_id = housekeeping_schedule_skip_id

    @property
    def housekeeping_id(self):
        """Gets the housekeeping_id of this HousekeepingScheduleSkipItem.  # noqa: E501

        Housekeeping  # noqa: E501

        :return: The housekeeping_id of this HousekeepingScheduleSkipItem.  # noqa: E501
        :rtype: int
        """
        return self._housekeeping_id

    @housekeeping_id.setter
    def housekeeping_id(self, housekeeping_id):
        """Sets the housekeeping_id of this HousekeepingScheduleSkipItem.

        Housekeeping  # noqa: E501

        :param housekeeping_id: The housekeeping_id of this HousekeepingScheduleSkipItem.  # noqa: E501
        :type: int
        """

        self._housekeeping_id = housekeeping_id

    @property
    def room_service_level(self):
        """Gets the room_service_level of this HousekeepingScheduleSkipItem.  # noqa: E501

        Room Service Level  # noqa: E501

        :return: The room_service_level of this HousekeepingScheduleSkipItem.  # noqa: E501
        :rtype: int
        """
        return self._room_service_level

    @room_service_level.setter
    def room_service_level(self, room_service_level):
        """Sets the room_service_level of this HousekeepingScheduleSkipItem.

        Room Service Level  # noqa: E501

        :param room_service_level: The room_service_level of this HousekeepingScheduleSkipItem.  # noqa: E501
        :type: int
        """

        self._room_service_level = room_service_level

    @property
    def schedule_enum(self):
        """Gets the schedule_enum of this HousekeepingScheduleSkipItem.  # noqa: E501

        Schedule  # noqa: E501

        :return: The schedule_enum of this HousekeepingScheduleSkipItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_enum

    @schedule_enum.setter
    def schedule_enum(self, schedule_enum):
        """Sets the schedule_enum of this HousekeepingScheduleSkipItem.

        Schedule  # noqa: E501

        :param schedule_enum: The schedule_enum of this HousekeepingScheduleSkipItem.  # noqa: E501
        :type: str
        """

        self._schedule_enum = schedule_enum

    @property
    def schedule_interval(self):
        """Gets the schedule_interval of this HousekeepingScheduleSkipItem.  # noqa: E501

        Schedule Interval  # noqa: E501

        :return: The schedule_interval of this HousekeepingScheduleSkipItem.  # noqa: E501
        :rtype: int
        """
        return self._schedule_interval

    @schedule_interval.setter
    def schedule_interval(self, schedule_interval):
        """Sets the schedule_interval of this HousekeepingScheduleSkipItem.

        Schedule Interval  # noqa: E501

        :param schedule_interval: The schedule_interval of this HousekeepingScheduleSkipItem.  # noqa: E501
        :type: int
        """

        self._schedule_interval = schedule_interval

    @property
    def schedule_day_in_week_enum(self):
        """Gets the schedule_day_in_week_enum of this HousekeepingScheduleSkipItem.  # noqa: E501

        Schedule Day In Week  # noqa: E501

        :return: The schedule_day_in_week_enum of this HousekeepingScheduleSkipItem.  # noqa: E501
        :rtype: str
        """
        return self._schedule_day_in_week_enum

    @schedule_day_in_week_enum.setter
    def schedule_day_in_week_enum(self, schedule_day_in_week_enum):
        """Sets the schedule_day_in_week_enum of this HousekeepingScheduleSkipItem.

        Schedule Day In Week  # noqa: E501

        :param schedule_day_in_week_enum: The schedule_day_in_week_enum of this HousekeepingScheduleSkipItem.  # noqa: E501
        :type: str
        """

        self._schedule_day_in_week_enum = schedule_day_in_week_enum

    @property
    def skip_days(self):
        """Gets the skip_days of this HousekeepingScheduleSkipItem.  # noqa: E501

        Skip Days  # noqa: E501

        :return: The skip_days of this HousekeepingScheduleSkipItem.  # noqa: E501
        :rtype: int
        """
        return self._skip_days

    @skip_days.setter
    def skip_days(self, skip_days):
        """Sets the skip_days of this HousekeepingScheduleSkipItem.

        Skip Days  # noqa: E501

        :param skip_days: The skip_days of this HousekeepingScheduleSkipItem.  # noqa: E501
        :type: int
        """

        self._skip_days = skip_days

    @property
    def comments(self):
        """Gets the comments of this HousekeepingScheduleSkipItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this HousekeepingScheduleSkipItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this HousekeepingScheduleSkipItem.

        Comments  # noqa: E501

        :param comments: The comments of this HousekeepingScheduleSkipItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 250:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `250`")  # noqa: E501

        self._comments = comments

    @property
    def date_modified(self):
        """Gets the date_modified of this HousekeepingScheduleSkipItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this HousekeepingScheduleSkipItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this HousekeepingScheduleSkipItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this HousekeepingScheduleSkipItem.  # noqa: E501
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
        if not isinstance(other, HousekeepingScheduleSkipItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
