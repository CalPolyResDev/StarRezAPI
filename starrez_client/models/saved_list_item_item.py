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


class SavedListItemItem(object):
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
        'saved_list_item_id': 'int',
        'saved_list_id': 'int',
        'item_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'saved_list_item_id': 'SavedListItemID',
        'saved_list_id': 'SavedListID',
        'item_id': 'ItemID',
        'date_modified': 'DateModified'
    }

    def __init__(self, saved_list_item_id=None, saved_list_id=None, item_id=None, date_modified=None):  # noqa: E501
        """SavedListItemItem - a model defined in Swagger"""  # noqa: E501

        self._saved_list_item_id = None
        self._saved_list_id = None
        self._item_id = None
        self._date_modified = None
        self.discriminator = None

        if saved_list_item_id is not None:
            self.saved_list_item_id = saved_list_item_id
        if saved_list_id is not None:
            self.saved_list_id = saved_list_id
        if item_id is not None:
            self.item_id = item_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def saved_list_item_id(self):
        """Gets the saved_list_item_id of this SavedListItemItem.  # noqa: E501

        Saved List Item  # noqa: E501

        :return: The saved_list_item_id of this SavedListItemItem.  # noqa: E501
        :rtype: int
        """
        return self._saved_list_item_id

    @saved_list_item_id.setter
    def saved_list_item_id(self, saved_list_item_id):
        """Sets the saved_list_item_id of this SavedListItemItem.

        Saved List Item  # noqa: E501

        :param saved_list_item_id: The saved_list_item_id of this SavedListItemItem.  # noqa: E501
        :type: int
        """

        self._saved_list_item_id = saved_list_item_id

    @property
    def saved_list_id(self):
        """Gets the saved_list_id of this SavedListItemItem.  # noqa: E501

        Saved List  # noqa: E501

        :return: The saved_list_id of this SavedListItemItem.  # noqa: E501
        :rtype: int
        """
        return self._saved_list_id

    @saved_list_id.setter
    def saved_list_id(self, saved_list_id):
        """Sets the saved_list_id of this SavedListItemItem.

        Saved List  # noqa: E501

        :param saved_list_id: The saved_list_id of this SavedListItemItem.  # noqa: E501
        :type: int
        """

        self._saved_list_id = saved_list_id

    @property
    def item_id(self):
        """Gets the item_id of this SavedListItemItem.  # noqa: E501

        Item  # noqa: E501

        :return: The item_id of this SavedListItemItem.  # noqa: E501
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this SavedListItemItem.

        Item  # noqa: E501

        :param item_id: The item_id of this SavedListItemItem.  # noqa: E501
        :type: int
        """

        self._item_id = item_id

    @property
    def date_modified(self):
        """Gets the date_modified of this SavedListItemItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this SavedListItemItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SavedListItemItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this SavedListItemItem.  # noqa: E501
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
        if not isinstance(other, SavedListItemItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
