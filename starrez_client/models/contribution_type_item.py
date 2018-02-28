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


class ContributionTypeItem(object):
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
        'contribution_type_id': 'int',
        'description': 'str',
        'comments': 'str',
        'category_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'contribution_type_id': 'ContributionTypeID',
        'description': 'Description',
        'comments': 'Comments',
        'category_id': 'CategoryID',
        'date_modified': 'DateModified'
    }

    def __init__(self, contribution_type_id=None, description=None, comments=None, category_id=None, date_modified=None):  # noqa: E501
        """ContributionTypeItem - a model defined in Swagger"""  # noqa: E501

        self._contribution_type_id = None
        self._description = None
        self._comments = None
        self._category_id = None
        self._date_modified = None
        self.discriminator = None

        if contribution_type_id is not None:
            self.contribution_type_id = contribution_type_id
        if description is not None:
            self.description = description
        if comments is not None:
            self.comments = comments
        if category_id is not None:
            self.category_id = category_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def contribution_type_id(self):
        """Gets the contribution_type_id of this ContributionTypeItem.  # noqa: E501

        Contribution Type  # noqa: E501

        :return: The contribution_type_id of this ContributionTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._contribution_type_id

    @contribution_type_id.setter
    def contribution_type_id(self, contribution_type_id):
        """Sets the contribution_type_id of this ContributionTypeItem.

        Contribution Type  # noqa: E501

        :param contribution_type_id: The contribution_type_id of this ContributionTypeItem.  # noqa: E501
        :type: int
        """

        self._contribution_type_id = contribution_type_id

    @property
    def description(self):
        """Gets the description of this ContributionTypeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ContributionTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ContributionTypeItem.

        Description  # noqa: E501

        :param description: The description of this ContributionTypeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def comments(self):
        """Gets the comments of this ContributionTypeItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this ContributionTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ContributionTypeItem.

        Comments  # noqa: E501

        :param comments: The comments of this ContributionTypeItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 500:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `500`")  # noqa: E501

        self._comments = comments

    @property
    def category_id(self):
        """Gets the category_id of this ContributionTypeItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this ContributionTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ContributionTypeItem.

        Category  # noqa: E501

        :param category_id: The category_id of this ContributionTypeItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def date_modified(self):
        """Gets the date_modified of this ContributionTypeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this ContributionTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ContributionTypeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this ContributionTypeItem.  # noqa: E501
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
        if not isinstance(other, ContributionTypeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
