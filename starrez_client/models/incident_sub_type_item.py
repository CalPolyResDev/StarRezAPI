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


class IncidentSubTypeItem(object):
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
        'incident_sub_type_id': 'int',
        'record_type_enum': 'str',
        'incident_type_id': 'int',
        'incident_severity_id': 'int',
        'description': 'str',
        'comments': 'str',
        'clery': 'bool',
        'clery_order': 'int',
        'always_count_in_clery': 'bool',
        'date_modified': 'str'
    }

    attribute_map = {
        'incident_sub_type_id': 'IncidentSubTypeID',
        'record_type_enum': 'RecordTypeEnum',
        'incident_type_id': 'IncidentTypeID',
        'incident_severity_id': 'IncidentSeverityID',
        'description': 'Description',
        'comments': 'Comments',
        'clery': 'Clery',
        'clery_order': 'CleryOrder',
        'always_count_in_clery': 'AlwaysCountInClery',
        'date_modified': 'DateModified'
    }

    def __init__(self, incident_sub_type_id=None, record_type_enum=None, incident_type_id=None, incident_severity_id=None, description=None, comments=None, clery=None, clery_order=None, always_count_in_clery=None, date_modified=None):  # noqa: E501
        """IncidentSubTypeItem - a model defined in Swagger"""  # noqa: E501

        self._incident_sub_type_id = None
        self._record_type_enum = None
        self._incident_type_id = None
        self._incident_severity_id = None
        self._description = None
        self._comments = None
        self._clery = None
        self._clery_order = None
        self._always_count_in_clery = None
        self._date_modified = None
        self.discriminator = None

        if incident_sub_type_id is not None:
            self.incident_sub_type_id = incident_sub_type_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if incident_type_id is not None:
            self.incident_type_id = incident_type_id
        if incident_severity_id is not None:
            self.incident_severity_id = incident_severity_id
        if description is not None:
            self.description = description
        if comments is not None:
            self.comments = comments
        if clery is not None:
            self.clery = clery
        if clery_order is not None:
            self.clery_order = clery_order
        if always_count_in_clery is not None:
            self.always_count_in_clery = always_count_in_clery
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def incident_sub_type_id(self):
        """Gets the incident_sub_type_id of this IncidentSubTypeItem.  # noqa: E501

        Incident Sub Type  # noqa: E501

        :return: The incident_sub_type_id of this IncidentSubTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_sub_type_id

    @incident_sub_type_id.setter
    def incident_sub_type_id(self, incident_sub_type_id):
        """Sets the incident_sub_type_id of this IncidentSubTypeItem.

        Incident Sub Type  # noqa: E501

        :param incident_sub_type_id: The incident_sub_type_id of this IncidentSubTypeItem.  # noqa: E501
        :type: int
        """

        self._incident_sub_type_id = incident_sub_type_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this IncidentSubTypeItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this IncidentSubTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this IncidentSubTypeItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this IncidentSubTypeItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def incident_type_id(self):
        """Gets the incident_type_id of this IncidentSubTypeItem.  # noqa: E501

        Incident Type  # noqa: E501

        :return: The incident_type_id of this IncidentSubTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_type_id

    @incident_type_id.setter
    def incident_type_id(self, incident_type_id):
        """Sets the incident_type_id of this IncidentSubTypeItem.

        Incident Type  # noqa: E501

        :param incident_type_id: The incident_type_id of this IncidentSubTypeItem.  # noqa: E501
        :type: int
        """

        self._incident_type_id = incident_type_id

    @property
    def incident_severity_id(self):
        """Gets the incident_severity_id of this IncidentSubTypeItem.  # noqa: E501

        Incident Severity  # noqa: E501

        :return: The incident_severity_id of this IncidentSubTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_severity_id

    @incident_severity_id.setter
    def incident_severity_id(self, incident_severity_id):
        """Sets the incident_severity_id of this IncidentSubTypeItem.

        Incident Severity  # noqa: E501

        :param incident_severity_id: The incident_severity_id of this IncidentSubTypeItem.  # noqa: E501
        :type: int
        """

        self._incident_severity_id = incident_severity_id

    @property
    def description(self):
        """Gets the description of this IncidentSubTypeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this IncidentSubTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IncidentSubTypeItem.

        Description  # noqa: E501

        :param description: The description of this IncidentSubTypeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def comments(self):
        """Gets the comments of this IncidentSubTypeItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this IncidentSubTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this IncidentSubTypeItem.

        Comments  # noqa: E501

        :param comments: The comments of this IncidentSubTypeItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 1000:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `1000`")  # noqa: E501

        self._comments = comments

    @property
    def clery(self):
        """Gets the clery of this IncidentSubTypeItem.  # noqa: E501

        Clery  # noqa: E501

        :return: The clery of this IncidentSubTypeItem.  # noqa: E501
        :rtype: bool
        """
        return self._clery

    @clery.setter
    def clery(self, clery):
        """Sets the clery of this IncidentSubTypeItem.

        Clery  # noqa: E501

        :param clery: The clery of this IncidentSubTypeItem.  # noqa: E501
        :type: bool
        """

        self._clery = clery

    @property
    def clery_order(self):
        """Gets the clery_order of this IncidentSubTypeItem.  # noqa: E501

        Clery Order  # noqa: E501

        :return: The clery_order of this IncidentSubTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._clery_order

    @clery_order.setter
    def clery_order(self, clery_order):
        """Sets the clery_order of this IncidentSubTypeItem.

        Clery Order  # noqa: E501

        :param clery_order: The clery_order of this IncidentSubTypeItem.  # noqa: E501
        :type: int
        """

        self._clery_order = clery_order

    @property
    def always_count_in_clery(self):
        """Gets the always_count_in_clery of this IncidentSubTypeItem.  # noqa: E501

        Always Count In Clery  # noqa: E501

        :return: The always_count_in_clery of this IncidentSubTypeItem.  # noqa: E501
        :rtype: bool
        """
        return self._always_count_in_clery

    @always_count_in_clery.setter
    def always_count_in_clery(self, always_count_in_clery):
        """Sets the always_count_in_clery of this IncidentSubTypeItem.

        Always Count In Clery  # noqa: E501

        :param always_count_in_clery: The always_count_in_clery of this IncidentSubTypeItem.  # noqa: E501
        :type: bool
        """

        self._always_count_in_clery = always_count_in_clery

    @property
    def date_modified(self):
        """Gets the date_modified of this IncidentSubTypeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this IncidentSubTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this IncidentSubTypeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this IncidentSubTypeItem.  # noqa: E501
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
        if not isinstance(other, IncidentSubTypeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
