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


class WaitListProfileItem(object):
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
        'wait_list_profile_id': 'int',
        'wait_list_id': 'int',
        'profile_item_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'wait_list_profile_id': 'WaitListProfileID',
        'wait_list_id': 'WaitListID',
        'profile_item_id': 'ProfileItemID',
        'date_modified': 'DateModified'
    }

    def __init__(self, wait_list_profile_id=None, wait_list_id=None, profile_item_id=None, date_modified=None):  # noqa: E501
        """WaitListProfileItem - a model defined in Swagger"""  # noqa: E501

        self._wait_list_profile_id = None
        self._wait_list_id = None
        self._profile_item_id = None
        self._date_modified = None
        self.discriminator = None

        if wait_list_profile_id is not None:
            self.wait_list_profile_id = wait_list_profile_id
        if wait_list_id is not None:
            self.wait_list_id = wait_list_id
        if profile_item_id is not None:
            self.profile_item_id = profile_item_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def wait_list_profile_id(self):
        """Gets the wait_list_profile_id of this WaitListProfileItem.  # noqa: E501

        Wait List Profile  # noqa: E501

        :return: The wait_list_profile_id of this WaitListProfileItem.  # noqa: E501
        :rtype: int
        """
        return self._wait_list_profile_id

    @wait_list_profile_id.setter
    def wait_list_profile_id(self, wait_list_profile_id):
        """Sets the wait_list_profile_id of this WaitListProfileItem.

        Wait List Profile  # noqa: E501

        :param wait_list_profile_id: The wait_list_profile_id of this WaitListProfileItem.  # noqa: E501
        :type: int
        """

        self._wait_list_profile_id = wait_list_profile_id

    @property
    def wait_list_id(self):
        """Gets the wait_list_id of this WaitListProfileItem.  # noqa: E501

        Wait List  # noqa: E501

        :return: The wait_list_id of this WaitListProfileItem.  # noqa: E501
        :rtype: int
        """
        return self._wait_list_id

    @wait_list_id.setter
    def wait_list_id(self, wait_list_id):
        """Sets the wait_list_id of this WaitListProfileItem.

        Wait List  # noqa: E501

        :param wait_list_id: The wait_list_id of this WaitListProfileItem.  # noqa: E501
        :type: int
        """

        self._wait_list_id = wait_list_id

    @property
    def profile_item_id(self):
        """Gets the profile_item_id of this WaitListProfileItem.  # noqa: E501

        Profile Item  # noqa: E501

        :return: The profile_item_id of this WaitListProfileItem.  # noqa: E501
        :rtype: int
        """
        return self._profile_item_id

    @profile_item_id.setter
    def profile_item_id(self, profile_item_id):
        """Sets the profile_item_id of this WaitListProfileItem.

        Profile Item  # noqa: E501

        :param profile_item_id: The profile_item_id of this WaitListProfileItem.  # noqa: E501
        :type: int
        """

        self._profile_item_id = profile_item_id

    @property
    def date_modified(self):
        """Gets the date_modified of this WaitListProfileItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this WaitListProfileItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this WaitListProfileItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this WaitListProfileItem.  # noqa: E501
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
        if not isinstance(other, WaitListProfileItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other