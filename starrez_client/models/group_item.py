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


class GroupItem(object):
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
        'group_id': 'int',
        'category_id': 'int',
        'event_id': 'int',
        'group_status_enum': 'str',
        'description': 'str',
        'term_session_id': 'int',
        'check_in_date': 'date',
        'check_out_date': 'date',
        'gender_enum': 'str',
        'contact_id': 'int',
        'booking_type_id': 'int',
        'room_rate_id': 'int',
        'housekeeping_id': 'int',
        'group_registration': 'bool',
        'leader_entry_id': 'int',
        'resv_charge_to_entry': 'bool',
        'resv_charge_to_entry_extra_days': 'bool',
        'meal_charge_to_entry': 'bool',
        'resv_charge_to_entry_extra_days_room_rate_id': 'int',
        'comments': 'str',
        'security_user_id': 'int',
        'created_by_security_user_id': 'int',
        'date_created': 'datetime',
        'timestamp': 'str',
        'active_date_start': 'str',
        'active_date_end': 'str',
        'advance_booking_days': 'int',
        'min_booking_nights': 'int',
        'max_booking_nights': 'int',
        'group_code': 'str',
        'keep_entire_range_blocked': 'bool',
        'date_modified': 'str'
    }

    attribute_map = {
        'group_id': 'GroupID',
        'category_id': 'CategoryID',
        'event_id': 'EventID',
        'group_status_enum': 'GroupStatusEnum',
        'description': 'Description',
        'term_session_id': 'TermSessionID',
        'check_in_date': 'CheckInDate',
        'check_out_date': 'CheckOutDate',
        'gender_enum': 'GenderEnum',
        'contact_id': 'ContactID',
        'booking_type_id': 'BookingTypeID',
        'room_rate_id': 'RoomRateID',
        'housekeeping_id': 'HousekeepingID',
        'group_registration': 'GroupRegistration',
        'leader_entry_id': 'Leader_EntryID',
        'resv_charge_to_entry': 'ResvChargeToEntry',
        'resv_charge_to_entry_extra_days': 'ResvChargeToEntryExtraDays',
        'meal_charge_to_entry': 'MealChargeToEntry',
        'resv_charge_to_entry_extra_days_room_rate_id': 'ResvChargeToEntryExtraDays_RoomRateID',
        'comments': 'Comments',
        'security_user_id': 'SecurityUserID',
        'created_by_security_user_id': 'CreatedBy_SecurityUserID',
        'date_created': 'DateCreated',
        'timestamp': 'timestamp',
        'active_date_start': 'ActiveDateStart',
        'active_date_end': 'ActiveDateEnd',
        'advance_booking_days': 'AdvanceBookingDays',
        'min_booking_nights': 'MinBookingNights',
        'max_booking_nights': 'MaxBookingNights',
        'group_code': 'GroupCode',
        'keep_entire_range_blocked': 'KeepEntireRangeBlocked',
        'date_modified': 'DateModified'
    }

    def __init__(self, group_id=None, category_id=None, event_id=None, group_status_enum=None, description=None, term_session_id=None, check_in_date=None, check_out_date=None, gender_enum=None, contact_id=None, booking_type_id=None, room_rate_id=None, housekeeping_id=None, group_registration=None, leader_entry_id=None, resv_charge_to_entry=None, resv_charge_to_entry_extra_days=None, meal_charge_to_entry=None, resv_charge_to_entry_extra_days_room_rate_id=None, comments=None, security_user_id=None, created_by_security_user_id=None, date_created=None, timestamp=None, active_date_start=None, active_date_end=None, advance_booking_days=None, min_booking_nights=None, max_booking_nights=None, group_code=None, keep_entire_range_blocked=None, date_modified=None):  # noqa: E501
        """GroupItem - a model defined in Swagger"""  # noqa: E501

        self._group_id = None
        self._category_id = None
        self._event_id = None
        self._group_status_enum = None
        self._description = None
        self._term_session_id = None
        self._check_in_date = None
        self._check_out_date = None
        self._gender_enum = None
        self._contact_id = None
        self._booking_type_id = None
        self._room_rate_id = None
        self._housekeeping_id = None
        self._group_registration = None
        self._leader_entry_id = None
        self._resv_charge_to_entry = None
        self._resv_charge_to_entry_extra_days = None
        self._meal_charge_to_entry = None
        self._resv_charge_to_entry_extra_days_room_rate_id = None
        self._comments = None
        self._security_user_id = None
        self._created_by_security_user_id = None
        self._date_created = None
        self._timestamp = None
        self._active_date_start = None
        self._active_date_end = None
        self._advance_booking_days = None
        self._min_booking_nights = None
        self._max_booking_nights = None
        self._group_code = None
        self._keep_entire_range_blocked = None
        self._date_modified = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if category_id is not None:
            self.category_id = category_id
        if event_id is not None:
            self.event_id = event_id
        if group_status_enum is not None:
            self.group_status_enum = group_status_enum
        if description is not None:
            self.description = description
        if term_session_id is not None:
            self.term_session_id = term_session_id
        if check_in_date is not None:
            self.check_in_date = check_in_date
        if check_out_date is not None:
            self.check_out_date = check_out_date
        if gender_enum is not None:
            self.gender_enum = gender_enum
        if contact_id is not None:
            self.contact_id = contact_id
        if booking_type_id is not None:
            self.booking_type_id = booking_type_id
        if room_rate_id is not None:
            self.room_rate_id = room_rate_id
        if housekeeping_id is not None:
            self.housekeeping_id = housekeeping_id
        if group_registration is not None:
            self.group_registration = group_registration
        if leader_entry_id is not None:
            self.leader_entry_id = leader_entry_id
        if resv_charge_to_entry is not None:
            self.resv_charge_to_entry = resv_charge_to_entry
        if resv_charge_to_entry_extra_days is not None:
            self.resv_charge_to_entry_extra_days = resv_charge_to_entry_extra_days
        if meal_charge_to_entry is not None:
            self.meal_charge_to_entry = meal_charge_to_entry
        if resv_charge_to_entry_extra_days_room_rate_id is not None:
            self.resv_charge_to_entry_extra_days_room_rate_id = resv_charge_to_entry_extra_days_room_rate_id
        if comments is not None:
            self.comments = comments
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if created_by_security_user_id is not None:
            self.created_by_security_user_id = created_by_security_user_id
        if date_created is not None:
            self.date_created = date_created
        if timestamp is not None:
            self.timestamp = timestamp
        if active_date_start is not None:
            self.active_date_start = active_date_start
        if active_date_end is not None:
            self.active_date_end = active_date_end
        if advance_booking_days is not None:
            self.advance_booking_days = advance_booking_days
        if min_booking_nights is not None:
            self.min_booking_nights = min_booking_nights
        if max_booking_nights is not None:
            self.max_booking_nights = max_booking_nights
        if group_code is not None:
            self.group_code = group_code
        if keep_entire_range_blocked is not None:
            self.keep_entire_range_blocked = keep_entire_range_blocked
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def group_id(self):
        """Gets the group_id of this GroupItem.  # noqa: E501

        Group  # noqa: E501

        :return: The group_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupItem.

        Group  # noqa: E501

        :param group_id: The group_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def category_id(self):
        """Gets the category_id of this GroupItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this GroupItem.

        Category  # noqa: E501

        :param category_id: The category_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def event_id(self):
        """Gets the event_id of this GroupItem.  # noqa: E501

        Event  # noqa: E501

        :return: The event_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this GroupItem.

        Event  # noqa: E501

        :param event_id: The event_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._event_id = event_id

    @property
    def group_status_enum(self):
        """Gets the group_status_enum of this GroupItem.  # noqa: E501

        Group Status  # noqa: E501

        :return: The group_status_enum of this GroupItem.  # noqa: E501
        :rtype: str
        """
        return self._group_status_enum

    @group_status_enum.setter
    def group_status_enum(self, group_status_enum):
        """Sets the group_status_enum of this GroupItem.

        Group Status  # noqa: E501

        :param group_status_enum: The group_status_enum of this GroupItem.  # noqa: E501
        :type: str
        """

        self._group_status_enum = group_status_enum

    @property
    def description(self):
        """Gets the description of this GroupItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this GroupItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupItem.

        Description  # noqa: E501

        :param description: The description of this GroupItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def term_session_id(self):
        """Gets the term_session_id of this GroupItem.  # noqa: E501

        Term Session  # noqa: E501

        :return: The term_session_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._term_session_id

    @term_session_id.setter
    def term_session_id(self, term_session_id):
        """Sets the term_session_id of this GroupItem.

        Term Session  # noqa: E501

        :param term_session_id: The term_session_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._term_session_id = term_session_id

    @property
    def check_in_date(self):
        """Gets the check_in_date of this GroupItem.  # noqa: E501

        Check In Date  # noqa: E501

        :return: The check_in_date of this GroupItem.  # noqa: E501
        :rtype: date
        """
        return self._check_in_date

    @check_in_date.setter
    def check_in_date(self, check_in_date):
        """Sets the check_in_date of this GroupItem.

        Check In Date  # noqa: E501

        :param check_in_date: The check_in_date of this GroupItem.  # noqa: E501
        :type: date
        """

        self._check_in_date = check_in_date

    @property
    def check_out_date(self):
        """Gets the check_out_date of this GroupItem.  # noqa: E501

        Check Out Date  # noqa: E501

        :return: The check_out_date of this GroupItem.  # noqa: E501
        :rtype: date
        """
        return self._check_out_date

    @check_out_date.setter
    def check_out_date(self, check_out_date):
        """Sets the check_out_date of this GroupItem.

        Check Out Date  # noqa: E501

        :param check_out_date: The check_out_date of this GroupItem.  # noqa: E501
        :type: date
        """

        self._check_out_date = check_out_date

    @property
    def gender_enum(self):
        """Gets the gender_enum of this GroupItem.  # noqa: E501

        Gender  # noqa: E501

        :return: The gender_enum of this GroupItem.  # noqa: E501
        :rtype: str
        """
        return self._gender_enum

    @gender_enum.setter
    def gender_enum(self, gender_enum):
        """Sets the gender_enum of this GroupItem.

        Gender  # noqa: E501

        :param gender_enum: The gender_enum of this GroupItem.  # noqa: E501
        :type: str
        """

        self._gender_enum = gender_enum

    @property
    def contact_id(self):
        """Gets the contact_id of this GroupItem.  # noqa: E501

        Contact  # noqa: E501

        :return: The contact_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this GroupItem.

        Contact  # noqa: E501

        :param contact_id: The contact_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._contact_id = contact_id

    @property
    def booking_type_id(self):
        """Gets the booking_type_id of this GroupItem.  # noqa: E501

        Booking Type  # noqa: E501

        :return: The booking_type_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._booking_type_id

    @booking_type_id.setter
    def booking_type_id(self, booking_type_id):
        """Sets the booking_type_id of this GroupItem.

        Booking Type  # noqa: E501

        :param booking_type_id: The booking_type_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._booking_type_id = booking_type_id

    @property
    def room_rate_id(self):
        """Gets the room_rate_id of this GroupItem.  # noqa: E501

        Room Rate  # noqa: E501

        :return: The room_rate_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._room_rate_id

    @room_rate_id.setter
    def room_rate_id(self, room_rate_id):
        """Sets the room_rate_id of this GroupItem.

        Room Rate  # noqa: E501

        :param room_rate_id: The room_rate_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._room_rate_id = room_rate_id

    @property
    def housekeeping_id(self):
        """Gets the housekeeping_id of this GroupItem.  # noqa: E501

        Housekeeping  # noqa: E501

        :return: The housekeeping_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._housekeeping_id

    @housekeeping_id.setter
    def housekeeping_id(self, housekeeping_id):
        """Sets the housekeeping_id of this GroupItem.

        Housekeeping  # noqa: E501

        :param housekeeping_id: The housekeeping_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._housekeeping_id = housekeeping_id

    @property
    def group_registration(self):
        """Gets the group_registration of this GroupItem.  # noqa: E501

        Group Registration  # noqa: E501

        :return: The group_registration of this GroupItem.  # noqa: E501
        :rtype: bool
        """
        return self._group_registration

    @group_registration.setter
    def group_registration(self, group_registration):
        """Sets the group_registration of this GroupItem.

        Group Registration  # noqa: E501

        :param group_registration: The group_registration of this GroupItem.  # noqa: E501
        :type: bool
        """

        self._group_registration = group_registration

    @property
    def leader_entry_id(self):
        """Gets the leader_entry_id of this GroupItem.  # noqa: E501

        Leader Entry  # noqa: E501

        :return: The leader_entry_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._leader_entry_id

    @leader_entry_id.setter
    def leader_entry_id(self, leader_entry_id):
        """Sets the leader_entry_id of this GroupItem.

        Leader Entry  # noqa: E501

        :param leader_entry_id: The leader_entry_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._leader_entry_id = leader_entry_id

    @property
    def resv_charge_to_entry(self):
        """Gets the resv_charge_to_entry of this GroupItem.  # noqa: E501

        Resv Charge To Entry  # noqa: E501

        :return: The resv_charge_to_entry of this GroupItem.  # noqa: E501
        :rtype: bool
        """
        return self._resv_charge_to_entry

    @resv_charge_to_entry.setter
    def resv_charge_to_entry(self, resv_charge_to_entry):
        """Sets the resv_charge_to_entry of this GroupItem.

        Resv Charge To Entry  # noqa: E501

        :param resv_charge_to_entry: The resv_charge_to_entry of this GroupItem.  # noqa: E501
        :type: bool
        """

        self._resv_charge_to_entry = resv_charge_to_entry

    @property
    def resv_charge_to_entry_extra_days(self):
        """Gets the resv_charge_to_entry_extra_days of this GroupItem.  # noqa: E501

        Resv Charge To Entry Extra Days  # noqa: E501

        :return: The resv_charge_to_entry_extra_days of this GroupItem.  # noqa: E501
        :rtype: bool
        """
        return self._resv_charge_to_entry_extra_days

    @resv_charge_to_entry_extra_days.setter
    def resv_charge_to_entry_extra_days(self, resv_charge_to_entry_extra_days):
        """Sets the resv_charge_to_entry_extra_days of this GroupItem.

        Resv Charge To Entry Extra Days  # noqa: E501

        :param resv_charge_to_entry_extra_days: The resv_charge_to_entry_extra_days of this GroupItem.  # noqa: E501
        :type: bool
        """

        self._resv_charge_to_entry_extra_days = resv_charge_to_entry_extra_days

    @property
    def meal_charge_to_entry(self):
        """Gets the meal_charge_to_entry of this GroupItem.  # noqa: E501

        Meal Charge To Entry  # noqa: E501

        :return: The meal_charge_to_entry of this GroupItem.  # noqa: E501
        :rtype: bool
        """
        return self._meal_charge_to_entry

    @meal_charge_to_entry.setter
    def meal_charge_to_entry(self, meal_charge_to_entry):
        """Sets the meal_charge_to_entry of this GroupItem.

        Meal Charge To Entry  # noqa: E501

        :param meal_charge_to_entry: The meal_charge_to_entry of this GroupItem.  # noqa: E501
        :type: bool
        """

        self._meal_charge_to_entry = meal_charge_to_entry

    @property
    def resv_charge_to_entry_extra_days_room_rate_id(self):
        """Gets the resv_charge_to_entry_extra_days_room_rate_id of this GroupItem.  # noqa: E501

        Resv Charge To Entry Extra Days Room Rate  # noqa: E501

        :return: The resv_charge_to_entry_extra_days_room_rate_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._resv_charge_to_entry_extra_days_room_rate_id

    @resv_charge_to_entry_extra_days_room_rate_id.setter
    def resv_charge_to_entry_extra_days_room_rate_id(self, resv_charge_to_entry_extra_days_room_rate_id):
        """Sets the resv_charge_to_entry_extra_days_room_rate_id of this GroupItem.

        Resv Charge To Entry Extra Days Room Rate  # noqa: E501

        :param resv_charge_to_entry_extra_days_room_rate_id: The resv_charge_to_entry_extra_days_room_rate_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._resv_charge_to_entry_extra_days_room_rate_id = resv_charge_to_entry_extra_days_room_rate_id

    @property
    def comments(self):
        """Gets the comments of this GroupItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this GroupItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this GroupItem.

        Comments  # noqa: E501

        :param comments: The comments of this GroupItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 1000:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `1000`")  # noqa: E501

        self._comments = comments

    @property
    def security_user_id(self):
        """Gets the security_user_id of this GroupItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this GroupItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def created_by_security_user_id(self):
        """Gets the created_by_security_user_id of this GroupItem.  # noqa: E501

        Created By Security User  # noqa: E501

        :return: The created_by_security_user_id of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._created_by_security_user_id

    @created_by_security_user_id.setter
    def created_by_security_user_id(self, created_by_security_user_id):
        """Sets the created_by_security_user_id of this GroupItem.

        Created By Security User  # noqa: E501

        :param created_by_security_user_id: The created_by_security_user_id of this GroupItem.  # noqa: E501
        :type: int
        """

        self._created_by_security_user_id = created_by_security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this GroupItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this GroupItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this GroupItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this GroupItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def timestamp(self):
        """Gets the timestamp of this GroupItem.  # noqa: E501

        Timestamp  # noqa: E501

        :return: The timestamp of this GroupItem.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this GroupItem.

        Timestamp  # noqa: E501

        :param timestamp: The timestamp of this GroupItem.  # noqa: E501
        :type: str
        """
        if timestamp is not None and len(timestamp) > 8:
            raise ValueError("Invalid value for `timestamp`, length must be less than or equal to `8`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def active_date_start(self):
        """Gets the active_date_start of this GroupItem.  # noqa: E501

        Active Date Start  # noqa: E501

        :return: The active_date_start of this GroupItem.  # noqa: E501
        :rtype: str
        """
        return self._active_date_start

    @active_date_start.setter
    def active_date_start(self, active_date_start):
        """Sets the active_date_start of this GroupItem.

        Active Date Start  # noqa: E501

        :param active_date_start: The active_date_start of this GroupItem.  # noqa: E501
        :type: str
        """

        self._active_date_start = active_date_start

    @property
    def active_date_end(self):
        """Gets the active_date_end of this GroupItem.  # noqa: E501

        Active Date End  # noqa: E501

        :return: The active_date_end of this GroupItem.  # noqa: E501
        :rtype: str
        """
        return self._active_date_end

    @active_date_end.setter
    def active_date_end(self, active_date_end):
        """Sets the active_date_end of this GroupItem.

        Active Date End  # noqa: E501

        :param active_date_end: The active_date_end of this GroupItem.  # noqa: E501
        :type: str
        """

        self._active_date_end = active_date_end

    @property
    def advance_booking_days(self):
        """Gets the advance_booking_days of this GroupItem.  # noqa: E501

        Advance Booking Days  # noqa: E501

        :return: The advance_booking_days of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._advance_booking_days

    @advance_booking_days.setter
    def advance_booking_days(self, advance_booking_days):
        """Sets the advance_booking_days of this GroupItem.

        Advance Booking Days  # noqa: E501

        :param advance_booking_days: The advance_booking_days of this GroupItem.  # noqa: E501
        :type: int
        """

        self._advance_booking_days = advance_booking_days

    @property
    def min_booking_nights(self):
        """Gets the min_booking_nights of this GroupItem.  # noqa: E501

        Min Booking Nights  # noqa: E501

        :return: The min_booking_nights of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._min_booking_nights

    @min_booking_nights.setter
    def min_booking_nights(self, min_booking_nights):
        """Sets the min_booking_nights of this GroupItem.

        Min Booking Nights  # noqa: E501

        :param min_booking_nights: The min_booking_nights of this GroupItem.  # noqa: E501
        :type: int
        """

        self._min_booking_nights = min_booking_nights

    @property
    def max_booking_nights(self):
        """Gets the max_booking_nights of this GroupItem.  # noqa: E501

        Max Booking Nights  # noqa: E501

        :return: The max_booking_nights of this GroupItem.  # noqa: E501
        :rtype: int
        """
        return self._max_booking_nights

    @max_booking_nights.setter
    def max_booking_nights(self, max_booking_nights):
        """Sets the max_booking_nights of this GroupItem.

        Max Booking Nights  # noqa: E501

        :param max_booking_nights: The max_booking_nights of this GroupItem.  # noqa: E501
        :type: int
        """

        self._max_booking_nights = max_booking_nights

    @property
    def group_code(self):
        """Gets the group_code of this GroupItem.  # noqa: E501

        Group Code  # noqa: E501

        :return: The group_code of this GroupItem.  # noqa: E501
        :rtype: str
        """
        return self._group_code

    @group_code.setter
    def group_code(self, group_code):
        """Sets the group_code of this GroupItem.

        Group Code  # noqa: E501

        :param group_code: The group_code of this GroupItem.  # noqa: E501
        :type: str
        """
        if group_code is not None and len(group_code) > 50:
            raise ValueError("Invalid value for `group_code`, length must be less than or equal to `50`")  # noqa: E501

        self._group_code = group_code

    @property
    def keep_entire_range_blocked(self):
        """Gets the keep_entire_range_blocked of this GroupItem.  # noqa: E501

        Keep Entire Range Blocked  # noqa: E501

        :return: The keep_entire_range_blocked of this GroupItem.  # noqa: E501
        :rtype: bool
        """
        return self._keep_entire_range_blocked

    @keep_entire_range_blocked.setter
    def keep_entire_range_blocked(self, keep_entire_range_blocked):
        """Sets the keep_entire_range_blocked of this GroupItem.

        Keep Entire Range Blocked  # noqa: E501

        :param keep_entire_range_blocked: The keep_entire_range_blocked of this GroupItem.  # noqa: E501
        :type: bool
        """

        self._keep_entire_range_blocked = keep_entire_range_blocked

    @property
    def date_modified(self):
        """Gets the date_modified of this GroupItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this GroupItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this GroupItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this GroupItem.  # noqa: E501
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
        if not isinstance(other, GroupItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
