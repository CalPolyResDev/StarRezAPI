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


class MealPlanItem(object):
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
        'meal_plan_id': 'int',
        'record_type_enum': 'str',
        'term_session_id': 'int',
        'meal_plan_dining_hall_id': 'int',
        'description': 'str',
        'code': 'str',
        'date_start': 'datetime',
        'date_end': 'datetime',
        'active': 'bool',
        'meal_setup_enum': 'str',
        'charges_not_allowed': 'bool',
        'meal_pricing_id': 'int',
        'number_of_meals': 'str',
        'number_of_servings': 'str',
        'charge_item_id': 'int',
        'allowance_a': 'str',
        'allowance_a_rate': 'str',
        'allowance_b': 'str',
        'allowance_b_rate': 'str',
        'allowance_c': 'str',
        'allowance_c_rate': 'str',
        'transaction_date_due': 'str',
        'update_contract_dates_when_dates_change': 'bool',
        'comments': 'str',
        'custom_bit1': 'bool',
        'custom_bit2': 'bool',
        'custom_string1': 'str',
        'custom_string2': 'str',
        'custom_string3': 'str',
        'custom_string4': 'str',
        'custom_string5': 'str',
        'custom_string6': 'str',
        'custom_date1': 'str',
        'custom_date2': 'str',
        'view_on_web': 'bool',
        'web_description': 'str',
        'web_order': 'int',
        'web_comments': 'str',
        'security_user_id': 'int',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'meal_plan_id': 'MealPlanID',
        'record_type_enum': 'RecordTypeEnum',
        'term_session_id': 'TermSessionID',
        'meal_plan_dining_hall_id': 'MealPlanDiningHallID',
        'description': 'Description',
        'code': 'Code',
        'date_start': 'DateStart',
        'date_end': 'DateEnd',
        'active': 'Active',
        'meal_setup_enum': 'MealSetupEnum',
        'charges_not_allowed': 'ChargesNotAllowed',
        'meal_pricing_id': 'MealPricingID',
        'number_of_meals': 'NumberOfMeals',
        'number_of_servings': 'NumberOfServings',
        'charge_item_id': 'ChargeItemID',
        'allowance_a': 'AllowanceA',
        'allowance_a_rate': 'AllowanceARate',
        'allowance_b': 'AllowanceB',
        'allowance_b_rate': 'AllowanceBRate',
        'allowance_c': 'AllowanceC',
        'allowance_c_rate': 'AllowanceCRate',
        'transaction_date_due': 'TransactionDateDue',
        'update_contract_dates_when_dates_change': 'UpdateContractDatesWhenDatesChange',
        'comments': 'Comments',
        'custom_bit1': 'CustomBit1',
        'custom_bit2': 'CustomBit2',
        'custom_string1': 'CustomString1',
        'custom_string2': 'CustomString2',
        'custom_string3': 'CustomString3',
        'custom_string4': 'CustomString4',
        'custom_string5': 'CustomString5',
        'custom_string6': 'CustomString6',
        'custom_date1': 'CustomDate1',
        'custom_date2': 'CustomDate2',
        'view_on_web': 'ViewOnWeb',
        'web_description': 'WebDescription',
        'web_order': 'WebOrder',
        'web_comments': 'WebComments',
        'security_user_id': 'SecurityUserID',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, meal_plan_id=None, record_type_enum=None, term_session_id=None, meal_plan_dining_hall_id=None, description=None, code=None, date_start=None, date_end=None, active=None, meal_setup_enum=None, charges_not_allowed=None, meal_pricing_id=None, number_of_meals=None, number_of_servings=None, charge_item_id=None, allowance_a=None, allowance_a_rate=None, allowance_b=None, allowance_b_rate=None, allowance_c=None, allowance_c_rate=None, transaction_date_due=None, update_contract_dates_when_dates_change=None, comments=None, custom_bit1=None, custom_bit2=None, custom_string1=None, custom_string2=None, custom_string3=None, custom_string4=None, custom_string5=None, custom_string6=None, custom_date1=None, custom_date2=None, view_on_web=None, web_description=None, web_order=None, web_comments=None, security_user_id=None, date_created=None, date_modified=None):  # noqa: E501
        """MealPlanItem - a model defined in Swagger"""  # noqa: E501

        self._meal_plan_id = None
        self._record_type_enum = None
        self._term_session_id = None
        self._meal_plan_dining_hall_id = None
        self._description = None
        self._code = None
        self._date_start = None
        self._date_end = None
        self._active = None
        self._meal_setup_enum = None
        self._charges_not_allowed = None
        self._meal_pricing_id = None
        self._number_of_meals = None
        self._number_of_servings = None
        self._charge_item_id = None
        self._allowance_a = None
        self._allowance_a_rate = None
        self._allowance_b = None
        self._allowance_b_rate = None
        self._allowance_c = None
        self._allowance_c_rate = None
        self._transaction_date_due = None
        self._update_contract_dates_when_dates_change = None
        self._comments = None
        self._custom_bit1 = None
        self._custom_bit2 = None
        self._custom_string1 = None
        self._custom_string2 = None
        self._custom_string3 = None
        self._custom_string4 = None
        self._custom_string5 = None
        self._custom_string6 = None
        self._custom_date1 = None
        self._custom_date2 = None
        self._view_on_web = None
        self._web_description = None
        self._web_order = None
        self._web_comments = None
        self._security_user_id = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if meal_plan_id is not None:
            self.meal_plan_id = meal_plan_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if term_session_id is not None:
            self.term_session_id = term_session_id
        if meal_plan_dining_hall_id is not None:
            self.meal_plan_dining_hall_id = meal_plan_dining_hall_id
        if description is not None:
            self.description = description
        if code is not None:
            self.code = code
        if date_start is not None:
            self.date_start = date_start
        if date_end is not None:
            self.date_end = date_end
        if active is not None:
            self.active = active
        if meal_setup_enum is not None:
            self.meal_setup_enum = meal_setup_enum
        if charges_not_allowed is not None:
            self.charges_not_allowed = charges_not_allowed
        if meal_pricing_id is not None:
            self.meal_pricing_id = meal_pricing_id
        if number_of_meals is not None:
            self.number_of_meals = number_of_meals
        if number_of_servings is not None:
            self.number_of_servings = number_of_servings
        if charge_item_id is not None:
            self.charge_item_id = charge_item_id
        if allowance_a is not None:
            self.allowance_a = allowance_a
        if allowance_a_rate is not None:
            self.allowance_a_rate = allowance_a_rate
        if allowance_b is not None:
            self.allowance_b = allowance_b
        if allowance_b_rate is not None:
            self.allowance_b_rate = allowance_b_rate
        if allowance_c is not None:
            self.allowance_c = allowance_c
        if allowance_c_rate is not None:
            self.allowance_c_rate = allowance_c_rate
        if transaction_date_due is not None:
            self.transaction_date_due = transaction_date_due
        if update_contract_dates_when_dates_change is not None:
            self.update_contract_dates_when_dates_change = update_contract_dates_when_dates_change
        if comments is not None:
            self.comments = comments
        if custom_bit1 is not None:
            self.custom_bit1 = custom_bit1
        if custom_bit2 is not None:
            self.custom_bit2 = custom_bit2
        if custom_string1 is not None:
            self.custom_string1 = custom_string1
        if custom_string2 is not None:
            self.custom_string2 = custom_string2
        if custom_string3 is not None:
            self.custom_string3 = custom_string3
        if custom_string4 is not None:
            self.custom_string4 = custom_string4
        if custom_string5 is not None:
            self.custom_string5 = custom_string5
        if custom_string6 is not None:
            self.custom_string6 = custom_string6
        if custom_date1 is not None:
            self.custom_date1 = custom_date1
        if custom_date2 is not None:
            self.custom_date2 = custom_date2
        if view_on_web is not None:
            self.view_on_web = view_on_web
        if web_description is not None:
            self.web_description = web_description
        if web_order is not None:
            self.web_order = web_order
        if web_comments is not None:
            self.web_comments = web_comments
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def meal_plan_id(self):
        """Gets the meal_plan_id of this MealPlanItem.  # noqa: E501

        Meal Plan  # noqa: E501

        :return: The meal_plan_id of this MealPlanItem.  # noqa: E501
        :rtype: int
        """
        return self._meal_plan_id

    @meal_plan_id.setter
    def meal_plan_id(self, meal_plan_id):
        """Sets the meal_plan_id of this MealPlanItem.

        Meal Plan  # noqa: E501

        :param meal_plan_id: The meal_plan_id of this MealPlanItem.  # noqa: E501
        :type: int
        """

        self._meal_plan_id = meal_plan_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this MealPlanItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this MealPlanItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def term_session_id(self):
        """Gets the term_session_id of this MealPlanItem.  # noqa: E501

        Term Session  # noqa: E501

        :return: The term_session_id of this MealPlanItem.  # noqa: E501
        :rtype: int
        """
        return self._term_session_id

    @term_session_id.setter
    def term_session_id(self, term_session_id):
        """Sets the term_session_id of this MealPlanItem.

        Term Session  # noqa: E501

        :param term_session_id: The term_session_id of this MealPlanItem.  # noqa: E501
        :type: int
        """

        self._term_session_id = term_session_id

    @property
    def meal_plan_dining_hall_id(self):
        """Gets the meal_plan_dining_hall_id of this MealPlanItem.  # noqa: E501

        Meal Plan Dining Hall  # noqa: E501

        :return: The meal_plan_dining_hall_id of this MealPlanItem.  # noqa: E501
        :rtype: int
        """
        return self._meal_plan_dining_hall_id

    @meal_plan_dining_hall_id.setter
    def meal_plan_dining_hall_id(self, meal_plan_dining_hall_id):
        """Sets the meal_plan_dining_hall_id of this MealPlanItem.

        Meal Plan Dining Hall  # noqa: E501

        :param meal_plan_dining_hall_id: The meal_plan_dining_hall_id of this MealPlanItem.  # noqa: E501
        :type: int
        """

        self._meal_plan_dining_hall_id = meal_plan_dining_hall_id

    @property
    def description(self):
        """Gets the description of this MealPlanItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MealPlanItem.

        Description  # noqa: E501

        :param description: The description of this MealPlanItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def code(self):
        """Gets the code of this MealPlanItem.  # noqa: E501

        Code  # noqa: E501

        :return: The code of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this MealPlanItem.

        Code  # noqa: E501

        :param code: The code of this MealPlanItem.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) > 20:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `20`")  # noqa: E501

        self._code = code

    @property
    def date_start(self):
        """Gets the date_start of this MealPlanItem.  # noqa: E501

        Date Start  # noqa: E501

        :return: The date_start of this MealPlanItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this MealPlanItem.

        Date Start  # noqa: E501

        :param date_start: The date_start of this MealPlanItem.  # noqa: E501
        :type: datetime
        """

        self._date_start = date_start

    @property
    def date_end(self):
        """Gets the date_end of this MealPlanItem.  # noqa: E501

        Date End  # noqa: E501

        :return: The date_end of this MealPlanItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this MealPlanItem.

        Date End  # noqa: E501

        :param date_end: The date_end of this MealPlanItem.  # noqa: E501
        :type: datetime
        """

        self._date_end = date_end

    @property
    def active(self):
        """Gets the active of this MealPlanItem.  # noqa: E501

        Active  # noqa: E501

        :return: The active of this MealPlanItem.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this MealPlanItem.

        Active  # noqa: E501

        :param active: The active of this MealPlanItem.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def meal_setup_enum(self):
        """Gets the meal_setup_enum of this MealPlanItem.  # noqa: E501

        Meal Setup  # noqa: E501

        :return: The meal_setup_enum of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._meal_setup_enum

    @meal_setup_enum.setter
    def meal_setup_enum(self, meal_setup_enum):
        """Sets the meal_setup_enum of this MealPlanItem.

        Meal Setup  # noqa: E501

        :param meal_setup_enum: The meal_setup_enum of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._meal_setup_enum = meal_setup_enum

    @property
    def charges_not_allowed(self):
        """Gets the charges_not_allowed of this MealPlanItem.  # noqa: E501

        Charges Not Allowed  # noqa: E501

        :return: The charges_not_allowed of this MealPlanItem.  # noqa: E501
        :rtype: bool
        """
        return self._charges_not_allowed

    @charges_not_allowed.setter
    def charges_not_allowed(self, charges_not_allowed):
        """Sets the charges_not_allowed of this MealPlanItem.

        Charges Not Allowed  # noqa: E501

        :param charges_not_allowed: The charges_not_allowed of this MealPlanItem.  # noqa: E501
        :type: bool
        """

        self._charges_not_allowed = charges_not_allowed

    @property
    def meal_pricing_id(self):
        """Gets the meal_pricing_id of this MealPlanItem.  # noqa: E501

        Meal Pricing  # noqa: E501

        :return: The meal_pricing_id of this MealPlanItem.  # noqa: E501
        :rtype: int
        """
        return self._meal_pricing_id

    @meal_pricing_id.setter
    def meal_pricing_id(self, meal_pricing_id):
        """Sets the meal_pricing_id of this MealPlanItem.

        Meal Pricing  # noqa: E501

        :param meal_pricing_id: The meal_pricing_id of this MealPlanItem.  # noqa: E501
        :type: int
        """

        self._meal_pricing_id = meal_pricing_id

    @property
    def number_of_meals(self):
        """Gets the number_of_meals of this MealPlanItem.  # noqa: E501

        Number Of Meals  # noqa: E501

        :return: The number_of_meals of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._number_of_meals

    @number_of_meals.setter
    def number_of_meals(self, number_of_meals):
        """Sets the number_of_meals of this MealPlanItem.

        Number Of Meals  # noqa: E501

        :param number_of_meals: The number_of_meals of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._number_of_meals = number_of_meals

    @property
    def number_of_servings(self):
        """Gets the number_of_servings of this MealPlanItem.  # noqa: E501

        Number Of Servings  # noqa: E501

        :return: The number_of_servings of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._number_of_servings

    @number_of_servings.setter
    def number_of_servings(self, number_of_servings):
        """Sets the number_of_servings of this MealPlanItem.

        Number Of Servings  # noqa: E501

        :param number_of_servings: The number_of_servings of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._number_of_servings = number_of_servings

    @property
    def charge_item_id(self):
        """Gets the charge_item_id of this MealPlanItem.  # noqa: E501

        Charge Item  # noqa: E501

        :return: The charge_item_id of this MealPlanItem.  # noqa: E501
        :rtype: int
        """
        return self._charge_item_id

    @charge_item_id.setter
    def charge_item_id(self, charge_item_id):
        """Sets the charge_item_id of this MealPlanItem.

        Charge Item  # noqa: E501

        :param charge_item_id: The charge_item_id of this MealPlanItem.  # noqa: E501
        :type: int
        """

        self._charge_item_id = charge_item_id

    @property
    def allowance_a(self):
        """Gets the allowance_a of this MealPlanItem.  # noqa: E501

        Allowance A  # noqa: E501

        :return: The allowance_a of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._allowance_a

    @allowance_a.setter
    def allowance_a(self, allowance_a):
        """Sets the allowance_a of this MealPlanItem.

        Allowance A  # noqa: E501

        :param allowance_a: The allowance_a of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._allowance_a = allowance_a

    @property
    def allowance_a_rate(self):
        """Gets the allowance_a_rate of this MealPlanItem.  # noqa: E501

        Allowance A Rate  # noqa: E501

        :return: The allowance_a_rate of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._allowance_a_rate

    @allowance_a_rate.setter
    def allowance_a_rate(self, allowance_a_rate):
        """Sets the allowance_a_rate of this MealPlanItem.

        Allowance A Rate  # noqa: E501

        :param allowance_a_rate: The allowance_a_rate of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._allowance_a_rate = allowance_a_rate

    @property
    def allowance_b(self):
        """Gets the allowance_b of this MealPlanItem.  # noqa: E501

        Allowance B  # noqa: E501

        :return: The allowance_b of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._allowance_b

    @allowance_b.setter
    def allowance_b(self, allowance_b):
        """Sets the allowance_b of this MealPlanItem.

        Allowance B  # noqa: E501

        :param allowance_b: The allowance_b of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._allowance_b = allowance_b

    @property
    def allowance_b_rate(self):
        """Gets the allowance_b_rate of this MealPlanItem.  # noqa: E501

        Allowance B Rate  # noqa: E501

        :return: The allowance_b_rate of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._allowance_b_rate

    @allowance_b_rate.setter
    def allowance_b_rate(self, allowance_b_rate):
        """Sets the allowance_b_rate of this MealPlanItem.

        Allowance B Rate  # noqa: E501

        :param allowance_b_rate: The allowance_b_rate of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._allowance_b_rate = allowance_b_rate

    @property
    def allowance_c(self):
        """Gets the allowance_c of this MealPlanItem.  # noqa: E501

        Allowance C  # noqa: E501

        :return: The allowance_c of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._allowance_c

    @allowance_c.setter
    def allowance_c(self, allowance_c):
        """Sets the allowance_c of this MealPlanItem.

        Allowance C  # noqa: E501

        :param allowance_c: The allowance_c of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._allowance_c = allowance_c

    @property
    def allowance_c_rate(self):
        """Gets the allowance_c_rate of this MealPlanItem.  # noqa: E501

        Allowance C Rate  # noqa: E501

        :return: The allowance_c_rate of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._allowance_c_rate

    @allowance_c_rate.setter
    def allowance_c_rate(self, allowance_c_rate):
        """Sets the allowance_c_rate of this MealPlanItem.

        Allowance C Rate  # noqa: E501

        :param allowance_c_rate: The allowance_c_rate of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._allowance_c_rate = allowance_c_rate

    @property
    def transaction_date_due(self):
        """Gets the transaction_date_due of this MealPlanItem.  # noqa: E501

        Transaction Date Due  # noqa: E501

        :return: The transaction_date_due of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date_due

    @transaction_date_due.setter
    def transaction_date_due(self, transaction_date_due):
        """Sets the transaction_date_due of this MealPlanItem.

        Transaction Date Due  # noqa: E501

        :param transaction_date_due: The transaction_date_due of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._transaction_date_due = transaction_date_due

    @property
    def update_contract_dates_when_dates_change(self):
        """Gets the update_contract_dates_when_dates_change of this MealPlanItem.  # noqa: E501

        Update Contract Dates When Dates Change  # noqa: E501

        :return: The update_contract_dates_when_dates_change of this MealPlanItem.  # noqa: E501
        :rtype: bool
        """
        return self._update_contract_dates_when_dates_change

    @update_contract_dates_when_dates_change.setter
    def update_contract_dates_when_dates_change(self, update_contract_dates_when_dates_change):
        """Sets the update_contract_dates_when_dates_change of this MealPlanItem.

        Update Contract Dates When Dates Change  # noqa: E501

        :param update_contract_dates_when_dates_change: The update_contract_dates_when_dates_change of this MealPlanItem.  # noqa: E501
        :type: bool
        """

        self._update_contract_dates_when_dates_change = update_contract_dates_when_dates_change

    @property
    def comments(self):
        """Gets the comments of this MealPlanItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this MealPlanItem.

        Comments  # noqa: E501

        :param comments: The comments of this MealPlanItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 200:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `200`")  # noqa: E501

        self._comments = comments

    @property
    def custom_bit1(self):
        """Gets the custom_bit1 of this MealPlanItem.  # noqa: E501

        Custom Flag 1  # noqa: E501

        :return: The custom_bit1 of this MealPlanItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit1

    @custom_bit1.setter
    def custom_bit1(self, custom_bit1):
        """Sets the custom_bit1 of this MealPlanItem.

        Custom Flag 1  # noqa: E501

        :param custom_bit1: The custom_bit1 of this MealPlanItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit1 = custom_bit1

    @property
    def custom_bit2(self):
        """Gets the custom_bit2 of this MealPlanItem.  # noqa: E501

        Custom Flag 2  # noqa: E501

        :return: The custom_bit2 of this MealPlanItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit2

    @custom_bit2.setter
    def custom_bit2(self, custom_bit2):
        """Sets the custom_bit2 of this MealPlanItem.

        Custom Flag 2  # noqa: E501

        :param custom_bit2: The custom_bit2 of this MealPlanItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit2 = custom_bit2

    @property
    def custom_string1(self):
        """Gets the custom_string1 of this MealPlanItem.  # noqa: E501

        Classification Availability  # noqa: E501

        :return: The custom_string1 of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string1

    @custom_string1.setter
    def custom_string1(self, custom_string1):
        """Sets the custom_string1 of this MealPlanItem.

        Classification Availability  # noqa: E501

        :param custom_string1: The custom_string1 of this MealPlanItem.  # noqa: E501
        :type: str
        """
        if custom_string1 is not None and len(custom_string1) > 50:
            raise ValueError("Invalid value for `custom_string1`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string1 = custom_string1

    @property
    def custom_string2(self):
        """Gets the custom_string2 of this MealPlanItem.  # noqa: E501

        Custom String 2  # noqa: E501

        :return: The custom_string2 of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string2

    @custom_string2.setter
    def custom_string2(self, custom_string2):
        """Sets the custom_string2 of this MealPlanItem.

        Custom String 2  # noqa: E501

        :param custom_string2: The custom_string2 of this MealPlanItem.  # noqa: E501
        :type: str
        """
        if custom_string2 is not None and len(custom_string2) > 50:
            raise ValueError("Invalid value for `custom_string2`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string2 = custom_string2

    @property
    def custom_string3(self):
        """Gets the custom_string3 of this MealPlanItem.  # noqa: E501

        Custom String 3  # noqa: E501

        :return: The custom_string3 of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string3

    @custom_string3.setter
    def custom_string3(self, custom_string3):
        """Sets the custom_string3 of this MealPlanItem.

        Custom String 3  # noqa: E501

        :param custom_string3: The custom_string3 of this MealPlanItem.  # noqa: E501
        :type: str
        """
        if custom_string3 is not None and len(custom_string3) > 50:
            raise ValueError("Invalid value for `custom_string3`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string3 = custom_string3

    @property
    def custom_string4(self):
        """Gets the custom_string4 of this MealPlanItem.  # noqa: E501

        Custom String 4  # noqa: E501

        :return: The custom_string4 of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string4

    @custom_string4.setter
    def custom_string4(self, custom_string4):
        """Sets the custom_string4 of this MealPlanItem.

        Custom String 4  # noqa: E501

        :param custom_string4: The custom_string4 of this MealPlanItem.  # noqa: E501
        :type: str
        """
        if custom_string4 is not None and len(custom_string4) > 50:
            raise ValueError("Invalid value for `custom_string4`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string4 = custom_string4

    @property
    def custom_string5(self):
        """Gets the custom_string5 of this MealPlanItem.  # noqa: E501

        Custom String 5  # noqa: E501

        :return: The custom_string5 of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string5

    @custom_string5.setter
    def custom_string5(self, custom_string5):
        """Sets the custom_string5 of this MealPlanItem.

        Custom String 5  # noqa: E501

        :param custom_string5: The custom_string5 of this MealPlanItem.  # noqa: E501
        :type: str
        """
        if custom_string5 is not None and len(custom_string5) > 50:
            raise ValueError("Invalid value for `custom_string5`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string5 = custom_string5

    @property
    def custom_string6(self):
        """Gets the custom_string6 of this MealPlanItem.  # noqa: E501

        Custom String 6  # noqa: E501

        :return: The custom_string6 of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string6

    @custom_string6.setter
    def custom_string6(self, custom_string6):
        """Sets the custom_string6 of this MealPlanItem.

        Custom String 6  # noqa: E501

        :param custom_string6: The custom_string6 of this MealPlanItem.  # noqa: E501
        :type: str
        """
        if custom_string6 is not None and len(custom_string6) > 50:
            raise ValueError("Invalid value for `custom_string6`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string6 = custom_string6

    @property
    def custom_date1(self):
        """Gets the custom_date1 of this MealPlanItem.  # noqa: E501

        Custom Date 1  # noqa: E501

        :return: The custom_date1 of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date1

    @custom_date1.setter
    def custom_date1(self, custom_date1):
        """Sets the custom_date1 of this MealPlanItem.

        Custom Date 1  # noqa: E501

        :param custom_date1: The custom_date1 of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._custom_date1 = custom_date1

    @property
    def custom_date2(self):
        """Gets the custom_date2 of this MealPlanItem.  # noqa: E501

        Custom Date 2  # noqa: E501

        :return: The custom_date2 of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date2

    @custom_date2.setter
    def custom_date2(self, custom_date2):
        """Sets the custom_date2 of this MealPlanItem.

        Custom Date 2  # noqa: E501

        :param custom_date2: The custom_date2 of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._custom_date2 = custom_date2

    @property
    def view_on_web(self):
        """Gets the view_on_web of this MealPlanItem.  # noqa: E501

        View On Web  # noqa: E501

        :return: The view_on_web of this MealPlanItem.  # noqa: E501
        :rtype: bool
        """
        return self._view_on_web

    @view_on_web.setter
    def view_on_web(self, view_on_web):
        """Sets the view_on_web of this MealPlanItem.

        View On Web  # noqa: E501

        :param view_on_web: The view_on_web of this MealPlanItem.  # noqa: E501
        :type: bool
        """

        self._view_on_web = view_on_web

    @property
    def web_description(self):
        """Gets the web_description of this MealPlanItem.  # noqa: E501

        Web Description  # noqa: E501

        :return: The web_description of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._web_description

    @web_description.setter
    def web_description(self, web_description):
        """Sets the web_description of this MealPlanItem.

        Web Description  # noqa: E501

        :param web_description: The web_description of this MealPlanItem.  # noqa: E501
        :type: str
        """
        if web_description is not None and len(web_description) > 1000:
            raise ValueError("Invalid value for `web_description`, length must be less than or equal to `1000`")  # noqa: E501

        self._web_description = web_description

    @property
    def web_order(self):
        """Gets the web_order of this MealPlanItem.  # noqa: E501

        Web Order  # noqa: E501

        :return: The web_order of this MealPlanItem.  # noqa: E501
        :rtype: int
        """
        return self._web_order

    @web_order.setter
    def web_order(self, web_order):
        """Sets the web_order of this MealPlanItem.

        Web Order  # noqa: E501

        :param web_order: The web_order of this MealPlanItem.  # noqa: E501
        :type: int
        """

        self._web_order = web_order

    @property
    def web_comments(self):
        """Gets the web_comments of this MealPlanItem.  # noqa: E501

        Web Comments  # noqa: E501

        :return: The web_comments of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._web_comments

    @web_comments.setter
    def web_comments(self, web_comments):
        """Sets the web_comments of this MealPlanItem.

        Web Comments  # noqa: E501

        :param web_comments: The web_comments of this MealPlanItem.  # noqa: E501
        :type: str
        """

        self._web_comments = web_comments

    @property
    def security_user_id(self):
        """Gets the security_user_id of this MealPlanItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this MealPlanItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this MealPlanItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this MealPlanItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this MealPlanItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this MealPlanItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this MealPlanItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this MealPlanItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this MealPlanItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this MealPlanItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this MealPlanItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this MealPlanItem.  # noqa: E501
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
        if not isinstance(other, MealPlanItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
