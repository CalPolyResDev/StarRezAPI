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


class RefundRequestBreakUpItem(object):
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
        'refund_request_break_up_id': 'int',
        'refund_request_id': 'int',
        'charge_group_id': 'int',
        'amount': 'str',
        'security_user_id': 'int',
        'created_by_security_user_id': 'int',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'refund_request_break_up_id': 'RefundRequestBreakUpID',
        'refund_request_id': 'RefundRequestID',
        'charge_group_id': 'ChargeGroupID',
        'amount': 'Amount',
        'security_user_id': 'SecurityUserID',
        'created_by_security_user_id': 'CreatedBy_SecurityUserID',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, refund_request_break_up_id=None, refund_request_id=None, charge_group_id=None, amount=None, security_user_id=None, created_by_security_user_id=None, date_created=None, date_modified=None):  # noqa: E501
        """RefundRequestBreakUpItem - a model defined in Swagger"""  # noqa: E501

        self._refund_request_break_up_id = None
        self._refund_request_id = None
        self._charge_group_id = None
        self._amount = None
        self._security_user_id = None
        self._created_by_security_user_id = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if refund_request_break_up_id is not None:
            self.refund_request_break_up_id = refund_request_break_up_id
        if refund_request_id is not None:
            self.refund_request_id = refund_request_id
        if charge_group_id is not None:
            self.charge_group_id = charge_group_id
        if amount is not None:
            self.amount = amount
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if created_by_security_user_id is not None:
            self.created_by_security_user_id = created_by_security_user_id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def refund_request_break_up_id(self):
        """Gets the refund_request_break_up_id of this RefundRequestBreakUpItem.  # noqa: E501

        Refund Request Break Up  # noqa: E501

        :return: The refund_request_break_up_id of this RefundRequestBreakUpItem.  # noqa: E501
        :rtype: int
        """
        return self._refund_request_break_up_id

    @refund_request_break_up_id.setter
    def refund_request_break_up_id(self, refund_request_break_up_id):
        """Sets the refund_request_break_up_id of this RefundRequestBreakUpItem.

        Refund Request Break Up  # noqa: E501

        :param refund_request_break_up_id: The refund_request_break_up_id of this RefundRequestBreakUpItem.  # noqa: E501
        :type: int
        """

        self._refund_request_break_up_id = refund_request_break_up_id

    @property
    def refund_request_id(self):
        """Gets the refund_request_id of this RefundRequestBreakUpItem.  # noqa: E501

        Refund Request  # noqa: E501

        :return: The refund_request_id of this RefundRequestBreakUpItem.  # noqa: E501
        :rtype: int
        """
        return self._refund_request_id

    @refund_request_id.setter
    def refund_request_id(self, refund_request_id):
        """Sets the refund_request_id of this RefundRequestBreakUpItem.

        Refund Request  # noqa: E501

        :param refund_request_id: The refund_request_id of this RefundRequestBreakUpItem.  # noqa: E501
        :type: int
        """

        self._refund_request_id = refund_request_id

    @property
    def charge_group_id(self):
        """Gets the charge_group_id of this RefundRequestBreakUpItem.  # noqa: E501

        Charge Group  # noqa: E501

        :return: The charge_group_id of this RefundRequestBreakUpItem.  # noqa: E501
        :rtype: int
        """
        return self._charge_group_id

    @charge_group_id.setter
    def charge_group_id(self, charge_group_id):
        """Sets the charge_group_id of this RefundRequestBreakUpItem.

        Charge Group  # noqa: E501

        :param charge_group_id: The charge_group_id of this RefundRequestBreakUpItem.  # noqa: E501
        :type: int
        """

        self._charge_group_id = charge_group_id

    @property
    def amount(self):
        """Gets the amount of this RefundRequestBreakUpItem.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this RefundRequestBreakUpItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RefundRequestBreakUpItem.

        Amount  # noqa: E501

        :param amount: The amount of this RefundRequestBreakUpItem.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def security_user_id(self):
        """Gets the security_user_id of this RefundRequestBreakUpItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this RefundRequestBreakUpItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this RefundRequestBreakUpItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this RefundRequestBreakUpItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def created_by_security_user_id(self):
        """Gets the created_by_security_user_id of this RefundRequestBreakUpItem.  # noqa: E501

        Created By Security User  # noqa: E501

        :return: The created_by_security_user_id of this RefundRequestBreakUpItem.  # noqa: E501
        :rtype: int
        """
        return self._created_by_security_user_id

    @created_by_security_user_id.setter
    def created_by_security_user_id(self, created_by_security_user_id):
        """Sets the created_by_security_user_id of this RefundRequestBreakUpItem.

        Created By Security User  # noqa: E501

        :param created_by_security_user_id: The created_by_security_user_id of this RefundRequestBreakUpItem.  # noqa: E501
        :type: int
        """

        self._created_by_security_user_id = created_by_security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this RefundRequestBreakUpItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this RefundRequestBreakUpItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this RefundRequestBreakUpItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this RefundRequestBreakUpItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this RefundRequestBreakUpItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RefundRequestBreakUpItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RefundRequestBreakUpItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RefundRequestBreakUpItem.  # noqa: E501
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
        if not isinstance(other, RefundRequestBreakUpItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other