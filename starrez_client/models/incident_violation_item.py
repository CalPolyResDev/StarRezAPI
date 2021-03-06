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


class IncidentViolationItem(object):
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
        'incident_violation_id': 'int',
        'incident_id': 'int',
        'incident_type_id': 'int',
        'incident_sub_type_id': 'int',
        'incident_severity_id': 'int',
        'clery': 'bool',
        'date_modified': 'str'
    }

    attribute_map = {
        'incident_violation_id': 'IncidentViolationID',
        'incident_id': 'IncidentID',
        'incident_type_id': 'IncidentTypeID',
        'incident_sub_type_id': 'IncidentSubTypeID',
        'incident_severity_id': 'IncidentSeverityID',
        'clery': 'Clery',
        'date_modified': 'DateModified'
    }

    def __init__(self, incident_violation_id=None, incident_id=None, incident_type_id=None, incident_sub_type_id=None, incident_severity_id=None, clery=None, date_modified=None):  # noqa: E501
        """IncidentViolationItem - a model defined in Swagger"""  # noqa: E501

        self._incident_violation_id = None
        self._incident_id = None
        self._incident_type_id = None
        self._incident_sub_type_id = None
        self._incident_severity_id = None
        self._clery = None
        self._date_modified = None
        self.discriminator = None

        if incident_violation_id is not None:
            self.incident_violation_id = incident_violation_id
        if incident_id is not None:
            self.incident_id = incident_id
        if incident_type_id is not None:
            self.incident_type_id = incident_type_id
        if incident_sub_type_id is not None:
            self.incident_sub_type_id = incident_sub_type_id
        if incident_severity_id is not None:
            self.incident_severity_id = incident_severity_id
        if clery is not None:
            self.clery = clery
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def incident_violation_id(self):
        """Gets the incident_violation_id of this IncidentViolationItem.  # noqa: E501

        Incident Violation  # noqa: E501

        :return: The incident_violation_id of this IncidentViolationItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_violation_id

    @incident_violation_id.setter
    def incident_violation_id(self, incident_violation_id):
        """Sets the incident_violation_id of this IncidentViolationItem.

        Incident Violation  # noqa: E501

        :param incident_violation_id: The incident_violation_id of this IncidentViolationItem.  # noqa: E501
        :type: int
        """

        self._incident_violation_id = incident_violation_id

    @property
    def incident_id(self):
        """Gets the incident_id of this IncidentViolationItem.  # noqa: E501

        Incident  # noqa: E501

        :return: The incident_id of this IncidentViolationItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this IncidentViolationItem.

        Incident  # noqa: E501

        :param incident_id: The incident_id of this IncidentViolationItem.  # noqa: E501
        :type: int
        """

        self._incident_id = incident_id

    @property
    def incident_type_id(self):
        """Gets the incident_type_id of this IncidentViolationItem.  # noqa: E501

        Incident Type  # noqa: E501

        :return: The incident_type_id of this IncidentViolationItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_type_id

    @incident_type_id.setter
    def incident_type_id(self, incident_type_id):
        """Sets the incident_type_id of this IncidentViolationItem.

        Incident Type  # noqa: E501

        :param incident_type_id: The incident_type_id of this IncidentViolationItem.  # noqa: E501
        :type: int
        """

        self._incident_type_id = incident_type_id

    @property
    def incident_sub_type_id(self):
        """Gets the incident_sub_type_id of this IncidentViolationItem.  # noqa: E501

        Incident Sub Type  # noqa: E501

        :return: The incident_sub_type_id of this IncidentViolationItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_sub_type_id

    @incident_sub_type_id.setter
    def incident_sub_type_id(self, incident_sub_type_id):
        """Sets the incident_sub_type_id of this IncidentViolationItem.

        Incident Sub Type  # noqa: E501

        :param incident_sub_type_id: The incident_sub_type_id of this IncidentViolationItem.  # noqa: E501
        :type: int
        """

        self._incident_sub_type_id = incident_sub_type_id

    @property
    def incident_severity_id(self):
        """Gets the incident_severity_id of this IncidentViolationItem.  # noqa: E501

        Incident Severity  # noqa: E501

        :return: The incident_severity_id of this IncidentViolationItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_severity_id

    @incident_severity_id.setter
    def incident_severity_id(self, incident_severity_id):
        """Sets the incident_severity_id of this IncidentViolationItem.

        Incident Severity  # noqa: E501

        :param incident_severity_id: The incident_severity_id of this IncidentViolationItem.  # noqa: E501
        :type: int
        """

        self._incident_severity_id = incident_severity_id

    @property
    def clery(self):
        """Gets the clery of this IncidentViolationItem.  # noqa: E501

        Clery  # noqa: E501

        :return: The clery of this IncidentViolationItem.  # noqa: E501
        :rtype: bool
        """
        return self._clery

    @clery.setter
    def clery(self, clery):
        """Sets the clery of this IncidentViolationItem.

        Clery  # noqa: E501

        :param clery: The clery of this IncidentViolationItem.  # noqa: E501
        :type: bool
        """

        self._clery = clery

    @property
    def date_modified(self):
        """Gets the date_modified of this IncidentViolationItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this IncidentViolationItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this IncidentViolationItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this IncidentViolationItem.  # noqa: E501
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
        if not isinstance(other, IncidentViolationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
