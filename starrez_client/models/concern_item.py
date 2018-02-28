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


class ConcernItem(object):
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
        'concern_id': 'int',
        'category_id': 'int',
        'concern_date': 'datetime',
        'room_location_id': 'int',
        'description': 'str',
        'location_comments': 'str',
        'concern_type_id': 'int',
        'concern_sub_type_id': 'int',
        'report_number': 'str',
        'comments': 'str',
        'resolution': 'str',
        'workflow_step_id': 'int',
        'assigned_to_security_user_id': 'int',
        'current_workflow_history_id': 'int',
        'previous_workflow_history_id': 'int',
        'date_created': 'datetime',
        'security_user_id': 'int',
        'created_by_security_user_id': 'int',
        'reported_by_name': 'str',
        'reported_by_email': 'str',
        'reported_by_phone': 'str',
        'reported_by_relationship': 'str',
        'reported_by_contact': 'bool',
        'date_modified': 'str'
    }

    attribute_map = {
        'concern_id': 'ConcernID',
        'category_id': 'CategoryID',
        'concern_date': 'ConcernDate',
        'room_location_id': 'RoomLocationID',
        'description': 'Description',
        'location_comments': 'LocationComments',
        'concern_type_id': 'ConcernTypeID',
        'concern_sub_type_id': 'ConcernSubTypeID',
        'report_number': 'ReportNumber',
        'comments': 'Comments',
        'resolution': 'Resolution',
        'workflow_step_id': 'WorkflowStepID',
        'assigned_to_security_user_id': 'AssignedTo_SecurityUserID',
        'current_workflow_history_id': 'Current_WorkflowHistoryID',
        'previous_workflow_history_id': 'Previous_WorkflowHistoryID',
        'date_created': 'DateCreated',
        'security_user_id': 'SecurityUserID',
        'created_by_security_user_id': 'CreatedBy_SecurityUserID',
        'reported_by_name': 'ReportedByName',
        'reported_by_email': 'ReportedByEmail',
        'reported_by_phone': 'ReportedByPhone',
        'reported_by_relationship': 'ReportedByRelationship',
        'reported_by_contact': 'ReportedByContact',
        'date_modified': 'DateModified'
    }

    def __init__(self, concern_id=None, category_id=None, concern_date=None, room_location_id=None, description=None, location_comments=None, concern_type_id=None, concern_sub_type_id=None, report_number=None, comments=None, resolution=None, workflow_step_id=None, assigned_to_security_user_id=None, current_workflow_history_id=None, previous_workflow_history_id=None, date_created=None, security_user_id=None, created_by_security_user_id=None, reported_by_name=None, reported_by_email=None, reported_by_phone=None, reported_by_relationship=None, reported_by_contact=None, date_modified=None):  # noqa: E501
        """ConcernItem - a model defined in Swagger"""  # noqa: E501

        self._concern_id = None
        self._category_id = None
        self._concern_date = None
        self._room_location_id = None
        self._description = None
        self._location_comments = None
        self._concern_type_id = None
        self._concern_sub_type_id = None
        self._report_number = None
        self._comments = None
        self._resolution = None
        self._workflow_step_id = None
        self._assigned_to_security_user_id = None
        self._current_workflow_history_id = None
        self._previous_workflow_history_id = None
        self._date_created = None
        self._security_user_id = None
        self._created_by_security_user_id = None
        self._reported_by_name = None
        self._reported_by_email = None
        self._reported_by_phone = None
        self._reported_by_relationship = None
        self._reported_by_contact = None
        self._date_modified = None
        self.discriminator = None

        if concern_id is not None:
            self.concern_id = concern_id
        if category_id is not None:
            self.category_id = category_id
        if concern_date is not None:
            self.concern_date = concern_date
        if room_location_id is not None:
            self.room_location_id = room_location_id
        if description is not None:
            self.description = description
        if location_comments is not None:
            self.location_comments = location_comments
        if concern_type_id is not None:
            self.concern_type_id = concern_type_id
        if concern_sub_type_id is not None:
            self.concern_sub_type_id = concern_sub_type_id
        if report_number is not None:
            self.report_number = report_number
        if comments is not None:
            self.comments = comments
        if resolution is not None:
            self.resolution = resolution
        if workflow_step_id is not None:
            self.workflow_step_id = workflow_step_id
        if assigned_to_security_user_id is not None:
            self.assigned_to_security_user_id = assigned_to_security_user_id
        if current_workflow_history_id is not None:
            self.current_workflow_history_id = current_workflow_history_id
        if previous_workflow_history_id is not None:
            self.previous_workflow_history_id = previous_workflow_history_id
        if date_created is not None:
            self.date_created = date_created
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if created_by_security_user_id is not None:
            self.created_by_security_user_id = created_by_security_user_id
        if reported_by_name is not None:
            self.reported_by_name = reported_by_name
        if reported_by_email is not None:
            self.reported_by_email = reported_by_email
        if reported_by_phone is not None:
            self.reported_by_phone = reported_by_phone
        if reported_by_relationship is not None:
            self.reported_by_relationship = reported_by_relationship
        if reported_by_contact is not None:
            self.reported_by_contact = reported_by_contact
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def concern_id(self):
        """Gets the concern_id of this ConcernItem.  # noqa: E501

        Concern  # noqa: E501

        :return: The concern_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._concern_id

    @concern_id.setter
    def concern_id(self, concern_id):
        """Sets the concern_id of this ConcernItem.

        Concern  # noqa: E501

        :param concern_id: The concern_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._concern_id = concern_id

    @property
    def category_id(self):
        """Gets the category_id of this ConcernItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this ConcernItem.

        Category  # noqa: E501

        :param category_id: The category_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def concern_date(self):
        """Gets the concern_date of this ConcernItem.  # noqa: E501

        Concern Date  # noqa: E501

        :return: The concern_date of this ConcernItem.  # noqa: E501
        :rtype: datetime
        """
        return self._concern_date

    @concern_date.setter
    def concern_date(self, concern_date):
        """Sets the concern_date of this ConcernItem.

        Concern Date  # noqa: E501

        :param concern_date: The concern_date of this ConcernItem.  # noqa: E501
        :type: datetime
        """

        self._concern_date = concern_date

    @property
    def room_location_id(self):
        """Gets the room_location_id of this ConcernItem.  # noqa: E501

        Room Location  # noqa: E501

        :return: The room_location_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._room_location_id

    @room_location_id.setter
    def room_location_id(self, room_location_id):
        """Sets the room_location_id of this ConcernItem.

        Room Location  # noqa: E501

        :param room_location_id: The room_location_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._room_location_id = room_location_id

    @property
    def description(self):
        """Gets the description of this ConcernItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this ConcernItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConcernItem.

        Description  # noqa: E501

        :param description: The description of this ConcernItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def location_comments(self):
        """Gets the location_comments of this ConcernItem.  # noqa: E501

        Location Comments  # noqa: E501

        :return: The location_comments of this ConcernItem.  # noqa: E501
        :rtype: str
        """
        return self._location_comments

    @location_comments.setter
    def location_comments(self, location_comments):
        """Sets the location_comments of this ConcernItem.

        Location Comments  # noqa: E501

        :param location_comments: The location_comments of this ConcernItem.  # noqa: E501
        :type: str
        """
        if location_comments is not None and len(location_comments) > 100:
            raise ValueError("Invalid value for `location_comments`, length must be less than or equal to `100`")  # noqa: E501

        self._location_comments = location_comments

    @property
    def concern_type_id(self):
        """Gets the concern_type_id of this ConcernItem.  # noqa: E501

        Concern Type  # noqa: E501

        :return: The concern_type_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._concern_type_id

    @concern_type_id.setter
    def concern_type_id(self, concern_type_id):
        """Sets the concern_type_id of this ConcernItem.

        Concern Type  # noqa: E501

        :param concern_type_id: The concern_type_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._concern_type_id = concern_type_id

    @property
    def concern_sub_type_id(self):
        """Gets the concern_sub_type_id of this ConcernItem.  # noqa: E501

        Concern Sub Type  # noqa: E501

        :return: The concern_sub_type_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._concern_sub_type_id

    @concern_sub_type_id.setter
    def concern_sub_type_id(self, concern_sub_type_id):
        """Sets the concern_sub_type_id of this ConcernItem.

        Concern Sub Type  # noqa: E501

        :param concern_sub_type_id: The concern_sub_type_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._concern_sub_type_id = concern_sub_type_id

    @property
    def report_number(self):
        """Gets the report_number of this ConcernItem.  # noqa: E501

        Report Number  # noqa: E501

        :return: The report_number of this ConcernItem.  # noqa: E501
        :rtype: str
        """
        return self._report_number

    @report_number.setter
    def report_number(self, report_number):
        """Sets the report_number of this ConcernItem.

        Report Number  # noqa: E501

        :param report_number: The report_number of this ConcernItem.  # noqa: E501
        :type: str
        """
        if report_number is not None and len(report_number) > 50:
            raise ValueError("Invalid value for `report_number`, length must be less than or equal to `50`")  # noqa: E501

        self._report_number = report_number

    @property
    def comments(self):
        """Gets the comments of this ConcernItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this ConcernItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ConcernItem.

        Comments  # noqa: E501

        :param comments: The comments of this ConcernItem.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def resolution(self):
        """Gets the resolution of this ConcernItem.  # noqa: E501

        Resolution  # noqa: E501

        :return: The resolution of this ConcernItem.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ConcernItem.

        Resolution  # noqa: E501

        :param resolution: The resolution of this ConcernItem.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

    @property
    def workflow_step_id(self):
        """Gets the workflow_step_id of this ConcernItem.  # noqa: E501

        Workflow Step  # noqa: E501

        :return: The workflow_step_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._workflow_step_id

    @workflow_step_id.setter
    def workflow_step_id(self, workflow_step_id):
        """Sets the workflow_step_id of this ConcernItem.

        Workflow Step  # noqa: E501

        :param workflow_step_id: The workflow_step_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._workflow_step_id = workflow_step_id

    @property
    def assigned_to_security_user_id(self):
        """Gets the assigned_to_security_user_id of this ConcernItem.  # noqa: E501

        Assigned To Security User  # noqa: E501

        :return: The assigned_to_security_user_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_security_user_id

    @assigned_to_security_user_id.setter
    def assigned_to_security_user_id(self, assigned_to_security_user_id):
        """Sets the assigned_to_security_user_id of this ConcernItem.

        Assigned To Security User  # noqa: E501

        :param assigned_to_security_user_id: The assigned_to_security_user_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._assigned_to_security_user_id = assigned_to_security_user_id

    @property
    def current_workflow_history_id(self):
        """Gets the current_workflow_history_id of this ConcernItem.  # noqa: E501

        Current Workflow History  # noqa: E501

        :return: The current_workflow_history_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._current_workflow_history_id

    @current_workflow_history_id.setter
    def current_workflow_history_id(self, current_workflow_history_id):
        """Sets the current_workflow_history_id of this ConcernItem.

        Current Workflow History  # noqa: E501

        :param current_workflow_history_id: The current_workflow_history_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._current_workflow_history_id = current_workflow_history_id

    @property
    def previous_workflow_history_id(self):
        """Gets the previous_workflow_history_id of this ConcernItem.  # noqa: E501

        Previous Workflow History  # noqa: E501

        :return: The previous_workflow_history_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._previous_workflow_history_id

    @previous_workflow_history_id.setter
    def previous_workflow_history_id(self, previous_workflow_history_id):
        """Sets the previous_workflow_history_id of this ConcernItem.

        Previous Workflow History  # noqa: E501

        :param previous_workflow_history_id: The previous_workflow_history_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._previous_workflow_history_id = previous_workflow_history_id

    @property
    def date_created(self):
        """Gets the date_created of this ConcernItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this ConcernItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ConcernItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this ConcernItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def security_user_id(self):
        """Gets the security_user_id of this ConcernItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this ConcernItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def created_by_security_user_id(self):
        """Gets the created_by_security_user_id of this ConcernItem.  # noqa: E501

        Created By Security User  # noqa: E501

        :return: The created_by_security_user_id of this ConcernItem.  # noqa: E501
        :rtype: int
        """
        return self._created_by_security_user_id

    @created_by_security_user_id.setter
    def created_by_security_user_id(self, created_by_security_user_id):
        """Sets the created_by_security_user_id of this ConcernItem.

        Created By Security User  # noqa: E501

        :param created_by_security_user_id: The created_by_security_user_id of this ConcernItem.  # noqa: E501
        :type: int
        """

        self._created_by_security_user_id = created_by_security_user_id

    @property
    def reported_by_name(self):
        """Gets the reported_by_name of this ConcernItem.  # noqa: E501

        Reported By Name  # noqa: E501

        :return: The reported_by_name of this ConcernItem.  # noqa: E501
        :rtype: str
        """
        return self._reported_by_name

    @reported_by_name.setter
    def reported_by_name(self, reported_by_name):
        """Sets the reported_by_name of this ConcernItem.

        Reported By Name  # noqa: E501

        :param reported_by_name: The reported_by_name of this ConcernItem.  # noqa: E501
        :type: str
        """
        if reported_by_name is not None and len(reported_by_name) > 50:
            raise ValueError("Invalid value for `reported_by_name`, length must be less than or equal to `50`")  # noqa: E501

        self._reported_by_name = reported_by_name

    @property
    def reported_by_email(self):
        """Gets the reported_by_email of this ConcernItem.  # noqa: E501

        Reported By Email  # noqa: E501

        :return: The reported_by_email of this ConcernItem.  # noqa: E501
        :rtype: str
        """
        return self._reported_by_email

    @reported_by_email.setter
    def reported_by_email(self, reported_by_email):
        """Sets the reported_by_email of this ConcernItem.

        Reported By Email  # noqa: E501

        :param reported_by_email: The reported_by_email of this ConcernItem.  # noqa: E501
        :type: str
        """
        if reported_by_email is not None and len(reported_by_email) > 255:
            raise ValueError("Invalid value for `reported_by_email`, length must be less than or equal to `255`")  # noqa: E501

        self._reported_by_email = reported_by_email

    @property
    def reported_by_phone(self):
        """Gets the reported_by_phone of this ConcernItem.  # noqa: E501

        Reported By Phone  # noqa: E501

        :return: The reported_by_phone of this ConcernItem.  # noqa: E501
        :rtype: str
        """
        return self._reported_by_phone

    @reported_by_phone.setter
    def reported_by_phone(self, reported_by_phone):
        """Sets the reported_by_phone of this ConcernItem.

        Reported By Phone  # noqa: E501

        :param reported_by_phone: The reported_by_phone of this ConcernItem.  # noqa: E501
        :type: str
        """
        if reported_by_phone is not None and len(reported_by_phone) > 20:
            raise ValueError("Invalid value for `reported_by_phone`, length must be less than or equal to `20`")  # noqa: E501

        self._reported_by_phone = reported_by_phone

    @property
    def reported_by_relationship(self):
        """Gets the reported_by_relationship of this ConcernItem.  # noqa: E501

        Reported By Relationship  # noqa: E501

        :return: The reported_by_relationship of this ConcernItem.  # noqa: E501
        :rtype: str
        """
        return self._reported_by_relationship

    @reported_by_relationship.setter
    def reported_by_relationship(self, reported_by_relationship):
        """Sets the reported_by_relationship of this ConcernItem.

        Reported By Relationship  # noqa: E501

        :param reported_by_relationship: The reported_by_relationship of this ConcernItem.  # noqa: E501
        :type: str
        """
        if reported_by_relationship is not None and len(reported_by_relationship) > 50:
            raise ValueError("Invalid value for `reported_by_relationship`, length must be less than or equal to `50`")  # noqa: E501

        self._reported_by_relationship = reported_by_relationship

    @property
    def reported_by_contact(self):
        """Gets the reported_by_contact of this ConcernItem.  # noqa: E501

        Reported By Contact  # noqa: E501

        :return: The reported_by_contact of this ConcernItem.  # noqa: E501
        :rtype: bool
        """
        return self._reported_by_contact

    @reported_by_contact.setter
    def reported_by_contact(self, reported_by_contact):
        """Sets the reported_by_contact of this ConcernItem.

        Reported By Contact  # noqa: E501

        :param reported_by_contact: The reported_by_contact of this ConcernItem.  # noqa: E501
        :type: bool
        """

        self._reported_by_contact = reported_by_contact

    @property
    def date_modified(self):
        """Gets the date_modified of this ConcernItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this ConcernItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ConcernItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this ConcernItem.  # noqa: E501
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
        if not isinstance(other, ConcernItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other