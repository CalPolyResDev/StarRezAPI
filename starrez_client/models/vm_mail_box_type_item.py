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


class VMMailBoxTypeItem(object):
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
        'vm_mail_box_type_id': 'int',
        'record_type_enum': 'str',
        'description': 'str',
        'comments': 'str',
        'allow_call_delivery': 'bool',
        'allow_group_create': 'bool',
        'allow_group_message': 'bool',
        'allow_shared': 'bool',
        'fixed_shared_greeting': 'bool',
        'date_modified': 'str'
    }

    attribute_map = {
        'vm_mail_box_type_id': 'VMMailBoxTypeID',
        'record_type_enum': 'RecordTypeEnum',
        'description': 'Description',
        'comments': 'Comments',
        'allow_call_delivery': 'AllowCallDelivery',
        'allow_group_create': 'AllowGroupCreate',
        'allow_group_message': 'AllowGroupMessage',
        'allow_shared': 'AllowShared',
        'fixed_shared_greeting': 'FixedSharedGreeting',
        'date_modified': 'DateModified'
    }

    def __init__(self, vm_mail_box_type_id=None, record_type_enum=None, description=None, comments=None, allow_call_delivery=None, allow_group_create=None, allow_group_message=None, allow_shared=None, fixed_shared_greeting=None, date_modified=None):  # noqa: E501
        """VMMailBoxTypeItem - a model defined in Swagger"""  # noqa: E501

        self._vm_mail_box_type_id = None
        self._record_type_enum = None
        self._description = None
        self._comments = None
        self._allow_call_delivery = None
        self._allow_group_create = None
        self._allow_group_message = None
        self._allow_shared = None
        self._fixed_shared_greeting = None
        self._date_modified = None
        self.discriminator = None

        if vm_mail_box_type_id is not None:
            self.vm_mail_box_type_id = vm_mail_box_type_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if description is not None:
            self.description = description
        if comments is not None:
            self.comments = comments
        if allow_call_delivery is not None:
            self.allow_call_delivery = allow_call_delivery
        if allow_group_create is not None:
            self.allow_group_create = allow_group_create
        if allow_group_message is not None:
            self.allow_group_message = allow_group_message
        if allow_shared is not None:
            self.allow_shared = allow_shared
        if fixed_shared_greeting is not None:
            self.fixed_shared_greeting = fixed_shared_greeting
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def vm_mail_box_type_id(self):
        """Gets the vm_mail_box_type_id of this VMMailBoxTypeItem.  # noqa: E501

        VM Mail Box Type  # noqa: E501

        :return: The vm_mail_box_type_id of this VMMailBoxTypeItem.  # noqa: E501
        :rtype: int
        """
        return self._vm_mail_box_type_id

    @vm_mail_box_type_id.setter
    def vm_mail_box_type_id(self, vm_mail_box_type_id):
        """Sets the vm_mail_box_type_id of this VMMailBoxTypeItem.

        VM Mail Box Type  # noqa: E501

        :param vm_mail_box_type_id: The vm_mail_box_type_id of this VMMailBoxTypeItem.  # noqa: E501
        :type: int
        """

        self._vm_mail_box_type_id = vm_mail_box_type_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this VMMailBoxTypeItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this VMMailBoxTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this VMMailBoxTypeItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this VMMailBoxTypeItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def description(self):
        """Gets the description of this VMMailBoxTypeItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this VMMailBoxTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VMMailBoxTypeItem.

        Description  # noqa: E501

        :param description: The description of this VMMailBoxTypeItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 25:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `25`")  # noqa: E501

        self._description = description

    @property
    def comments(self):
        """Gets the comments of this VMMailBoxTypeItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this VMMailBoxTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this VMMailBoxTypeItem.

        Comments  # noqa: E501

        :param comments: The comments of this VMMailBoxTypeItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 100:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `100`")  # noqa: E501

        self._comments = comments

    @property
    def allow_call_delivery(self):
        """Gets the allow_call_delivery of this VMMailBoxTypeItem.  # noqa: E501

        Allow Call Delivery  # noqa: E501

        :return: The allow_call_delivery of this VMMailBoxTypeItem.  # noqa: E501
        :rtype: bool
        """
        return self._allow_call_delivery

    @allow_call_delivery.setter
    def allow_call_delivery(self, allow_call_delivery):
        """Sets the allow_call_delivery of this VMMailBoxTypeItem.

        Allow Call Delivery  # noqa: E501

        :param allow_call_delivery: The allow_call_delivery of this VMMailBoxTypeItem.  # noqa: E501
        :type: bool
        """

        self._allow_call_delivery = allow_call_delivery

    @property
    def allow_group_create(self):
        """Gets the allow_group_create of this VMMailBoxTypeItem.  # noqa: E501

        Allow Group Create  # noqa: E501

        :return: The allow_group_create of this VMMailBoxTypeItem.  # noqa: E501
        :rtype: bool
        """
        return self._allow_group_create

    @allow_group_create.setter
    def allow_group_create(self, allow_group_create):
        """Sets the allow_group_create of this VMMailBoxTypeItem.

        Allow Group Create  # noqa: E501

        :param allow_group_create: The allow_group_create of this VMMailBoxTypeItem.  # noqa: E501
        :type: bool
        """

        self._allow_group_create = allow_group_create

    @property
    def allow_group_message(self):
        """Gets the allow_group_message of this VMMailBoxTypeItem.  # noqa: E501

        Allow Group Message  # noqa: E501

        :return: The allow_group_message of this VMMailBoxTypeItem.  # noqa: E501
        :rtype: bool
        """
        return self._allow_group_message

    @allow_group_message.setter
    def allow_group_message(self, allow_group_message):
        """Sets the allow_group_message of this VMMailBoxTypeItem.

        Allow Group Message  # noqa: E501

        :param allow_group_message: The allow_group_message of this VMMailBoxTypeItem.  # noqa: E501
        :type: bool
        """

        self._allow_group_message = allow_group_message

    @property
    def allow_shared(self):
        """Gets the allow_shared of this VMMailBoxTypeItem.  # noqa: E501

        Allow Shared  # noqa: E501

        :return: The allow_shared of this VMMailBoxTypeItem.  # noqa: E501
        :rtype: bool
        """
        return self._allow_shared

    @allow_shared.setter
    def allow_shared(self, allow_shared):
        """Sets the allow_shared of this VMMailBoxTypeItem.

        Allow Shared  # noqa: E501

        :param allow_shared: The allow_shared of this VMMailBoxTypeItem.  # noqa: E501
        :type: bool
        """

        self._allow_shared = allow_shared

    @property
    def fixed_shared_greeting(self):
        """Gets the fixed_shared_greeting of this VMMailBoxTypeItem.  # noqa: E501

        Fixed Shared Greeting  # noqa: E501

        :return: The fixed_shared_greeting of this VMMailBoxTypeItem.  # noqa: E501
        :rtype: bool
        """
        return self._fixed_shared_greeting

    @fixed_shared_greeting.setter
    def fixed_shared_greeting(self, fixed_shared_greeting):
        """Sets the fixed_shared_greeting of this VMMailBoxTypeItem.

        Fixed Shared Greeting  # noqa: E501

        :param fixed_shared_greeting: The fixed_shared_greeting of this VMMailBoxTypeItem.  # noqa: E501
        :type: bool
        """

        self._fixed_shared_greeting = fixed_shared_greeting

    @property
    def date_modified(self):
        """Gets the date_modified of this VMMailBoxTypeItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this VMMailBoxTypeItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this VMMailBoxTypeItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this VMMailBoxTypeItem.  # noqa: E501
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
        if not isinstance(other, VMMailBoxTypeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
