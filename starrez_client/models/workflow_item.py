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


class WorkflowItem(object):
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
        'workflow_id': 'int',
        'table_name': 'str',
        'description': 'str',
        'workflow_order': 'int',
        'date_created': 'datetime',
        'security_user_id': 'int',
        'created_by_security_user_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'workflow_id': 'WorkflowID',
        'table_name': 'TableName',
        'description': 'Description',
        'workflow_order': 'WorkflowOrder',
        'date_created': 'DateCreated',
        'security_user_id': 'SecurityUserID',
        'created_by_security_user_id': 'CreatedBy_SecurityUserID',
        'date_modified': 'DateModified'
    }

    def __init__(self, workflow_id=None, table_name=None, description=None, workflow_order=None, date_created=None, security_user_id=None, created_by_security_user_id=None, date_modified=None):  # noqa: E501
        """WorkflowItem - a model defined in Swagger"""  # noqa: E501

        self._workflow_id = None
        self._table_name = None
        self._description = None
        self._workflow_order = None
        self._date_created = None
        self._security_user_id = None
        self._created_by_security_user_id = None
        self._date_modified = None
        self.discriminator = None

        if workflow_id is not None:
            self.workflow_id = workflow_id
        if table_name is not None:
            self.table_name = table_name
        if description is not None:
            self.description = description
        if workflow_order is not None:
            self.workflow_order = workflow_order
        if date_created is not None:
            self.date_created = date_created
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if created_by_security_user_id is not None:
            self.created_by_security_user_id = created_by_security_user_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def workflow_id(self):
        """Gets the workflow_id of this WorkflowItem.  # noqa: E501

        Workflow  # noqa: E501

        :return: The workflow_id of this WorkflowItem.  # noqa: E501
        :rtype: int
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this WorkflowItem.

        Workflow  # noqa: E501

        :param workflow_id: The workflow_id of this WorkflowItem.  # noqa: E501
        :type: int
        """

        self._workflow_id = workflow_id

    @property
    def table_name(self):
        """Gets the table_name of this WorkflowItem.  # noqa: E501

        Table Name  # noqa: E501

        :return: The table_name of this WorkflowItem.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this WorkflowItem.

        Table Name  # noqa: E501

        :param table_name: The table_name of this WorkflowItem.  # noqa: E501
        :type: str
        """
        if table_name is not None and len(table_name) > 25:
            raise ValueError("Invalid value for `table_name`, length must be less than or equal to `25`")  # noqa: E501

        self._table_name = table_name

    @property
    def description(self):
        """Gets the description of this WorkflowItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this WorkflowItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowItem.

        Description  # noqa: E501

        :param description: The description of this WorkflowItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 50:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501

        self._description = description

    @property
    def workflow_order(self):
        """Gets the workflow_order of this WorkflowItem.  # noqa: E501

        Workflow Order  # noqa: E501

        :return: The workflow_order of this WorkflowItem.  # noqa: E501
        :rtype: int
        """
        return self._workflow_order

    @workflow_order.setter
    def workflow_order(self, workflow_order):
        """Sets the workflow_order of this WorkflowItem.

        Workflow Order  # noqa: E501

        :param workflow_order: The workflow_order of this WorkflowItem.  # noqa: E501
        :type: int
        """

        self._workflow_order = workflow_order

    @property
    def date_created(self):
        """Gets the date_created of this WorkflowItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this WorkflowItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this WorkflowItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this WorkflowItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def security_user_id(self):
        """Gets the security_user_id of this WorkflowItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this WorkflowItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this WorkflowItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this WorkflowItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def created_by_security_user_id(self):
        """Gets the created_by_security_user_id of this WorkflowItem.  # noqa: E501

        Created By Security User  # noqa: E501

        :return: The created_by_security_user_id of this WorkflowItem.  # noqa: E501
        :rtype: int
        """
        return self._created_by_security_user_id

    @created_by_security_user_id.setter
    def created_by_security_user_id(self, created_by_security_user_id):
        """Sets the created_by_security_user_id of this WorkflowItem.

        Created By Security User  # noqa: E501

        :param created_by_security_user_id: The created_by_security_user_id of this WorkflowItem.  # noqa: E501
        :type: int
        """

        self._created_by_security_user_id = created_by_security_user_id

    @property
    def date_modified(self):
        """Gets the date_modified of this WorkflowItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this WorkflowItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this WorkflowItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this WorkflowItem.  # noqa: E501
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
        if not isinstance(other, WorkflowItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
