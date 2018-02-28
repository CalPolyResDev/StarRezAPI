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


class ContributionEntryItem(object):
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
        'contribution_entry_id': 'int',
        'contribution_id': 'int',
        'entry_id': 'int',
        'involvement_type': 'str',
        'involvement_comments': 'str',
        'workflow_step_id': 'int',
        'assigned_to_security_user_id': 'int',
        'current_workflow_history_id': 'int',
        'previous_workflow_history_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'contribution_entry_id': 'ContributionEntryID',
        'contribution_id': 'ContributionID',
        'entry_id': 'EntryID',
        'involvement_type': 'InvolvementType',
        'involvement_comments': 'InvolvementComments',
        'workflow_step_id': 'WorkflowStepID',
        'assigned_to_security_user_id': 'AssignedTo_SecurityUserID',
        'current_workflow_history_id': 'Current_WorkflowHistoryID',
        'previous_workflow_history_id': 'Previous_WorkflowHistoryID',
        'date_modified': 'DateModified'
    }

    def __init__(self, contribution_entry_id=None, contribution_id=None, entry_id=None, involvement_type=None, involvement_comments=None, workflow_step_id=None, assigned_to_security_user_id=None, current_workflow_history_id=None, previous_workflow_history_id=None, date_modified=None):  # noqa: E501
        """ContributionEntryItem - a model defined in Swagger"""  # noqa: E501

        self._contribution_entry_id = None
        self._contribution_id = None
        self._entry_id = None
        self._involvement_type = None
        self._involvement_comments = None
        self._workflow_step_id = None
        self._assigned_to_security_user_id = None
        self._current_workflow_history_id = None
        self._previous_workflow_history_id = None
        self._date_modified = None
        self.discriminator = None

        if contribution_entry_id is not None:
            self.contribution_entry_id = contribution_entry_id
        if contribution_id is not None:
            self.contribution_id = contribution_id
        if entry_id is not None:
            self.entry_id = entry_id
        if involvement_type is not None:
            self.involvement_type = involvement_type
        if involvement_comments is not None:
            self.involvement_comments = involvement_comments
        if workflow_step_id is not None:
            self.workflow_step_id = workflow_step_id
        if assigned_to_security_user_id is not None:
            self.assigned_to_security_user_id = assigned_to_security_user_id
        if current_workflow_history_id is not None:
            self.current_workflow_history_id = current_workflow_history_id
        if previous_workflow_history_id is not None:
            self.previous_workflow_history_id = previous_workflow_history_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def contribution_entry_id(self):
        """Gets the contribution_entry_id of this ContributionEntryItem.  # noqa: E501

        Contribution Entry  # noqa: E501

        :return: The contribution_entry_id of this ContributionEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._contribution_entry_id

    @contribution_entry_id.setter
    def contribution_entry_id(self, contribution_entry_id):
        """Sets the contribution_entry_id of this ContributionEntryItem.

        Contribution Entry  # noqa: E501

        :param contribution_entry_id: The contribution_entry_id of this ContributionEntryItem.  # noqa: E501
        :type: int
        """

        self._contribution_entry_id = contribution_entry_id

    @property
    def contribution_id(self):
        """Gets the contribution_id of this ContributionEntryItem.  # noqa: E501

        Contribution  # noqa: E501

        :return: The contribution_id of this ContributionEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._contribution_id

    @contribution_id.setter
    def contribution_id(self, contribution_id):
        """Sets the contribution_id of this ContributionEntryItem.

        Contribution  # noqa: E501

        :param contribution_id: The contribution_id of this ContributionEntryItem.  # noqa: E501
        :type: int
        """

        self._contribution_id = contribution_id

    @property
    def entry_id(self):
        """Gets the entry_id of this ContributionEntryItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this ContributionEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this ContributionEntryItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this ContributionEntryItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def involvement_type(self):
        """Gets the involvement_type of this ContributionEntryItem.  # noqa: E501

        Involvement Type  # noqa: E501

        :return: The involvement_type of this ContributionEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._involvement_type

    @involvement_type.setter
    def involvement_type(self, involvement_type):
        """Sets the involvement_type of this ContributionEntryItem.

        Involvement Type  # noqa: E501

        :param involvement_type: The involvement_type of this ContributionEntryItem.  # noqa: E501
        :type: str
        """
        if involvement_type is not None and len(involvement_type) > 50:
            raise ValueError("Invalid value for `involvement_type`, length must be less than or equal to `50`")  # noqa: E501

        self._involvement_type = involvement_type

    @property
    def involvement_comments(self):
        """Gets the involvement_comments of this ContributionEntryItem.  # noqa: E501

        Involvement Comments  # noqa: E501

        :return: The involvement_comments of this ContributionEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._involvement_comments

    @involvement_comments.setter
    def involvement_comments(self, involvement_comments):
        """Sets the involvement_comments of this ContributionEntryItem.

        Involvement Comments  # noqa: E501

        :param involvement_comments: The involvement_comments of this ContributionEntryItem.  # noqa: E501
        :type: str
        """

        self._involvement_comments = involvement_comments

    @property
    def workflow_step_id(self):
        """Gets the workflow_step_id of this ContributionEntryItem.  # noqa: E501

        Workflow Step  # noqa: E501

        :return: The workflow_step_id of this ContributionEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._workflow_step_id

    @workflow_step_id.setter
    def workflow_step_id(self, workflow_step_id):
        """Sets the workflow_step_id of this ContributionEntryItem.

        Workflow Step  # noqa: E501

        :param workflow_step_id: The workflow_step_id of this ContributionEntryItem.  # noqa: E501
        :type: int
        """

        self._workflow_step_id = workflow_step_id

    @property
    def assigned_to_security_user_id(self):
        """Gets the assigned_to_security_user_id of this ContributionEntryItem.  # noqa: E501

        Assigned To Security User  # noqa: E501

        :return: The assigned_to_security_user_id of this ContributionEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_security_user_id

    @assigned_to_security_user_id.setter
    def assigned_to_security_user_id(self, assigned_to_security_user_id):
        """Sets the assigned_to_security_user_id of this ContributionEntryItem.

        Assigned To Security User  # noqa: E501

        :param assigned_to_security_user_id: The assigned_to_security_user_id of this ContributionEntryItem.  # noqa: E501
        :type: int
        """

        self._assigned_to_security_user_id = assigned_to_security_user_id

    @property
    def current_workflow_history_id(self):
        """Gets the current_workflow_history_id of this ContributionEntryItem.  # noqa: E501

        Current Workflow History  # noqa: E501

        :return: The current_workflow_history_id of this ContributionEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._current_workflow_history_id

    @current_workflow_history_id.setter
    def current_workflow_history_id(self, current_workflow_history_id):
        """Sets the current_workflow_history_id of this ContributionEntryItem.

        Current Workflow History  # noqa: E501

        :param current_workflow_history_id: The current_workflow_history_id of this ContributionEntryItem.  # noqa: E501
        :type: int
        """

        self._current_workflow_history_id = current_workflow_history_id

    @property
    def previous_workflow_history_id(self):
        """Gets the previous_workflow_history_id of this ContributionEntryItem.  # noqa: E501

        Previous Workflow History  # noqa: E501

        :return: The previous_workflow_history_id of this ContributionEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._previous_workflow_history_id

    @previous_workflow_history_id.setter
    def previous_workflow_history_id(self, previous_workflow_history_id):
        """Sets the previous_workflow_history_id of this ContributionEntryItem.

        Previous Workflow History  # noqa: E501

        :param previous_workflow_history_id: The previous_workflow_history_id of this ContributionEntryItem.  # noqa: E501
        :type: int
        """

        self._previous_workflow_history_id = previous_workflow_history_id

    @property
    def date_modified(self):
        """Gets the date_modified of this ContributionEntryItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this ContributionEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ContributionEntryItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this ContributionEntryItem.  # noqa: E501
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
        if not isinstance(other, ContributionEntryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other