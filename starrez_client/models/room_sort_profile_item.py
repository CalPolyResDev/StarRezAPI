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


class RoomSortProfileItem(object):
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
        'room_sort_profile_id': 'int',
        'name': 'str',
        'term_id': 'int',
        'room_sort_profile_type_enum': 'str',
        'date_start': 'str',
        'date_end': 'str',
        'view_on_portal': 'bool',
        'security_user_id': 'int',
        'created_by_security_user_id': 'int',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'room_sort_profile_id': 'RoomSortProfileID',
        'name': 'Name',
        'term_id': 'TermID',
        'room_sort_profile_type_enum': 'RoomSortProfileTypeEnum',
        'date_start': 'DateStart',
        'date_end': 'DateEnd',
        'view_on_portal': 'ViewOnPortal',
        'security_user_id': 'SecurityUserID',
        'created_by_security_user_id': 'CreatedBy_SecurityUserID',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, room_sort_profile_id=None, name=None, term_id=None, room_sort_profile_type_enum=None, date_start=None, date_end=None, view_on_portal=None, security_user_id=None, created_by_security_user_id=None, date_created=None, date_modified=None):  # noqa: E501
        """RoomSortProfileItem - a model defined in Swagger"""  # noqa: E501

        self._room_sort_profile_id = None
        self._name = None
        self._term_id = None
        self._room_sort_profile_type_enum = None
        self._date_start = None
        self._date_end = None
        self._view_on_portal = None
        self._security_user_id = None
        self._created_by_security_user_id = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if room_sort_profile_id is not None:
            self.room_sort_profile_id = room_sort_profile_id
        if name is not None:
            self.name = name
        if term_id is not None:
            self.term_id = term_id
        if room_sort_profile_type_enum is not None:
            self.room_sort_profile_type_enum = room_sort_profile_type_enum
        if date_start is not None:
            self.date_start = date_start
        if date_end is not None:
            self.date_end = date_end
        if view_on_portal is not None:
            self.view_on_portal = view_on_portal
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if created_by_security_user_id is not None:
            self.created_by_security_user_id = created_by_security_user_id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def room_sort_profile_id(self):
        """Gets the room_sort_profile_id of this RoomSortProfileItem.  # noqa: E501

        Room Sort Profile  # noqa: E501

        :return: The room_sort_profile_id of this RoomSortProfileItem.  # noqa: E501
        :rtype: int
        """
        return self._room_sort_profile_id

    @room_sort_profile_id.setter
    def room_sort_profile_id(self, room_sort_profile_id):
        """Sets the room_sort_profile_id of this RoomSortProfileItem.

        Room Sort Profile  # noqa: E501

        :param room_sort_profile_id: The room_sort_profile_id of this RoomSortProfileItem.  # noqa: E501
        :type: int
        """

        self._room_sort_profile_id = room_sort_profile_id

    @property
    def name(self):
        """Gets the name of this RoomSortProfileItem.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this RoomSortProfileItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoomSortProfileItem.

        Name  # noqa: E501

        :param name: The name of this RoomSortProfileItem.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501

        self._name = name

    @property
    def term_id(self):
        """Gets the term_id of this RoomSortProfileItem.  # noqa: E501

        Term  # noqa: E501

        :return: The term_id of this RoomSortProfileItem.  # noqa: E501
        :rtype: int
        """
        return self._term_id

    @term_id.setter
    def term_id(self, term_id):
        """Sets the term_id of this RoomSortProfileItem.

        Term  # noqa: E501

        :param term_id: The term_id of this RoomSortProfileItem.  # noqa: E501
        :type: int
        """

        self._term_id = term_id

    @property
    def room_sort_profile_type_enum(self):
        """Gets the room_sort_profile_type_enum of this RoomSortProfileItem.  # noqa: E501

        Room Sort Profile Type  # noqa: E501

        :return: The room_sort_profile_type_enum of this RoomSortProfileItem.  # noqa: E501
        :rtype: str
        """
        return self._room_sort_profile_type_enum

    @room_sort_profile_type_enum.setter
    def room_sort_profile_type_enum(self, room_sort_profile_type_enum):
        """Sets the room_sort_profile_type_enum of this RoomSortProfileItem.

        Room Sort Profile Type  # noqa: E501

        :param room_sort_profile_type_enum: The room_sort_profile_type_enum of this RoomSortProfileItem.  # noqa: E501
        :type: str
        """

        self._room_sort_profile_type_enum = room_sort_profile_type_enum

    @property
    def date_start(self):
        """Gets the date_start of this RoomSortProfileItem.  # noqa: E501

        Date Start  # noqa: E501

        :return: The date_start of this RoomSortProfileItem.  # noqa: E501
        :rtype: str
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this RoomSortProfileItem.

        Date Start  # noqa: E501

        :param date_start: The date_start of this RoomSortProfileItem.  # noqa: E501
        :type: str
        """

        self._date_start = date_start

    @property
    def date_end(self):
        """Gets the date_end of this RoomSortProfileItem.  # noqa: E501

        Date End  # noqa: E501

        :return: The date_end of this RoomSortProfileItem.  # noqa: E501
        :rtype: str
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this RoomSortProfileItem.

        Date End  # noqa: E501

        :param date_end: The date_end of this RoomSortProfileItem.  # noqa: E501
        :type: str
        """

        self._date_end = date_end

    @property
    def view_on_portal(self):
        """Gets the view_on_portal of this RoomSortProfileItem.  # noqa: E501

        View On Portal  # noqa: E501

        :return: The view_on_portal of this RoomSortProfileItem.  # noqa: E501
        :rtype: bool
        """
        return self._view_on_portal

    @view_on_portal.setter
    def view_on_portal(self, view_on_portal):
        """Sets the view_on_portal of this RoomSortProfileItem.

        View On Portal  # noqa: E501

        :param view_on_portal: The view_on_portal of this RoomSortProfileItem.  # noqa: E501
        :type: bool
        """

        self._view_on_portal = view_on_portal

    @property
    def security_user_id(self):
        """Gets the security_user_id of this RoomSortProfileItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this RoomSortProfileItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this RoomSortProfileItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this RoomSortProfileItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def created_by_security_user_id(self):
        """Gets the created_by_security_user_id of this RoomSortProfileItem.  # noqa: E501

        Created By Security User  # noqa: E501

        :return: The created_by_security_user_id of this RoomSortProfileItem.  # noqa: E501
        :rtype: int
        """
        return self._created_by_security_user_id

    @created_by_security_user_id.setter
    def created_by_security_user_id(self, created_by_security_user_id):
        """Sets the created_by_security_user_id of this RoomSortProfileItem.

        Created By Security User  # noqa: E501

        :param created_by_security_user_id: The created_by_security_user_id of this RoomSortProfileItem.  # noqa: E501
        :type: int
        """

        self._created_by_security_user_id = created_by_security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this RoomSortProfileItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this RoomSortProfileItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this RoomSortProfileItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this RoomSortProfileItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this RoomSortProfileItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RoomSortProfileItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RoomSortProfileItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RoomSortProfileItem.  # noqa: E501
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
        if not isinstance(other, RoomSortProfileItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other