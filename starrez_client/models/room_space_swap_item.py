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


class RoomSpaceSwapItem(object):
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
        'room_space_swap_id': 'int',
        'initiated_by_booking_id': 'int',
        'offered_booking_id': 'int',
        'requested_booking_id': 'int',
        'room_space_swap_status_enum': 'str',
        'accepted_date': 'str',
        'confirmed_date': 'str',
        'web_comments': 'str',
        'interim': 'bool',
        'security_user_id': 'int',
        'created_by_security_user_id': 'int',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'room_space_swap_id': 'RoomSpaceSwapID',
        'initiated_by_booking_id': 'InitiatedBy_BookingID',
        'offered_booking_id': 'Offered_BookingID',
        'requested_booking_id': 'Requested_BookingID',
        'room_space_swap_status_enum': 'RoomSpaceSwapStatusEnum',
        'accepted_date': 'AcceptedDate',
        'confirmed_date': 'ConfirmedDate',
        'web_comments': 'WebComments',
        'interim': 'Interim',
        'security_user_id': 'SecurityUserID',
        'created_by_security_user_id': 'CreatedBy_SecurityUserID',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, room_space_swap_id=None, initiated_by_booking_id=None, offered_booking_id=None, requested_booking_id=None, room_space_swap_status_enum=None, accepted_date=None, confirmed_date=None, web_comments=None, interim=None, security_user_id=None, created_by_security_user_id=None, date_created=None, date_modified=None):  # noqa: E501
        """RoomSpaceSwapItem - a model defined in Swagger"""  # noqa: E501

        self._room_space_swap_id = None
        self._initiated_by_booking_id = None
        self._offered_booking_id = None
        self._requested_booking_id = None
        self._room_space_swap_status_enum = None
        self._accepted_date = None
        self._confirmed_date = None
        self._web_comments = None
        self._interim = None
        self._security_user_id = None
        self._created_by_security_user_id = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if room_space_swap_id is not None:
            self.room_space_swap_id = room_space_swap_id
        if initiated_by_booking_id is not None:
            self.initiated_by_booking_id = initiated_by_booking_id
        if offered_booking_id is not None:
            self.offered_booking_id = offered_booking_id
        if requested_booking_id is not None:
            self.requested_booking_id = requested_booking_id
        if room_space_swap_status_enum is not None:
            self.room_space_swap_status_enum = room_space_swap_status_enum
        if accepted_date is not None:
            self.accepted_date = accepted_date
        if confirmed_date is not None:
            self.confirmed_date = confirmed_date
        if web_comments is not None:
            self.web_comments = web_comments
        if interim is not None:
            self.interim = interim
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if created_by_security_user_id is not None:
            self.created_by_security_user_id = created_by_security_user_id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def room_space_swap_id(self):
        """Gets the room_space_swap_id of this RoomSpaceSwapItem.  # noqa: E501

        Room Space Swap  # noqa: E501

        :return: The room_space_swap_id of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: int
        """
        return self._room_space_swap_id

    @room_space_swap_id.setter
    def room_space_swap_id(self, room_space_swap_id):
        """Sets the room_space_swap_id of this RoomSpaceSwapItem.

        Room Space Swap  # noqa: E501

        :param room_space_swap_id: The room_space_swap_id of this RoomSpaceSwapItem.  # noqa: E501
        :type: int
        """

        self._room_space_swap_id = room_space_swap_id

    @property
    def initiated_by_booking_id(self):
        """Gets the initiated_by_booking_id of this RoomSpaceSwapItem.  # noqa: E501

        Initiated By Booking  # noqa: E501

        :return: The initiated_by_booking_id of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: int
        """
        return self._initiated_by_booking_id

    @initiated_by_booking_id.setter
    def initiated_by_booking_id(self, initiated_by_booking_id):
        """Sets the initiated_by_booking_id of this RoomSpaceSwapItem.

        Initiated By Booking  # noqa: E501

        :param initiated_by_booking_id: The initiated_by_booking_id of this RoomSpaceSwapItem.  # noqa: E501
        :type: int
        """

        self._initiated_by_booking_id = initiated_by_booking_id

    @property
    def offered_booking_id(self):
        """Gets the offered_booking_id of this RoomSpaceSwapItem.  # noqa: E501

        Offered Booking  # noqa: E501

        :return: The offered_booking_id of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: int
        """
        return self._offered_booking_id

    @offered_booking_id.setter
    def offered_booking_id(self, offered_booking_id):
        """Sets the offered_booking_id of this RoomSpaceSwapItem.

        Offered Booking  # noqa: E501

        :param offered_booking_id: The offered_booking_id of this RoomSpaceSwapItem.  # noqa: E501
        :type: int
        """

        self._offered_booking_id = offered_booking_id

    @property
    def requested_booking_id(self):
        """Gets the requested_booking_id of this RoomSpaceSwapItem.  # noqa: E501

        Requested Booking  # noqa: E501

        :return: The requested_booking_id of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: int
        """
        return self._requested_booking_id

    @requested_booking_id.setter
    def requested_booking_id(self, requested_booking_id):
        """Sets the requested_booking_id of this RoomSpaceSwapItem.

        Requested Booking  # noqa: E501

        :param requested_booking_id: The requested_booking_id of this RoomSpaceSwapItem.  # noqa: E501
        :type: int
        """

        self._requested_booking_id = requested_booking_id

    @property
    def room_space_swap_status_enum(self):
        """Gets the room_space_swap_status_enum of this RoomSpaceSwapItem.  # noqa: E501

        Room Space Swap Status  # noqa: E501

        :return: The room_space_swap_status_enum of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: str
        """
        return self._room_space_swap_status_enum

    @room_space_swap_status_enum.setter
    def room_space_swap_status_enum(self, room_space_swap_status_enum):
        """Sets the room_space_swap_status_enum of this RoomSpaceSwapItem.

        Room Space Swap Status  # noqa: E501

        :param room_space_swap_status_enum: The room_space_swap_status_enum of this RoomSpaceSwapItem.  # noqa: E501
        :type: str
        """

        self._room_space_swap_status_enum = room_space_swap_status_enum

    @property
    def accepted_date(self):
        """Gets the accepted_date of this RoomSpaceSwapItem.  # noqa: E501

        Accepted Date  # noqa: E501

        :return: The accepted_date of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: str
        """
        return self._accepted_date

    @accepted_date.setter
    def accepted_date(self, accepted_date):
        """Sets the accepted_date of this RoomSpaceSwapItem.

        Accepted Date  # noqa: E501

        :param accepted_date: The accepted_date of this RoomSpaceSwapItem.  # noqa: E501
        :type: str
        """

        self._accepted_date = accepted_date

    @property
    def confirmed_date(self):
        """Gets the confirmed_date of this RoomSpaceSwapItem.  # noqa: E501

        Confirmed Date  # noqa: E501

        :return: The confirmed_date of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: str
        """
        return self._confirmed_date

    @confirmed_date.setter
    def confirmed_date(self, confirmed_date):
        """Sets the confirmed_date of this RoomSpaceSwapItem.

        Confirmed Date  # noqa: E501

        :param confirmed_date: The confirmed_date of this RoomSpaceSwapItem.  # noqa: E501
        :type: str
        """

        self._confirmed_date = confirmed_date

    @property
    def web_comments(self):
        """Gets the web_comments of this RoomSpaceSwapItem.  # noqa: E501

        Web Comments  # noqa: E501

        :return: The web_comments of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: str
        """
        return self._web_comments

    @web_comments.setter
    def web_comments(self, web_comments):
        """Sets the web_comments of this RoomSpaceSwapItem.

        Web Comments  # noqa: E501

        :param web_comments: The web_comments of this RoomSpaceSwapItem.  # noqa: E501
        :type: str
        """
        if web_comments is not None and len(web_comments) > 4000:
            raise ValueError("Invalid value for `web_comments`, length must be less than or equal to `4000`")  # noqa: E501

        self._web_comments = web_comments

    @property
    def interim(self):
        """Gets the interim of this RoomSpaceSwapItem.  # noqa: E501

        Interim  # noqa: E501

        :return: The interim of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: bool
        """
        return self._interim

    @interim.setter
    def interim(self, interim):
        """Sets the interim of this RoomSpaceSwapItem.

        Interim  # noqa: E501

        :param interim: The interim of this RoomSpaceSwapItem.  # noqa: E501
        :type: bool
        """

        self._interim = interim

    @property
    def security_user_id(self):
        """Gets the security_user_id of this RoomSpaceSwapItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this RoomSpaceSwapItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this RoomSpaceSwapItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def created_by_security_user_id(self):
        """Gets the created_by_security_user_id of this RoomSpaceSwapItem.  # noqa: E501

        Created By Security User  # noqa: E501

        :return: The created_by_security_user_id of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: int
        """
        return self._created_by_security_user_id

    @created_by_security_user_id.setter
    def created_by_security_user_id(self, created_by_security_user_id):
        """Sets the created_by_security_user_id of this RoomSpaceSwapItem.

        Created By Security User  # noqa: E501

        :param created_by_security_user_id: The created_by_security_user_id of this RoomSpaceSwapItem.  # noqa: E501
        :type: int
        """

        self._created_by_security_user_id = created_by_security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this RoomSpaceSwapItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this RoomSpaceSwapItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this RoomSpaceSwapItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this RoomSpaceSwapItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RoomSpaceSwapItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RoomSpaceSwapItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RoomSpaceSwapItem.  # noqa: E501
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
        if not isinstance(other, RoomSpaceSwapItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
