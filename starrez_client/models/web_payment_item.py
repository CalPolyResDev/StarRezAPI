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


class WebPaymentItem(object):
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
        'web_payment_id': 'int',
        'entry_id': 'int',
        'payment_date': 'str',
        'description': 'str',
        'successful': 'bool',
        'amount': 'str',
        'amount_paid': 'str',
        'invoice_number': 'str',
        'receipt_values': 'str',
        'payment_id': 'int',
        'request_data': 'str',
        'response_data': 'str',
        'custom_string1': 'str',
        'custom_string2': 'str',
        'processed_date': 'str',
        'web_section_id': 'int',
        'source_web_module_id': 'int',
        'entry_application_id': 'int',
        'invoice_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'web_payment_id': 'WebPaymentID',
        'entry_id': 'EntryID',
        'payment_date': 'PaymentDate',
        'description': 'Description',
        'successful': 'Successful',
        'amount': 'Amount',
        'amount_paid': 'AmountPaid',
        'invoice_number': 'InvoiceNumber',
        'receipt_values': 'ReceiptValues',
        'payment_id': 'PaymentID',
        'request_data': 'RequestData',
        'response_data': 'ResponseData',
        'custom_string1': 'CustomString1',
        'custom_string2': 'CustomString2',
        'processed_date': 'ProcessedDate',
        'web_section_id': 'WebSectionID',
        'source_web_module_id': 'Source_WebModuleID',
        'entry_application_id': 'EntryApplicationID',
        'invoice_id': 'InvoiceID',
        'date_modified': 'DateModified'
    }

    def __init__(self, web_payment_id=None, entry_id=None, payment_date=None, description=None, successful=None, amount=None, amount_paid=None, invoice_number=None, receipt_values=None, payment_id=None, request_data=None, response_data=None, custom_string1=None, custom_string2=None, processed_date=None, web_section_id=None, source_web_module_id=None, entry_application_id=None, invoice_id=None, date_modified=None):  # noqa: E501
        """WebPaymentItem - a model defined in Swagger"""  # noqa: E501

        self._web_payment_id = None
        self._entry_id = None
        self._payment_date = None
        self._description = None
        self._successful = None
        self._amount = None
        self._amount_paid = None
        self._invoice_number = None
        self._receipt_values = None
        self._payment_id = None
        self._request_data = None
        self._response_data = None
        self._custom_string1 = None
        self._custom_string2 = None
        self._processed_date = None
        self._web_section_id = None
        self._source_web_module_id = None
        self._entry_application_id = None
        self._invoice_id = None
        self._date_modified = None
        self.discriminator = None

        if web_payment_id is not None:
            self.web_payment_id = web_payment_id
        if entry_id is not None:
            self.entry_id = entry_id
        if payment_date is not None:
            self.payment_date = payment_date
        if description is not None:
            self.description = description
        if successful is not None:
            self.successful = successful
        if amount is not None:
            self.amount = amount
        if amount_paid is not None:
            self.amount_paid = amount_paid
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if receipt_values is not None:
            self.receipt_values = receipt_values
        if payment_id is not None:
            self.payment_id = payment_id
        if request_data is not None:
            self.request_data = request_data
        if response_data is not None:
            self.response_data = response_data
        if custom_string1 is not None:
            self.custom_string1 = custom_string1
        if custom_string2 is not None:
            self.custom_string2 = custom_string2
        if processed_date is not None:
            self.processed_date = processed_date
        if web_section_id is not None:
            self.web_section_id = web_section_id
        if source_web_module_id is not None:
            self.source_web_module_id = source_web_module_id
        if entry_application_id is not None:
            self.entry_application_id = entry_application_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def web_payment_id(self):
        """Gets the web_payment_id of this WebPaymentItem.  # noqa: E501

        Web Payment  # noqa: E501

        :return: The web_payment_id of this WebPaymentItem.  # noqa: E501
        :rtype: int
        """
        return self._web_payment_id

    @web_payment_id.setter
    def web_payment_id(self, web_payment_id):
        """Sets the web_payment_id of this WebPaymentItem.

        Web Payment  # noqa: E501

        :param web_payment_id: The web_payment_id of this WebPaymentItem.  # noqa: E501
        :type: int
        """

        self._web_payment_id = web_payment_id

    @property
    def entry_id(self):
        """Gets the entry_id of this WebPaymentItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this WebPaymentItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this WebPaymentItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this WebPaymentItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def payment_date(self):
        """Gets the payment_date of this WebPaymentItem.  # noqa: E501

        Payment Date  # noqa: E501

        :return: The payment_date of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this WebPaymentItem.

        Payment Date  # noqa: E501

        :param payment_date: The payment_date of this WebPaymentItem.  # noqa: E501
        :type: str
        """

        self._payment_date = payment_date

    @property
    def description(self):
        """Gets the description of this WebPaymentItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebPaymentItem.

        Description  # noqa: E501

        :param description: The description of this WebPaymentItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def successful(self):
        """Gets the successful of this WebPaymentItem.  # noqa: E501

        Successful  # noqa: E501

        :return: The successful of this WebPaymentItem.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this WebPaymentItem.

        Successful  # noqa: E501

        :param successful: The successful of this WebPaymentItem.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def amount(self):
        """Gets the amount of this WebPaymentItem.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this WebPaymentItem.

        Amount  # noqa: E501

        :param amount: The amount of this WebPaymentItem.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def amount_paid(self):
        """Gets the amount_paid of this WebPaymentItem.  # noqa: E501

        Amount Paid  # noqa: E501

        :return: The amount_paid of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._amount_paid

    @amount_paid.setter
    def amount_paid(self, amount_paid):
        """Sets the amount_paid of this WebPaymentItem.

        Amount Paid  # noqa: E501

        :param amount_paid: The amount_paid of this WebPaymentItem.  # noqa: E501
        :type: str
        """

        self._amount_paid = amount_paid

    @property
    def invoice_number(self):
        """Gets the invoice_number of this WebPaymentItem.  # noqa: E501

        Invoice Number  # noqa: E501

        :return: The invoice_number of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this WebPaymentItem.

        Invoice Number  # noqa: E501

        :param invoice_number: The invoice_number of this WebPaymentItem.  # noqa: E501
        :type: str
        """
        if invoice_number is not None and len(invoice_number) > 200:
            raise ValueError("Invalid value for `invoice_number`, length must be less than or equal to `200`")  # noqa: E501

        self._invoice_number = invoice_number

    @property
    def receipt_values(self):
        """Gets the receipt_values of this WebPaymentItem.  # noqa: E501

        Receipt Values  # noqa: E501

        :return: The receipt_values of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._receipt_values

    @receipt_values.setter
    def receipt_values(self, receipt_values):
        """Sets the receipt_values of this WebPaymentItem.

        Receipt Values  # noqa: E501

        :param receipt_values: The receipt_values of this WebPaymentItem.  # noqa: E501
        :type: str
        """
        if receipt_values is not None and len(receipt_values) > 5000:
            raise ValueError("Invalid value for `receipt_values`, length must be less than or equal to `5000`")  # noqa: E501

        self._receipt_values = receipt_values

    @property
    def payment_id(self):
        """Gets the payment_id of this WebPaymentItem.  # noqa: E501

        Payment  # noqa: E501

        :return: The payment_id of this WebPaymentItem.  # noqa: E501
        :rtype: int
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this WebPaymentItem.

        Payment  # noqa: E501

        :param payment_id: The payment_id of this WebPaymentItem.  # noqa: E501
        :type: int
        """

        self._payment_id = payment_id

    @property
    def request_data(self):
        """Gets the request_data of this WebPaymentItem.  # noqa: E501

        Request Data  # noqa: E501

        :return: The request_data of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        """Sets the request_data of this WebPaymentItem.

        Request Data  # noqa: E501

        :param request_data: The request_data of this WebPaymentItem.  # noqa: E501
        :type: str
        """
        if request_data is not None and len(request_data) > 5000:
            raise ValueError("Invalid value for `request_data`, length must be less than or equal to `5000`")  # noqa: E501

        self._request_data = request_data

    @property
    def response_data(self):
        """Gets the response_data of this WebPaymentItem.  # noqa: E501

        Response Data  # noqa: E501

        :return: The response_data of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._response_data

    @response_data.setter
    def response_data(self, response_data):
        """Sets the response_data of this WebPaymentItem.

        Response Data  # noqa: E501

        :param response_data: The response_data of this WebPaymentItem.  # noqa: E501
        :type: str
        """
        if response_data is not None and len(response_data) > 5000:
            raise ValueError("Invalid value for `response_data`, length must be less than or equal to `5000`")  # noqa: E501

        self._response_data = response_data

    @property
    def custom_string1(self):
        """Gets the custom_string1 of this WebPaymentItem.  # noqa: E501

        Custom String 1  # noqa: E501

        :return: The custom_string1 of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string1

    @custom_string1.setter
    def custom_string1(self, custom_string1):
        """Sets the custom_string1 of this WebPaymentItem.

        Custom String 1  # noqa: E501

        :param custom_string1: The custom_string1 of this WebPaymentItem.  # noqa: E501
        :type: str
        """
        if custom_string1 is not None and len(custom_string1) > 5000:
            raise ValueError("Invalid value for `custom_string1`, length must be less than or equal to `5000`")  # noqa: E501

        self._custom_string1 = custom_string1

    @property
    def custom_string2(self):
        """Gets the custom_string2 of this WebPaymentItem.  # noqa: E501

        Custom String 2  # noqa: E501

        :return: The custom_string2 of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string2

    @custom_string2.setter
    def custom_string2(self, custom_string2):
        """Sets the custom_string2 of this WebPaymentItem.

        Custom String 2  # noqa: E501

        :param custom_string2: The custom_string2 of this WebPaymentItem.  # noqa: E501
        :type: str
        """
        if custom_string2 is not None and len(custom_string2) > 5000:
            raise ValueError("Invalid value for `custom_string2`, length must be less than or equal to `5000`")  # noqa: E501

        self._custom_string2 = custom_string2

    @property
    def processed_date(self):
        """Gets the processed_date of this WebPaymentItem.  # noqa: E501

        Processed Date  # noqa: E501

        :return: The processed_date of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._processed_date

    @processed_date.setter
    def processed_date(self, processed_date):
        """Sets the processed_date of this WebPaymentItem.

        Processed Date  # noqa: E501

        :param processed_date: The processed_date of this WebPaymentItem.  # noqa: E501
        :type: str
        """

        self._processed_date = processed_date

    @property
    def web_section_id(self):
        """Gets the web_section_id of this WebPaymentItem.  # noqa: E501

        Web Section  # noqa: E501

        :return: The web_section_id of this WebPaymentItem.  # noqa: E501
        :rtype: int
        """
        return self._web_section_id

    @web_section_id.setter
    def web_section_id(self, web_section_id):
        """Sets the web_section_id of this WebPaymentItem.

        Web Section  # noqa: E501

        :param web_section_id: The web_section_id of this WebPaymentItem.  # noqa: E501
        :type: int
        """

        self._web_section_id = web_section_id

    @property
    def source_web_module_id(self):
        """Gets the source_web_module_id of this WebPaymentItem.  # noqa: E501

        Source Web Module  # noqa: E501

        :return: The source_web_module_id of this WebPaymentItem.  # noqa: E501
        :rtype: int
        """
        return self._source_web_module_id

    @source_web_module_id.setter
    def source_web_module_id(self, source_web_module_id):
        """Sets the source_web_module_id of this WebPaymentItem.

        Source Web Module  # noqa: E501

        :param source_web_module_id: The source_web_module_id of this WebPaymentItem.  # noqa: E501
        :type: int
        """

        self._source_web_module_id = source_web_module_id

    @property
    def entry_application_id(self):
        """Gets the entry_application_id of this WebPaymentItem.  # noqa: E501

        Entry Application  # noqa: E501

        :return: The entry_application_id of this WebPaymentItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_application_id

    @entry_application_id.setter
    def entry_application_id(self, entry_application_id):
        """Sets the entry_application_id of this WebPaymentItem.

        Entry Application  # noqa: E501

        :param entry_application_id: The entry_application_id of this WebPaymentItem.  # noqa: E501
        :type: int
        """

        self._entry_application_id = entry_application_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this WebPaymentItem.  # noqa: E501

        Invoice  # noqa: E501

        :return: The invoice_id of this WebPaymentItem.  # noqa: E501
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this WebPaymentItem.

        Invoice  # noqa: E501

        :param invoice_id: The invoice_id of this WebPaymentItem.  # noqa: E501
        :type: int
        """

        self._invoice_id = invoice_id

    @property
    def date_modified(self):
        """Gets the date_modified of this WebPaymentItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this WebPaymentItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this WebPaymentItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this WebPaymentItem.  # noqa: E501
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
        if not isinstance(other, WebPaymentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
