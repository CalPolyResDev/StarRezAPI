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


class FunctionRoomClosedItem(object):
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
        'function_room_closed_id': 'int',
        'function_room_id': 'int',
        'date_start': 'datetime',
        'date_end': 'datetime',
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
        'date_created': 'datetime',
        'security_user_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'function_room_closed_id': 'FunctionRoomClosedID',
        'function_room_id': 'FunctionRoomID',
        'date_start': 'DateStart',
        'date_end': 'DateEnd',
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
        'date_created': 'DateCreated',
        'security_user_id': 'SecurityUserID',
        'date_modified': 'DateModified'
    }

    def __init__(self, function_room_closed_id=None, function_room_id=None, date_start=None, date_end=None, comments=None, custom_bit1=None, custom_bit2=None, custom_string1=None, custom_string2=None, custom_string3=None, custom_string4=None, custom_string5=None, custom_string6=None, custom_date1=None, custom_date2=None, date_created=None, security_user_id=None, date_modified=None):  # noqa: E501
        """FunctionRoomClosedItem - a model defined in Swagger"""  # noqa: E501

        self._function_room_closed_id = None
        self._function_room_id = None
        self._date_start = None
        self._date_end = None
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
        self._date_created = None
        self._security_user_id = None
        self._date_modified = None
        self.discriminator = None

        if function_room_closed_id is not None:
            self.function_room_closed_id = function_room_closed_id
        if function_room_id is not None:
            self.function_room_id = function_room_id
        if date_start is not None:
            self.date_start = date_start
        if date_end is not None:
            self.date_end = date_end
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
        if date_created is not None:
            self.date_created = date_created
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def function_room_closed_id(self):
        """Gets the function_room_closed_id of this FunctionRoomClosedItem.  # noqa: E501

        Function Room Closed  # noqa: E501

        :return: The function_room_closed_id of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: int
        """
        return self._function_room_closed_id

    @function_room_closed_id.setter
    def function_room_closed_id(self, function_room_closed_id):
        """Sets the function_room_closed_id of this FunctionRoomClosedItem.

        Function Room Closed  # noqa: E501

        :param function_room_closed_id: The function_room_closed_id of this FunctionRoomClosedItem.  # noqa: E501
        :type: int
        """

        self._function_room_closed_id = function_room_closed_id

    @property
    def function_room_id(self):
        """Gets the function_room_id of this FunctionRoomClosedItem.  # noqa: E501

        Function Room  # noqa: E501

        :return: The function_room_id of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: int
        """
        return self._function_room_id

    @function_room_id.setter
    def function_room_id(self, function_room_id):
        """Sets the function_room_id of this FunctionRoomClosedItem.

        Function Room  # noqa: E501

        :param function_room_id: The function_room_id of this FunctionRoomClosedItem.  # noqa: E501
        :type: int
        """

        self._function_room_id = function_room_id

    @property
    def date_start(self):
        """Gets the date_start of this FunctionRoomClosedItem.  # noqa: E501

        Date Start  # noqa: E501

        :return: The date_start of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this FunctionRoomClosedItem.

        Date Start  # noqa: E501

        :param date_start: The date_start of this FunctionRoomClosedItem.  # noqa: E501
        :type: datetime
        """

        self._date_start = date_start

    @property
    def date_end(self):
        """Gets the date_end of this FunctionRoomClosedItem.  # noqa: E501

        Date End  # noqa: E501

        :return: The date_end of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this FunctionRoomClosedItem.

        Date End  # noqa: E501

        :param date_end: The date_end of this FunctionRoomClosedItem.  # noqa: E501
        :type: datetime
        """

        self._date_end = date_end

    @property
    def comments(self):
        """Gets the comments of this FunctionRoomClosedItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this FunctionRoomClosedItem.

        Comments  # noqa: E501

        :param comments: The comments of this FunctionRoomClosedItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 100:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `100`")  # noqa: E501

        self._comments = comments

    @property
    def custom_bit1(self):
        """Gets the custom_bit1 of this FunctionRoomClosedItem.  # noqa: E501

        Custom Flag 1  # noqa: E501

        :return: The custom_bit1 of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit1

    @custom_bit1.setter
    def custom_bit1(self, custom_bit1):
        """Sets the custom_bit1 of this FunctionRoomClosedItem.

        Custom Flag 1  # noqa: E501

        :param custom_bit1: The custom_bit1 of this FunctionRoomClosedItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit1 = custom_bit1

    @property
    def custom_bit2(self):
        """Gets the custom_bit2 of this FunctionRoomClosedItem.  # noqa: E501

        Custom Flag 2  # noqa: E501

        :return: The custom_bit2 of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit2

    @custom_bit2.setter
    def custom_bit2(self, custom_bit2):
        """Sets the custom_bit2 of this FunctionRoomClosedItem.

        Custom Flag 2  # noqa: E501

        :param custom_bit2: The custom_bit2 of this FunctionRoomClosedItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit2 = custom_bit2

    @property
    def custom_string1(self):
        """Gets the custom_string1 of this FunctionRoomClosedItem.  # noqa: E501

        Custom String 1  # noqa: E501

        :return: The custom_string1 of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string1

    @custom_string1.setter
    def custom_string1(self, custom_string1):
        """Sets the custom_string1 of this FunctionRoomClosedItem.

        Custom String 1  # noqa: E501

        :param custom_string1: The custom_string1 of this FunctionRoomClosedItem.  # noqa: E501
        :type: str
        """
        if custom_string1 is not None and len(custom_string1) > 50:
            raise ValueError("Invalid value for `custom_string1`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string1 = custom_string1

    @property
    def custom_string2(self):
        """Gets the custom_string2 of this FunctionRoomClosedItem.  # noqa: E501

        Custom String 2  # noqa: E501

        :return: The custom_string2 of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string2

    @custom_string2.setter
    def custom_string2(self, custom_string2):
        """Sets the custom_string2 of this FunctionRoomClosedItem.

        Custom String 2  # noqa: E501

        :param custom_string2: The custom_string2 of this FunctionRoomClosedItem.  # noqa: E501
        :type: str
        """
        if custom_string2 is not None and len(custom_string2) > 50:
            raise ValueError("Invalid value for `custom_string2`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string2 = custom_string2

    @property
    def custom_string3(self):
        """Gets the custom_string3 of this FunctionRoomClosedItem.  # noqa: E501

        Custom String 3  # noqa: E501

        :return: The custom_string3 of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string3

    @custom_string3.setter
    def custom_string3(self, custom_string3):
        """Sets the custom_string3 of this FunctionRoomClosedItem.

        Custom String 3  # noqa: E501

        :param custom_string3: The custom_string3 of this FunctionRoomClosedItem.  # noqa: E501
        :type: str
        """
        if custom_string3 is not None and len(custom_string3) > 50:
            raise ValueError("Invalid value for `custom_string3`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string3 = custom_string3

    @property
    def custom_string4(self):
        """Gets the custom_string4 of this FunctionRoomClosedItem.  # noqa: E501

        Custom String 4  # noqa: E501

        :return: The custom_string4 of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string4

    @custom_string4.setter
    def custom_string4(self, custom_string4):
        """Sets the custom_string4 of this FunctionRoomClosedItem.

        Custom String 4  # noqa: E501

        :param custom_string4: The custom_string4 of this FunctionRoomClosedItem.  # noqa: E501
        :type: str
        """
        if custom_string4 is not None and len(custom_string4) > 50:
            raise ValueError("Invalid value for `custom_string4`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string4 = custom_string4

    @property
    def custom_string5(self):
        """Gets the custom_string5 of this FunctionRoomClosedItem.  # noqa: E501

        Custom String 5  # noqa: E501

        :return: The custom_string5 of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string5

    @custom_string5.setter
    def custom_string5(self, custom_string5):
        """Sets the custom_string5 of this FunctionRoomClosedItem.

        Custom String 5  # noqa: E501

        :param custom_string5: The custom_string5 of this FunctionRoomClosedItem.  # noqa: E501
        :type: str
        """
        if custom_string5 is not None and len(custom_string5) > 50:
            raise ValueError("Invalid value for `custom_string5`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string5 = custom_string5

    @property
    def custom_string6(self):
        """Gets the custom_string6 of this FunctionRoomClosedItem.  # noqa: E501

        Custom String 6  # noqa: E501

        :return: The custom_string6 of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string6

    @custom_string6.setter
    def custom_string6(self, custom_string6):
        """Sets the custom_string6 of this FunctionRoomClosedItem.

        Custom String 6  # noqa: E501

        :param custom_string6: The custom_string6 of this FunctionRoomClosedItem.  # noqa: E501
        :type: str
        """
        if custom_string6 is not None and len(custom_string6) > 50:
            raise ValueError("Invalid value for `custom_string6`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string6 = custom_string6

    @property
    def custom_date1(self):
        """Gets the custom_date1 of this FunctionRoomClosedItem.  # noqa: E501

        Custom Date 1  # noqa: E501

        :return: The custom_date1 of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date1

    @custom_date1.setter
    def custom_date1(self, custom_date1):
        """Sets the custom_date1 of this FunctionRoomClosedItem.

        Custom Date 1  # noqa: E501

        :param custom_date1: The custom_date1 of this FunctionRoomClosedItem.  # noqa: E501
        :type: str
        """

        self._custom_date1 = custom_date1

    @property
    def custom_date2(self):
        """Gets the custom_date2 of this FunctionRoomClosedItem.  # noqa: E501

        Custom Date 2  # noqa: E501

        :return: The custom_date2 of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date2

    @custom_date2.setter
    def custom_date2(self, custom_date2):
        """Sets the custom_date2 of this FunctionRoomClosedItem.

        Custom Date 2  # noqa: E501

        :param custom_date2: The custom_date2 of this FunctionRoomClosedItem.  # noqa: E501
        :type: str
        """

        self._custom_date2 = custom_date2

    @property
    def date_created(self):
        """Gets the date_created of this FunctionRoomClosedItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this FunctionRoomClosedItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this FunctionRoomClosedItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def security_user_id(self):
        """Gets the security_user_id of this FunctionRoomClosedItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this FunctionRoomClosedItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this FunctionRoomClosedItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_modified(self):
        """Gets the date_modified of this FunctionRoomClosedItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this FunctionRoomClosedItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this FunctionRoomClosedItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this FunctionRoomClosedItem.  # noqa: E501
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
        if not isinstance(other, FunctionRoomClosedItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
