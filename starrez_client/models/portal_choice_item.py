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


class PortalChoiceItem(object):
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
        'portal_choice_id': 'int',
        'portal_process_id': 'int',
        'description': 'str',
        'comments': 'str',
        'class_name': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'portal_choice_id': 'PortalChoiceID',
        'portal_process_id': 'PortalProcessID',
        'description': 'Description',
        'comments': 'Comments',
        'class_name': 'ClassName',
        'date_modified': 'DateModified'
    }

    def __init__(self, portal_choice_id=None, portal_process_id=None, description=None, comments=None, class_name=None, date_modified=None):  # noqa: E501
        """PortalChoiceItem - a model defined in Swagger"""  # noqa: E501

        self._portal_choice_id = None
        self._portal_process_id = None
        self._description = None
        self._comments = None
        self._class_name = None
        self._date_modified = None
        self.discriminator = None

        if portal_choice_id is not None:
            self.portal_choice_id = portal_choice_id
        if portal_process_id is not None:
            self.portal_process_id = portal_process_id
        if description is not None:
            self.description = description
        if comments is not None:
            self.comments = comments
        if class_name is not None:
            self.class_name = class_name
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def portal_choice_id(self):
        """Gets the portal_choice_id of this PortalChoiceItem.  # noqa: E501

        Portal Choice  # noqa: E501

        :return: The portal_choice_id of this PortalChoiceItem.  # noqa: E501
        :rtype: int
        """
        return self._portal_choice_id

    @portal_choice_id.setter
    def portal_choice_id(self, portal_choice_id):
        """Sets the portal_choice_id of this PortalChoiceItem.

        Portal Choice  # noqa: E501

        :param portal_choice_id: The portal_choice_id of this PortalChoiceItem.  # noqa: E501
        :type: int
        """

        self._portal_choice_id = portal_choice_id

    @property
    def portal_process_id(self):
        """Gets the portal_process_id of this PortalChoiceItem.  # noqa: E501

        Portal Process  # noqa: E501

        :return: The portal_process_id of this PortalChoiceItem.  # noqa: E501
        :rtype: int
        """
        return self._portal_process_id

    @portal_process_id.setter
    def portal_process_id(self, portal_process_id):
        """Sets the portal_process_id of this PortalChoiceItem.

        Portal Process  # noqa: E501

        :param portal_process_id: The portal_process_id of this PortalChoiceItem.  # noqa: E501
        :type: int
        """

        self._portal_process_id = portal_process_id

    @property
    def description(self):
        """Gets the description of this PortalChoiceItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this PortalChoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortalChoiceItem.

        Description  # noqa: E501

        :param description: The description of this PortalChoiceItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")  # noqa: E501

        self._description = description

    @property
    def comments(self):
        """Gets the comments of this PortalChoiceItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this PortalChoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this PortalChoiceItem.

        Comments  # noqa: E501

        :param comments: The comments of this PortalChoiceItem.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def class_name(self):
        """Gets the class_name of this PortalChoiceItem.  # noqa: E501

        Class Name  # noqa: E501

        :return: The class_name of this PortalChoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this PortalChoiceItem.

        Class Name  # noqa: E501

        :param class_name: The class_name of this PortalChoiceItem.  # noqa: E501
        :type: str
        """
        if class_name is not None and len(class_name) > 200:
            raise ValueError("Invalid value for `class_name`, length must be less than or equal to `200`")  # noqa: E501

        self._class_name = class_name

    @property
    def date_modified(self):
        """Gets the date_modified of this PortalChoiceItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this PortalChoiceItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this PortalChoiceItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this PortalChoiceItem.  # noqa: E501
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
        if not isinstance(other, PortalChoiceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
