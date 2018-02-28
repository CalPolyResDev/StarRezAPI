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


class ContactItem(object):
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
        'contact_id': 'int',
        'record_type_enum': 'str',
        'contact_type_enum': 'str',
        'contact_status_id': 'int',
        'category_id': 'int',
        'tax_exemption_enum': 'str',
        'description': 'str',
        'street': 'str',
        'street2': 'str',
        'city': 'str',
        'country_id': 'int',
        'state_province': 'str',
        'zip_postcode': 'str',
        'entry_id': 'int',
        'phone': 'str',
        'phone_mobile_cell': 'str',
        'phone_other': 'str',
        'phone_other2': 'str',
        'email': 'str',
        'reference': 'str',
        'account_code': 'str',
        'account_comments': 'str',
        'account_payment_type_id': 'int',
        'account_bank_name': 'str',
        'account_bank_number': 'str',
        'account_detail1': 'str',
        'account_detail2': 'str',
        'account_detail3': 'str',
        'account_detail4': 'str',
        'comments': 'str',
        'security_user_id': 'int',
        'date_created': 'datetime',
        'timestamp': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'contact_id': 'ContactID',
        'record_type_enum': 'RecordTypeEnum',
        'contact_type_enum': 'ContactTypeEnum',
        'contact_status_id': 'ContactStatusID',
        'category_id': 'CategoryID',
        'tax_exemption_enum': 'TaxExemptionEnum',
        'description': 'Description',
        'street': 'Street',
        'street2': 'Street2',
        'city': 'City',
        'country_id': 'CountryID',
        'state_province': 'StateProvince',
        'zip_postcode': 'ZipPostcode',
        'entry_id': 'EntryID',
        'phone': 'Phone',
        'phone_mobile_cell': 'PhoneMobileCell',
        'phone_other': 'PhoneOther',
        'phone_other2': 'PhoneOther2',
        'email': 'Email',
        'reference': 'Reference',
        'account_code': 'AccountCode',
        'account_comments': 'AccountComments',
        'account_payment_type_id': 'Account_PaymentTypeID',
        'account_bank_name': 'AccountBankName',
        'account_bank_number': 'AccountBankNumber',
        'account_detail1': 'AccountDetail1',
        'account_detail2': 'AccountDetail2',
        'account_detail3': 'AccountDetail3',
        'account_detail4': 'AccountDetail4',
        'comments': 'Comments',
        'security_user_id': 'SecurityUserID',
        'date_created': 'DateCreated',
        'timestamp': 'timestamp',
        'date_modified': 'DateModified'
    }

    def __init__(self, contact_id=None, record_type_enum=None, contact_type_enum=None, contact_status_id=None, category_id=None, tax_exemption_enum=None, description=None, street=None, street2=None, city=None, country_id=None, state_province=None, zip_postcode=None, entry_id=None, phone=None, phone_mobile_cell=None, phone_other=None, phone_other2=None, email=None, reference=None, account_code=None, account_comments=None, account_payment_type_id=None, account_bank_name=None, account_bank_number=None, account_detail1=None, account_detail2=None, account_detail3=None, account_detail4=None, comments=None, security_user_id=None, date_created=None, timestamp=None, date_modified=None):  # noqa: E501
        """ContactItem - a model defined in Swagger"""  # noqa: E501

        self._contact_id = None
        self._record_type_enum = None
        self._contact_type_enum = None
        self._contact_status_id = None
        self._category_id = None
        self._tax_exemption_enum = None
        self._description = None
        self._street = None
        self._street2 = None
        self._city = None
        self._country_id = None
        self._state_province = None
        self._zip_postcode = None
        self._entry_id = None
        self._phone = None
        self._phone_mobile_cell = None
        self._phone_other = None
        self._phone_other2 = None
        self._email = None
        self._reference = None
        self._account_code = None
        self._account_comments = None
        self._account_payment_type_id = None
        self._account_bank_name = None
        self._account_bank_number = None
        self._account_detail1 = None
        self._account_detail2 = None
        self._account_detail3 = None
        self._account_detail4 = None
        self._comments = None
        self._security_user_id = None
        self._date_created = None
        self._timestamp = None
        self._date_modified = None
        self.discriminator = None

        if contact_id is not None:
            self.contact_id = contact_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if contact_type_enum is not None:
            self.contact_type_enum = contact_type_enum
        if contact_status_id is not None:
            self.contact_status_id = contact_status_id
        if category_id is not None:
            self.category_id = category_id
        if tax_exemption_enum is not None:
            self.tax_exemption_enum = tax_exemption_enum
        if description is not None:
            self.description = description
        if street is not None:
            self.street = street
        if street2 is not None:
            self.street2 = street2
        if city is not None:
            self.city = city
        if country_id is not None:
            self.country_id = country_id
        if state_province is not None:
            self.state_province = state_province
        if zip_postcode is not None:
            self.zip_postcode = zip_postcode
        if entry_id is not None:
            self.entry_id = entry_id
        if phone is not None:
            self.phone = phone
        if phone_mobile_cell is not None:
            self.phone_mobile_cell = phone_mobile_cell
        if phone_other is not None:
            self.phone_other = phone_other
        if phone_other2 is not None:
            self.phone_other2 = phone_other2
        if email is not None:
            self.email = email
        if reference is not None:
            self.reference = reference
        if account_code is not None:
            self.account_code = account_code
        if account_comments is not None:
            self.account_comments = account_comments
        if account_payment_type_id is not None:
            self.account_payment_type_id = account_payment_type_id
        if account_bank_name is not None:
            self.account_bank_name = account_bank_name
        if account_bank_number is not None:
            self.account_bank_number = account_bank_number
        if account_detail1 is not None:
            self.account_detail1 = account_detail1
        if account_detail2 is not None:
            self.account_detail2 = account_detail2
        if account_detail3 is not None:
            self.account_detail3 = account_detail3
        if account_detail4 is not None:
            self.account_detail4 = account_detail4
        if comments is not None:
            self.comments = comments
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_created is not None:
            self.date_created = date_created
        if timestamp is not None:
            self.timestamp = timestamp
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def contact_id(self):
        """Gets the contact_id of this ContactItem.  # noqa: E501

        Contact  # noqa: E501

        :return: The contact_id of this ContactItem.  # noqa: E501
        :rtype: int
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this ContactItem.

        Contact  # noqa: E501

        :param contact_id: The contact_id of this ContactItem.  # noqa: E501
        :type: int
        """

        self._contact_id = contact_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this ContactItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this ContactItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this ContactItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def contact_type_enum(self):
        """Gets the contact_type_enum of this ContactItem.  # noqa: E501

        Contact Type  # noqa: E501

        :return: The contact_type_enum of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._contact_type_enum

    @contact_type_enum.setter
    def contact_type_enum(self, contact_type_enum):
        """Sets the contact_type_enum of this ContactItem.

        Contact Type  # noqa: E501

        :param contact_type_enum: The contact_type_enum of this ContactItem.  # noqa: E501
        :type: str
        """

        self._contact_type_enum = contact_type_enum

    @property
    def contact_status_id(self):
        """Gets the contact_status_id of this ContactItem.  # noqa: E501

        Contact Status  # noqa: E501

        :return: The contact_status_id of this ContactItem.  # noqa: E501
        :rtype: int
        """
        return self._contact_status_id

    @contact_status_id.setter
    def contact_status_id(self, contact_status_id):
        """Sets the contact_status_id of this ContactItem.

        Contact Status  # noqa: E501

        :param contact_status_id: The contact_status_id of this ContactItem.  # noqa: E501
        :type: int
        """

        self._contact_status_id = contact_status_id

    @property
    def category_id(self):
        """Gets the category_id of this ContactItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this ContactItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ContactItem.

        Category  # noqa: E501

        :param category_id: The category_id of this ContactItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def tax_exemption_enum(self):
        """Gets the tax_exemption_enum of this ContactItem.  # noqa: E501

        Tax Exemption  # noqa: E501

        :return: The tax_exemption_enum of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._tax_exemption_enum

    @tax_exemption_enum.setter
    def tax_exemption_enum(self, tax_exemption_enum):
        """Sets the tax_exemption_enum of this ContactItem.

        Tax Exemption  # noqa: E501

        :param tax_exemption_enum: The tax_exemption_enum of this ContactItem.  # noqa: E501
        :type: str
        """

        self._tax_exemption_enum = tax_exemption_enum

    @property
    def description(self):
        """Gets the description of this ContactItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ContactItem.

        Description  # noqa: E501

        :param description: The description of this ContactItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def street(self):
        """Gets the street of this ContactItem.  # noqa: E501

        Street  # noqa: E501

        :return: The street of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this ContactItem.

        Street  # noqa: E501

        :param street: The street of this ContactItem.  # noqa: E501
        :type: str
        """
        if street is not None and len(street) > 80:
            raise ValueError("Invalid value for `street`, length must be less than or equal to `80`")  # noqa: E501

        self._street = street

    @property
    def street2(self):
        """Gets the street2 of this ContactItem.  # noqa: E501

        Street 2  # noqa: E501

        :return: The street2 of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """Sets the street2 of this ContactItem.

        Street 2  # noqa: E501

        :param street2: The street2 of this ContactItem.  # noqa: E501
        :type: str
        """
        if street2 is not None and len(street2) > 80:
            raise ValueError("Invalid value for `street2`, length must be less than or equal to `80`")  # noqa: E501

        self._street2 = street2

    @property
    def city(self):
        """Gets the city of this ContactItem.  # noqa: E501

        City  # noqa: E501

        :return: The city of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ContactItem.

        City  # noqa: E501

        :param city: The city of this ContactItem.  # noqa: E501
        :type: str
        """
        if city is not None and len(city) > 60:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `60`")  # noqa: E501

        self._city = city

    @property
    def country_id(self):
        """Gets the country_id of this ContactItem.  # noqa: E501

        Country  # noqa: E501

        :return: The country_id of this ContactItem.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this ContactItem.

        Country  # noqa: E501

        :param country_id: The country_id of this ContactItem.  # noqa: E501
        :type: int
        """

        self._country_id = country_id

    @property
    def state_province(self):
        """Gets the state_province of this ContactItem.  # noqa: E501

        State Province  # noqa: E501

        :return: The state_province of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._state_province

    @state_province.setter
    def state_province(self, state_province):
        """Sets the state_province of this ContactItem.

        State Province  # noqa: E501

        :param state_province: The state_province of this ContactItem.  # noqa: E501
        :type: str
        """
        if state_province is not None and len(state_province) > 60:
            raise ValueError("Invalid value for `state_province`, length must be less than or equal to `60`")  # noqa: E501

        self._state_province = state_province

    @property
    def zip_postcode(self):
        """Gets the zip_postcode of this ContactItem.  # noqa: E501

        Zip Postcode  # noqa: E501

        :return: The zip_postcode of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._zip_postcode

    @zip_postcode.setter
    def zip_postcode(self, zip_postcode):
        """Sets the zip_postcode of this ContactItem.

        Zip Postcode  # noqa: E501

        :param zip_postcode: The zip_postcode of this ContactItem.  # noqa: E501
        :type: str
        """
        if zip_postcode is not None and len(zip_postcode) > 15:
            raise ValueError("Invalid value for `zip_postcode`, length must be less than or equal to `15`")  # noqa: E501

        self._zip_postcode = zip_postcode

    @property
    def entry_id(self):
        """Gets the entry_id of this ContactItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this ContactItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this ContactItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this ContactItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def phone(self):
        """Gets the phone of this ContactItem.  # noqa: E501

        Phone  # noqa: E501

        :return: The phone of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ContactItem.

        Phone  # noqa: E501

        :param phone: The phone of this ContactItem.  # noqa: E501
        :type: str
        """
        if phone is not None and len(phone) > 25:
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `25`")  # noqa: E501

        self._phone = phone

    @property
    def phone_mobile_cell(self):
        """Gets the phone_mobile_cell of this ContactItem.  # noqa: E501

        Phone Mobile Cell  # noqa: E501

        :return: The phone_mobile_cell of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._phone_mobile_cell

    @phone_mobile_cell.setter
    def phone_mobile_cell(self, phone_mobile_cell):
        """Sets the phone_mobile_cell of this ContactItem.

        Phone Mobile Cell  # noqa: E501

        :param phone_mobile_cell: The phone_mobile_cell of this ContactItem.  # noqa: E501
        :type: str
        """
        if phone_mobile_cell is not None and len(phone_mobile_cell) > 25:
            raise ValueError("Invalid value for `phone_mobile_cell`, length must be less than or equal to `25`")  # noqa: E501

        self._phone_mobile_cell = phone_mobile_cell

    @property
    def phone_other(self):
        """Gets the phone_other of this ContactItem.  # noqa: E501

        Phone Other  # noqa: E501

        :return: The phone_other of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._phone_other

    @phone_other.setter
    def phone_other(self, phone_other):
        """Sets the phone_other of this ContactItem.

        Phone Other  # noqa: E501

        :param phone_other: The phone_other of this ContactItem.  # noqa: E501
        :type: str
        """
        if phone_other is not None and len(phone_other) > 25:
            raise ValueError("Invalid value for `phone_other`, length must be less than or equal to `25`")  # noqa: E501

        self._phone_other = phone_other

    @property
    def phone_other2(self):
        """Gets the phone_other2 of this ContactItem.  # noqa: E501

        Phone Other 2  # noqa: E501

        :return: The phone_other2 of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._phone_other2

    @phone_other2.setter
    def phone_other2(self, phone_other2):
        """Sets the phone_other2 of this ContactItem.

        Phone Other 2  # noqa: E501

        :param phone_other2: The phone_other2 of this ContactItem.  # noqa: E501
        :type: str
        """
        if phone_other2 is not None and len(phone_other2) > 25:
            raise ValueError("Invalid value for `phone_other2`, length must be less than or equal to `25`")  # noqa: E501

        self._phone_other2 = phone_other2

    @property
    def email(self):
        """Gets the email of this ContactItem.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactItem.

        Email  # noqa: E501

        :param email: The email of this ContactItem.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 100:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `100`")  # noqa: E501

        self._email = email

    @property
    def reference(self):
        """Gets the reference of this ContactItem.  # noqa: E501

        Reference  # noqa: E501

        :return: The reference of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ContactItem.

        Reference  # noqa: E501

        :param reference: The reference of this ContactItem.  # noqa: E501
        :type: str
        """
        if reference is not None and len(reference) > 30:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `30`")  # noqa: E501

        self._reference = reference

    @property
    def account_code(self):
        """Gets the account_code of this ContactItem.  # noqa: E501

        Account Code  # noqa: E501

        :return: The account_code of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this ContactItem.

        Account Code  # noqa: E501

        :param account_code: The account_code of this ContactItem.  # noqa: E501
        :type: str
        """
        if account_code is not None and len(account_code) > 20:
            raise ValueError("Invalid value for `account_code`, length must be less than or equal to `20`")  # noqa: E501

        self._account_code = account_code

    @property
    def account_comments(self):
        """Gets the account_comments of this ContactItem.  # noqa: E501

        Account Comments  # noqa: E501

        :return: The account_comments of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._account_comments

    @account_comments.setter
    def account_comments(self, account_comments):
        """Sets the account_comments of this ContactItem.

        Account Comments  # noqa: E501

        :param account_comments: The account_comments of this ContactItem.  # noqa: E501
        :type: str
        """
        if account_comments is not None and len(account_comments) > 100:
            raise ValueError("Invalid value for `account_comments`, length must be less than or equal to `100`")  # noqa: E501

        self._account_comments = account_comments

    @property
    def account_payment_type_id(self):
        """Gets the account_payment_type_id of this ContactItem.  # noqa: E501

        Account Payment Type  # noqa: E501

        :return: The account_payment_type_id of this ContactItem.  # noqa: E501
        :rtype: int
        """
        return self._account_payment_type_id

    @account_payment_type_id.setter
    def account_payment_type_id(self, account_payment_type_id):
        """Sets the account_payment_type_id of this ContactItem.

        Account Payment Type  # noqa: E501

        :param account_payment_type_id: The account_payment_type_id of this ContactItem.  # noqa: E501
        :type: int
        """

        self._account_payment_type_id = account_payment_type_id

    @property
    def account_bank_name(self):
        """Gets the account_bank_name of this ContactItem.  # noqa: E501

        Account Bank Name  # noqa: E501

        :return: The account_bank_name of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._account_bank_name

    @account_bank_name.setter
    def account_bank_name(self, account_bank_name):
        """Sets the account_bank_name of this ContactItem.

        Account Bank Name  # noqa: E501

        :param account_bank_name: The account_bank_name of this ContactItem.  # noqa: E501
        :type: str
        """

        self._account_bank_name = account_bank_name

    @property
    def account_bank_number(self):
        """Gets the account_bank_number of this ContactItem.  # noqa: E501

        Account Bank Number  # noqa: E501

        :return: The account_bank_number of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._account_bank_number

    @account_bank_number.setter
    def account_bank_number(self, account_bank_number):
        """Sets the account_bank_number of this ContactItem.

        Account Bank Number  # noqa: E501

        :param account_bank_number: The account_bank_number of this ContactItem.  # noqa: E501
        :type: str
        """

        self._account_bank_number = account_bank_number

    @property
    def account_detail1(self):
        """Gets the account_detail1 of this ContactItem.  # noqa: E501

        Account 1  # noqa: E501

        :return: The account_detail1 of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._account_detail1

    @account_detail1.setter
    def account_detail1(self, account_detail1):
        """Sets the account_detail1 of this ContactItem.

        Account 1  # noqa: E501

        :param account_detail1: The account_detail1 of this ContactItem.  # noqa: E501
        :type: str
        """

        self._account_detail1 = account_detail1

    @property
    def account_detail2(self):
        """Gets the account_detail2 of this ContactItem.  # noqa: E501

        Account 2  # noqa: E501

        :return: The account_detail2 of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._account_detail2

    @account_detail2.setter
    def account_detail2(self, account_detail2):
        """Sets the account_detail2 of this ContactItem.

        Account 2  # noqa: E501

        :param account_detail2: The account_detail2 of this ContactItem.  # noqa: E501
        :type: str
        """

        self._account_detail2 = account_detail2

    @property
    def account_detail3(self):
        """Gets the account_detail3 of this ContactItem.  # noqa: E501

        Account 3  # noqa: E501

        :return: The account_detail3 of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._account_detail3

    @account_detail3.setter
    def account_detail3(self, account_detail3):
        """Sets the account_detail3 of this ContactItem.

        Account 3  # noqa: E501

        :param account_detail3: The account_detail3 of this ContactItem.  # noqa: E501
        :type: str
        """

        self._account_detail3 = account_detail3

    @property
    def account_detail4(self):
        """Gets the account_detail4 of this ContactItem.  # noqa: E501

        Account 4  # noqa: E501

        :return: The account_detail4 of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._account_detail4

    @account_detail4.setter
    def account_detail4(self, account_detail4):
        """Sets the account_detail4 of this ContactItem.

        Account 4  # noqa: E501

        :param account_detail4: The account_detail4 of this ContactItem.  # noqa: E501
        :type: str
        """

        self._account_detail4 = account_detail4

    @property
    def comments(self):
        """Gets the comments of this ContactItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ContactItem.

        Comments  # noqa: E501

        :param comments: The comments of this ContactItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 500:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `500`")  # noqa: E501

        self._comments = comments

    @property
    def security_user_id(self):
        """Gets the security_user_id of this ContactItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this ContactItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this ContactItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this ContactItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this ContactItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this ContactItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ContactItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this ContactItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def timestamp(self):
        """Gets the timestamp of this ContactItem.  # noqa: E501

        Timestamp  # noqa: E501

        :return: The timestamp of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ContactItem.

        Timestamp  # noqa: E501

        :param timestamp: The timestamp of this ContactItem.  # noqa: E501
        :type: str
        """
        if timestamp is not None and len(timestamp) > 8:
            raise ValueError("Invalid value for `timestamp`, length must be less than or equal to `8`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def date_modified(self):
        """Gets the date_modified of this ContactItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this ContactItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ContactItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this ContactItem.  # noqa: E501
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
        if not isinstance(other, ContactItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
