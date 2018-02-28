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


class EndOfSessionItem(object):
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
        'end_of_session_id': 'int',
        'end_of_session_type_enum': 'str',
        'date_session': 'str',
        'comments': 'str',
        'machine_name': 'str',
        'date_created': 'datetime',
        'security_user_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'end_of_session_id': 'EndOfSessionID',
        'end_of_session_type_enum': 'EndOfSessionTypeEnum',
        'date_session': 'DateSession',
        'comments': 'Comments',
        'machine_name': 'MachineName',
        'date_created': 'DateCreated',
        'security_user_id': 'SecurityUserID',
        'date_modified': 'DateModified'
    }

    def __init__(self, end_of_session_id=None, end_of_session_type_enum=None, date_session=None, comments=None, machine_name=None, date_created=None, security_user_id=None, date_modified=None):  # noqa: E501
        """EndOfSessionItem - a model defined in Swagger"""  # noqa: E501

        self._end_of_session_id = None
        self._end_of_session_type_enum = None
        self._date_session = None
        self._comments = None
        self._machine_name = None
        self._date_created = None
        self._security_user_id = None
        self._date_modified = None
        self.discriminator = None

        if end_of_session_id is not None:
            self.end_of_session_id = end_of_session_id
        if end_of_session_type_enum is not None:
            self.end_of_session_type_enum = end_of_session_type_enum
        if date_session is not None:
            self.date_session = date_session
        if comments is not None:
            self.comments = comments
        if machine_name is not None:
            self.machine_name = machine_name
        if date_created is not None:
            self.date_created = date_created
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def end_of_session_id(self):
        """Gets the end_of_session_id of this EndOfSessionItem.  # noqa: E501

        End Of Session  # noqa: E501

        :return: The end_of_session_id of this EndOfSessionItem.  # noqa: E501
        :rtype: int
        """
        return self._end_of_session_id

    @end_of_session_id.setter
    def end_of_session_id(self, end_of_session_id):
        """Sets the end_of_session_id of this EndOfSessionItem.

        End Of Session  # noqa: E501

        :param end_of_session_id: The end_of_session_id of this EndOfSessionItem.  # noqa: E501
        :type: int
        """

        self._end_of_session_id = end_of_session_id

    @property
    def end_of_session_type_enum(self):
        """Gets the end_of_session_type_enum of this EndOfSessionItem.  # noqa: E501

        End Of Session Type  # noqa: E501

        :return: The end_of_session_type_enum of this EndOfSessionItem.  # noqa: E501
        :rtype: str
        """
        return self._end_of_session_type_enum

    @end_of_session_type_enum.setter
    def end_of_session_type_enum(self, end_of_session_type_enum):
        """Sets the end_of_session_type_enum of this EndOfSessionItem.

        End Of Session Type  # noqa: E501

        :param end_of_session_type_enum: The end_of_session_type_enum of this EndOfSessionItem.  # noqa: E501
        :type: str
        """

        self._end_of_session_type_enum = end_of_session_type_enum

    @property
    def date_session(self):
        """Gets the date_session of this EndOfSessionItem.  # noqa: E501

        Date Session  # noqa: E501

        :return: The date_session of this EndOfSessionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_session

    @date_session.setter
    def date_session(self, date_session):
        """Sets the date_session of this EndOfSessionItem.

        Date Session  # noqa: E501

        :param date_session: The date_session of this EndOfSessionItem.  # noqa: E501
        :type: str
        """

        self._date_session = date_session

    @property
    def comments(self):
        """Gets the comments of this EndOfSessionItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this EndOfSessionItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this EndOfSessionItem.

        Comments  # noqa: E501

        :param comments: The comments of this EndOfSessionItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 100:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `100`")  # noqa: E501

        self._comments = comments

    @property
    def machine_name(self):
        """Gets the machine_name of this EndOfSessionItem.  # noqa: E501

        Machine Name  # noqa: E501

        :return: The machine_name of this EndOfSessionItem.  # noqa: E501
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this EndOfSessionItem.

        Machine Name  # noqa: E501

        :param machine_name: The machine_name of this EndOfSessionItem.  # noqa: E501
        :type: str
        """
        if machine_name is not None and len(machine_name) > 30:
            raise ValueError("Invalid value for `machine_name`, length must be less than or equal to `30`")  # noqa: E501

        self._machine_name = machine_name

    @property
    def date_created(self):
        """Gets the date_created of this EndOfSessionItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this EndOfSessionItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this EndOfSessionItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this EndOfSessionItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def security_user_id(self):
        """Gets the security_user_id of this EndOfSessionItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this EndOfSessionItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this EndOfSessionItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this EndOfSessionItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_modified(self):
        """Gets the date_modified of this EndOfSessionItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this EndOfSessionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this EndOfSessionItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this EndOfSessionItem.  # noqa: E501
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
        if not isinstance(other, EndOfSessionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
