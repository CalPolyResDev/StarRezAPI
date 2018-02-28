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


class PaymentTypeItem(object):
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
        'payment_type_id': 'int',
        'record_type_enum': 'str',
        'description': 'str',
        'category_id': 'int',
        'payment_method_enum': 'str',
        'account_receivable_gl_posting_id': 'int',
        'bank_gl_posting_id': 'int',
        'refund_chq': 'bool',
        'group_by': 'str',
        'credit_card_surcharge': 'str',
        'ccs_charge_item_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'payment_type_id': 'PaymentTypeID',
        'record_type_enum': 'RecordTypeEnum',
        'description': 'Description',
        'category_id': 'CategoryID',
        'payment_method_enum': 'PaymentMethodEnum',
        'account_receivable_gl_posting_id': 'AccountReceivable_GLPostingID',
        'bank_gl_posting_id': 'Bank_GLPostingID',
        'refund_chq': 'RefundChq',
        'group_by': 'GroupBy',
        'credit_card_surcharge': 'CreditCardSurcharge',
        'ccs_charge_item_id': 'CCS_ChargeItemID',
        'date_modified': 'DateModified'
    }

    def __init__(self, payment_type_id=None, record_type_enum=None, description=None, category_id=None, payment_method_enum=None, account_receivable_gl_posting_id=None, bank_gl_posting_id=None, refund_chq=None, group_by=None, credit_card_surcharge=None, ccs_charge_item_id=None, date_modified=None):  # noqa: E501
        """PaymentTypeItem - a model defined in Swagger"""  # noqa: E501

        self._payment_type_id = None
        self._record_type_enum = None
        self._description = None
        self._category_id = None
        self._payment_method_enum = None
        self._account_receivable_gl_posting_id = None
        self._bank_gl_posting_id = None
        self._refund_chq = None
        self._group_by = None
        self._credit_card_surcharge = None
        self._ccs_charge_item_id = None
        self._date_modified = None
        self.discriminator = None

        if payment_type_id is not None:
            self.payment_type_id = payment_type_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if description is not None:
            self.description = description
        if category_id is not None:
            self.category_id = category_id
        if payment_method_enum is not None:
            self.payment_method_enum = payment_method_enum
        if account_receivable_gl_posting_id is not None:
            self.account_receivable_gl_posting_id = account_receivable_gl_posting_id
        if bank_gl_posting_id is not None:
            self.bank_gl_posting_id = bank_gl_posting_id
        if refund_chq is not None:
            self.refund_chq = refund_chq
        if group_by is not None:
            self.group_by = group_by
        if credit_card_surcharge is not None:
            self.credit_card_surcharge = credit_card_surcharge
        if ccs_charge_item_id is not None:
            self.ccs_charge_item_id = ccs_charge_item_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def payment_type_id(self):
        """Gets the payment_type_id of this PaymentTypeItem.  # noqa: E501

        Payment Type  # noqa: E501

        :return: The payment_type_id of this PaymentTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._payment_type_id

    @payment_type_id.setter
    def payment_type_id(self, payment_type_id):
        """Sets the payment_type_id of this PaymentTypeItem.

        Payment Type  # noqa: E501

        :param payment_type_id: The payment_type_id of this PaymentTypeItem.  # noqa: E501
        :type: int
        """

        self._payment_type_id = payment_type_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this PaymentTypeItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this PaymentTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this PaymentTypeItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this PaymentTypeItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def description(self):
        """Gets the description of this PaymentTypeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this PaymentTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentTypeItem.

        Description  # noqa: E501

        :param description: The description of this PaymentTypeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 30:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `30`")  # noqa: E501

        self._description = description

    @property
    def category_id(self):
        """Gets the category_id of this PaymentTypeItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this PaymentTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this PaymentTypeItem.

        Category  # noqa: E501

        :param category_id: The category_id of this PaymentTypeItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def payment_method_enum(self):
        """Gets the payment_method_enum of this PaymentTypeItem.  # noqa: E501

        Payment Method  # noqa: E501

        :return: The payment_method_enum of this PaymentTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_enum

    @payment_method_enum.setter
    def payment_method_enum(self, payment_method_enum):
        """Sets the payment_method_enum of this PaymentTypeItem.

        Payment Method  # noqa: E501

        :param payment_method_enum: The payment_method_enum of this PaymentTypeItem.  # noqa: E501
        :type: str
        """

        self._payment_method_enum = payment_method_enum

    @property
    def account_receivable_gl_posting_id(self):
        """Gets the account_receivable_gl_posting_id of this PaymentTypeItem.  # noqa: E501

        Account Receivable GL Posting  # noqa: E501

        :return: The account_receivable_gl_posting_id of this PaymentTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._account_receivable_gl_posting_id

    @account_receivable_gl_posting_id.setter
    def account_receivable_gl_posting_id(self, account_receivable_gl_posting_id):
        """Sets the account_receivable_gl_posting_id of this PaymentTypeItem.

        Account Receivable GL Posting  # noqa: E501

        :param account_receivable_gl_posting_id: The account_receivable_gl_posting_id of this PaymentTypeItem.  # noqa: E501
        :type: int
        """

        self._account_receivable_gl_posting_id = account_receivable_gl_posting_id

    @property
    def bank_gl_posting_id(self):
        """Gets the bank_gl_posting_id of this PaymentTypeItem.  # noqa: E501

        Bank GL Posting  # noqa: E501

        :return: The bank_gl_posting_id of this PaymentTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._bank_gl_posting_id

    @bank_gl_posting_id.setter
    def bank_gl_posting_id(self, bank_gl_posting_id):
        """Sets the bank_gl_posting_id of this PaymentTypeItem.

        Bank GL Posting  # noqa: E501

        :param bank_gl_posting_id: The bank_gl_posting_id of this PaymentTypeItem.  # noqa: E501
        :type: int
        """

        self._bank_gl_posting_id = bank_gl_posting_id

    @property
    def refund_chq(self):
        """Gets the refund_chq of this PaymentTypeItem.  # noqa: E501

        Refund Chq  # noqa: E501

        :return: The refund_chq of this PaymentTypeItem.  # noqa: E501
        :rtype: bool
        """
        return self._refund_chq

    @refund_chq.setter
    def refund_chq(self, refund_chq):
        """Sets the refund_chq of this PaymentTypeItem.

        Refund Chq  # noqa: E501

        :param refund_chq: The refund_chq of this PaymentTypeItem.  # noqa: E501
        :type: bool
        """

        self._refund_chq = refund_chq

    @property
    def group_by(self):
        """Gets the group_by of this PaymentTypeItem.  # noqa: E501

        Group By  # noqa: E501

        :return: The group_by of this PaymentTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this PaymentTypeItem.

        Group By  # noqa: E501

        :param group_by: The group_by of this PaymentTypeItem.  # noqa: E501
        :type: str
        """
        if group_by is not None and len(group_by) > 20:
            raise ValueError("Invalid value for `group_by`, length must be less than or equal to `20`")  # noqa: E501

        self._group_by = group_by

    @property
    def credit_card_surcharge(self):
        """Gets the credit_card_surcharge of this PaymentTypeItem.  # noqa: E501

        Credit Card Surcharge  # noqa: E501

        :return: The credit_card_surcharge of this PaymentTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_surcharge

    @credit_card_surcharge.setter
    def credit_card_surcharge(self, credit_card_surcharge):
        """Sets the credit_card_surcharge of this PaymentTypeItem.

        Credit Card Surcharge  # noqa: E501

        :param credit_card_surcharge: The credit_card_surcharge of this PaymentTypeItem.  # noqa: E501
        :type: str
        """

        self._credit_card_surcharge = credit_card_surcharge

    @property
    def ccs_charge_item_id(self):
        """Gets the ccs_charge_item_id of this PaymentTypeItem.  # noqa: E501

        CCS Charge Item  # noqa: E501

        :return: The ccs_charge_item_id of this PaymentTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._ccs_charge_item_id

    @ccs_charge_item_id.setter
    def ccs_charge_item_id(self, ccs_charge_item_id):
        """Sets the ccs_charge_item_id of this PaymentTypeItem.

        CCS Charge Item  # noqa: E501

        :param ccs_charge_item_id: The ccs_charge_item_id of this PaymentTypeItem.  # noqa: E501
        :type: int
        """

        self._ccs_charge_item_id = ccs_charge_item_id

    @property
    def date_modified(self):
        """Gets the date_modified of this PaymentTypeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this PaymentTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this PaymentTypeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this PaymentTypeItem.  # noqa: E501
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
        if not isinstance(other, PaymentTypeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other