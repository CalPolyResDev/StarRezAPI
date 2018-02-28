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


class ProgramSubTypeItem(object):
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
        'program_sub_type_id': 'int',
        'program_type_id': 'int',
        'description': 'str',
        'comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'program_sub_type_id': 'ProgramSubTypeID',
        'program_type_id': 'ProgramTypeID',
        'description': 'Description',
        'comments': 'Comments',
        'date_modified': 'DateModified'
    }

    def __init__(self, program_sub_type_id=None, program_type_id=None, description=None, comments=None, date_modified=None):  # noqa: E501
        """ProgramSubTypeItem - a model defined in Swagger"""  # noqa: E501

        self._program_sub_type_id = None
        self._program_type_id = None
        self._description = None
        self._comments = None
        self._date_modified = None
        self.discriminator = None

        if program_sub_type_id is not None:
            self.program_sub_type_id = program_sub_type_id
        if program_type_id is not None:
            self.program_type_id = program_type_id
        if description is not None:
            self.description = description
        if comments is not None:
            self.comments = comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def program_sub_type_id(self):
        """Gets the program_sub_type_id of this ProgramSubTypeItem.  # noqa: E501

        Program Sub Type  # noqa: E501

        :return: The program_sub_type_id of this ProgramSubTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._program_sub_type_id

    @program_sub_type_id.setter
    def program_sub_type_id(self, program_sub_type_id):
        """Sets the program_sub_type_id of this ProgramSubTypeItem.

        Program Sub Type  # noqa: E501

        :param program_sub_type_id: The program_sub_type_id of this ProgramSubTypeItem.  # noqa: E501
        :type: int
        """

        self._program_sub_type_id = program_sub_type_id

    @property
    def program_type_id(self):
        """Gets the program_type_id of this ProgramSubTypeItem.  # noqa: E501

        Program Type  # noqa: E501

        :return: The program_type_id of this ProgramSubTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._program_type_id

    @program_type_id.setter
    def program_type_id(self, program_type_id):
        """Sets the program_type_id of this ProgramSubTypeItem.

        Program Type  # noqa: E501

        :param program_type_id: The program_type_id of this ProgramSubTypeItem.  # noqa: E501
        :type: int
        """

        self._program_type_id = program_type_id

    @property
    def description(self):
        """Gets the description of this ProgramSubTypeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ProgramSubTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProgramSubTypeItem.

        Description  # noqa: E501

        :param description: The description of this ProgramSubTypeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def comments(self):
        """Gets the comments of this ProgramSubTypeItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this ProgramSubTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ProgramSubTypeItem.

        Comments  # noqa: E501

        :param comments: The comments of this ProgramSubTypeItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 500:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `500`")  # noqa: E501

        self._comments = comments

    @property
    def date_modified(self):
        """Gets the date_modified of this ProgramSubTypeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this ProgramSubTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ProgramSubTypeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this ProgramSubTypeItem.  # noqa: E501
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
        if not isinstance(other, ProgramSubTypeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
