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


class EventChargeItem(object):
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
        'event_charge_id': 'int',
        'event_id': 'int',
        'description': 'str',
        'charge_item_id': 'int',
        'transaction_type_enum': 'str',
        'term_session_id': 'int',
        'amount': 'str',
        'amount_cost': 'str',
        'comments': 'str',
        'posted': 'bool',
        'table_name': 'str',
        'table_id': 'int',
        'charge_to_entry': 'bool',
        'per_entry': 'bool',
        'date_modified': 'str'
    }

    attribute_map = {
        'event_charge_id': 'EventChargeID',
        'event_id': 'EventID',
        'description': 'Description',
        'charge_item_id': 'ChargeItemID',
        'transaction_type_enum': 'TransactionTypeEnum',
        'term_session_id': 'TermSessionID',
        'amount': 'Amount',
        'amount_cost': 'AmountCost',
        'comments': 'Comments',
        'posted': 'Posted',
        'table_name': 'TableName',
        'table_id': 'TableID',
        'charge_to_entry': 'ChargeToEntry',
        'per_entry': 'PerEntry',
        'date_modified': 'DateModified'
    }

    def __init__(self, event_charge_id=None, event_id=None, description=None, charge_item_id=None, transaction_type_enum=None, term_session_id=None, amount=None, amount_cost=None, comments=None, posted=None, table_name=None, table_id=None, charge_to_entry=None, per_entry=None, date_modified=None):  # noqa: E501
        """EventChargeItem - a model defined in Swagger"""  # noqa: E501

        self._event_charge_id = None
        self._event_id = None
        self._description = None
        self._charge_item_id = None
        self._transaction_type_enum = None
        self._term_session_id = None
        self._amount = None
        self._amount_cost = None
        self._comments = None
        self._posted = None
        self._table_name = None
        self._table_id = None
        self._charge_to_entry = None
        self._per_entry = None
        self._date_modified = None
        self.discriminator = None

        if event_charge_id is not None:
            self.event_charge_id = event_charge_id
        if event_id is not None:
            self.event_id = event_id
        if description is not None:
            self.description = description
        if charge_item_id is not None:
            self.charge_item_id = charge_item_id
        if transaction_type_enum is not None:
            self.transaction_type_enum = transaction_type_enum
        if term_session_id is not None:
            self.term_session_id = term_session_id
        if amount is not None:
            self.amount = amount
        if amount_cost is not None:
            self.amount_cost = amount_cost
        if comments is not None:
            self.comments = comments
        if posted is not None:
            self.posted = posted
        if table_name is not None:
            self.table_name = table_name
        if table_id is not None:
            self.table_id = table_id
        if charge_to_entry is not None:
            self.charge_to_entry = charge_to_entry
        if per_entry is not None:
            self.per_entry = per_entry
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def event_charge_id(self):
        """Gets the event_charge_id of this EventChargeItem.  # noqa: E501

        Event Charge  # noqa: E501

        :return: The event_charge_id of this EventChargeItem.  # noqa: E501
        :rtype: int
        """
        return self._event_charge_id

    @event_charge_id.setter
    def event_charge_id(self, event_charge_id):
        """Sets the event_charge_id of this EventChargeItem.

        Event Charge  # noqa: E501

        :param event_charge_id: The event_charge_id of this EventChargeItem.  # noqa: E501
        :type: int
        """

        self._event_charge_id = event_charge_id

    @property
    def event_id(self):
        """Gets the event_id of this EventChargeItem.  # noqa: E501

        Event  # noqa: E501

        :return: The event_id of this EventChargeItem.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this EventChargeItem.

        Event  # noqa: E501

        :param event_id: The event_id of this EventChargeItem.  # noqa: E501
        :type: int
        """

        self._event_id = event_id

    @property
    def description(self):
        """Gets the description of this EventChargeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this EventChargeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventChargeItem.

        Description  # noqa: E501

        :param description: The description of this EventChargeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def charge_item_id(self):
        """Gets the charge_item_id of this EventChargeItem.  # noqa: E501

        Charge Item  # noqa: E501

        :return: The charge_item_id of this EventChargeItem.  # noqa: E501
        :rtype: int
        """
        return self._charge_item_id

    @charge_item_id.setter
    def charge_item_id(self, charge_item_id):
        """Sets the charge_item_id of this EventChargeItem.

        Charge Item  # noqa: E501

        :param charge_item_id: The charge_item_id of this EventChargeItem.  # noqa: E501
        :type: int
        """

        self._charge_item_id = charge_item_id

    @property
    def transaction_type_enum(self):
        """Gets the transaction_type_enum of this EventChargeItem.  # noqa: E501

        Transaction Type  # noqa: E501

        :return: The transaction_type_enum of this EventChargeItem.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type_enum

    @transaction_type_enum.setter
    def transaction_type_enum(self, transaction_type_enum):
        """Sets the transaction_type_enum of this EventChargeItem.

        Transaction Type  # noqa: E501

        :param transaction_type_enum: The transaction_type_enum of this EventChargeItem.  # noqa: E501
        :type: str
        """

        self._transaction_type_enum = transaction_type_enum

    @property
    def term_session_id(self):
        """Gets the term_session_id of this EventChargeItem.  # noqa: E501

        Term Session  # noqa: E501

        :return: The term_session_id of this EventChargeItem.  # noqa: E501
        :rtype: int
        """
        return self._term_session_id

    @term_session_id.setter
    def term_session_id(self, term_session_id):
        """Sets the term_session_id of this EventChargeItem.

        Term Session  # noqa: E501

        :param term_session_id: The term_session_id of this EventChargeItem.  # noqa: E501
        :type: int
        """

        self._term_session_id = term_session_id

    @property
    def amount(self):
        """Gets the amount of this EventChargeItem.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this EventChargeItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EventChargeItem.

        Amount  # noqa: E501

        :param amount: The amount of this EventChargeItem.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def amount_cost(self):
        """Gets the amount_cost of this EventChargeItem.  # noqa: E501

        Amount Cost  # noqa: E501

        :return: The amount_cost of this EventChargeItem.  # noqa: E501
        :rtype: str
        """
        return self._amount_cost

    @amount_cost.setter
    def amount_cost(self, amount_cost):
        """Sets the amount_cost of this EventChargeItem.

        Amount Cost  # noqa: E501

        :param amount_cost: The amount_cost of this EventChargeItem.  # noqa: E501
        :type: str
        """

        self._amount_cost = amount_cost

    @property
    def comments(self):
        """Gets the comments of this EventChargeItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this EventChargeItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this EventChargeItem.

        Comments  # noqa: E501

        :param comments: The comments of this EventChargeItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 250:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `250`")  # noqa: E501

        self._comments = comments

    @property
    def posted(self):
        """Gets the posted of this EventChargeItem.  # noqa: E501

        Posted  # noqa: E501

        :return: The posted of this EventChargeItem.  # noqa: E501
        :rtype: bool
        """
        return self._posted

    @posted.setter
    def posted(self, posted):
        """Sets the posted of this EventChargeItem.

        Posted  # noqa: E501

        :param posted: The posted of this EventChargeItem.  # noqa: E501
        :type: bool
        """

        self._posted = posted

    @property
    def table_name(self):
        """Gets the table_name of this EventChargeItem.  # noqa: E501

        Table Name  # noqa: E501

        :return: The table_name of this EventChargeItem.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this EventChargeItem.

        Table Name  # noqa: E501

        :param table_name: The table_name of this EventChargeItem.  # noqa: E501
        :type: str
        """
        if table_name is not None and len(table_name) > 50:
            raise ValueError("Invalid value for `table_name`, length must be less than or equal to `50`")  # noqa: E501

        self._table_name = table_name

    @property
    def table_id(self):
        """Gets the table_id of this EventChargeItem.  # noqa: E501

        Table  # noqa: E501

        :return: The table_id of this EventChargeItem.  # noqa: E501
        :rtype: int
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this EventChargeItem.

        Table  # noqa: E501

        :param table_id: The table_id of this EventChargeItem.  # noqa: E501
        :type: int
        """

        self._table_id = table_id

    @property
    def charge_to_entry(self):
        """Gets the charge_to_entry of this EventChargeItem.  # noqa: E501

        Charge To Entry  # noqa: E501

        :return: The charge_to_entry of this EventChargeItem.  # noqa: E501
        :rtype: bool
        """
        return self._charge_to_entry

    @charge_to_entry.setter
    def charge_to_entry(self, charge_to_entry):
        """Sets the charge_to_entry of this EventChargeItem.

        Charge To Entry  # noqa: E501

        :param charge_to_entry: The charge_to_entry of this EventChargeItem.  # noqa: E501
        :type: bool
        """

        self._charge_to_entry = charge_to_entry

    @property
    def per_entry(self):
        """Gets the per_entry of this EventChargeItem.  # noqa: E501

        Per Entry  # noqa: E501

        :return: The per_entry of this EventChargeItem.  # noqa: E501
        :rtype: bool
        """
        return self._per_entry

    @per_entry.setter
    def per_entry(self, per_entry):
        """Sets the per_entry of this EventChargeItem.

        Per Entry  # noqa: E501

        :param per_entry: The per_entry of this EventChargeItem.  # noqa: E501
        :type: bool
        """

        self._per_entry = per_entry

    @property
    def date_modified(self):
        """Gets the date_modified of this EventChargeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this EventChargeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this EventChargeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this EventChargeItem.  # noqa: E501
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
        if not isinstance(other, EventChargeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
