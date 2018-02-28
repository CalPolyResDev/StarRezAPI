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


class VisitorItem(object):
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
        'visitor_id': 'int',
        'visitor_entry_id': 'int',
        'name_last': 'str',
        'name_first': 'str',
        'gender_enum': 'str',
        'id1': 'str',
        'id_type': 'str',
        'id_number': 'str',
        'phone_number': 'str',
        'banned': 'bool',
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
        'comments': 'str',
        'security_user_id': 'int',
        'created_by_security_user_id': 'int',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'visitor_id': 'VisitorID',
        'visitor_entry_id': 'Visitor_EntryID',
        'name_last': 'NameLast',
        'name_first': 'NameFirst',
        'gender_enum': 'GenderEnum',
        'id1': 'ID1',
        'id_type': 'IDType',
        'id_number': 'IDNumber',
        'phone_number': 'PhoneNumber',
        'banned': 'Banned',
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
        'comments': 'Comments',
        'security_user_id': 'SecurityUserID',
        'created_by_security_user_id': 'CreatedBy_SecurityUserID',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, visitor_id=None, visitor_entry_id=None, name_last=None, name_first=None, gender_enum=None, id1=None, id_type=None, id_number=None, phone_number=None, banned=None, custom_bit1=None, custom_bit2=None, custom_string1=None, custom_string2=None, custom_string3=None, custom_string4=None, custom_string5=None, custom_string6=None, custom_date1=None, custom_date2=None, comments=None, security_user_id=None, created_by_security_user_id=None, date_created=None, date_modified=None):  # noqa: E501
        """VisitorItem - a model defined in Swagger"""  # noqa: E501

        self._visitor_id = None
        self._visitor_entry_id = None
        self._name_last = None
        self._name_first = None
        self._gender_enum = None
        self._id1 = None
        self._id_type = None
        self._id_number = None
        self._phone_number = None
        self._banned = None
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
        self._comments = None
        self._security_user_id = None
        self._created_by_security_user_id = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if visitor_id is not None:
            self.visitor_id = visitor_id
        if visitor_entry_id is not None:
            self.visitor_entry_id = visitor_entry_id
        if name_last is not None:
            self.name_last = name_last
        if name_first is not None:
            self.name_first = name_first
        if gender_enum is not None:
            self.gender_enum = gender_enum
        if id1 is not None:
            self.id1 = id1
        if id_type is not None:
            self.id_type = id_type
        if id_number is not None:
            self.id_number = id_number
        if phone_number is not None:
            self.phone_number = phone_number
        if banned is not None:
            self.banned = banned
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
        if comments is not None:
            self.comments = comments
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if created_by_security_user_id is not None:
            self.created_by_security_user_id = created_by_security_user_id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def visitor_id(self):
        """Gets the visitor_id of this VisitorItem.  # noqa: E501

        Visitor  # noqa: E501

        :return: The visitor_id of this VisitorItem.  # noqa: E501
        :rtype: int
        """
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, visitor_id):
        """Sets the visitor_id of this VisitorItem.

        Visitor  # noqa: E501

        :param visitor_id: The visitor_id of this VisitorItem.  # noqa: E501
        :type: int
        """

        self._visitor_id = visitor_id

    @property
    def visitor_entry_id(self):
        """Gets the visitor_entry_id of this VisitorItem.  # noqa: E501

        Visitor Entry  # noqa: E501

        :return: The visitor_entry_id of this VisitorItem.  # noqa: E501
        :rtype: int
        """
        return self._visitor_entry_id

    @visitor_entry_id.setter
    def visitor_entry_id(self, visitor_entry_id):
        """Sets the visitor_entry_id of this VisitorItem.

        Visitor Entry  # noqa: E501

        :param visitor_entry_id: The visitor_entry_id of this VisitorItem.  # noqa: E501
        :type: int
        """

        self._visitor_entry_id = visitor_entry_id

    @property
    def name_last(self):
        """Gets the name_last of this VisitorItem.  # noqa: E501

        Name Last  # noqa: E501

        :return: The name_last of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._name_last

    @name_last.setter
    def name_last(self, name_last):
        """Sets the name_last of this VisitorItem.

        Name Last  # noqa: E501

        :param name_last: The name_last of this VisitorItem.  # noqa: E501
        :type: str
        """
        if name_last is not None and len(name_last) > 40:
            raise ValueError("Invalid value for `name_last`, length must be less than or equal to `40`")  # noqa: E501

        self._name_last = name_last

    @property
    def name_first(self):
        """Gets the name_first of this VisitorItem.  # noqa: E501

        Name First  # noqa: E501

        :return: The name_first of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._name_first

    @name_first.setter
    def name_first(self, name_first):
        """Sets the name_first of this VisitorItem.

        Name First  # noqa: E501

        :param name_first: The name_first of this VisitorItem.  # noqa: E501
        :type: str
        """
        if name_first is not None and len(name_first) > 40:
            raise ValueError("Invalid value for `name_first`, length must be less than or equal to `40`")  # noqa: E501

        self._name_first = name_first

    @property
    def gender_enum(self):
        """Gets the gender_enum of this VisitorItem.  # noqa: E501

        Gender  # noqa: E501

        :return: The gender_enum of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._gender_enum

    @gender_enum.setter
    def gender_enum(self, gender_enum):
        """Sets the gender_enum of this VisitorItem.

        Gender  # noqa: E501

        :param gender_enum: The gender_enum of this VisitorItem.  # noqa: E501
        :type: str
        """

        self._gender_enum = gender_enum

    @property
    def id1(self):
        """Gets the id1 of this VisitorItem.  # noqa: E501

        ID 1  # noqa: E501

        :return: The id1 of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._id1

    @id1.setter
    def id1(self, id1):
        """Sets the id1 of this VisitorItem.

        ID 1  # noqa: E501

        :param id1: The id1 of this VisitorItem.  # noqa: E501
        :type: str
        """
        if id1 is not None and len(id1) > 30:
            raise ValueError("Invalid value for `id1`, length must be less than or equal to `30`")  # noqa: E501

        self._id1 = id1

    @property
    def id_type(self):
        """Gets the id_type of this VisitorItem.  # noqa: E501

        ID Type  # noqa: E501

        :return: The id_type of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this VisitorItem.

        ID Type  # noqa: E501

        :param id_type: The id_type of this VisitorItem.  # noqa: E501
        :type: str
        """
        if id_type is not None and len(id_type) > 50:
            raise ValueError("Invalid value for `id_type`, length must be less than or equal to `50`")  # noqa: E501

        self._id_type = id_type

    @property
    def id_number(self):
        """Gets the id_number of this VisitorItem.  # noqa: E501

        ID Number  # noqa: E501

        :return: The id_number of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this VisitorItem.

        ID Number  # noqa: E501

        :param id_number: The id_number of this VisitorItem.  # noqa: E501
        :type: str
        """
        if id_number is not None and len(id_number) > 200:
            raise ValueError("Invalid value for `id_number`, length must be less than or equal to `200`")  # noqa: E501

        self._id_number = id_number

    @property
    def phone_number(self):
        """Gets the phone_number of this VisitorItem.  # noqa: E501

        Phone Number  # noqa: E501

        :return: The phone_number of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this VisitorItem.

        Phone Number  # noqa: E501

        :param phone_number: The phone_number of this VisitorItem.  # noqa: E501
        :type: str
        """
        if phone_number is not None and len(phone_number) > 25:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `25`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def banned(self):
        """Gets the banned of this VisitorItem.  # noqa: E501

        Banned  # noqa: E501

        :return: The banned of this VisitorItem.  # noqa: E501
        :rtype: bool
        """
        return self._banned

    @banned.setter
    def banned(self, banned):
        """Sets the banned of this VisitorItem.

        Banned  # noqa: E501

        :param banned: The banned of this VisitorItem.  # noqa: E501
        :type: bool
        """

        self._banned = banned

    @property
    def custom_bit1(self):
        """Gets the custom_bit1 of this VisitorItem.  # noqa: E501

        Custom Flag 1  # noqa: E501

        :return: The custom_bit1 of this VisitorItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit1

    @custom_bit1.setter
    def custom_bit1(self, custom_bit1):
        """Sets the custom_bit1 of this VisitorItem.

        Custom Flag 1  # noqa: E501

        :param custom_bit1: The custom_bit1 of this VisitorItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit1 = custom_bit1

    @property
    def custom_bit2(self):
        """Gets the custom_bit2 of this VisitorItem.  # noqa: E501

        Custom Flag 2  # noqa: E501

        :return: The custom_bit2 of this VisitorItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit2

    @custom_bit2.setter
    def custom_bit2(self, custom_bit2):
        """Sets the custom_bit2 of this VisitorItem.

        Custom Flag 2  # noqa: E501

        :param custom_bit2: The custom_bit2 of this VisitorItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit2 = custom_bit2

    @property
    def custom_string1(self):
        """Gets the custom_string1 of this VisitorItem.  # noqa: E501

        Custom String 1  # noqa: E501

        :return: The custom_string1 of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string1

    @custom_string1.setter
    def custom_string1(self, custom_string1):
        """Sets the custom_string1 of this VisitorItem.

        Custom String 1  # noqa: E501

        :param custom_string1: The custom_string1 of this VisitorItem.  # noqa: E501
        :type: str
        """
        if custom_string1 is not None and len(custom_string1) > 50:
            raise ValueError("Invalid value for `custom_string1`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string1 = custom_string1

    @property
    def custom_string2(self):
        """Gets the custom_string2 of this VisitorItem.  # noqa: E501

        Custom String 2  # noqa: E501

        :return: The custom_string2 of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string2

    @custom_string2.setter
    def custom_string2(self, custom_string2):
        """Sets the custom_string2 of this VisitorItem.

        Custom String 2  # noqa: E501

        :param custom_string2: The custom_string2 of this VisitorItem.  # noqa: E501
        :type: str
        """
        if custom_string2 is not None and len(custom_string2) > 50:
            raise ValueError("Invalid value for `custom_string2`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string2 = custom_string2

    @property
    def custom_string3(self):
        """Gets the custom_string3 of this VisitorItem.  # noqa: E501

        Custom String 3  # noqa: E501

        :return: The custom_string3 of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string3

    @custom_string3.setter
    def custom_string3(self, custom_string3):
        """Sets the custom_string3 of this VisitorItem.

        Custom String 3  # noqa: E501

        :param custom_string3: The custom_string3 of this VisitorItem.  # noqa: E501
        :type: str
        """
        if custom_string3 is not None and len(custom_string3) > 50:
            raise ValueError("Invalid value for `custom_string3`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string3 = custom_string3

    @property
    def custom_string4(self):
        """Gets the custom_string4 of this VisitorItem.  # noqa: E501

        Custom String 4  # noqa: E501

        :return: The custom_string4 of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string4

    @custom_string4.setter
    def custom_string4(self, custom_string4):
        """Sets the custom_string4 of this VisitorItem.

        Custom String 4  # noqa: E501

        :param custom_string4: The custom_string4 of this VisitorItem.  # noqa: E501
        :type: str
        """
        if custom_string4 is not None and len(custom_string4) > 50:
            raise ValueError("Invalid value for `custom_string4`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string4 = custom_string4

    @property
    def custom_string5(self):
        """Gets the custom_string5 of this VisitorItem.  # noqa: E501

        Custom String 5  # noqa: E501

        :return: The custom_string5 of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string5

    @custom_string5.setter
    def custom_string5(self, custom_string5):
        """Sets the custom_string5 of this VisitorItem.

        Custom String 5  # noqa: E501

        :param custom_string5: The custom_string5 of this VisitorItem.  # noqa: E501
        :type: str
        """
        if custom_string5 is not None and len(custom_string5) > 50:
            raise ValueError("Invalid value for `custom_string5`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string5 = custom_string5

    @property
    def custom_string6(self):
        """Gets the custom_string6 of this VisitorItem.  # noqa: E501

        Custom String 6  # noqa: E501

        :return: The custom_string6 of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string6

    @custom_string6.setter
    def custom_string6(self, custom_string6):
        """Sets the custom_string6 of this VisitorItem.

        Custom String 6  # noqa: E501

        :param custom_string6: The custom_string6 of this VisitorItem.  # noqa: E501
        :type: str
        """
        if custom_string6 is not None and len(custom_string6) > 50:
            raise ValueError("Invalid value for `custom_string6`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string6 = custom_string6

    @property
    def custom_date1(self):
        """Gets the custom_date1 of this VisitorItem.  # noqa: E501

        Custom Date 1  # noqa: E501

        :return: The custom_date1 of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date1

    @custom_date1.setter
    def custom_date1(self, custom_date1):
        """Sets the custom_date1 of this VisitorItem.

        Custom Date 1  # noqa: E501

        :param custom_date1: The custom_date1 of this VisitorItem.  # noqa: E501
        :type: str
        """

        self._custom_date1 = custom_date1

    @property
    def custom_date2(self):
        """Gets the custom_date2 of this VisitorItem.  # noqa: E501

        Custom Date 2  # noqa: E501

        :return: The custom_date2 of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date2

    @custom_date2.setter
    def custom_date2(self, custom_date2):
        """Sets the custom_date2 of this VisitorItem.

        Custom Date 2  # noqa: E501

        :param custom_date2: The custom_date2 of this VisitorItem.  # noqa: E501
        :type: str
        """

        self._custom_date2 = custom_date2

    @property
    def comments(self):
        """Gets the comments of this VisitorItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this VisitorItem.

        Comments  # noqa: E501

        :param comments: The comments of this VisitorItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 200:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `200`")  # noqa: E501

        self._comments = comments

    @property
    def security_user_id(self):
        """Gets the security_user_id of this VisitorItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this VisitorItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this VisitorItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this VisitorItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def created_by_security_user_id(self):
        """Gets the created_by_security_user_id of this VisitorItem.  # noqa: E501

        Created By Security User  # noqa: E501

        :return: The created_by_security_user_id of this VisitorItem.  # noqa: E501
        :rtype: int
        """
        return self._created_by_security_user_id

    @created_by_security_user_id.setter
    def created_by_security_user_id(self, created_by_security_user_id):
        """Sets the created_by_security_user_id of this VisitorItem.

        Created By Security User  # noqa: E501

        :param created_by_security_user_id: The created_by_security_user_id of this VisitorItem.  # noqa: E501
        :type: int
        """

        self._created_by_security_user_id = created_by_security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this VisitorItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this VisitorItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this VisitorItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this VisitorItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this VisitorItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this VisitorItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this VisitorItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this VisitorItem.  # noqa: E501
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
        if not isinstance(other, VisitorItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other