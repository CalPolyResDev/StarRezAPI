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


class WorkflowStepItem(object):
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
        'workflow_step_id': 'int',
        'workflow_id': 'int',
        'description': 'str',
        'step_order': 'int',
        'template_id': 'int',
        'security_user_id': 'int',
        'created_by_security_user_id': 'int',
        'comments': 'str',
        'date_created': 'datetime',
        'record_type_enum': 'str',
        'assign_to_option_enum': 'str',
        'assign_to_security_user_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'workflow_step_id': 'WorkflowStepID',
        'workflow_id': 'WorkflowID',
        'description': 'Description',
        'step_order': 'StepOrder',
        'template_id': 'TemplateID',
        'security_user_id': 'SecurityUserID',
        'created_by_security_user_id': 'CreatedBy_SecurityUserID',
        'comments': 'Comments',
        'date_created': 'DateCreated',
        'record_type_enum': 'RecordTypeEnum',
        'assign_to_option_enum': 'AssignToOptionEnum',
        'assign_to_security_user_id': 'AssignTo_SecurityUserID',
        'date_modified': 'DateModified'
    }

    def __init__(self, workflow_step_id=None, workflow_id=None, description=None, step_order=None, template_id=None, security_user_id=None, created_by_security_user_id=None, comments=None, date_created=None, record_type_enum=None, assign_to_option_enum=None, assign_to_security_user_id=None, date_modified=None):  # noqa: E501
        """WorkflowStepItem - a model defined in Swagger"""  # noqa: E501

        self._workflow_step_id = None
        self._workflow_id = None
        self._description = None
        self._step_order = None
        self._template_id = None
        self._security_user_id = None
        self._created_by_security_user_id = None
        self._comments = None
        self._date_created = None
        self._record_type_enum = None
        self._assign_to_option_enum = None
        self._assign_to_security_user_id = None
        self._date_modified = None
        self.discriminator = None

        if workflow_step_id is not None:
            self.workflow_step_id = workflow_step_id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if description is not None:
            self.description = description
        if step_order is not None:
            self.step_order = step_order
        if template_id is not None:
            self.template_id = template_id
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if created_by_security_user_id is not None:
            self.created_by_security_user_id = created_by_security_user_id
        if comments is not None:
            self.comments = comments
        if date_created is not None:
            self.date_created = date_created
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if assign_to_option_enum is not None:
            self.assign_to_option_enum = assign_to_option_enum
        if assign_to_security_user_id is not None:
            self.assign_to_security_user_id = assign_to_security_user_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def workflow_step_id(self):
        """Gets the workflow_step_id of this WorkflowStepItem.  # noqa: E501

        Workflow Step  # noqa: E501

        :return: The workflow_step_id of this WorkflowStepItem.  # noqa: E501
        :rtype: int
        """
        return self._workflow_step_id

    @workflow_step_id.setter
    def workflow_step_id(self, workflow_step_id):
        """Sets the workflow_step_id of this WorkflowStepItem.

        Workflow Step  # noqa: E501

        :param workflow_step_id: The workflow_step_id of this WorkflowStepItem.  # noqa: E501
        :type: int
        """

        self._workflow_step_id = workflow_step_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this WorkflowStepItem.  # noqa: E501

        Workflow  # noqa: E501

        :return: The workflow_id of this WorkflowStepItem.  # noqa: E501
        :rtype: int
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this WorkflowStepItem.

        Workflow  # noqa: E501

        :param workflow_id: The workflow_id of this WorkflowStepItem.  # noqa: E501
        :type: int
        """

        self._workflow_id = workflow_id

    @property
    def description(self):
        """Gets the description of this WorkflowStepItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this WorkflowStepItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowStepItem.

        Description  # noqa: E501

        :param description: The description of this WorkflowStepItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def step_order(self):
        """Gets the step_order of this WorkflowStepItem.  # noqa: E501

        Step Order  # noqa: E501

        :return: The step_order of this WorkflowStepItem.  # noqa: E501
        :rtype: int
        """
        return self._step_order

    @step_order.setter
    def step_order(self, step_order):
        """Sets the step_order of this WorkflowStepItem.

        Step Order  # noqa: E501

        :param step_order: The step_order of this WorkflowStepItem.  # noqa: E501
        :type: int
        """

        self._step_order = step_order

    @property
    def template_id(self):
        """Gets the template_id of this WorkflowStepItem.  # noqa: E501

        Template  # noqa: E501

        :return: The template_id of this WorkflowStepItem.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this WorkflowStepItem.

        Template  # noqa: E501

        :param template_id: The template_id of this WorkflowStepItem.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def security_user_id(self):
        """Gets the security_user_id of this WorkflowStepItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this WorkflowStepItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this WorkflowStepItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this WorkflowStepItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def created_by_security_user_id(self):
        """Gets the created_by_security_user_id of this WorkflowStepItem.  # noqa: E501

        Created By Security User  # noqa: E501

        :return: The created_by_security_user_id of this WorkflowStepItem.  # noqa: E501
        :rtype: int
        """
        return self._created_by_security_user_id

    @created_by_security_user_id.setter
    def created_by_security_user_id(self, created_by_security_user_id):
        """Sets the created_by_security_user_id of this WorkflowStepItem.

        Created By Security User  # noqa: E501

        :param created_by_security_user_id: The created_by_security_user_id of this WorkflowStepItem.  # noqa: E501
        :type: int
        """

        self._created_by_security_user_id = created_by_security_user_id

    @property
    def comments(self):
        """Gets the comments of this WorkflowStepItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this WorkflowStepItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this WorkflowStepItem.

        Comments  # noqa: E501

        :param comments: The comments of this WorkflowStepItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 1000:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `1000`")  # noqa: E501

        self._comments = comments

    @property
    def date_created(self):
        """Gets the date_created of this WorkflowStepItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this WorkflowStepItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this WorkflowStepItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this WorkflowStepItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this WorkflowStepItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this WorkflowStepItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this WorkflowStepItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this WorkflowStepItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def assign_to_option_enum(self):
        """Gets the assign_to_option_enum of this WorkflowStepItem.  # noqa: E501

        Assign To Option  # noqa: E501

        :return: The assign_to_option_enum of this WorkflowStepItem.  # noqa: E501
        :rtype: str
        """
        return self._assign_to_option_enum

    @assign_to_option_enum.setter
    def assign_to_option_enum(self, assign_to_option_enum):
        """Sets the assign_to_option_enum of this WorkflowStepItem.

        Assign To Option  # noqa: E501

        :param assign_to_option_enum: The assign_to_option_enum of this WorkflowStepItem.  # noqa: E501
        :type: str
        """

        self._assign_to_option_enum = assign_to_option_enum

    @property
    def assign_to_security_user_id(self):
        """Gets the assign_to_security_user_id of this WorkflowStepItem.  # noqa: E501

        Assign To Security User  # noqa: E501

        :return: The assign_to_security_user_id of this WorkflowStepItem.  # noqa: E501
        :rtype: int
        """
        return self._assign_to_security_user_id

    @assign_to_security_user_id.setter
    def assign_to_security_user_id(self, assign_to_security_user_id):
        """Sets the assign_to_security_user_id of this WorkflowStepItem.

        Assign To Security User  # noqa: E501

        :param assign_to_security_user_id: The assign_to_security_user_id of this WorkflowStepItem.  # noqa: E501
        :type: int
        """

        self._assign_to_security_user_id = assign_to_security_user_id

    @property
    def date_modified(self):
        """Gets the date_modified of this WorkflowStepItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this WorkflowStepItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this WorkflowStepItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this WorkflowStepItem.  # noqa: E501
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
        if not isinstance(other, WorkflowStepItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
