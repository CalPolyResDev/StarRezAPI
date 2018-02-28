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


class BookingTagItem(object):
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
        'booking_tag_id': 'int',
        'booking_id': 'int',
        'tag_type': 'str',
        'tag': 'str',
        'date_created': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'booking_tag_id': 'BookingTagID',
        'booking_id': 'BookingID',
        'tag_type': 'TagType',
        'tag': 'Tag',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, booking_tag_id=None, booking_id=None, tag_type=None, tag=None, date_created=None, date_modified=None):  # noqa: E501
        """BookingTagItem - a model defined in Swagger"""  # noqa: E501

        self._booking_tag_id = None
        self._booking_id = None
        self._tag_type = None
        self._tag = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if booking_tag_id is not None:
            self.booking_tag_id = booking_tag_id
        if booking_id is not None:
            self.booking_id = booking_id
        if tag_type is not None:
            self.tag_type = tag_type
        if tag is not None:
            self.tag = tag
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def booking_tag_id(self):
        """Gets the booking_tag_id of this BookingTagItem.  # noqa: E501

        Booking Tag  # noqa: E501

        :return: The booking_tag_id of this BookingTagItem.  # noqa: E501
        :rtype: int
        """
        return self._booking_tag_id

    @booking_tag_id.setter
    def booking_tag_id(self, booking_tag_id):
        """Sets the booking_tag_id of this BookingTagItem.

        Booking Tag  # noqa: E501

        :param booking_tag_id: The booking_tag_id of this BookingTagItem.  # noqa: E501
        :type: int
        """

        self._booking_tag_id = booking_tag_id

    @property
    def booking_id(self):
        """Gets the booking_id of this BookingTagItem.  # noqa: E501

        Booking  # noqa: E501

        :return: The booking_id of this BookingTagItem.  # noqa: E501
        :rtype: int
        """
        return self._booking_id

    @booking_id.setter
    def booking_id(self, booking_id):
        """Sets the booking_id of this BookingTagItem.

        Booking  # noqa: E501

        :param booking_id: The booking_id of this BookingTagItem.  # noqa: E501
        :type: int
        """

        self._booking_id = booking_id

    @property
    def tag_type(self):
        """Gets the tag_type of this BookingTagItem.  # noqa: E501

        Tag Type  # noqa: E501

        :return: The tag_type of this BookingTagItem.  # noqa: E501
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """Sets the tag_type of this BookingTagItem.

        Tag Type  # noqa: E501

        :param tag_type: The tag_type of this BookingTagItem.  # noqa: E501
        :type: str
        """
        if tag_type is not None and len(tag_type) > 20:
            raise ValueError("Invalid value for `tag_type`, length must be less than or equal to `20`")  # noqa: E501

        self._tag_type = tag_type

    @property
    def tag(self):
        """Gets the tag of this BookingTagItem.  # noqa: E501

        Tag  # noqa: E501

        :return: The tag of this BookingTagItem.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this BookingTagItem.

        Tag  # noqa: E501

        :param tag: The tag of this BookingTagItem.  # noqa: E501
        :type: str
        """
        if tag is not None and len(tag) > 10:
            raise ValueError("Invalid value for `tag`, length must be less than or equal to `10`")  # noqa: E501

        self._tag = tag

    @property
    def date_created(self):
        """Gets the date_created of this BookingTagItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this BookingTagItem.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this BookingTagItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this BookingTagItem.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this BookingTagItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this BookingTagItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this BookingTagItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this BookingTagItem.  # noqa: E501
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
        if not isinstance(other, BookingTagItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
