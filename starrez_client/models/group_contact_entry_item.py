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


class GroupContactEntryItem(object):
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
        'group_contact_entry_id': 'int',
        'group_id': 'int',
        'entry_id': 'int',
        'responsibilities': 'str',
        'comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'group_contact_entry_id': 'GroupContactEntryID',
        'group_id': 'GroupID',
        'entry_id': 'EntryID',
        'responsibilities': 'Responsibilities',
        'comments': 'Comments',
        'date_modified': 'DateModified'
    }

    def __init__(self, group_contact_entry_id=None, group_id=None, entry_id=None, responsibilities=None, comments=None, date_modified=None):  # noqa: E501
        """GroupContactEntryItem - a model defined in Swagger"""  # noqa: E501

        self._group_contact_entry_id = None
        self._group_id = None
        self._entry_id = None
        self._responsibilities = None
        self._comments = None
        self._date_modified = None
        self.discriminator = None

        if group_contact_entry_id is not None:
            self.group_contact_entry_id = group_contact_entry_id
        if group_id is not None:
            self.group_id = group_id
        if entry_id is not None:
            self.entry_id = entry_id
        if responsibilities is not None:
            self.responsibilities = responsibilities
        if comments is not None:
            self.comments = comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def group_contact_entry_id(self):
        """Gets the group_contact_entry_id of this GroupContactEntryItem.  # noqa: E501

        Group Contact Entry  # noqa: E501

        :return: The group_contact_entry_id of this GroupContactEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._group_contact_entry_id

    @group_contact_entry_id.setter
    def group_contact_entry_id(self, group_contact_entry_id):
        """Sets the group_contact_entry_id of this GroupContactEntryItem.

        Group Contact Entry  # noqa: E501

        :param group_contact_entry_id: The group_contact_entry_id of this GroupContactEntryItem.  # noqa: E501
        :type: int
        """

        self._group_contact_entry_id = group_contact_entry_id

    @property
    def group_id(self):
        """Gets the group_id of this GroupContactEntryItem.  # noqa: E501

        Group  # noqa: E501

        :return: The group_id of this GroupContactEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupContactEntryItem.

        Group  # noqa: E501

        :param group_id: The group_id of this GroupContactEntryItem.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def entry_id(self):
        """Gets the entry_id of this GroupContactEntryItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this GroupContactEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this GroupContactEntryItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this GroupContactEntryItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def responsibilities(self):
        """Gets the responsibilities of this GroupContactEntryItem.  # noqa: E501

        Responsibilities  # noqa: E501

        :return: The responsibilities of this GroupContactEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._responsibilities

    @responsibilities.setter
    def responsibilities(self, responsibilities):
        """Sets the responsibilities of this GroupContactEntryItem.

        Responsibilities  # noqa: E501

        :param responsibilities: The responsibilities of this GroupContactEntryItem.  # noqa: E501
        :type: str
        """
        if responsibilities is not None and len(responsibilities) > 100:
            raise ValueError("Invalid value for `responsibilities`, length must be less than or equal to `100`")  # noqa: E501

        self._responsibilities = responsibilities

    @property
    def comments(self):
        """Gets the comments of this GroupContactEntryItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this GroupContactEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this GroupContactEntryItem.

        Comments  # noqa: E501

        :param comments: The comments of this GroupContactEntryItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 1000:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `1000`")  # noqa: E501

        self._comments = comments

    @property
    def date_modified(self):
        """Gets the date_modified of this GroupContactEntryItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this GroupContactEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this GroupContactEntryItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this GroupContactEntryItem.  # noqa: E501
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
        if not isinstance(other, GroupContactEntryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other