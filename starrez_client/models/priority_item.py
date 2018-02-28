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


class PriorityItem(object):
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
        'priority_id': 'int',
        'description': 'str',
        'sort_order': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'priority_id': 'PriorityID',
        'description': 'Description',
        'sort_order': 'SortOrder',
        'date_modified': 'DateModified'
    }

    def __init__(self, priority_id=None, description=None, sort_order=None, date_modified=None):  # noqa: E501
        """PriorityItem - a model defined in Swagger"""  # noqa: E501

        self._priority_id = None
        self._description = None
        self._sort_order = None
        self._date_modified = None
        self.discriminator = None

        if priority_id is not None:
            self.priority_id = priority_id
        if description is not None:
            self.description = description
        if sort_order is not None:
            self.sort_order = sort_order
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def priority_id(self):
        """Gets the priority_id of this PriorityItem.  # noqa: E501

        Priority  # noqa: E501

        :return: The priority_id of this PriorityItem.  # noqa: E501
        :rtype: int
        """
        return self._priority_id

    @priority_id.setter
    def priority_id(self, priority_id):
        """Sets the priority_id of this PriorityItem.

        Priority  # noqa: E501

        :param priority_id: The priority_id of this PriorityItem.  # noqa: E501
        :type: int
        """

        self._priority_id = priority_id

    @property
    def description(self):
        """Gets the description of this PriorityItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this PriorityItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PriorityItem.

        Description  # noqa: E501

        :param description: The description of this PriorityItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 20:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `20`")  # noqa: E501

        self._description = description

    @property
    def sort_order(self):
        """Gets the sort_order of this PriorityItem.  # noqa: E501

        Sort Order  # noqa: E501

        :return: The sort_order of this PriorityItem.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this PriorityItem.

        Sort Order  # noqa: E501

        :param sort_order: The sort_order of this PriorityItem.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def date_modified(self):
        """Gets the date_modified of this PriorityItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this PriorityItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this PriorityItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this PriorityItem.  # noqa: E501
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
        if not isinstance(other, PriorityItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
