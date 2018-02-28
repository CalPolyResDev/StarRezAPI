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


class CategoryItem(object):
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
        'category_id': 'int',
        'description': 'str',
        'parent_id': 'int',
        'category_level': 'int',
        'category_type_enum': 'str',
        'abbreviation': 'str',
        'comments': 'str',
        'default_charge_group_id': 'int',
        'update_entry_defaults': 'bool',
        'update_entry_defaults_on_change': 'bool',
        'phone_disable_value': 'str',
        'phone_restrict_value': 'str',
        'phone_control_enum': 'str',
        'phone_charge_type_id': 'int',
        'history_category_enabled': 'bool',
        'history_category_id': 'int',
        'alumni_category_enabled': 'bool',
        'alumni_category_id': 'int',
        'reservation_category_enabled': 'bool',
        'reservation_category_id': 'int',
        'vm_mail_box_type_id': 'int',
        'vm_check_out_option_enum': 'str',
        'vm_check_out_remove_message_enum': 'str',
        'category_colour': 'str',
        'security_user_id': 'int',
        'date_created': 'datetime',
        'timestamp': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'category_id': 'CategoryID',
        'description': 'Description',
        'parent_id': 'ParentID',
        'category_level': 'CategoryLevel',
        'category_type_enum': 'CategoryTypeEnum',
        'abbreviation': 'Abbreviation',
        'comments': 'Comments',
        'default_charge_group_id': 'Default_ChargeGroupID',
        'update_entry_defaults': 'UpdateEntryDefaults',
        'update_entry_defaults_on_change': 'UpdateEntryDefaultsOnChange',
        'phone_disable_value': 'PhoneDisableValue',
        'phone_restrict_value': 'PhoneRestrictValue',
        'phone_control_enum': 'PhoneControlEnum',
        'phone_charge_type_id': 'PhoneChargeTypeID',
        'history_category_enabled': 'HistoryCategoryEnabled',
        'history_category_id': 'History_CategoryID',
        'alumni_category_enabled': 'AlumniCategoryEnabled',
        'alumni_category_id': 'Alumni_CategoryID',
        'reservation_category_enabled': 'ReservationCategoryEnabled',
        'reservation_category_id': 'Reservation_CategoryID',
        'vm_mail_box_type_id': 'VMMailBoxTypeID',
        'vm_check_out_option_enum': 'VMCheckOutOptionEnum',
        'vm_check_out_remove_message_enum': 'VMCheckOutRemoveMessageEnum',
        'category_colour': 'CategoryColour',
        'security_user_id': 'SecurityUserID',
        'date_created': 'DateCreated',
        'timestamp': 'timestamp',
        'date_modified': 'DateModified'
    }

    def __init__(self, category_id=None, description=None, parent_id=None, category_level=None, category_type_enum=None, abbreviation=None, comments=None, default_charge_group_id=None, update_entry_defaults=None, update_entry_defaults_on_change=None, phone_disable_value=None, phone_restrict_value=None, phone_control_enum=None, phone_charge_type_id=None, history_category_enabled=None, history_category_id=None, alumni_category_enabled=None, alumni_category_id=None, reservation_category_enabled=None, reservation_category_id=None, vm_mail_box_type_id=None, vm_check_out_option_enum=None, vm_check_out_remove_message_enum=None, category_colour=None, security_user_id=None, date_created=None, timestamp=None, date_modified=None):  # noqa: E501
        """CategoryItem - a model defined in Swagger"""  # noqa: E501

        self._category_id = None
        self._description = None
        self._parent_id = None
        self._category_level = None
        self._category_type_enum = None
        self._abbreviation = None
        self._comments = None
        self._default_charge_group_id = None
        self._update_entry_defaults = None
        self._update_entry_defaults_on_change = None
        self._phone_disable_value = None
        self._phone_restrict_value = None
        self._phone_control_enum = None
        self._phone_charge_type_id = None
        self._history_category_enabled = None
        self._history_category_id = None
        self._alumni_category_enabled = None
        self._alumni_category_id = None
        self._reservation_category_enabled = None
        self._reservation_category_id = None
        self._vm_mail_box_type_id = None
        self._vm_check_out_option_enum = None
        self._vm_check_out_remove_message_enum = None
        self._category_colour = None
        self._security_user_id = None
        self._date_created = None
        self._timestamp = None
        self._date_modified = None
        self.discriminator = None

        if category_id is not None:
            self.category_id = category_id
        if description is not None:
            self.description = description
        if parent_id is not None:
            self.parent_id = parent_id
        if category_level is not None:
            self.category_level = category_level
        if category_type_enum is not None:
            self.category_type_enum = category_type_enum
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if comments is not None:
            self.comments = comments
        if default_charge_group_id is not None:
            self.default_charge_group_id = default_charge_group_id
        if update_entry_defaults is not None:
            self.update_entry_defaults = update_entry_defaults
        if update_entry_defaults_on_change is not None:
            self.update_entry_defaults_on_change = update_entry_defaults_on_change
        if phone_disable_value is not None:
            self.phone_disable_value = phone_disable_value
        if phone_restrict_value is not None:
            self.phone_restrict_value = phone_restrict_value
        if phone_control_enum is not None:
            self.phone_control_enum = phone_control_enum
        if phone_charge_type_id is not None:
            self.phone_charge_type_id = phone_charge_type_id
        if history_category_enabled is not None:
            self.history_category_enabled = history_category_enabled
        if history_category_id is not None:
            self.history_category_id = history_category_id
        if alumni_category_enabled is not None:
            self.alumni_category_enabled = alumni_category_enabled
        if alumni_category_id is not None:
            self.alumni_category_id = alumni_category_id
        if reservation_category_enabled is not None:
            self.reservation_category_enabled = reservation_category_enabled
        if reservation_category_id is not None:
            self.reservation_category_id = reservation_category_id
        if vm_mail_box_type_id is not None:
            self.vm_mail_box_type_id = vm_mail_box_type_id
        if vm_check_out_option_enum is not None:
            self.vm_check_out_option_enum = vm_check_out_option_enum
        if vm_check_out_remove_message_enum is not None:
            self.vm_check_out_remove_message_enum = vm_check_out_remove_message_enum
        if category_colour is not None:
            self.category_colour = category_colour
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_created is not None:
            self.date_created = date_created
        if timestamp is not None:
            self.timestamp = timestamp
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def category_id(self):
        """Gets the category_id of this CategoryItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this CategoryItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this CategoryItem.

        Category  # noqa: E501

        :param category_id: The category_id of this CategoryItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def description(self):
        """Gets the description of this CategoryItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CategoryItem.

        Description  # noqa: E501

        :param description: The description of this CategoryItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 80:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `80`")  # noqa: E501

        self._description = description

    @property
    def parent_id(self):
        """Gets the parent_id of this CategoryItem.  # noqa: E501

        Parent  # noqa: E501

        :return: The parent_id of this CategoryItem.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CategoryItem.

        Parent  # noqa: E501

        :param parent_id: The parent_id of this CategoryItem.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def category_level(self):
        """Gets the category_level of this CategoryItem.  # noqa: E501

        Category Level  # noqa: E501

        :return: The category_level of this CategoryItem.  # noqa: E501
        :rtype: int
        """
        return self._category_level

    @category_level.setter
    def category_level(self, category_level):
        """Sets the category_level of this CategoryItem.

        Category Level  # noqa: E501

        :param category_level: The category_level of this CategoryItem.  # noqa: E501
        :type: int
        """

        self._category_level = category_level

    @property
    def category_type_enum(self):
        """Gets the category_type_enum of this CategoryItem.  # noqa: E501

        Category Type  # noqa: E501

        :return: The category_type_enum of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._category_type_enum

    @category_type_enum.setter
    def category_type_enum(self, category_type_enum):
        """Sets the category_type_enum of this CategoryItem.

        Category Type  # noqa: E501

        :param category_type_enum: The category_type_enum of this CategoryItem.  # noqa: E501
        :type: str
        """

        self._category_type_enum = category_type_enum

    @property
    def abbreviation(self):
        """Gets the abbreviation of this CategoryItem.  # noqa: E501

        Abbreviation  # noqa: E501

        :return: The abbreviation of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this CategoryItem.

        Abbreviation  # noqa: E501

        :param abbreviation: The abbreviation of this CategoryItem.  # noqa: E501
        :type: str
        """
        if abbreviation is not None and len(abbreviation) > 10:
            raise ValueError("Invalid value for `abbreviation`, length must be less than or equal to `10`")  # noqa: E501

        self._abbreviation = abbreviation

    @property
    def comments(self):
        """Gets the comments of this CategoryItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this CategoryItem.

        Comments  # noqa: E501

        :param comments: The comments of this CategoryItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 500:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `500`")  # noqa: E501

        self._comments = comments

    @property
    def default_charge_group_id(self):
        """Gets the default_charge_group_id of this CategoryItem.  # noqa: E501

        Default Charge Group  # noqa: E501

        :return: The default_charge_group_id of this CategoryItem.  # noqa: E501
        :rtype: int
        """
        return self._default_charge_group_id

    @default_charge_group_id.setter
    def default_charge_group_id(self, default_charge_group_id):
        """Sets the default_charge_group_id of this CategoryItem.

        Default Charge Group  # noqa: E501

        :param default_charge_group_id: The default_charge_group_id of this CategoryItem.  # noqa: E501
        :type: int
        """

        self._default_charge_group_id = default_charge_group_id

    @property
    def update_entry_defaults(self):
        """Gets the update_entry_defaults of this CategoryItem.  # noqa: E501

        Update Entry Defaults  # noqa: E501

        :return: The update_entry_defaults of this CategoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._update_entry_defaults

    @update_entry_defaults.setter
    def update_entry_defaults(self, update_entry_defaults):
        """Sets the update_entry_defaults of this CategoryItem.

        Update Entry Defaults  # noqa: E501

        :param update_entry_defaults: The update_entry_defaults of this CategoryItem.  # noqa: E501
        :type: bool
        """

        self._update_entry_defaults = update_entry_defaults

    @property
    def update_entry_defaults_on_change(self):
        """Gets the update_entry_defaults_on_change of this CategoryItem.  # noqa: E501

        Update Entry Defaults On Change  # noqa: E501

        :return: The update_entry_defaults_on_change of this CategoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._update_entry_defaults_on_change

    @update_entry_defaults_on_change.setter
    def update_entry_defaults_on_change(self, update_entry_defaults_on_change):
        """Sets the update_entry_defaults_on_change of this CategoryItem.

        Update Entry Defaults On Change  # noqa: E501

        :param update_entry_defaults_on_change: The update_entry_defaults_on_change of this CategoryItem.  # noqa: E501
        :type: bool
        """

        self._update_entry_defaults_on_change = update_entry_defaults_on_change

    @property
    def phone_disable_value(self):
        """Gets the phone_disable_value of this CategoryItem.  # noqa: E501

        Phone Disable Value  # noqa: E501

        :return: The phone_disable_value of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._phone_disable_value

    @phone_disable_value.setter
    def phone_disable_value(self, phone_disable_value):
        """Sets the phone_disable_value of this CategoryItem.

        Phone Disable Value  # noqa: E501

        :param phone_disable_value: The phone_disable_value of this CategoryItem.  # noqa: E501
        :type: str
        """

        self._phone_disable_value = phone_disable_value

    @property
    def phone_restrict_value(self):
        """Gets the phone_restrict_value of this CategoryItem.  # noqa: E501

        Phone Restrict Value  # noqa: E501

        :return: The phone_restrict_value of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._phone_restrict_value

    @phone_restrict_value.setter
    def phone_restrict_value(self, phone_restrict_value):
        """Sets the phone_restrict_value of this CategoryItem.

        Phone Restrict Value  # noqa: E501

        :param phone_restrict_value: The phone_restrict_value of this CategoryItem.  # noqa: E501
        :type: str
        """

        self._phone_restrict_value = phone_restrict_value

    @property
    def phone_control_enum(self):
        """Gets the phone_control_enum of this CategoryItem.  # noqa: E501

        Phone Control  # noqa: E501

        :return: The phone_control_enum of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._phone_control_enum

    @phone_control_enum.setter
    def phone_control_enum(self, phone_control_enum):
        """Sets the phone_control_enum of this CategoryItem.

        Phone Control  # noqa: E501

        :param phone_control_enum: The phone_control_enum of this CategoryItem.  # noqa: E501
        :type: str
        """

        self._phone_control_enum = phone_control_enum

    @property
    def phone_charge_type_id(self):
        """Gets the phone_charge_type_id of this CategoryItem.  # noqa: E501

        Phone Charge Type  # noqa: E501

        :return: The phone_charge_type_id of this CategoryItem.  # noqa: E501
        :rtype: int
        """
        return self._phone_charge_type_id

    @phone_charge_type_id.setter
    def phone_charge_type_id(self, phone_charge_type_id):
        """Sets the phone_charge_type_id of this CategoryItem.

        Phone Charge Type  # noqa: E501

        :param phone_charge_type_id: The phone_charge_type_id of this CategoryItem.  # noqa: E501
        :type: int
        """

        self._phone_charge_type_id = phone_charge_type_id

    @property
    def history_category_enabled(self):
        """Gets the history_category_enabled of this CategoryItem.  # noqa: E501

        History Category Enabled  # noqa: E501

        :return: The history_category_enabled of this CategoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._history_category_enabled

    @history_category_enabled.setter
    def history_category_enabled(self, history_category_enabled):
        """Sets the history_category_enabled of this CategoryItem.

        History Category Enabled  # noqa: E501

        :param history_category_enabled: The history_category_enabled of this CategoryItem.  # noqa: E501
        :type: bool
        """

        self._history_category_enabled = history_category_enabled

    @property
    def history_category_id(self):
        """Gets the history_category_id of this CategoryItem.  # noqa: E501

        History Category  # noqa: E501

        :return: The history_category_id of this CategoryItem.  # noqa: E501
        :rtype: int
        """
        return self._history_category_id

    @history_category_id.setter
    def history_category_id(self, history_category_id):
        """Sets the history_category_id of this CategoryItem.

        History Category  # noqa: E501

        :param history_category_id: The history_category_id of this CategoryItem.  # noqa: E501
        :type: int
        """

        self._history_category_id = history_category_id

    @property
    def alumni_category_enabled(self):
        """Gets the alumni_category_enabled of this CategoryItem.  # noqa: E501

        Alumni Category Enabled  # noqa: E501

        :return: The alumni_category_enabled of this CategoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._alumni_category_enabled

    @alumni_category_enabled.setter
    def alumni_category_enabled(self, alumni_category_enabled):
        """Sets the alumni_category_enabled of this CategoryItem.

        Alumni Category Enabled  # noqa: E501

        :param alumni_category_enabled: The alumni_category_enabled of this CategoryItem.  # noqa: E501
        :type: bool
        """

        self._alumni_category_enabled = alumni_category_enabled

    @property
    def alumni_category_id(self):
        """Gets the alumni_category_id of this CategoryItem.  # noqa: E501

        Alumni Category  # noqa: E501

        :return: The alumni_category_id of this CategoryItem.  # noqa: E501
        :rtype: int
        """
        return self._alumni_category_id

    @alumni_category_id.setter
    def alumni_category_id(self, alumni_category_id):
        """Sets the alumni_category_id of this CategoryItem.

        Alumni Category  # noqa: E501

        :param alumni_category_id: The alumni_category_id of this CategoryItem.  # noqa: E501
        :type: int
        """

        self._alumni_category_id = alumni_category_id

    @property
    def reservation_category_enabled(self):
        """Gets the reservation_category_enabled of this CategoryItem.  # noqa: E501

        Reservation Category Enabled  # noqa: E501

        :return: The reservation_category_enabled of this CategoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._reservation_category_enabled

    @reservation_category_enabled.setter
    def reservation_category_enabled(self, reservation_category_enabled):
        """Sets the reservation_category_enabled of this CategoryItem.

        Reservation Category Enabled  # noqa: E501

        :param reservation_category_enabled: The reservation_category_enabled of this CategoryItem.  # noqa: E501
        :type: bool
        """

        self._reservation_category_enabled = reservation_category_enabled

    @property
    def reservation_category_id(self):
        """Gets the reservation_category_id of this CategoryItem.  # noqa: E501

        Reservation Category  # noqa: E501

        :return: The reservation_category_id of this CategoryItem.  # noqa: E501
        :rtype: int
        """
        return self._reservation_category_id

    @reservation_category_id.setter
    def reservation_category_id(self, reservation_category_id):
        """Sets the reservation_category_id of this CategoryItem.

        Reservation Category  # noqa: E501

        :param reservation_category_id: The reservation_category_id of this CategoryItem.  # noqa: E501
        :type: int
        """

        self._reservation_category_id = reservation_category_id

    @property
    def vm_mail_box_type_id(self):
        """Gets the vm_mail_box_type_id of this CategoryItem.  # noqa: E501

        VM Mail Box Type  # noqa: E501

        :return: The vm_mail_box_type_id of this CategoryItem.  # noqa: E501
        :rtype: int
        """
        return self._vm_mail_box_type_id

    @vm_mail_box_type_id.setter
    def vm_mail_box_type_id(self, vm_mail_box_type_id):
        """Sets the vm_mail_box_type_id of this CategoryItem.

        VM Mail Box Type  # noqa: E501

        :param vm_mail_box_type_id: The vm_mail_box_type_id of this CategoryItem.  # noqa: E501
        :type: int
        """

        self._vm_mail_box_type_id = vm_mail_box_type_id

    @property
    def vm_check_out_option_enum(self):
        """Gets the vm_check_out_option_enum of this CategoryItem.  # noqa: E501

        VM Check Out Option  # noqa: E501

        :return: The vm_check_out_option_enum of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._vm_check_out_option_enum

    @vm_check_out_option_enum.setter
    def vm_check_out_option_enum(self, vm_check_out_option_enum):
        """Sets the vm_check_out_option_enum of this CategoryItem.

        VM Check Out Option  # noqa: E501

        :param vm_check_out_option_enum: The vm_check_out_option_enum of this CategoryItem.  # noqa: E501
        :type: str
        """

        self._vm_check_out_option_enum = vm_check_out_option_enum

    @property
    def vm_check_out_remove_message_enum(self):
        """Gets the vm_check_out_remove_message_enum of this CategoryItem.  # noqa: E501

        VM Check Out Remove Message  # noqa: E501

        :return: The vm_check_out_remove_message_enum of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._vm_check_out_remove_message_enum

    @vm_check_out_remove_message_enum.setter
    def vm_check_out_remove_message_enum(self, vm_check_out_remove_message_enum):
        """Sets the vm_check_out_remove_message_enum of this CategoryItem.

        VM Check Out Remove Message  # noqa: E501

        :param vm_check_out_remove_message_enum: The vm_check_out_remove_message_enum of this CategoryItem.  # noqa: E501
        :type: str
        """

        self._vm_check_out_remove_message_enum = vm_check_out_remove_message_enum

    @property
    def category_colour(self):
        """Gets the category_colour of this CategoryItem.  # noqa: E501

        Category Color  # noqa: E501

        :return: The category_colour of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._category_colour

    @category_colour.setter
    def category_colour(self, category_colour):
        """Sets the category_colour of this CategoryItem.

        Category Color  # noqa: E501

        :param category_colour: The category_colour of this CategoryItem.  # noqa: E501
        :type: str
        """
        if category_colour is not None and len(category_colour) > 20:
            raise ValueError("Invalid value for `category_colour`, length must be less than or equal to `20`")  # noqa: E501

        self._category_colour = category_colour

    @property
    def security_user_id(self):
        """Gets the security_user_id of this CategoryItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this CategoryItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this CategoryItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this CategoryItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this CategoryItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this CategoryItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this CategoryItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this CategoryItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def timestamp(self):
        """Gets the timestamp of this CategoryItem.  # noqa: E501

        Timestamp  # noqa: E501

        :return: The timestamp of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CategoryItem.

        Timestamp  # noqa: E501

        :param timestamp: The timestamp of this CategoryItem.  # noqa: E501
        :type: str
        """
        if timestamp is not None and len(timestamp) > 8:
            raise ValueError("Invalid value for `timestamp`, length must be less than or equal to `8`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def date_modified(self):
        """Gets the date_modified of this CategoryItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this CategoryItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this CategoryItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this CategoryItem.  # noqa: E501
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
        if not isinstance(other, CategoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other