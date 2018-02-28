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


class WebMenuItem(object):
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
        'web_menu_id': 'int',
        'web_module_id': 'int',
        'description': 'str',
        'menu_order': 'int',
        'comments': 'str',
        'security_user_id': 'int',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'web_menu_id': 'WebMenuID',
        'web_module_id': 'WebModuleID',
        'description': 'Description',
        'menu_order': 'MenuOrder',
        'comments': 'Comments',
        'security_user_id': 'SecurityUserID',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, web_menu_id=None, web_module_id=None, description=None, menu_order=None, comments=None, security_user_id=None, date_created=None, date_modified=None):  # noqa: E501
        """WebMenuItem - a model defined in Swagger"""  # noqa: E501

        self._web_menu_id = None
        self._web_module_id = None
        self._description = None
        self._menu_order = None
        self._comments = None
        self._security_user_id = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if web_menu_id is not None:
            self.web_menu_id = web_menu_id
        if web_module_id is not None:
            self.web_module_id = web_module_id
        if description is not None:
            self.description = description
        if menu_order is not None:
            self.menu_order = menu_order
        if comments is not None:
            self.comments = comments
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def web_menu_id(self):
        """Gets the web_menu_id of this WebMenuItem.  # noqa: E501

        Web Menu  # noqa: E501

        :return: The web_menu_id of this WebMenuItem.  # noqa: E501
        :rtype: int
        """
        return self._web_menu_id

    @web_menu_id.setter
    def web_menu_id(self, web_menu_id):
        """Sets the web_menu_id of this WebMenuItem.

        Web Menu  # noqa: E501

        :param web_menu_id: The web_menu_id of this WebMenuItem.  # noqa: E501
        :type: int
        """

        self._web_menu_id = web_menu_id

    @property
    def web_module_id(self):
        """Gets the web_module_id of this WebMenuItem.  # noqa: E501

        Web Module  # noqa: E501

        :return: The web_module_id of this WebMenuItem.  # noqa: E501
        :rtype: int
        """
        return self._web_module_id

    @web_module_id.setter
    def web_module_id(self, web_module_id):
        """Sets the web_module_id of this WebMenuItem.

        Web Module  # noqa: E501

        :param web_module_id: The web_module_id of this WebMenuItem.  # noqa: E501
        :type: int
        """

        self._web_module_id = web_module_id

    @property
    def description(self):
        """Gets the description of this WebMenuItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this WebMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebMenuItem.

        Description  # noqa: E501

        :param description: The description of this WebMenuItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def menu_order(self):
        """Gets the menu_order of this WebMenuItem.  # noqa: E501

        Menu Order  # noqa: E501

        :return: The menu_order of this WebMenuItem.  # noqa: E501
        :rtype: int
        """
        return self._menu_order

    @menu_order.setter
    def menu_order(self, menu_order):
        """Sets the menu_order of this WebMenuItem.

        Menu Order  # noqa: E501

        :param menu_order: The menu_order of this WebMenuItem.  # noqa: E501
        :type: int
        """

        self._menu_order = menu_order

    @property
    def comments(self):
        """Gets the comments of this WebMenuItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this WebMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this WebMenuItem.

        Comments  # noqa: E501

        :param comments: The comments of this WebMenuItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 2000:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `2000`")  # noqa: E501

        self._comments = comments

    @property
    def security_user_id(self):
        """Gets the security_user_id of this WebMenuItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this WebMenuItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this WebMenuItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this WebMenuItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this WebMenuItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this WebMenuItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this WebMenuItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this WebMenuItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this WebMenuItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this WebMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this WebMenuItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this WebMenuItem.  # noqa: E501
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
        if not isinstance(other, WebMenuItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other