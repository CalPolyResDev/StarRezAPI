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


class EventRegistrationFeeItem(object):
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
        'event_registration_fee_id': 'int',
        'event_id': 'int',
        'charge_to_entry': 'bool',
        'charge_item_id': 'int',
        'description': 'str',
        'date_start': 'str',
        'date_end': 'str',
        'amount': 'str',
        'comments': 'str',
        'registration_code': 'str',
        'max_registrations': 'int',
        'view_on_web': 'bool',
        'web_description': 'str',
        'web_order': 'int',
        'web_comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'event_registration_fee_id': 'EventRegistrationFeeID',
        'event_id': 'EventID',
        'charge_to_entry': 'ChargeToEntry',
        'charge_item_id': 'ChargeItemID',
        'description': 'Description',
        'date_start': 'DateStart',
        'date_end': 'DateEnd',
        'amount': 'Amount',
        'comments': 'Comments',
        'registration_code': 'RegistrationCode',
        'max_registrations': 'MaxRegistrations',
        'view_on_web': 'ViewOnWeb',
        'web_description': 'WebDescription',
        'web_order': 'WebOrder',
        'web_comments': 'WebComments',
        'date_modified': 'DateModified'
    }

    def __init__(self, event_registration_fee_id=None, event_id=None, charge_to_entry=None, charge_item_id=None, description=None, date_start=None, date_end=None, amount=None, comments=None, registration_code=None, max_registrations=None, view_on_web=None, web_description=None, web_order=None, web_comments=None, date_modified=None):  # noqa: E501
        """EventRegistrationFeeItem - a model defined in Swagger"""  # noqa: E501

        self._event_registration_fee_id = None
        self._event_id = None
        self._charge_to_entry = None
        self._charge_item_id = None
        self._description = None
        self._date_start = None
        self._date_end = None
        self._amount = None
        self._comments = None
        self._registration_code = None
        self._max_registrations = None
        self._view_on_web = None
        self._web_description = None
        self._web_order = None
        self._web_comments = None
        self._date_modified = None
        self.discriminator = None

        if event_registration_fee_id is not None:
            self.event_registration_fee_id = event_registration_fee_id
        if event_id is not None:
            self.event_id = event_id
        if charge_to_entry is not None:
            self.charge_to_entry = charge_to_entry
        if charge_item_id is not None:
            self.charge_item_id = charge_item_id
        if description is not None:
            self.description = description
        if date_start is not None:
            self.date_start = date_start
        if date_end is not None:
            self.date_end = date_end
        if amount is not None:
            self.amount = amount
        if comments is not None:
            self.comments = comments
        if registration_code is not None:
            self.registration_code = registration_code
        if max_registrations is not None:
            self.max_registrations = max_registrations
        if view_on_web is not None:
            self.view_on_web = view_on_web
        if web_description is not None:
            self.web_description = web_description
        if web_order is not None:
            self.web_order = web_order
        if web_comments is not None:
            self.web_comments = web_comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def event_registration_fee_id(self):
        """Gets the event_registration_fee_id of this EventRegistrationFeeItem.  # noqa: E501

        Event Registration Fee  # noqa: E501

        :return: The event_registration_fee_id of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: int
        """
        return self._event_registration_fee_id

    @event_registration_fee_id.setter
    def event_registration_fee_id(self, event_registration_fee_id):
        """Sets the event_registration_fee_id of this EventRegistrationFeeItem.

        Event Registration Fee  # noqa: E501

        :param event_registration_fee_id: The event_registration_fee_id of this EventRegistrationFeeItem.  # noqa: E501
        :type: int
        """

        self._event_registration_fee_id = event_registration_fee_id

    @property
    def event_id(self):
        """Gets the event_id of this EventRegistrationFeeItem.  # noqa: E501

        Event  # noqa: E501

        :return: The event_id of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this EventRegistrationFeeItem.

        Event  # noqa: E501

        :param event_id: The event_id of this EventRegistrationFeeItem.  # noqa: E501
        :type: int
        """

        self._event_id = event_id

    @property
    def charge_to_entry(self):
        """Gets the charge_to_entry of this EventRegistrationFeeItem.  # noqa: E501

        Charge To Entry  # noqa: E501

        :return: The charge_to_entry of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: bool
        """
        return self._charge_to_entry

    @charge_to_entry.setter
    def charge_to_entry(self, charge_to_entry):
        """Sets the charge_to_entry of this EventRegistrationFeeItem.

        Charge To Entry  # noqa: E501

        :param charge_to_entry: The charge_to_entry of this EventRegistrationFeeItem.  # noqa: E501
        :type: bool
        """

        self._charge_to_entry = charge_to_entry

    @property
    def charge_item_id(self):
        """Gets the charge_item_id of this EventRegistrationFeeItem.  # noqa: E501

        Charge Item  # noqa: E501

        :return: The charge_item_id of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: int
        """
        return self._charge_item_id

    @charge_item_id.setter
    def charge_item_id(self, charge_item_id):
        """Sets the charge_item_id of this EventRegistrationFeeItem.

        Charge Item  # noqa: E501

        :param charge_item_id: The charge_item_id of this EventRegistrationFeeItem.  # noqa: E501
        :type: int
        """

        self._charge_item_id = charge_item_id

    @property
    def description(self):
        """Gets the description of this EventRegistrationFeeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventRegistrationFeeItem.

        Description  # noqa: E501

        :param description: The description of this EventRegistrationFeeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def date_start(self):
        """Gets the date_start of this EventRegistrationFeeItem.  # noqa: E501

        Date Start  # noqa: E501

        :return: The date_start of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this EventRegistrationFeeItem.

        Date Start  # noqa: E501

        :param date_start: The date_start of this EventRegistrationFeeItem.  # noqa: E501
        :type: str
        """

        self._date_start = date_start

    @property
    def date_end(self):
        """Gets the date_end of this EventRegistrationFeeItem.  # noqa: E501

        Date End  # noqa: E501

        :return: The date_end of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this EventRegistrationFeeItem.

        Date End  # noqa: E501

        :param date_end: The date_end of this EventRegistrationFeeItem.  # noqa: E501
        :type: str
        """

        self._date_end = date_end

    @property
    def amount(self):
        """Gets the amount of this EventRegistrationFeeItem.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EventRegistrationFeeItem.

        Amount  # noqa: E501

        :param amount: The amount of this EventRegistrationFeeItem.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def comments(self):
        """Gets the comments of this EventRegistrationFeeItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this EventRegistrationFeeItem.

        Comments  # noqa: E501

        :param comments: The comments of this EventRegistrationFeeItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 250:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `250`")  # noqa: E501

        self._comments = comments

    @property
    def registration_code(self):
        """Gets the registration_code of this EventRegistrationFeeItem.  # noqa: E501

        Registration Code  # noqa: E501

        :return: The registration_code of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: str
        """
        return self._registration_code

    @registration_code.setter
    def registration_code(self, registration_code):
        """Sets the registration_code of this EventRegistrationFeeItem.

        Registration Code  # noqa: E501

        :param registration_code: The registration_code of this EventRegistrationFeeItem.  # noqa: E501
        :type: str
        """
        if registration_code is not None and len(registration_code) > 100:
            raise ValueError("Invalid value for `registration_code`, length must be less than or equal to `100`")  # noqa: E501

        self._registration_code = registration_code

    @property
    def max_registrations(self):
        """Gets the max_registrations of this EventRegistrationFeeItem.  # noqa: E501

        Max Registrations  # noqa: E501

        :return: The max_registrations of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: int
        """
        return self._max_registrations

    @max_registrations.setter
    def max_registrations(self, max_registrations):
        """Sets the max_registrations of this EventRegistrationFeeItem.

        Max Registrations  # noqa: E501

        :param max_registrations: The max_registrations of this EventRegistrationFeeItem.  # noqa: E501
        :type: int
        """

        self._max_registrations = max_registrations

    @property
    def view_on_web(self):
        """Gets the view_on_web of this EventRegistrationFeeItem.  # noqa: E501

        View On Web  # noqa: E501

        :return: The view_on_web of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: bool
        """
        return self._view_on_web

    @view_on_web.setter
    def view_on_web(self, view_on_web):
        """Sets the view_on_web of this EventRegistrationFeeItem.

        View On Web  # noqa: E501

        :param view_on_web: The view_on_web of this EventRegistrationFeeItem.  # noqa: E501
        :type: bool
        """

        self._view_on_web = view_on_web

    @property
    def web_description(self):
        """Gets the web_description of this EventRegistrationFeeItem.  # noqa: E501

        Web Description  # noqa: E501

        :return: The web_description of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: str
        """
        return self._web_description

    @web_description.setter
    def web_description(self, web_description):
        """Sets the web_description of this EventRegistrationFeeItem.

        Web Description  # noqa: E501

        :param web_description: The web_description of this EventRegistrationFeeItem.  # noqa: E501
        :type: str
        """
        if web_description is not None and len(web_description) > 1000:
            raise ValueError("Invalid value for `web_description`, length must be less than or equal to `1000`")  # noqa: E501

        self._web_description = web_description

    @property
    def web_order(self):
        """Gets the web_order of this EventRegistrationFeeItem.  # noqa: E501

        Web Order  # noqa: E501

        :return: The web_order of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: int
        """
        return self._web_order

    @web_order.setter
    def web_order(self, web_order):
        """Sets the web_order of this EventRegistrationFeeItem.

        Web Order  # noqa: E501

        :param web_order: The web_order of this EventRegistrationFeeItem.  # noqa: E501
        :type: int
        """

        self._web_order = web_order

    @property
    def web_comments(self):
        """Gets the web_comments of this EventRegistrationFeeItem.  # noqa: E501

        Web Comments  # noqa: E501

        :return: The web_comments of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: str
        """
        return self._web_comments

    @web_comments.setter
    def web_comments(self, web_comments):
        """Sets the web_comments of this EventRegistrationFeeItem.

        Web Comments  # noqa: E501

        :param web_comments: The web_comments of this EventRegistrationFeeItem.  # noqa: E501
        :type: str
        """

        self._web_comments = web_comments

    @property
    def date_modified(self):
        """Gets the date_modified of this EventRegistrationFeeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this EventRegistrationFeeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this EventRegistrationFeeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this EventRegistrationFeeItem.  # noqa: E501
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
        if not isinstance(other, EventRegistrationFeeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
