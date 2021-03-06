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


class RefundRequestBatchConfigurationItem(object):
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
        'refund_request_batch_configuration_id': 'int',
        'dynamic_list_id': 'int',
        'description': 'str',
        'comments': 'str',
        'security_user_id': 'int',
        'created_by_security_user_id': 'int',
        'date_created': 'datetime',
        'record_type_enum': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'refund_request_batch_configuration_id': 'RefundRequestBatchConfigurationID',
        'dynamic_list_id': 'DynamicListID',
        'description': 'Description',
        'comments': 'Comments',
        'security_user_id': 'SecurityUserID',
        'created_by_security_user_id': 'CreatedBy_SecurityUserID',
        'date_created': 'DateCreated',
        'record_type_enum': 'RecordTypeEnum',
        'date_modified': 'DateModified'
    }

    def __init__(self, refund_request_batch_configuration_id=None, dynamic_list_id=None, description=None, comments=None, security_user_id=None, created_by_security_user_id=None, date_created=None, record_type_enum=None, date_modified=None):  # noqa: E501
        """RefundRequestBatchConfigurationItem - a model defined in Swagger"""  # noqa: E501

        self._refund_request_batch_configuration_id = None
        self._dynamic_list_id = None
        self._description = None
        self._comments = None
        self._security_user_id = None
        self._created_by_security_user_id = None
        self._date_created = None
        self._record_type_enum = None
        self._date_modified = None
        self.discriminator = None

        if refund_request_batch_configuration_id is not None:
            self.refund_request_batch_configuration_id = refund_request_batch_configuration_id
        if dynamic_list_id is not None:
            self.dynamic_list_id = dynamic_list_id
        if description is not None:
            self.description = description
        if comments is not None:
            self.comments = comments
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if created_by_security_user_id is not None:
            self.created_by_security_user_id = created_by_security_user_id
        if date_created is not None:
            self.date_created = date_created
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def refund_request_batch_configuration_id(self):
        """Gets the refund_request_batch_configuration_id of this RefundRequestBatchConfigurationItem.  # noqa: E501

        Refund Request Batch Configuration  # noqa: E501

        :return: The refund_request_batch_configuration_id of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._refund_request_batch_configuration_id

    @refund_request_batch_configuration_id.setter
    def refund_request_batch_configuration_id(self, refund_request_batch_configuration_id):
        """Sets the refund_request_batch_configuration_id of this RefundRequestBatchConfigurationItem.

        Refund Request Batch Configuration  # noqa: E501

        :param refund_request_batch_configuration_id: The refund_request_batch_configuration_id of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :type: int
        """

        self._refund_request_batch_configuration_id = refund_request_batch_configuration_id

    @property
    def dynamic_list_id(self):
        """Gets the dynamic_list_id of this RefundRequestBatchConfigurationItem.  # noqa: E501

        Dynamic List  # noqa: E501

        :return: The dynamic_list_id of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._dynamic_list_id

    @dynamic_list_id.setter
    def dynamic_list_id(self, dynamic_list_id):
        """Sets the dynamic_list_id of this RefundRequestBatchConfigurationItem.

        Dynamic List  # noqa: E501

        :param dynamic_list_id: The dynamic_list_id of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :type: int
        """

        self._dynamic_list_id = dynamic_list_id

    @property
    def description(self):
        """Gets the description of this RefundRequestBatchConfigurationItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RefundRequestBatchConfigurationItem.

        Description  # noqa: E501

        :param description: The description of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def comments(self):
        """Gets the comments of this RefundRequestBatchConfigurationItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this RefundRequestBatchConfigurationItem.

        Comments  # noqa: E501

        :param comments: The comments of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 300:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `300`")  # noqa: E501

        self._comments = comments

    @property
    def security_user_id(self):
        """Gets the security_user_id of this RefundRequestBatchConfigurationItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this RefundRequestBatchConfigurationItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def created_by_security_user_id(self):
        """Gets the created_by_security_user_id of this RefundRequestBatchConfigurationItem.  # noqa: E501

        Created By Security User  # noqa: E501

        :return: The created_by_security_user_id of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._created_by_security_user_id

    @created_by_security_user_id.setter
    def created_by_security_user_id(self, created_by_security_user_id):
        """Sets the created_by_security_user_id of this RefundRequestBatchConfigurationItem.

        Created By Security User  # noqa: E501

        :param created_by_security_user_id: The created_by_security_user_id of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :type: int
        """

        self._created_by_security_user_id = created_by_security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this RefundRequestBatchConfigurationItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this RefundRequestBatchConfigurationItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this RefundRequestBatchConfigurationItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this RefundRequestBatchConfigurationItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def date_modified(self):
        """Gets the date_modified of this RefundRequestBatchConfigurationItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RefundRequestBatchConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RefundRequestBatchConfigurationItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RefundRequestBatchConfigurationItem.  # noqa: E501
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
        if not isinstance(other, RefundRequestBatchConfigurationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
