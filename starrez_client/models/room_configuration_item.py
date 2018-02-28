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


class RoomConfigurationItem(object):
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
        'room_configuration_id': 'int',
        'date_start': 'str',
        'date_end': 'str',
        'room_base_id': 'int',
        'gender_type_enum': 'str',
        'room_type_id': 'int',
        'view_on_web_maintenance': 'bool',
        'view_on_web_inventory': 'bool',
        'view_on_web': 'bool',
        'web_image_location': 'str',
        'web_description': 'str',
        'web_comments': 'str',
        'date_created': 'datetime',
        'security_user_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'room_configuration_id': 'RoomConfigurationID',
        'date_start': 'DateStart',
        'date_end': 'DateEnd',
        'room_base_id': 'RoomBaseID',
        'gender_type_enum': 'GenderTypeEnum',
        'room_type_id': 'RoomTypeID',
        'view_on_web_maintenance': 'ViewOnWebMaintenance',
        'view_on_web_inventory': 'ViewOnWebInventory',
        'view_on_web': 'ViewOnWeb',
        'web_image_location': 'WebImageLocation',
        'web_description': 'WebDescription',
        'web_comments': 'WebComments',
        'date_created': 'DateCreated',
        'security_user_id': 'SecurityUserID',
        'date_modified': 'DateModified'
    }

    def __init__(self, room_configuration_id=None, date_start=None, date_end=None, room_base_id=None, gender_type_enum=None, room_type_id=None, view_on_web_maintenance=None, view_on_web_inventory=None, view_on_web=None, web_image_location=None, web_description=None, web_comments=None, date_created=None, security_user_id=None, date_modified=None):  # noqa: E501
        """RoomConfigurationItem - a model defined in Swagger"""  # noqa: E501

        self._room_configuration_id = None
        self._date_start = None
        self._date_end = None
        self._room_base_id = None
        self._gender_type_enum = None
        self._room_type_id = None
        self._view_on_web_maintenance = None
        self._view_on_web_inventory = None
        self._view_on_web = None
        self._web_image_location = None
        self._web_description = None
        self._web_comments = None
        self._date_created = None
        self._security_user_id = None
        self._date_modified = None
        self.discriminator = None

        if room_configuration_id is not None:
            self.room_configuration_id = room_configuration_id
        if date_start is not None:
            self.date_start = date_start
        if date_end is not None:
            self.date_end = date_end
        if room_base_id is not None:
            self.room_base_id = room_base_id
        if gender_type_enum is not None:
            self.gender_type_enum = gender_type_enum
        if room_type_id is not None:
            self.room_type_id = room_type_id
        if view_on_web_maintenance is not None:
            self.view_on_web_maintenance = view_on_web_maintenance
        if view_on_web_inventory is not None:
            self.view_on_web_inventory = view_on_web_inventory
        if view_on_web is not None:
            self.view_on_web = view_on_web
        if web_image_location is not None:
            self.web_image_location = web_image_location
        if web_description is not None:
            self.web_description = web_description
        if web_comments is not None:
            self.web_comments = web_comments
        if date_created is not None:
            self.date_created = date_created
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def room_configuration_id(self):
        """Gets the room_configuration_id of this RoomConfigurationItem.  # noqa: E501

        Room Configuration  # noqa: E501

        :return: The room_configuration_id of this RoomConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_configuration_id

    @room_configuration_id.setter
    def room_configuration_id(self, room_configuration_id):
        """Sets the room_configuration_id of this RoomConfigurationItem.

        Room Configuration  # noqa: E501

        :param room_configuration_id: The room_configuration_id of this RoomConfigurationItem.  # noqa: E501
        :type: int
        """

        self._room_configuration_id = room_configuration_id

    @property
    def date_start(self):
        """Gets the date_start of this RoomConfigurationItem.  # noqa: E501

        Date Start  # noqa: E501

        :return: The date_start of this RoomConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this RoomConfigurationItem.

        Date Start  # noqa: E501

        :param date_start: The date_start of this RoomConfigurationItem.  # noqa: E501
        :type: str
        """

        self._date_start = date_start

    @property
    def date_end(self):
        """Gets the date_end of this RoomConfigurationItem.  # noqa: E501

        Date End  # noqa: E501

        :return: The date_end of this RoomConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this RoomConfigurationItem.

        Date End  # noqa: E501

        :param date_end: The date_end of this RoomConfigurationItem.  # noqa: E501
        :type: str
        """

        self._date_end = date_end

    @property
    def room_base_id(self):
        """Gets the room_base_id of this RoomConfigurationItem.  # noqa: E501

        Room Base  # noqa: E501

        :return: The room_base_id of this RoomConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_base_id

    @room_base_id.setter
    def room_base_id(self, room_base_id):
        """Sets the room_base_id of this RoomConfigurationItem.

        Room Base  # noqa: E501

        :param room_base_id: The room_base_id of this RoomConfigurationItem.  # noqa: E501
        :type: int
        """

        self._room_base_id = room_base_id

    @property
    def gender_type_enum(self):
        """Gets the gender_type_enum of this RoomConfigurationItem.  # noqa: E501

        Gender Type  # noqa: E501

        :return: The gender_type_enum of this RoomConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._gender_type_enum

    @gender_type_enum.setter
    def gender_type_enum(self, gender_type_enum):
        """Sets the gender_type_enum of this RoomConfigurationItem.

        Gender Type  # noqa: E501

        :param gender_type_enum: The gender_type_enum of this RoomConfigurationItem.  # noqa: E501
        :type: str
        """

        self._gender_type_enum = gender_type_enum

    @property
    def room_type_id(self):
        """Gets the room_type_id of this RoomConfigurationItem.  # noqa: E501

        Room Type  # noqa: E501

        :return: The room_type_id of this RoomConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_type_id

    @room_type_id.setter
    def room_type_id(self, room_type_id):
        """Sets the room_type_id of this RoomConfigurationItem.

        Room Type  # noqa: E501

        :param room_type_id: The room_type_id of this RoomConfigurationItem.  # noqa: E501
        :type: int
        """

        self._room_type_id = room_type_id

    @property
    def view_on_web_maintenance(self):
        """Gets the view_on_web_maintenance of this RoomConfigurationItem.  # noqa: E501

        View On Web Maintenance  # noqa: E501

        :return: The view_on_web_maintenance of this RoomConfigurationItem.  # noqa: E501
        :rtype: bool
        """
        return self._view_on_web_maintenance

    @view_on_web_maintenance.setter
    def view_on_web_maintenance(self, view_on_web_maintenance):
        """Sets the view_on_web_maintenance of this RoomConfigurationItem.

        View On Web Maintenance  # noqa: E501

        :param view_on_web_maintenance: The view_on_web_maintenance of this RoomConfigurationItem.  # noqa: E501
        :type: bool
        """

        self._view_on_web_maintenance = view_on_web_maintenance

    @property
    def view_on_web_inventory(self):
        """Gets the view_on_web_inventory of this RoomConfigurationItem.  # noqa: E501

        View On Web Inventory  # noqa: E501

        :return: The view_on_web_inventory of this RoomConfigurationItem.  # noqa: E501
        :rtype: bool
        """
        return self._view_on_web_inventory

    @view_on_web_inventory.setter
    def view_on_web_inventory(self, view_on_web_inventory):
        """Sets the view_on_web_inventory of this RoomConfigurationItem.

        View On Web Inventory  # noqa: E501

        :param view_on_web_inventory: The view_on_web_inventory of this RoomConfigurationItem.  # noqa: E501
        :type: bool
        """

        self._view_on_web_inventory = view_on_web_inventory

    @property
    def view_on_web(self):
        """Gets the view_on_web of this RoomConfigurationItem.  # noqa: E501

        View On Web  # noqa: E501

        :return: The view_on_web of this RoomConfigurationItem.  # noqa: E501
        :rtype: bool
        """
        return self._view_on_web

    @view_on_web.setter
    def view_on_web(self, view_on_web):
        """Sets the view_on_web of this RoomConfigurationItem.

        View On Web  # noqa: E501

        :param view_on_web: The view_on_web of this RoomConfigurationItem.  # noqa: E501
        :type: bool
        """

        self._view_on_web = view_on_web

    @property
    def web_image_location(self):
        """Gets the web_image_location of this RoomConfigurationItem.  # noqa: E501

        Web Image Location  # noqa: E501

        :return: The web_image_location of this RoomConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._web_image_location

    @web_image_location.setter
    def web_image_location(self, web_image_location):
        """Sets the web_image_location of this RoomConfigurationItem.

        Web Image Location  # noqa: E501

        :param web_image_location: The web_image_location of this RoomConfigurationItem.  # noqa: E501
        :type: str
        """
        if web_image_location is not None and len(web_image_location) > 200:
            raise ValueError("Invalid value for `web_image_location`, length must be less than or equal to `200`")  # noqa: E501

        self._web_image_location = web_image_location

    @property
    def web_description(self):
        """Gets the web_description of this RoomConfigurationItem.  # noqa: E501

        Web Description  # noqa: E501

        :return: The web_description of this RoomConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._web_description

    @web_description.setter
    def web_description(self, web_description):
        """Sets the web_description of this RoomConfigurationItem.

        Web Description  # noqa: E501

        :param web_description: The web_description of this RoomConfigurationItem.  # noqa: E501
        :type: str
        """
        if web_description is not None and len(web_description) > 1000:
            raise ValueError("Invalid value for `web_description`, length must be less than or equal to `1000`")  # noqa: E501

        self._web_description = web_description

    @property
    def web_comments(self):
        """Gets the web_comments of this RoomConfigurationItem.  # noqa: E501

        Web Comments  # noqa: E501

        :return: The web_comments of this RoomConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._web_comments

    @web_comments.setter
    def web_comments(self, web_comments):
        """Sets the web_comments of this RoomConfigurationItem.

        Web Comments  # noqa: E501

        :param web_comments: The web_comments of this RoomConfigurationItem.  # noqa: E501
        :type: str
        """

        self._web_comments = web_comments

    @property
    def date_created(self):
        """Gets the date_created of this RoomConfigurationItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this RoomConfigurationItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this RoomConfigurationItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this RoomConfigurationItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def security_user_id(self):
        """Gets the security_user_id of this RoomConfigurationItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this RoomConfigurationItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this RoomConfigurationItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this RoomConfigurationItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_modified(self):
        """Gets the date_modified of this RoomConfigurationItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RoomConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RoomConfigurationItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RoomConfigurationItem.  # noqa: E501
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
        if not isinstance(other, RoomConfigurationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other