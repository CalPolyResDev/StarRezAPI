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


class BookingLinkedItem(object):
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
        'booking_linked_id': 'int',
        'booking_id': 'int',
        'linked_booking_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'booking_linked_id': 'BookingLinkedID',
        'booking_id': 'BookingID',
        'linked_booking_id': 'Linked_BookingID',
        'date_modified': 'DateModified'
    }

    def __init__(self, booking_linked_id=None, booking_id=None, linked_booking_id=None, date_modified=None):  # noqa: E501
        """BookingLinkedItem - a model defined in Swagger"""  # noqa: E501

        self._booking_linked_id = None
        self._booking_id = None
        self._linked_booking_id = None
        self._date_modified = None
        self.discriminator = None

        if booking_linked_id is not None:
            self.booking_linked_id = booking_linked_id
        if booking_id is not None:
            self.booking_id = booking_id
        if linked_booking_id is not None:
            self.linked_booking_id = linked_booking_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def booking_linked_id(self):
        """Gets the booking_linked_id of this BookingLinkedItem.  # noqa: E501

        Booking Linked  # noqa: E501

        :return: The booking_linked_id of this BookingLinkedItem.  # noqa: E501
        :rtype: int
        """
        return self._booking_linked_id

    @booking_linked_id.setter
    def booking_linked_id(self, booking_linked_id):
        """Sets the booking_linked_id of this BookingLinkedItem.

        Booking Linked  # noqa: E501

        :param booking_linked_id: The booking_linked_id of this BookingLinkedItem.  # noqa: E501
        :type: int
        """

        self._booking_linked_id = booking_linked_id

    @property
    def booking_id(self):
        """Gets the booking_id of this BookingLinkedItem.  # noqa: E501

        Booking  # noqa: E501

        :return: The booking_id of this BookingLinkedItem.  # noqa: E501
        :rtype: int
        """
        return self._booking_id

    @booking_id.setter
    def booking_id(self, booking_id):
        """Sets the booking_id of this BookingLinkedItem.

        Booking  # noqa: E501

        :param booking_id: The booking_id of this BookingLinkedItem.  # noqa: E501
        :type: int
        """

        self._booking_id = booking_id

    @property
    def linked_booking_id(self):
        """Gets the linked_booking_id of this BookingLinkedItem.  # noqa: E501

        Linked Booking  # noqa: E501

        :return: The linked_booking_id of this BookingLinkedItem.  # noqa: E501
        :rtype: int
        """
        return self._linked_booking_id

    @linked_booking_id.setter
    def linked_booking_id(self, linked_booking_id):
        """Sets the linked_booking_id of this BookingLinkedItem.

        Linked Booking  # noqa: E501

        :param linked_booking_id: The linked_booking_id of this BookingLinkedItem.  # noqa: E501
        :type: int
        """

        self._linked_booking_id = linked_booking_id

    @property
    def date_modified(self):
        """Gets the date_modified of this BookingLinkedItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this BookingLinkedItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this BookingLinkedItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this BookingLinkedItem.  # noqa: E501
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
        if not isinstance(other, BookingLinkedItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
