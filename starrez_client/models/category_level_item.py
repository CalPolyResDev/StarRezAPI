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


class CategoryLevelItem(object):
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
        'category_id': 'int',
        'level1': 'str',
        'level1_id': 'int',
        'level2': 'str',
        'level2_id': 'int',
        'level3': 'str',
        'level3_id': 'int',
        'level4': 'str',
        'level4_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'category_id': 'CategoryID',
        'level1': 'Level1',
        'level1_id': 'Level1ID',
        'level2': 'Level2',
        'level2_id': 'Level2ID',
        'level3': 'Level3',
        'level3_id': 'Level3ID',
        'level4': 'Level4',
        'level4_id': 'Level4ID',
        'date_modified': 'DateModified'
    }

    def __init__(self, category_id=None, level1=None, level1_id=None, level2=None, level2_id=None, level3=None, level3_id=None, level4=None, level4_id=None, date_modified=None):  # noqa: E501
        """CategoryLevelItem - a model defined in Swagger"""  # noqa: E501

        self._category_id = None
        self._level1 = None
        self._level1_id = None
        self._level2 = None
        self._level2_id = None
        self._level3 = None
        self._level3_id = None
        self._level4 = None
        self._level4_id = None
        self._date_modified = None
        self.discriminator = None

        if category_id is not None:
            self.category_id = category_id
        if level1 is not None:
            self.level1 = level1
        if level1_id is not None:
            self.level1_id = level1_id
        if level2 is not None:
            self.level2 = level2
        if level2_id is not None:
            self.level2_id = level2_id
        if level3 is not None:
            self.level3 = level3
        if level3_id is not None:
            self.level3_id = level3_id
        if level4 is not None:
            self.level4 = level4
        if level4_id is not None:
            self.level4_id = level4_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def category_id(self):
        """Gets the category_id of this CategoryLevelItem.  # noqa: E501

        Category  # noqa: E501

        :return: The category_id of this CategoryLevelItem.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this CategoryLevelItem.

        Category  # noqa: E501

        :param category_id: The category_id of this CategoryLevelItem.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def level1(self):
        """Gets the level1 of this CategoryLevelItem.  # noqa: E501

        Level 1  # noqa: E501

        :return: The level1 of this CategoryLevelItem.  # noqa: E501
        :rtype: str
        """
        return self._level1

    @level1.setter
    def level1(self, level1):
        """Sets the level1 of this CategoryLevelItem.

        Level 1  # noqa: E501

        :param level1: The level1 of this CategoryLevelItem.  # noqa: E501
        :type: str
        """
        if level1 is not None and len(level1) > 100:
            raise ValueError("Invalid value for `level1`, length must be less than or equal to `100`")  # noqa: E501

        self._level1 = level1

    @property
    def level1_id(self):
        """Gets the level1_id of this CategoryLevelItem.  # noqa: E501

        Level 1  # noqa: E501

        :return: The level1_id of this CategoryLevelItem.  # noqa: E501
        :rtype: int
        """
        return self._level1_id

    @level1_id.setter
    def level1_id(self, level1_id):
        """Sets the level1_id of this CategoryLevelItem.

        Level 1  # noqa: E501

        :param level1_id: The level1_id of this CategoryLevelItem.  # noqa: E501
        :type: int
        """

        self._level1_id = level1_id

    @property
    def level2(self):
        """Gets the level2 of this CategoryLevelItem.  # noqa: E501

        Level 2  # noqa: E501

        :return: The level2 of this CategoryLevelItem.  # noqa: E501
        :rtype: str
        """
        return self._level2

    @level2.setter
    def level2(self, level2):
        """Sets the level2 of this CategoryLevelItem.

        Level 2  # noqa: E501

        :param level2: The level2 of this CategoryLevelItem.  # noqa: E501
        :type: str
        """
        if level2 is not None and len(level2) > 100:
            raise ValueError("Invalid value for `level2`, length must be less than or equal to `100`")  # noqa: E501

        self._level2 = level2

    @property
    def level2_id(self):
        """Gets the level2_id of this CategoryLevelItem.  # noqa: E501

        Level 2  # noqa: E501

        :return: The level2_id of this CategoryLevelItem.  # noqa: E501
        :rtype: int
        """
        return self._level2_id

    @level2_id.setter
    def level2_id(self, level2_id):
        """Sets the level2_id of this CategoryLevelItem.

        Level 2  # noqa: E501

        :param level2_id: The level2_id of this CategoryLevelItem.  # noqa: E501
        :type: int
        """

        self._level2_id = level2_id

    @property
    def level3(self):
        """Gets the level3 of this CategoryLevelItem.  # noqa: E501

        Level 3  # noqa: E501

        :return: The level3 of this CategoryLevelItem.  # noqa: E501
        :rtype: str
        """
        return self._level3

    @level3.setter
    def level3(self, level3):
        """Sets the level3 of this CategoryLevelItem.

        Level 3  # noqa: E501

        :param level3: The level3 of this CategoryLevelItem.  # noqa: E501
        :type: str
        """
        if level3 is not None and len(level3) > 100:
            raise ValueError("Invalid value for `level3`, length must be less than or equal to `100`")  # noqa: E501

        self._level3 = level3

    @property
    def level3_id(self):
        """Gets the level3_id of this CategoryLevelItem.  # noqa: E501

        Level 3  # noqa: E501

        :return: The level3_id of this CategoryLevelItem.  # noqa: E501
        :rtype: int
        """
        return self._level3_id

    @level3_id.setter
    def level3_id(self, level3_id):
        """Sets the level3_id of this CategoryLevelItem.

        Level 3  # noqa: E501

        :param level3_id: The level3_id of this CategoryLevelItem.  # noqa: E501
        :type: int
        """

        self._level3_id = level3_id

    @property
    def level4(self):
        """Gets the level4 of this CategoryLevelItem.  # noqa: E501

        Level 4  # noqa: E501

        :return: The level4 of this CategoryLevelItem.  # noqa: E501
        :rtype: str
        """
        return self._level4

    @level4.setter
    def level4(self, level4):
        """Sets the level4 of this CategoryLevelItem.

        Level 4  # noqa: E501

        :param level4: The level4 of this CategoryLevelItem.  # noqa: E501
        :type: str
        """
        if level4 is not None and len(level4) > 100:
            raise ValueError("Invalid value for `level4`, length must be less than or equal to `100`")  # noqa: E501

        self._level4 = level4

    @property
    def level4_id(self):
        """Gets the level4_id of this CategoryLevelItem.  # noqa: E501

        Level 4  # noqa: E501

        :return: The level4_id of this CategoryLevelItem.  # noqa: E501
        :rtype: int
        """
        return self._level4_id

    @level4_id.setter
    def level4_id(self, level4_id):
        """Sets the level4_id of this CategoryLevelItem.

        Level 4  # noqa: E501

        :param level4_id: The level4_id of this CategoryLevelItem.  # noqa: E501
        :type: int
        """

        self._level4_id = level4_id

    @property
    def date_modified(self):
        """Gets the date_modified of this CategoryLevelItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this CategoryLevelItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this CategoryLevelItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this CategoryLevelItem.  # noqa: E501
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
        if not isinstance(other, CategoryLevelItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
