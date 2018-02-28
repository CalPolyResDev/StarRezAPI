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


class MealPlanSessionItem(object):
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
        'meal_plan_session_id': 'int',
        'meal_plan_id': 'int',
        'date_start': 'str',
        'date_end': 'str',
        'transaction_date_due': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'meal_plan_session_id': 'MealPlanSessionID',
        'meal_plan_id': 'MealPlanID',
        'date_start': 'DateStart',
        'date_end': 'DateEnd',
        'transaction_date_due': 'TransactionDateDue',
        'date_modified': 'DateModified'
    }

    def __init__(self, meal_plan_session_id=None, meal_plan_id=None, date_start=None, date_end=None, transaction_date_due=None, date_modified=None):  # noqa: E501
        """MealPlanSessionItem - a model defined in Swagger"""  # noqa: E501

        self._meal_plan_session_id = None
        self._meal_plan_id = None
        self._date_start = None
        self._date_end = None
        self._transaction_date_due = None
        self._date_modified = None
        self.discriminator = None

        if meal_plan_session_id is not None:
            self.meal_plan_session_id = meal_plan_session_id
        if meal_plan_id is not None:
            self.meal_plan_id = meal_plan_id
        if date_start is not None:
            self.date_start = date_start
        if date_end is not None:
            self.date_end = date_end
        if transaction_date_due is not None:
            self.transaction_date_due = transaction_date_due
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def meal_plan_session_id(self):
        """Gets the meal_plan_session_id of this MealPlanSessionItem.  # noqa: E501

        Meal Plan Session  # noqa: E501

        :return: The meal_plan_session_id of this MealPlanSessionItem.  # noqa: E501
        :rtype: int
        """
        return self._meal_plan_session_id

    @meal_plan_session_id.setter
    def meal_plan_session_id(self, meal_plan_session_id):
        """Sets the meal_plan_session_id of this MealPlanSessionItem.

        Meal Plan Session  # noqa: E501

        :param meal_plan_session_id: The meal_plan_session_id of this MealPlanSessionItem.  # noqa: E501
        :type: int
        """

        self._meal_plan_session_id = meal_plan_session_id

    @property
    def meal_plan_id(self):
        """Gets the meal_plan_id of this MealPlanSessionItem.  # noqa: E501

        Meal Plan  # noqa: E501

        :return: The meal_plan_id of this MealPlanSessionItem.  # noqa: E501
        :rtype: int
        """
        return self._meal_plan_id

    @meal_plan_id.setter
    def meal_plan_id(self, meal_plan_id):
        """Sets the meal_plan_id of this MealPlanSessionItem.

        Meal Plan  # noqa: E501

        :param meal_plan_id: The meal_plan_id of this MealPlanSessionItem.  # noqa: E501
        :type: int
        """

        self._meal_plan_id = meal_plan_id

    @property
    def date_start(self):
        """Gets the date_start of this MealPlanSessionItem.  # noqa: E501

        Date Start  # noqa: E501

        :return: The date_start of this MealPlanSessionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this MealPlanSessionItem.

        Date Start  # noqa: E501

        :param date_start: The date_start of this MealPlanSessionItem.  # noqa: E501
        :type: str
        """

        self._date_start = date_start

    @property
    def date_end(self):
        """Gets the date_end of this MealPlanSessionItem.  # noqa: E501

        Date End  # noqa: E501

        :return: The date_end of this MealPlanSessionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this MealPlanSessionItem.

        Date End  # noqa: E501

        :param date_end: The date_end of this MealPlanSessionItem.  # noqa: E501
        :type: str
        """

        self._date_end = date_end

    @property
    def transaction_date_due(self):
        """Gets the transaction_date_due of this MealPlanSessionItem.  # noqa: E501

        Transaction Date Due  # noqa: E501

        :return: The transaction_date_due of this MealPlanSessionItem.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date_due

    @transaction_date_due.setter
    def transaction_date_due(self, transaction_date_due):
        """Sets the transaction_date_due of this MealPlanSessionItem.

        Transaction Date Due  # noqa: E501

        :param transaction_date_due: The transaction_date_due of this MealPlanSessionItem.  # noqa: E501
        :type: str
        """

        self._transaction_date_due = transaction_date_due

    @property
    def date_modified(self):
        """Gets the date_modified of this MealPlanSessionItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this MealPlanSessionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this MealPlanSessionItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this MealPlanSessionItem.  # noqa: E501
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
        if not isinstance(other, MealPlanSessionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other