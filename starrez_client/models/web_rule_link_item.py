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


class WebRuleLinkItem(object):
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
        'web_rule_link_id': 'int',
        'web_rule_id': 'int',
        'table_id': 'int',
        'table_name': 'str',
        'active': 'bool',
        'rule_link_order': 'int',
        'security_user_id': 'int',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'web_rule_link_id': 'WebRuleLinkID',
        'web_rule_id': 'WebRuleID',
        'table_id': 'TableID',
        'table_name': 'TableName',
        'active': 'Active',
        'rule_link_order': 'RuleLinkOrder',
        'security_user_id': 'SecurityUserID',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, web_rule_link_id=None, web_rule_id=None, table_id=None, table_name=None, active=None, rule_link_order=None, security_user_id=None, date_created=None, date_modified=None):  # noqa: E501
        """WebRuleLinkItem - a model defined in Swagger"""  # noqa: E501

        self._web_rule_link_id = None
        self._web_rule_id = None
        self._table_id = None
        self._table_name = None
        self._active = None
        self._rule_link_order = None
        self._security_user_id = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if web_rule_link_id is not None:
            self.web_rule_link_id = web_rule_link_id
        if web_rule_id is not None:
            self.web_rule_id = web_rule_id
        if table_id is not None:
            self.table_id = table_id
        if table_name is not None:
            self.table_name = table_name
        if active is not None:
            self.active = active
        if rule_link_order is not None:
            self.rule_link_order = rule_link_order
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def web_rule_link_id(self):
        """Gets the web_rule_link_id of this WebRuleLinkItem.  # noqa: E501

        Web Rule Link  # noqa: E501

        :return: The web_rule_link_id of this WebRuleLinkItem.  # noqa: E501
        :rtype: int
        """
        return self._web_rule_link_id

    @web_rule_link_id.setter
    def web_rule_link_id(self, web_rule_link_id):
        """Sets the web_rule_link_id of this WebRuleLinkItem.

        Web Rule Link  # noqa: E501

        :param web_rule_link_id: The web_rule_link_id of this WebRuleLinkItem.  # noqa: E501
        :type: int
        """

        self._web_rule_link_id = web_rule_link_id

    @property
    def web_rule_id(self):
        """Gets the web_rule_id of this WebRuleLinkItem.  # noqa: E501

        Web Rule  # noqa: E501

        :return: The web_rule_id of this WebRuleLinkItem.  # noqa: E501
        :rtype: int
        """
        return self._web_rule_id

    @web_rule_id.setter
    def web_rule_id(self, web_rule_id):
        """Sets the web_rule_id of this WebRuleLinkItem.

        Web Rule  # noqa: E501

        :param web_rule_id: The web_rule_id of this WebRuleLinkItem.  # noqa: E501
        :type: int
        """

        self._web_rule_id = web_rule_id

    @property
    def table_id(self):
        """Gets the table_id of this WebRuleLinkItem.  # noqa: E501

        Table  # noqa: E501

        :return: The table_id of this WebRuleLinkItem.  # noqa: E501
        :rtype: int
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this WebRuleLinkItem.

        Table  # noqa: E501

        :param table_id: The table_id of this WebRuleLinkItem.  # noqa: E501
        :type: int
        """

        self._table_id = table_id

    @property
    def table_name(self):
        """Gets the table_name of this WebRuleLinkItem.  # noqa: E501

        Table Name  # noqa: E501

        :return: The table_name of this WebRuleLinkItem.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this WebRuleLinkItem.

        Table Name  # noqa: E501

        :param table_name: The table_name of this WebRuleLinkItem.  # noqa: E501
        :type: str
        """
        if table_name is not None and len(table_name) > 20:
            raise ValueError("Invalid value for `table_name`, length must be less than or equal to `20`")  # noqa: E501

        self._table_name = table_name

    @property
    def active(self):
        """Gets the active of this WebRuleLinkItem.  # noqa: E501

        Active  # noqa: E501

        :return: The active of this WebRuleLinkItem.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this WebRuleLinkItem.

        Active  # noqa: E501

        :param active: The active of this WebRuleLinkItem.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def rule_link_order(self):
        """Gets the rule_link_order of this WebRuleLinkItem.  # noqa: E501

        Rule Link Order  # noqa: E501

        :return: The rule_link_order of this WebRuleLinkItem.  # noqa: E501
        :rtype: int
        """
        return self._rule_link_order

    @rule_link_order.setter
    def rule_link_order(self, rule_link_order):
        """Sets the rule_link_order of this WebRuleLinkItem.

        Rule Link Order  # noqa: E501

        :param rule_link_order: The rule_link_order of this WebRuleLinkItem.  # noqa: E501
        :type: int
        """

        self._rule_link_order = rule_link_order

    @property
    def security_user_id(self):
        """Gets the security_user_id of this WebRuleLinkItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this WebRuleLinkItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this WebRuleLinkItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this WebRuleLinkItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this WebRuleLinkItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this WebRuleLinkItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this WebRuleLinkItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this WebRuleLinkItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this WebRuleLinkItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this WebRuleLinkItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this WebRuleLinkItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this WebRuleLinkItem.  # noqa: E501
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
        if not isinstance(other, WebRuleLinkItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
