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


class CalendarItem(object):
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
        'calendar_id': 'int',
        'calendar_date': 'date',
        'date_modified': 'str'
    }

    attribute_map = {
        'calendar_id': 'CalendarID',
        'calendar_date': 'CalendarDate',
        'date_modified': 'DateModified'
    }

    def __init__(self, calendar_id=None, calendar_date=None, date_modified=None):  # noqa: E501
        """CalendarItem - a model defined in Swagger"""  # noqa: E501

        self._calendar_id = None
        self._calendar_date = None
        self._date_modified = None
        self.discriminator = None

        if calendar_id is not None:
            self.calendar_id = calendar_id
        if calendar_date is not None:
            self.calendar_date = calendar_date
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def calendar_id(self):
        """Gets the calendar_id of this CalendarItem.  # noqa: E501

        Calendar  # noqa: E501

        :return: The calendar_id of this CalendarItem.  # noqa: E501
        :rtype: int
        """
        return self._calendar_id

    @calendar_id.setter
    def calendar_id(self, calendar_id):
        """Sets the calendar_id of this CalendarItem.

        Calendar  # noqa: E501

        :param calendar_id: The calendar_id of this CalendarItem.  # noqa: E501
        :type: int
        """

        self._calendar_id = calendar_id

    @property
    def calendar_date(self):
        """Gets the calendar_date of this CalendarItem.  # noqa: E501

        Calendar Date  # noqa: E501

        :return: The calendar_date of this CalendarItem.  # noqa: E501
        :rtype: date
        """
        return self._calendar_date

    @calendar_date.setter
    def calendar_date(self, calendar_date):
        """Sets the calendar_date of this CalendarItem.

        Calendar Date  # noqa: E501

        :param calendar_date: The calendar_date of this CalendarItem.  # noqa: E501
        :type: date
        """

        self._calendar_date = calendar_date

    @property
    def date_modified(self):
        """Gets the date_modified of this CalendarItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this CalendarItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this CalendarItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this CalendarItem.  # noqa: E501
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
        if not isinstance(other, CalendarItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other