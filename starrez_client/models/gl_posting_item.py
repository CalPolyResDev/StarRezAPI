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


class GLPostingItem(object):
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
        'gl_posting_id': 'int',
        'gl_posting_type_enum': 'str',
        'description': 'str',
        'gl_number': 'str',
        'comments': 'str',
        'record_type_enum': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'gl_posting_id': 'GLPostingID',
        'gl_posting_type_enum': 'GLPostingTypeEnum',
        'description': 'Description',
        'gl_number': 'GLNumber',
        'comments': 'Comments',
        'record_type_enum': 'RecordTypeEnum',
        'date_modified': 'DateModified'
    }

    def __init__(self, gl_posting_id=None, gl_posting_type_enum=None, description=None, gl_number=None, comments=None, record_type_enum=None, date_modified=None):  # noqa: E501
        """GLPostingItem - a model defined in Swagger"""  # noqa: E501

        self._gl_posting_id = None
        self._gl_posting_type_enum = None
        self._description = None
        self._gl_number = None
        self._comments = None
        self._record_type_enum = None
        self._date_modified = None
        self.discriminator = None

        if gl_posting_id is not None:
            self.gl_posting_id = gl_posting_id
        if gl_posting_type_enum is not None:
            self.gl_posting_type_enum = gl_posting_type_enum
        if description is not None:
            self.description = description
        if gl_number is not None:
            self.gl_number = gl_number
        if comments is not None:
            self.comments = comments
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def gl_posting_id(self):
        """Gets the gl_posting_id of this GLPostingItem.  # noqa: E501

        GL Posting  # noqa: E501

        :return: The gl_posting_id of this GLPostingItem.  # noqa: E501
        :rtype: int
        """
        return self._gl_posting_id

    @gl_posting_id.setter
    def gl_posting_id(self, gl_posting_id):
        """Sets the gl_posting_id of this GLPostingItem.

        GL Posting  # noqa: E501

        :param gl_posting_id: The gl_posting_id of this GLPostingItem.  # noqa: E501
        :type: int
        """

        self._gl_posting_id = gl_posting_id

    @property
    def gl_posting_type_enum(self):
        """Gets the gl_posting_type_enum of this GLPostingItem.  # noqa: E501

        GL Posting Type  # noqa: E501

        :return: The gl_posting_type_enum of this GLPostingItem.  # noqa: E501
        :rtype: str
        """
        return self._gl_posting_type_enum

    @gl_posting_type_enum.setter
    def gl_posting_type_enum(self, gl_posting_type_enum):
        """Sets the gl_posting_type_enum of this GLPostingItem.

        GL Posting Type  # noqa: E501

        :param gl_posting_type_enum: The gl_posting_type_enum of this GLPostingItem.  # noqa: E501
        :type: str
        """

        self._gl_posting_type_enum = gl_posting_type_enum

    @property
    def description(self):
        """Gets the description of this GLPostingItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this GLPostingItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GLPostingItem.

        Description  # noqa: E501

        :param description: The description of this GLPostingItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def gl_number(self):
        """Gets the gl_number of this GLPostingItem.  # noqa: E501

        GL Number  # noqa: E501

        :return: The gl_number of this GLPostingItem.  # noqa: E501
        :rtype: str
        """
        return self._gl_number

    @gl_number.setter
    def gl_number(self, gl_number):
        """Sets the gl_number of this GLPostingItem.

        GL Number  # noqa: E501

        :param gl_number: The gl_number of this GLPostingItem.  # noqa: E501
        :type: str
        """
        if gl_number is not None and len(gl_number) > 50:
            raise ValueError("Invalid value for `gl_number`, length must be less than or equal to `50`")  # noqa: E501

        self._gl_number = gl_number

    @property
    def comments(self):
        """Gets the comments of this GLPostingItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this GLPostingItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this GLPostingItem.

        Comments  # noqa: E501

        :param comments: The comments of this GLPostingItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 100:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `100`")  # noqa: E501

        self._comments = comments

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this GLPostingItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this GLPostingItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this GLPostingItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this GLPostingItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def date_modified(self):
        """Gets the date_modified of this GLPostingItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this GLPostingItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this GLPostingItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this GLPostingItem.  # noqa: E501
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
        if not isinstance(other, GLPostingItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
