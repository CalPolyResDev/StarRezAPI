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


class RoomLocationItem(object):
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
        'room_location_id': 'int',
        'record_type_enum': 'str',
        'room_location_area_id': 'int',
        'category_id': 'int',
        'non_residential': 'bool',
        'description': 'str',
        'comments': 'str',
        'lease': 'bool',
        'allocate_sort_order': 'int',
        'city': 'str',
        'country_id': 'int',
        'state_province': 'str',
        'zip_postcode': 'str',
        'gender_type_enum': 'str',
        'custom_bit1': 'bool',
        'custom_bit2': 'bool',
        'custom_string1': 'str',
        'custom_string2': 'str',
        'custom_string3': 'str',
        'custom_string4': 'str',
        'custom_string5': 'str',
        'custom_string6': 'str',
        'custom_date1': 'str',
        'custom_date2': 'str',
        'view_on_web': 'bool',
        'web_image_location': 'str',
        'web_description': 'str',
        'web_comments': 'str',
        'date_modified': 'str'
    }

    attribute_map = {
        'room_location_id': 'RoomLocationID',
        'record_type_enum': 'RecordTypeEnum',
        'room_location_area_id': 'RoomLocationAreaID',
        'category_id': 'CategoryID',
        'non_residential': 'NonResidential',
        'description': 'Description',
        'comments': 'Comments',
        'lease': 'Lease',
        'allocate_sort_order': 'AllocateSortOrder',
        'city': 'City',
        'country_id': 'CountryID',
        'state_province': 'StateProvince',
        'zip_postcode': 'ZipPostcode',
        'gender_type_enum': 'GenderTypeEnum',
        'custom_bit1': 'CustomBit1',
        'custom_bit2': 'CustomBit2',
        'custom_string1': 'CustomString1',
        'custom_string2': 'CustomString2',
        'custom_string3': 'CustomString3',
        'custom_string4': 'CustomString4',
        'custom_string5': 'CustomString5',
        'custom_string6': 'CustomString6',
        'custom_date1': 'CustomDate1',
        'custom_date2': 'CustomDate2',
        'view_on_web': 'ViewOnWeb',
        'web_image_location': 'WebImageLocation',
        'web_description': 'WebDescription',
        'web_comments': 'WebComments',
        'date_modified': 'DateModified'
    }

    def __init__(self, room_location_id=None, record_type_enum=None, room_location_area_id=None, category_id=None, non_residential=None, description=None, comments=None, lease=None, allocate_sort_order=None, city=None, country_id=None, state_province=None, zip_postcode=None, gender_type_enum=None, custom_bit1=None, custom_bit2=None, custom_string1=None, custom_string2=None, custom_string3=None, custom_string4=None, custom_string5=None, custom_string6=None, custom_date1=None, custom_date2=None, view_on_web=None, web_image_location=None, web_description=None, web_comments=None, date_modified=None):  # noqa: E501
        """RoomLocationItem - a model defined in Swagger"""  # noqa: E501

        self._room_location_id = None
        self._record_type_enum = None
        self._room_location_area_id = None
        self._category_id = None
        self._non_residential = None
        self._description = None
        self._comments = None
        self._lease = None
        self._allocate_sort_order = None
        self._city = None
        self._country_id = None
        self._state_province = None
        self._zip_postcode = None
        self._gender_type_enum = None
        self._custom_bit1 = None
        self._custom_bit2 = None
        self._custom_string1 = None
        self._custom_string2 = None
        self._custom_string3 = None
        self._custom_string4 = None
        self._custom_string5 = None
        self._custom_string6 = None
        self._custom_date1 = None
        self._custom_date2 = None
        self._view_on_web = None
        self._web_image_location = None
        self._web_description = None
        self._web_comments = None
        self._date_modified = None
        self.discriminator = None

        if room_location_id is not None:
            self.room_location_id = room_location_id
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if room_location_area_id is not None:
            self.room_location_area_id = room_location_area_id
        if category_id is not None:
            self.category_id = category_id
        if non_residential is not None:
            self.non_residential = non_residential
        if description is not None:
            self.description = description
        if comments is not None:
            self.comments = comments
        if lease is not None:
            self.lease = lease
        if allocate_sort_order is not None:
            self.allocate_sort_order = allocate_sort_order
        if city is not None:
            self.city = city
        if country_id is not None:
            self.country_id = country_id
        if state_province is not None:
            self.state_province = state_province
        if zip_postcode is not None:
            self.zip_postcode = zip_postcode
        if gender_type_enum is not None:
            self.gender_type_enum = gender_type_enum
        if custom_bit1 is not None:
            self.custom_bit1 = custom_bit1
        if custom_bit2 is not None:
            self.custom_bit2 = custom_bit2
        if custom_string1 is not None:
            self.custom_string1 = custom_string1
        if custom_string2 is not None:
            self.custom_string2 = custom_string2
        if custom_string3 is not None:
            self.custom_string3 = custom_string3
        if custom_string4 is not None:
            self.custom_string4 = custom_string4
        if custom_string5 is not None:
            self.custom_string5 = custom_string5
        if custom_string6 is not None:
            self.custom_string6 = custom_string6
        if custom_date1 is not None:
            self.custom_date1 = custom_date1
        if custom_date2 is not None:
            self.custom_date2 = custom_date2
        if view_on_web is not None:
            self.view_on_web = view_on_web
        if web_image_location is not None:
            self.web_image_location = web_image_location
        if web_description is not None:
            self.web_description = web_description
        if web_comments is not None:
            self.web_comments = web_comments
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def room_location_id(self):
        """Gets the room_location_id of this RoomLocationItem.  # noqa: E501

        Room Location  # noqa: E501

        :return: The room_location_id of this RoomLocationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_location_id

    @room_location_id.setter
    def room_location_id(self, room_location_id):
        """Sets the room_location_id of this RoomLocationItem.

        Room Location  # noqa: E501

        :param room_location_id: The room_location_id of this RoomLocationItem.  # noqa: E501
        :type: int
        """

        self._room_location_id = room_location_id

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this RoomLocationItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this RoomLocationItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this RoomLocationItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def room_location_area_id(self):
        """Gets the room_location_area_id of this RoomLocationItem.  # noqa: E501

        Room Location Area  # noqa: E501

        :return: The room_location_area_id of this RoomLocationItem.  # noqa: E501
        :rtype: int
        """
        return self._room_location_area_id

    @room_location_area_id.setter
    def room_location_area_id(self, room_location_area_id):
        """Sets the room_location_area_id of this RoomLocationItem.

        Room Location Area  # noqa: E501

        :param room_location_area_id: The room_location_area_id of this RoomLocationItem.  # noqa: E501
        :type: int
        """

        self._room_location_area_id = room_location_area_id

    @property
    def category_id(self):
        """Gets the category_id of this RoomLocationItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this RoomLocationItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this RoomLocationItem.

        Category  # noqa: E501

        :param category_id: The category_id of this RoomLocationItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def non_residential(self):
        """Gets the non_residential of this RoomLocationItem.  # noqa: E501

        Non Residential  # noqa: E501

        :return: The non_residential of this RoomLocationItem.  # noqa: E501
        :rtype: bool
        """
        return self._non_residential

    @non_residential.setter
    def non_residential(self, non_residential):
        """Sets the non_residential of this RoomLocationItem.

        Non Residential  # noqa: E501

        :param non_residential: The non_residential of this RoomLocationItem.  # noqa: E501
        :type: bool
        """

        self._non_residential = non_residential

    @property
    def description(self):
        """Gets the description of this RoomLocationItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoomLocationItem.

        Description  # noqa: E501

        :param description: The description of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 25:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `25`")  # noqa: E501

        self._description = description

    @property
    def comments(self):
        """Gets the comments of this RoomLocationItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this RoomLocationItem.

        Comments  # noqa: E501

        :param comments: The comments of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 200:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `200`")  # noqa: E501

        self._comments = comments

    @property
    def lease(self):
        """Gets the lease of this RoomLocationItem.  # noqa: E501

        Lease  # noqa: E501

        :return: The lease of this RoomLocationItem.  # noqa: E501
        :rtype: bool
        """
        return self._lease

    @lease.setter
    def lease(self, lease):
        """Sets the lease of this RoomLocationItem.

        Lease  # noqa: E501

        :param lease: The lease of this RoomLocationItem.  # noqa: E501
        :type: bool
        """

        self._lease = lease

    @property
    def allocate_sort_order(self):
        """Gets the allocate_sort_order of this RoomLocationItem.  # noqa: E501

        Allocate Sort Order  # noqa: E501

        :return: The allocate_sort_order of this RoomLocationItem.  # noqa: E501
        :rtype: int
        """
        return self._allocate_sort_order

    @allocate_sort_order.setter
    def allocate_sort_order(self, allocate_sort_order):
        """Sets the allocate_sort_order of this RoomLocationItem.

        Allocate Sort Order  # noqa: E501

        :param allocate_sort_order: The allocate_sort_order of this RoomLocationItem.  # noqa: E501
        :type: int
        """

        self._allocate_sort_order = allocate_sort_order

    @property
    def city(self):
        """Gets the city of this RoomLocationItem.  # noqa: E501

        City  # noqa: E501

        :return: The city of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this RoomLocationItem.

        City  # noqa: E501

        :param city: The city of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if city is not None and len(city) > 60:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `60`")  # noqa: E501

        self._city = city

    @property
    def country_id(self):
        """Gets the country_id of this RoomLocationItem.  # noqa: E501

        Country  # noqa: E501

        :return: The country_id of this RoomLocationItem.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this RoomLocationItem.

        Country  # noqa: E501

        :param country_id: The country_id of this RoomLocationItem.  # noqa: E501
        :type: int
        """

        self._country_id = country_id

    @property
    def state_province(self):
        """Gets the state_province of this RoomLocationItem.  # noqa: E501

        State Province  # noqa: E501

        :return: The state_province of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._state_province

    @state_province.setter
    def state_province(self, state_province):
        """Sets the state_province of this RoomLocationItem.

        State Province  # noqa: E501

        :param state_province: The state_province of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if state_province is not None and len(state_province) > 60:
            raise ValueError("Invalid value for `state_province`, length must be less than or equal to `60`")  # noqa: E501

        self._state_province = state_province

    @property
    def zip_postcode(self):
        """Gets the zip_postcode of this RoomLocationItem.  # noqa: E501

        Zip Postcode  # noqa: E501

        :return: The zip_postcode of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._zip_postcode

    @zip_postcode.setter
    def zip_postcode(self, zip_postcode):
        """Sets the zip_postcode of this RoomLocationItem.

        Zip Postcode  # noqa: E501

        :param zip_postcode: The zip_postcode of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if zip_postcode is not None and len(zip_postcode) > 15:
            raise ValueError("Invalid value for `zip_postcode`, length must be less than or equal to `15`")  # noqa: E501

        self._zip_postcode = zip_postcode

    @property
    def gender_type_enum(self):
        """Gets the gender_type_enum of this RoomLocationItem.  # noqa: E501

        Gender Type  # noqa: E501

        :return: The gender_type_enum of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._gender_type_enum

    @gender_type_enum.setter
    def gender_type_enum(self, gender_type_enum):
        """Sets the gender_type_enum of this RoomLocationItem.

        Gender Type  # noqa: E501

        :param gender_type_enum: The gender_type_enum of this RoomLocationItem.  # noqa: E501
        :type: str
        """

        self._gender_type_enum = gender_type_enum

    @property
    def custom_bit1(self):
        """Gets the custom_bit1 of this RoomLocationItem.  # noqa: E501

        Custom Flag 1  # noqa: E501

        :return: The custom_bit1 of this RoomLocationItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit1

    @custom_bit1.setter
    def custom_bit1(self, custom_bit1):
        """Sets the custom_bit1 of this RoomLocationItem.

        Custom Flag 1  # noqa: E501

        :param custom_bit1: The custom_bit1 of this RoomLocationItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit1 = custom_bit1

    @property
    def custom_bit2(self):
        """Gets the custom_bit2 of this RoomLocationItem.  # noqa: E501

        Custom Flag 2  # noqa: E501

        :return: The custom_bit2 of this RoomLocationItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit2

    @custom_bit2.setter
    def custom_bit2(self, custom_bit2):
        """Sets the custom_bit2 of this RoomLocationItem.

        Custom Flag 2  # noqa: E501

        :param custom_bit2: The custom_bit2 of this RoomLocationItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit2 = custom_bit2

    @property
    def custom_string1(self):
        """Gets the custom_string1 of this RoomLocationItem.  # noqa: E501

        Custom String 1  # noqa: E501

        :return: The custom_string1 of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string1

    @custom_string1.setter
    def custom_string1(self, custom_string1):
        """Sets the custom_string1 of this RoomLocationItem.

        Custom String 1  # noqa: E501

        :param custom_string1: The custom_string1 of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if custom_string1 is not None and len(custom_string1) > 50:
            raise ValueError("Invalid value for `custom_string1`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string1 = custom_string1

    @property
    def custom_string2(self):
        """Gets the custom_string2 of this RoomLocationItem.  # noqa: E501

        Custom String 2  # noqa: E501

        :return: The custom_string2 of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string2

    @custom_string2.setter
    def custom_string2(self, custom_string2):
        """Sets the custom_string2 of this RoomLocationItem.

        Custom String 2  # noqa: E501

        :param custom_string2: The custom_string2 of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if custom_string2 is not None and len(custom_string2) > 50:
            raise ValueError("Invalid value for `custom_string2`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string2 = custom_string2

    @property
    def custom_string3(self):
        """Gets the custom_string3 of this RoomLocationItem.  # noqa: E501

        Custom String 3  # noqa: E501

        :return: The custom_string3 of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string3

    @custom_string3.setter
    def custom_string3(self, custom_string3):
        """Sets the custom_string3 of this RoomLocationItem.

        Custom String 3  # noqa: E501

        :param custom_string3: The custom_string3 of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if custom_string3 is not None and len(custom_string3) > 50:
            raise ValueError("Invalid value for `custom_string3`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string3 = custom_string3

    @property
    def custom_string4(self):
        """Gets the custom_string4 of this RoomLocationItem.  # noqa: E501

        Custom String 4  # noqa: E501

        :return: The custom_string4 of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string4

    @custom_string4.setter
    def custom_string4(self, custom_string4):
        """Sets the custom_string4 of this RoomLocationItem.

        Custom String 4  # noqa: E501

        :param custom_string4: The custom_string4 of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if custom_string4 is not None and len(custom_string4) > 50:
            raise ValueError("Invalid value for `custom_string4`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string4 = custom_string4

    @property
    def custom_string5(self):
        """Gets the custom_string5 of this RoomLocationItem.  # noqa: E501

        Custom String 5  # noqa: E501

        :return: The custom_string5 of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string5

    @custom_string5.setter
    def custom_string5(self, custom_string5):
        """Sets the custom_string5 of this RoomLocationItem.

        Custom String 5  # noqa: E501

        :param custom_string5: The custom_string5 of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if custom_string5 is not None and len(custom_string5) > 50:
            raise ValueError("Invalid value for `custom_string5`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string5 = custom_string5

    @property
    def custom_string6(self):
        """Gets the custom_string6 of this RoomLocationItem.  # noqa: E501

        Custom String 6  # noqa: E501

        :return: The custom_string6 of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string6

    @custom_string6.setter
    def custom_string6(self, custom_string6):
        """Sets the custom_string6 of this RoomLocationItem.

        Custom String 6  # noqa: E501

        :param custom_string6: The custom_string6 of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if custom_string6 is not None and len(custom_string6) > 50:
            raise ValueError("Invalid value for `custom_string6`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string6 = custom_string6

    @property
    def custom_date1(self):
        """Gets the custom_date1 of this RoomLocationItem.  # noqa: E501

        Custom Date 1  # noqa: E501

        :return: The custom_date1 of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date1

    @custom_date1.setter
    def custom_date1(self, custom_date1):
        """Sets the custom_date1 of this RoomLocationItem.

        Custom Date 1  # noqa: E501

        :param custom_date1: The custom_date1 of this RoomLocationItem.  # noqa: E501
        :type: str
        """

        self._custom_date1 = custom_date1

    @property
    def custom_date2(self):
        """Gets the custom_date2 of this RoomLocationItem.  # noqa: E501

        Custom Date 2  # noqa: E501

        :return: The custom_date2 of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date2

    @custom_date2.setter
    def custom_date2(self, custom_date2):
        """Sets the custom_date2 of this RoomLocationItem.

        Custom Date 2  # noqa: E501

        :param custom_date2: The custom_date2 of this RoomLocationItem.  # noqa: E501
        :type: str
        """

        self._custom_date2 = custom_date2

    @property
    def view_on_web(self):
        """Gets the view_on_web of this RoomLocationItem.  # noqa: E501

        View On Web  # noqa: E501

        :return: The view_on_web of this RoomLocationItem.  # noqa: E501
        :rtype: bool
        """
        return self._view_on_web

    @view_on_web.setter
    def view_on_web(self, view_on_web):
        """Sets the view_on_web of this RoomLocationItem.

        View On Web  # noqa: E501

        :param view_on_web: The view_on_web of this RoomLocationItem.  # noqa: E501
        :type: bool
        """

        self._view_on_web = view_on_web

    @property
    def web_image_location(self):
        """Gets the web_image_location of this RoomLocationItem.  # noqa: E501

        Web Image Location  # noqa: E501

        :return: The web_image_location of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._web_image_location

    @web_image_location.setter
    def web_image_location(self, web_image_location):
        """Sets the web_image_location of this RoomLocationItem.

        Web Image Location  # noqa: E501

        :param web_image_location: The web_image_location of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if web_image_location is not None and len(web_image_location) > 200:
            raise ValueError("Invalid value for `web_image_location`, length must be less than or equal to `200`")  # noqa: E501

        self._web_image_location = web_image_location

    @property
    def web_description(self):
        """Gets the web_description of this RoomLocationItem.  # noqa: E501

        Web Description  # noqa: E501

        :return: The web_description of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._web_description

    @web_description.setter
    def web_description(self, web_description):
        """Sets the web_description of this RoomLocationItem.

        Web Description  # noqa: E501

        :param web_description: The web_description of this RoomLocationItem.  # noqa: E501
        :type: str
        """
        if web_description is not None and len(web_description) > 1000:
            raise ValueError("Invalid value for `web_description`, length must be less than or equal to `1000`")  # noqa: E501

        self._web_description = web_description

    @property
    def web_comments(self):
        """Gets the web_comments of this RoomLocationItem.  # noqa: E501

        Web Comments  # noqa: E501

        :return: The web_comments of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._web_comments

    @web_comments.setter
    def web_comments(self, web_comments):
        """Sets the web_comments of this RoomLocationItem.

        Web Comments  # noqa: E501

        :param web_comments: The web_comments of this RoomLocationItem.  # noqa: E501
        :type: str
        """

        self._web_comments = web_comments

    @property
    def date_modified(self):
        """Gets the date_modified of this RoomLocationItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this RoomLocationItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this RoomLocationItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this RoomLocationItem.  # noqa: E501
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
        if not isinstance(other, RoomLocationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
