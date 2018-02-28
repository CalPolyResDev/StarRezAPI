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


class EntryScholarshipItem(object):
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
        'entry_scholarship_id': 'int',
        'entry_id': 'int',
        'scholarship_type': 'str',
        'scholarship_date_start': 'str',
        'scholarship_date_end': 'str',
        'scholarship_name': 'str',
        'description': 'str',
        'amount': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'entry_scholarship_id': 'EntryScholarshipID',
        'entry_id': 'EntryID',
        'scholarship_type': 'ScholarshipType',
        'scholarship_date_start': 'ScholarshipDateStart',
        'scholarship_date_end': 'ScholarshipDateEnd',
        'scholarship_name': 'ScholarshipName',
        'description': 'Description',
        'amount': 'Amount',
        'date_modified': 'DateModified'
    }

    def __init__(self, entry_scholarship_id=None, entry_id=None, scholarship_type=None, scholarship_date_start=None, scholarship_date_end=None, scholarship_name=None, description=None, amount=None, date_modified=None):  # noqa: E501
        """EntryScholarshipItem - a model defined in Swagger"""  # noqa: E501

        self._entry_scholarship_id = None
        self._entry_id = None
        self._scholarship_type = None
        self._scholarship_date_start = None
        self._scholarship_date_end = None
        self._scholarship_name = None
        self._description = None
        self._amount = None
        self._date_modified = None
        self.discriminator = None

        if entry_scholarship_id is not None:
            self.entry_scholarship_id = entry_scholarship_id
        if entry_id is not None:
            self.entry_id = entry_id
        if scholarship_type is not None:
            self.scholarship_type = scholarship_type
        if scholarship_date_start is not None:
            self.scholarship_date_start = scholarship_date_start
        if scholarship_date_end is not None:
            self.scholarship_date_end = scholarship_date_end
        if scholarship_name is not None:
            self.scholarship_name = scholarship_name
        if description is not None:
            self.description = description
        if amount is not None:
            self.amount = amount
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def entry_scholarship_id(self):
        """Gets the entry_scholarship_id of this EntryScholarshipItem.  # noqa: E501

        Entry Scholarship  # noqa: E501

        :return: The entry_scholarship_id of this EntryScholarshipItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_scholarship_id

    @entry_scholarship_id.setter
    def entry_scholarship_id(self, entry_scholarship_id):
        """Sets the entry_scholarship_id of this EntryScholarshipItem.

        Entry Scholarship  # noqa: E501

        :param entry_scholarship_id: The entry_scholarship_id of this EntryScholarshipItem.  # noqa: E501
        :type: int
        """

        self._entry_scholarship_id = entry_scholarship_id

    @property
    def entry_id(self):
        """Gets the entry_id of this EntryScholarshipItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this EntryScholarshipItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this EntryScholarshipItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this EntryScholarshipItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def scholarship_type(self):
        """Gets the scholarship_type of this EntryScholarshipItem.  # noqa: E501

        Scholarship Type  # noqa: E501

        :return: The scholarship_type of this EntryScholarshipItem.  # noqa: E501
        :rtype: str
        """
        return self._scholarship_type

    @scholarship_type.setter
    def scholarship_type(self, scholarship_type):
        """Sets the scholarship_type of this EntryScholarshipItem.

        Scholarship Type  # noqa: E501

        :param scholarship_type: The scholarship_type of this EntryScholarshipItem.  # noqa: E501
        :type: str
        """
        if scholarship_type is not None and len(scholarship_type) > 50:
            raise ValueError("Invalid value for `scholarship_type`, length must be less than or equal to `50`")  # noqa: E501

        self._scholarship_type = scholarship_type

    @property
    def scholarship_date_start(self):
        """Gets the scholarship_date_start of this EntryScholarshipItem.  # noqa: E501

        Scholarship Date Start  # noqa: E501

        :return: The scholarship_date_start of this EntryScholarshipItem.  # noqa: E501
        :rtype: str
        """
        return self._scholarship_date_start

    @scholarship_date_start.setter
    def scholarship_date_start(self, scholarship_date_start):
        """Sets the scholarship_date_start of this EntryScholarshipItem.

        Scholarship Date Start  # noqa: E501

        :param scholarship_date_start: The scholarship_date_start of this EntryScholarshipItem.  # noqa: E501
        :type: str
        """

        self._scholarship_date_start = scholarship_date_start

    @property
    def scholarship_date_end(self):
        """Gets the scholarship_date_end of this EntryScholarshipItem.  # noqa: E501

        Scholarship Date End  # noqa: E501

        :return: The scholarship_date_end of this EntryScholarshipItem.  # noqa: E501
        :rtype: str
        """
        return self._scholarship_date_end

    @scholarship_date_end.setter
    def scholarship_date_end(self, scholarship_date_end):
        """Sets the scholarship_date_end of this EntryScholarshipItem.

        Scholarship Date End  # noqa: E501

        :param scholarship_date_end: The scholarship_date_end of this EntryScholarshipItem.  # noqa: E501
        :type: str
        """

        self._scholarship_date_end = scholarship_date_end

    @property
    def scholarship_name(self):
        """Gets the scholarship_name of this EntryScholarshipItem.  # noqa: E501

        Scholarship Name  # noqa: E501

        :return: The scholarship_name of this EntryScholarshipItem.  # noqa: E501
        :rtype: str
        """
        return self._scholarship_name

    @scholarship_name.setter
    def scholarship_name(self, scholarship_name):
        """Sets the scholarship_name of this EntryScholarshipItem.

        Scholarship Name  # noqa: E501

        :param scholarship_name: The scholarship_name of this EntryScholarshipItem.  # noqa: E501
        :type: str
        """
        if scholarship_name is not None and len(scholarship_name) > 50:
            raise ValueError("Invalid value for `scholarship_name`, length must be less than or equal to `50`")  # noqa: E501

        self._scholarship_name = scholarship_name

    @property
    def description(self):
        """Gets the description of this EntryScholarshipItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this EntryScholarshipItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EntryScholarshipItem.

        Description  # noqa: E501

        :param description: The description of this EntryScholarshipItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def amount(self):
        """Gets the amount of this EntryScholarshipItem.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this EntryScholarshipItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EntryScholarshipItem.

        Amount  # noqa: E501

        :param amount: The amount of this EntryScholarshipItem.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def date_modified(self):
        """Gets the date_modified of this EntryScholarshipItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this EntryScholarshipItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this EntryScholarshipItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this EntryScholarshipItem.  # noqa: E501
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
        if not isinstance(other, EntryScholarshipItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
