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


class TermItem(object):
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
        'term_id': 'int',
        'record_type_enum': 'str',
        'description': 'str',
        'web_description': 'str',
        'category_id': 'int',
        'term_code': 'str',
        'term_type_id': 'int',
        'active': 'bool',
        'active_date_open': 'str',
        'active_date_close': 'str',
        'comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'term_id': 'TermID',
        'record_type_enum': 'RecordTypeEnum',
        'description': 'Description',
        'web_description': 'WebDescription',
        'category_id': 'CategoryID',
        'term_code': 'TermCode',
        'term_type_id': 'TermTypeID',
        'active': 'Active',
        'active_date_open': 'ActiveDateOpen',
        'active_date_close': 'ActiveDateClose',
        'comments': 'Comments',
        'date_modified': 'DateModified'
    }

    def __init__(self, term_id=None, record_type_enum=None, description=None, web_description=None, category_id=None, term_code=None, term_type_id=None, active=None, active_date_open=None, active_date_close=None, comments=None, date_modified=None):  # noqa: E501
        """TermItem - a model defined in Swagger"""  # noqa: E501

        self._term_id = None
        self._record_type_enum = None
        self._description = None
        self._web_description = None
        self._category_id = None
        self._term_code = None
        self._term_type_id = None
        self._active = None
        self._active_date_open = None
        self._active_date_close = None
        self._comments = None
        self._date_modified = None
        self.discriminator = None

        if term_id is not None:
            self.term_id = term_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if description is not None:
            self.description = description
        if web_description is not None:
            self.web_description = web_description
        if category_id is not None:
            self.category_id = category_id
        if term_code is not None:
            self.term_code = term_code
        if term_type_id is not None:
            self.term_type_id = term_type_id
        if active is not None:
            self.active = active
        if active_date_open is not None:
            self.active_date_open = active_date_open
        if active_date_close is not None:
            self.active_date_close = active_date_close
        if comments is not None:
            self.comments = comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def term_id(self):
        """Gets the term_id of this TermItem.  # noqa: E501

        Term  # noqa: E501

        :return: The term_id of this TermItem.  # noqa: E501
        :rtype: int
        """
        return self._term_id

    @term_id.setter
    def term_id(self, term_id):
        """Sets the term_id of this TermItem.

        Term  # noqa: E501

        :param term_id: The term_id of this TermItem.  # noqa: E501
        :type: int
        """

        self._term_id = term_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this TermItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this TermItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this TermItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this TermItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def description(self):
        """Gets the description of this TermItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this TermItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TermItem.

        Description  # noqa: E501

        :param description: The description of this TermItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 40:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `40`")  # noqa: E501

        self._description = description

    @property
    def web_description(self):
        """Gets the web_description of this TermItem.  # noqa: E501

        Web Description  # noqa: E501

        :return: The web_description of this TermItem.  # noqa: E501
        :rtype: str
        """
        return self._web_description

    @web_description.setter
    def web_description(self, web_description):
        """Sets the web_description of this TermItem.

        Web Description  # noqa: E501

        :param web_description: The web_description of this TermItem.  # noqa: E501
        :type: str
        """
        if web_description is not None and len(web_description) > 40:
            raise ValueError("Invalid value for `web_description`, length must be less than or equal to `40`")  # noqa: E501

        self._web_description = web_description

    @property
    def category_id(self):
        """Gets the category_id of this TermItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this TermItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this TermItem.

        Category  # noqa: E501

        :param category_id: The category_id of this TermItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def term_code(self):
        """Gets the term_code of this TermItem.  # noqa: E501

        Term Code  # noqa: E501

        :return: The term_code of this TermItem.  # noqa: E501
        :rtype: str
        """
        return self._term_code

    @term_code.setter
    def term_code(self, term_code):
        """Sets the term_code of this TermItem.

        Term Code  # noqa: E501

        :param term_code: The term_code of this TermItem.  # noqa: E501
        :type: str
        """
        if term_code is not None and len(term_code) > 40:
            raise ValueError("Invalid value for `term_code`, length must be less than or equal to `40`")  # noqa: E501

        self._term_code = term_code

    @property
    def term_type_id(self):
        """Gets the term_type_id of this TermItem.  # noqa: E501

        Term Type  # noqa: E501

        :return: The term_type_id of this TermItem.  # noqa: E501
        :rtype: int
        """
        return self._term_type_id

    @term_type_id.setter
    def term_type_id(self, term_type_id):
        """Sets the term_type_id of this TermItem.

        Term Type  # noqa: E501

        :param term_type_id: The term_type_id of this TermItem.  # noqa: E501
        :type: int
        """

        self._term_type_id = term_type_id

    @property
    def active(self):
        """Gets the active of this TermItem.  # noqa: E501

        Active  # noqa: E501

        :return: The active of this TermItem.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this TermItem.

        Active  # noqa: E501

        :param active: The active of this TermItem.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def active_date_open(self):
        """Gets the active_date_open of this TermItem.  # noqa: E501

        Active Date Open  # noqa: E501

        :return: The active_date_open of this TermItem.  # noqa: E501
        :rtype: str
        """
        return self._active_date_open

    @active_date_open.setter
    def active_date_open(self, active_date_open):
        """Sets the active_date_open of this TermItem.

        Active Date Open  # noqa: E501

        :param active_date_open: The active_date_open of this TermItem.  # noqa: E501
        :type: str
        """

        self._active_date_open = active_date_open

    @property
    def active_date_close(self):
        """Gets the active_date_close of this TermItem.  # noqa: E501

        Active Date Close  # noqa: E501

        :return: The active_date_close of this TermItem.  # noqa: E501
        :rtype: str
        """
        return self._active_date_close

    @active_date_close.setter
    def active_date_close(self, active_date_close):
        """Sets the active_date_close of this TermItem.

        Active Date Close  # noqa: E501

        :param active_date_close: The active_date_close of this TermItem.  # noqa: E501
        :type: str
        """

        self._active_date_close = active_date_close

    @property
    def comments(self):
        """Gets the comments of this TermItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this TermItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this TermItem.

        Comments  # noqa: E501

        :param comments: The comments of this TermItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 100:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `100`")  # noqa: E501

        self._comments = comments

    @property
    def date_modified(self):
        """Gets the date_modified of this TermItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this TermItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this TermItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this TermItem.  # noqa: E501
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
        if not isinstance(other, TermItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
