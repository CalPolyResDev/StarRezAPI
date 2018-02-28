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


class IncidentActionItem(object):
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
        'incident_action_id': 'int',
        'incident_id': 'int',
        'incident_action_type_id': 'int',
        'incident_action_date': 'datetime',
        'action_title': 'str',
        'action_manager_entry_id': 'int',
        'attendees': 'str',
        'location': 'str',
        'description': 'str',
        'comments': 'str',
        'date_due': 'str',
        'date_complete': 'str',
        'outcome': 'str',
        'incident_action_guid': 'str',
        'security_user_id': 'int',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'incident_action_id': 'IncidentActionID',
        'incident_id': 'IncidentID',
        'incident_action_type_id': 'IncidentActionTypeID',
        'incident_action_date': 'IncidentActionDate',
        'action_title': 'ActionTitle',
        'action_manager_entry_id': 'ActionManager_EntryID',
        'attendees': 'Attendees',
        'location': 'Location',
        'description': 'Description',
        'comments': 'Comments',
        'date_due': 'DateDue',
        'date_complete': 'DateComplete',
        'outcome': 'Outcome',
        'incident_action_guid': 'IncidentActionGUID',
        'security_user_id': 'SecurityUserID',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, incident_action_id=None, incident_id=None, incident_action_type_id=None, incident_action_date=None, action_title=None, action_manager_entry_id=None, attendees=None, location=None, description=None, comments=None, date_due=None, date_complete=None, outcome=None, incident_action_guid=None, security_user_id=None, date_created=None, date_modified=None):  # noqa: E501
        """IncidentActionItem - a model defined in Swagger"""  # noqa: E501

        self._incident_action_id = None
        self._incident_id = None
        self._incident_action_type_id = None
        self._incident_action_date = None
        self._action_title = None
        self._action_manager_entry_id = None
        self._attendees = None
        self._location = None
        self._description = None
        self._comments = None
        self._date_due = None
        self._date_complete = None
        self._outcome = None
        self._incident_action_guid = None
        self._security_user_id = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if incident_action_id is not None:
            self.incident_action_id = incident_action_id
        if incident_id is not None:
            self.incident_id = incident_id
        if incident_action_type_id is not None:
            self.incident_action_type_id = incident_action_type_id
        if incident_action_date is not None:
            self.incident_action_date = incident_action_date
        if action_title is not None:
            self.action_title = action_title
        if action_manager_entry_id is not None:
            self.action_manager_entry_id = action_manager_entry_id
        if attendees is not None:
            self.attendees = attendees
        if location is not None:
            self.location = location
        if description is not None:
            self.description = description
        if comments is not None:
            self.comments = comments
        if date_due is not None:
            self.date_due = date_due
        if date_complete is not None:
            self.date_complete = date_complete
        if outcome is not None:
            self.outcome = outcome
        if incident_action_guid is not None:
            self.incident_action_guid = incident_action_guid
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def incident_action_id(self):
        """Gets the incident_action_id of this IncidentActionItem.  # noqa: E501

        Incident Action  # noqa: E501

        :return: The incident_action_id of this IncidentActionItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_action_id

    @incident_action_id.setter
    def incident_action_id(self, incident_action_id):
        """Sets the incident_action_id of this IncidentActionItem.

        Incident Action  # noqa: E501

        :param incident_action_id: The incident_action_id of this IncidentActionItem.  # noqa: E501
        :type: int
        """

        self._incident_action_id = incident_action_id

    @property
    def incident_id(self):
        """Gets the incident_id of this IncidentActionItem.  # noqa: E501

        Incident  # noqa: E501

        :return: The incident_id of this IncidentActionItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this IncidentActionItem.

        Incident  # noqa: E501

        :param incident_id: The incident_id of this IncidentActionItem.  # noqa: E501
        :type: int
        """

        self._incident_id = incident_id

    @property
    def incident_action_type_id(self):
        """Gets the incident_action_type_id of this IncidentActionItem.  # noqa: E501

        Incident Action Type  # noqa: E501

        :return: The incident_action_type_id of this IncidentActionItem.  # noqa: E501
        :rtype: int
        """
        return self._incident_action_type_id

    @incident_action_type_id.setter
    def incident_action_type_id(self, incident_action_type_id):
        """Sets the incident_action_type_id of this IncidentActionItem.

        Incident Action Type  # noqa: E501

        :param incident_action_type_id: The incident_action_type_id of this IncidentActionItem.  # noqa: E501
        :type: int
        """

        self._incident_action_type_id = incident_action_type_id

    @property
    def incident_action_date(self):
        """Gets the incident_action_date of this IncidentActionItem.  # noqa: E501

        Incident Action Date  # noqa: E501

        :return: The incident_action_date of this IncidentActionItem.  # noqa: E501
        :rtype: datetime
        """
        return self._incident_action_date

    @incident_action_date.setter
    def incident_action_date(self, incident_action_date):
        """Sets the incident_action_date of this IncidentActionItem.

        Incident Action Date  # noqa: E501

        :param incident_action_date: The incident_action_date of this IncidentActionItem.  # noqa: E501
        :type: datetime
        """

        self._incident_action_date = incident_action_date

    @property
    def action_title(self):
        """Gets the action_title of this IncidentActionItem.  # noqa: E501

        Action Title  # noqa: E501

        :return: The action_title of this IncidentActionItem.  # noqa: E501
        :rtype: str
        """
        return self._action_title

    @action_title.setter
    def action_title(self, action_title):
        """Sets the action_title of this IncidentActionItem.

        Action Title  # noqa: E501

        :param action_title: The action_title of this IncidentActionItem.  # noqa: E501
        :type: str
        """
        if action_title is not None and len(action_title) > 100:
            raise ValueError("Invalid value for `action_title`, length must be less than or equal to `100`")  # noqa: E501

        self._action_title = action_title

    @property
    def action_manager_entry_id(self):
        """Gets the action_manager_entry_id of this IncidentActionItem.  # noqa: E501

        Action Manager Entry  # noqa: E501

        :return: The action_manager_entry_id of this IncidentActionItem.  # noqa: E501
        :rtype: int
        """
        return self._action_manager_entry_id

    @action_manager_entry_id.setter
    def action_manager_entry_id(self, action_manager_entry_id):
        """Sets the action_manager_entry_id of this IncidentActionItem.

        Action Manager Entry  # noqa: E501

        :param action_manager_entry_id: The action_manager_entry_id of this IncidentActionItem.  # noqa: E501
        :type: int
        """

        self._action_manager_entry_id = action_manager_entry_id

    @property
    def attendees(self):
        """Gets the attendees of this IncidentActionItem.  # noqa: E501

        Attendees  # noqa: E501

        :return: The attendees of this IncidentActionItem.  # noqa: E501
        :rtype: str
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        """Sets the attendees of this IncidentActionItem.

        Attendees  # noqa: E501

        :param attendees: The attendees of this IncidentActionItem.  # noqa: E501
        :type: str
        """
        if attendees is not None and len(attendees) > 100:
            raise ValueError("Invalid value for `attendees`, length must be less than or equal to `100`")  # noqa: E501

        self._attendees = attendees

    @property
    def location(self):
        """Gets the location of this IncidentActionItem.  # noqa: E501

        Location  # noqa: E501

        :return: The location of this IncidentActionItem.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this IncidentActionItem.

        Location  # noqa: E501

        :param location: The location of this IncidentActionItem.  # noqa: E501
        :type: str
        """
        if location is not None and len(location) > 100:
            raise ValueError("Invalid value for `location`, length must be less than or equal to `100`")  # noqa: E501

        self._location = location

    @property
    def description(self):
        """Gets the description of this IncidentActionItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this IncidentActionItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IncidentActionItem.

        Description  # noqa: E501

        :param description: The description of this IncidentActionItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 5000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `5000`")  # noqa: E501

        self._description = description

    @property
    def comments(self):
        """Gets the comments of this IncidentActionItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this IncidentActionItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this IncidentActionItem.

        Comments  # noqa: E501

        :param comments: The comments of this IncidentActionItem.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def date_due(self):
        """Gets the date_due of this IncidentActionItem.  # noqa: E501

        Date Due  # noqa: E501

        :return: The date_due of this IncidentActionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_due

    @date_due.setter
    def date_due(self, date_due):
        """Sets the date_due of this IncidentActionItem.

        Date Due  # noqa: E501

        :param date_due: The date_due of this IncidentActionItem.  # noqa: E501
        :type: str
        """

        self._date_due = date_due

    @property
    def date_complete(self):
        """Gets the date_complete of this IncidentActionItem.  # noqa: E501

        Date Complete  # noqa: E501

        :return: The date_complete of this IncidentActionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_complete

    @date_complete.setter
    def date_complete(self, date_complete):
        """Sets the date_complete of this IncidentActionItem.

        Date Complete  # noqa: E501

        :param date_complete: The date_complete of this IncidentActionItem.  # noqa: E501
        :type: str
        """

        self._date_complete = date_complete

    @property
    def outcome(self):
        """Gets the outcome of this IncidentActionItem.  # noqa: E501

        Outcome  # noqa: E501

        :return: The outcome of this IncidentActionItem.  # noqa: E501
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this IncidentActionItem.

        Outcome  # noqa: E501

        :param outcome: The outcome of this IncidentActionItem.  # noqa: E501
        :type: str
        """

        self._outcome = outcome

    @property
    def incident_action_guid(self):
        """Gets the incident_action_guid of this IncidentActionItem.  # noqa: E501

        Incident Action GUID  # noqa: E501

        :return: The incident_action_guid of this IncidentActionItem.  # noqa: E501
        :rtype: str
        """
        return self._incident_action_guid

    @incident_action_guid.setter
    def incident_action_guid(self, incident_action_guid):
        """Sets the incident_action_guid of this IncidentActionItem.

        Incident Action GUID  # noqa: E501

        :param incident_action_guid: The incident_action_guid of this IncidentActionItem.  # noqa: E501
        :type: str
        """

        self._incident_action_guid = incident_action_guid

    @property
    def security_user_id(self):
        """Gets the security_user_id of this IncidentActionItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this IncidentActionItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this IncidentActionItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this IncidentActionItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this IncidentActionItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this IncidentActionItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this IncidentActionItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this IncidentActionItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this IncidentActionItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this IncidentActionItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this IncidentActionItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this IncidentActionItem.  # noqa: E501
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
        if not isinstance(other, IncidentActionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
