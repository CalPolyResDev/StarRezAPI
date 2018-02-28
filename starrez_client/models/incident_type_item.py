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


class IncidentTypeItem(object):
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
        'incident_type_id': 'int',
        'record_type_enum': 'str',
        'description': 'str',
        'grade': 'int',
        'comments': 'str',
        'category_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'incident_type_id': 'IncidentTypeID',
        'record_type_enum': 'RecordTypeEnum',
        'description': 'Description',
        'grade': 'Grade',
        'comments': 'Comments',
        'category_id': 'CategoryID',
        'date_modified': 'DateModified'
    }

    def __init__(self, incident_type_id=None, record_type_enum=None, description=None, grade=None, comments=None, category_id=None, date_modified=None):  # noqa: E501
        """IncidentTypeItem - a model defined in Swagger"""  # noqa: E501

        self._incident_type_id = None
        self._record_type_enum = None
        self._description = None
        self._grade = None
        self._comments = None
        self._category_id = None
        self._date_modified = None
        self.discriminator = None

        if incident_type_id is not None:
            self.incident_type_id = incident_type_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if description is not None:
            self.description = description
        if grade is not None:
            self.grade = grade
        if comments is not None:
            self.comments = comments
        if category_id is not None:
            self.category_id = category_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def incident_type_id(self):
        """Gets the incident_type_id of this IncidentTypeItem.  # noqa: E501

        Incident Type  # noqa: E501

        :return: The incident_type_id of this IncidentTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_type_id

    @incident_type_id.setter
    def incident_type_id(self, incident_type_id):
        """Sets the incident_type_id of this IncidentTypeItem.

        Incident Type  # noqa: E501

        :param incident_type_id: The incident_type_id of this IncidentTypeItem.  # noqa: E501
        :type: int
        """

        self._incident_type_id = incident_type_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this IncidentTypeItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this IncidentTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this IncidentTypeItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this IncidentTypeItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def description(self):
        """Gets the description of this IncidentTypeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this IncidentTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IncidentTypeItem.

        Description  # noqa: E501

        :param description: The description of this IncidentTypeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def grade(self):
        """Gets the grade of this IncidentTypeItem.  # noqa: E501

        Grade  # noqa: E501

        :return: The grade of this IncidentTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._grade

    @grade.setter
    def grade(self, grade):
        """Sets the grade of this IncidentTypeItem.

        Grade  # noqa: E501

        :param grade: The grade of this IncidentTypeItem.  # noqa: E501
        :type: int
        """

        self._grade = grade

    @property
    def comments(self):
        """Gets the comments of this IncidentTypeItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this IncidentTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this IncidentTypeItem.

        Comments  # noqa: E501

        :param comments: The comments of this IncidentTypeItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 1000:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `1000`")  # noqa: E501

        self._comments = comments

    @property
    def category_id(self):
        """Gets the category_id of this IncidentTypeItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this IncidentTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this IncidentTypeItem.

        Category  # noqa: E501

        :param category_id: The category_id of this IncidentTypeItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def date_modified(self):
        """Gets the date_modified of this IncidentTypeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this IncidentTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this IncidentTypeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this IncidentTypeItem.  # noqa: E501
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
        if not isinstance(other, IncidentTypeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
