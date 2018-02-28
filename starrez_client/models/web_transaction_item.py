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


class WebTransactionItem(object):
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
        'web_transaction_id': 'int',
        'web_payment_id': 'int',
        'charge_group_id': 'int',
        'charge_item_id': 'int',
        'description': 'str',
        'amount': 'str',
        'full_account_payment': 'bool',
        'table_id': 'int',
        'table_name': 'str',
        'data': 'str',
        'term_session_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'web_transaction_id': 'WebTransactionID',
        'web_payment_id': 'WebPaymentID',
        'charge_group_id': 'ChargeGroupID',
        'charge_item_id': 'ChargeItemID',
        'description': 'Description',
        'amount': 'Amount',
        'full_account_payment': 'FullAccountPayment',
        'table_id': 'TableID',
        'table_name': 'TableName',
        'data': 'Data',
        'term_session_id': 'TermSessionID',
        'date_modified': 'DateModified'
    }

    def __init__(self, web_transaction_id=None, web_payment_id=None, charge_group_id=None, charge_item_id=None, description=None, amount=None, full_account_payment=None, table_id=None, table_name=None, data=None, term_session_id=None, date_modified=None):  # noqa: E501
        """WebTransactionItem - a model defined in Swagger"""  # noqa: E501

        self._web_transaction_id = None
        self._web_payment_id = None
        self._charge_group_id = None
        self._charge_item_id = None
        self._description = None
        self._amount = None
        self._full_account_payment = None
        self._table_id = None
        self._table_name = None
        self._data = None
        self._term_session_id = None
        self._date_modified = None
        self.discriminator = None

        if web_transaction_id is not None:
            self.web_transaction_id = web_transaction_id
        if web_payment_id is not None:
            self.web_payment_id = web_payment_id
        if charge_group_id is not None:
            self.charge_group_id = charge_group_id
        if charge_item_id is not None:
            self.charge_item_id = charge_item_id
        if description is not None:
            self.description = description
        if amount is not None:
            self.amount = amount
        if full_account_payment is not None:
            self.full_account_payment = full_account_payment
        if table_id is not None:
            self.table_id = table_id
        if table_name is not None:
            self.table_name = table_name
        if data is not None:
            self.data = data
        if term_session_id is not None:
            self.term_session_id = term_session_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def web_transaction_id(self):
        """Gets the web_transaction_id of this WebTransactionItem.  # noqa: E501

        Web Transaction  # noqa: E501

        :return: The web_transaction_id of this WebTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._web_transaction_id

    @web_transaction_id.setter
    def web_transaction_id(self, web_transaction_id):
        """Sets the web_transaction_id of this WebTransactionItem.

        Web Transaction  # noqa: E501

        :param web_transaction_id: The web_transaction_id of this WebTransactionItem.  # noqa: E501
        :type: int
        """

        self._web_transaction_id = web_transaction_id

    @property
    def web_payment_id(self):
        """Gets the web_payment_id of this WebTransactionItem.  # noqa: E501

        Web Payment  # noqa: E501

        :return: The web_payment_id of this WebTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._web_payment_id

    @web_payment_id.setter
    def web_payment_id(self, web_payment_id):
        """Sets the web_payment_id of this WebTransactionItem.

        Web Payment  # noqa: E501

        :param web_payment_id: The web_payment_id of this WebTransactionItem.  # noqa: E501
        :type: int
        """

        self._web_payment_id = web_payment_id

    @property
    def charge_group_id(self):
        """Gets the charge_group_id of this WebTransactionItem.  # noqa: E501

        Charge Group  # noqa: E501

        :return: The charge_group_id of this WebTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._charge_group_id

    @charge_group_id.setter
    def charge_group_id(self, charge_group_id):
        """Sets the charge_group_id of this WebTransactionItem.

        Charge Group  # noqa: E501

        :param charge_group_id: The charge_group_id of this WebTransactionItem.  # noqa: E501
        :type: int
        """

        self._charge_group_id = charge_group_id

    @property
    def charge_item_id(self):
        """Gets the charge_item_id of this WebTransactionItem.  # noqa: E501

        Charge Item  # noqa: E501

        :return: The charge_item_id of this WebTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._charge_item_id

    @charge_item_id.setter
    def charge_item_id(self, charge_item_id):
        """Sets the charge_item_id of this WebTransactionItem.

        Charge Item  # noqa: E501

        :param charge_item_id: The charge_item_id of this WebTransactionItem.  # noqa: E501
        :type: int
        """

        self._charge_item_id = charge_item_id

    @property
    def description(self):
        """Gets the description of this WebTransactionItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this WebTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebTransactionItem.

        Description  # noqa: E501

        :param description: The description of this WebTransactionItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 150:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `150`")  # noqa: E501

        self._description = description

    @property
    def amount(self):
        """Gets the amount of this WebTransactionItem.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this WebTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this WebTransactionItem.

        Amount  # noqa: E501

        :param amount: The amount of this WebTransactionItem.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def full_account_payment(self):
        """Gets the full_account_payment of this WebTransactionItem.  # noqa: E501

        Full Account Payment  # noqa: E501

        :return: The full_account_payment of this WebTransactionItem.  # noqa: E501
        :rtype: bool
        """
        return self._full_account_payment

    @full_account_payment.setter
    def full_account_payment(self, full_account_payment):
        """Sets the full_account_payment of this WebTransactionItem.

        Full Account Payment  # noqa: E501

        :param full_account_payment: The full_account_payment of this WebTransactionItem.  # noqa: E501
        :type: bool
        """

        self._full_account_payment = full_account_payment

    @property
    def table_id(self):
        """Gets the table_id of this WebTransactionItem.  # noqa: E501

        Table  # noqa: E501

        :return: The table_id of this WebTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this WebTransactionItem.

        Table  # noqa: E501

        :param table_id: The table_id of this WebTransactionItem.  # noqa: E501
        :type: int
        """

        self._table_id = table_id

    @property
    def table_name(self):
        """Gets the table_name of this WebTransactionItem.  # noqa: E501

        Table Name  # noqa: E501

        :return: The table_name of this WebTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this WebTransactionItem.

        Table Name  # noqa: E501

        :param table_name: The table_name of this WebTransactionItem.  # noqa: E501
        :type: str
        """
        if table_name is not None and len(table_name) > 50:
            raise ValueError("Invalid value for `table_name`, length must be less than or equal to `50`")  # noqa: E501

        self._table_name = table_name

    @property
    def data(self):
        """Gets the data of this WebTransactionItem.  # noqa: E501

        Data  # noqa: E501

        :return: The data of this WebTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this WebTransactionItem.

        Data  # noqa: E501

        :param data: The data of this WebTransactionItem.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def term_session_id(self):
        """Gets the term_session_id of this WebTransactionItem.  # noqa: E501

        Term Session  # noqa: E501

        :return: The term_session_id of this WebTransactionItem.  # noqa: E501
        :rtype: int
        """
        return self._term_session_id

    @term_session_id.setter
    def term_session_id(self, term_session_id):
        """Sets the term_session_id of this WebTransactionItem.

        Term Session  # noqa: E501

        :param term_session_id: The term_session_id of this WebTransactionItem.  # noqa: E501
        :type: int
        """

        self._term_session_id = term_session_id

    @property
    def date_modified(self):
        """Gets the date_modified of this WebTransactionItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this WebTransactionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this WebTransactionItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this WebTransactionItem.  # noqa: E501
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
        if not isinstance(other, WebTransactionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
