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


class WebModuleItem(object):
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
        'web_module_id': 'int',
        'web_site_id': 'int',
        'module_name': 'str',
        'description': 'str',
        'module_order': 'int',
        'manager': 'str',
        'visible': 'bool',
        'access_roles': 'str',
        'global_module': 'bool',
        'security_user_id': 'int',
        'date_created': 'datetime',
        'date_modified': 'str'
    }

    attribute_map = {
        'web_module_id': 'WebModuleID',
        'web_site_id': 'WebSiteID',
        'module_name': 'ModuleName',
        'description': 'Description',
        'module_order': 'ModuleOrder',
        'manager': 'Manager',
        'visible': 'Visible',
        'access_roles': 'AccessRoles',
        'global_module': 'GlobalModule',
        'security_user_id': 'SecurityUserID',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified'
    }

    def __init__(self, web_module_id=None, web_site_id=None, module_name=None, description=None, module_order=None, manager=None, visible=None, access_roles=None, global_module=None, security_user_id=None, date_created=None, date_modified=None):  # noqa: E501
        """WebModuleItem - a model defined in Swagger"""  # noqa: E501

        self._web_module_id = None
        self._web_site_id = None
        self._module_name = None
        self._description = None
        self._module_order = None
        self._manager = None
        self._visible = None
        self._access_roles = None
        self._global_module = None
        self._security_user_id = None
        self._date_created = None
        self._date_modified = None
        self.discriminator = None

        if web_module_id is not None:
            self.web_module_id = web_module_id
        if web_site_id is not None:
            self.web_site_id = web_site_id
        if module_name is not None:
            self.module_name = module_name
        if description is not None:
            self.description = description
        if module_order is not None:
            self.module_order = module_order
        if manager is not None:
            self.manager = manager
        if visible is not None:
            self.visible = visible
        if access_roles is not None:
            self.access_roles = access_roles
        if global_module is not None:
            self.global_module = global_module
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def web_module_id(self):
        """Gets the web_module_id of this WebModuleItem.  # noqa: E501

        Web Module  # noqa: E501

        :return: The web_module_id of this WebModuleItem.  # noqa: E501
        :rtype: int
        """
        return self._web_module_id

    @web_module_id.setter
    def web_module_id(self, web_module_id):
        """Sets the web_module_id of this WebModuleItem.

        Web Module  # noqa: E501

        :param web_module_id: The web_module_id of this WebModuleItem.  # noqa: E501
        :type: int
        """

        self._web_module_id = web_module_id

    @property
    def web_site_id(self):
        """Gets the web_site_id of this WebModuleItem.  # noqa: E501

        Web Site  # noqa: E501

        :return: The web_site_id of this WebModuleItem.  # noqa: E501
        :rtype: int
        """
        return self._web_site_id

    @web_site_id.setter
    def web_site_id(self, web_site_id):
        """Sets the web_site_id of this WebModuleItem.

        Web Site  # noqa: E501

        :param web_site_id: The web_site_id of this WebModuleItem.  # noqa: E501
        :type: int
        """

        self._web_site_id = web_site_id

    @property
    def module_name(self):
        """Gets the module_name of this WebModuleItem.  # noqa: E501

        Module Name  # noqa: E501

        :return: The module_name of this WebModuleItem.  # noqa: E501
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """Sets the module_name of this WebModuleItem.

        Module Name  # noqa: E501

        :param module_name: The module_name of this WebModuleItem.  # noqa: E501
        :type: str
        """
        if module_name is not None and len(module_name) > 100:
            raise ValueError("Invalid value for `module_name`, length must be less than or equal to `100`")  # noqa: E501

        self._module_name = module_name

    @property
    def description(self):
        """Gets the description of this WebModuleItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this WebModuleItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebModuleItem.

        Description  # noqa: E501

        :param description: The description of this WebModuleItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def module_order(self):
        """Gets the module_order of this WebModuleItem.  # noqa: E501

        Module Order  # noqa: E501

        :return: The module_order of this WebModuleItem.  # noqa: E501
        :rtype: int
        """
        return self._module_order

    @module_order.setter
    def module_order(self, module_order):
        """Sets the module_order of this WebModuleItem.

        Module Order  # noqa: E501

        :param module_order: The module_order of this WebModuleItem.  # noqa: E501
        :type: int
        """

        self._module_order = module_order

    @property
    def manager(self):
        """Gets the manager of this WebModuleItem.  # noqa: E501

        Manager  # noqa: E501

        :return: The manager of this WebModuleItem.  # noqa: E501
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this WebModuleItem.

        Manager  # noqa: E501

        :param manager: The manager of this WebModuleItem.  # noqa: E501
        :type: str
        """
        if manager is not None and len(manager) > 200:
            raise ValueError("Invalid value for `manager`, length must be less than or equal to `200`")  # noqa: E501

        self._manager = manager

    @property
    def visible(self):
        """Gets the visible of this WebModuleItem.  # noqa: E501

        Visible  # noqa: E501

        :return: The visible of this WebModuleItem.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this WebModuleItem.

        Visible  # noqa: E501

        :param visible: The visible of this WebModuleItem.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def access_roles(self):
        """Gets the access_roles of this WebModuleItem.  # noqa: E501

        Access Roles  # noqa: E501

        :return: The access_roles of this WebModuleItem.  # noqa: E501
        :rtype: str
        """
        return self._access_roles

    @access_roles.setter
    def access_roles(self, access_roles):
        """Sets the access_roles of this WebModuleItem.

        Access Roles  # noqa: E501

        :param access_roles: The access_roles of this WebModuleItem.  # noqa: E501
        :type: str
        """
        if access_roles is not None and len(access_roles) > 200:
            raise ValueError("Invalid value for `access_roles`, length must be less than or equal to `200`")  # noqa: E501

        self._access_roles = access_roles

    @property
    def global_module(self):
        """Gets the global_module of this WebModuleItem.  # noqa: E501

        Global Module  # noqa: E501

        :return: The global_module of this WebModuleItem.  # noqa: E501
        :rtype: bool
        """
        return self._global_module

    @global_module.setter
    def global_module(self, global_module):
        """Sets the global_module of this WebModuleItem.

        Global Module  # noqa: E501

        :param global_module: The global_module of this WebModuleItem.  # noqa: E501
        :type: bool
        """

        self._global_module = global_module

    @property
    def security_user_id(self):
        """Gets the security_user_id of this WebModuleItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this WebModuleItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this WebModuleItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this WebModuleItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_created(self):
        """Gets the date_created of this WebModuleItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this WebModuleItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this WebModuleItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this WebModuleItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this WebModuleItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this WebModuleItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this WebModuleItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this WebModuleItem.  # noqa: E501
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
        if not isinstance(other, WebModuleItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
