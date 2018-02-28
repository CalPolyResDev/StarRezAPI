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


class PromoCodeRecordItem(object):
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
        'promo_code_record_id': 'int',
        'promo_code_id': 'int',
        'table_id': 'int',
        'table_name': 'str',
        'security_user_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'promo_code_record_id': 'PromoCodeRecordID',
        'promo_code_id': 'PromoCodeID',
        'table_id': 'TableID',
        'table_name': 'TableName',
        'security_user_id': 'SecurityUserID',
        'date_modified': 'DateModified'
    }

    def __init__(self, promo_code_record_id=None, promo_code_id=None, table_id=None, table_name=None, security_user_id=None, date_modified=None):  # noqa: E501
        """PromoCodeRecordItem - a model defined in Swagger"""  # noqa: E501

        self._promo_code_record_id = None
        self._promo_code_id = None
        self._table_id = None
        self._table_name = None
        self._security_user_id = None
        self._date_modified = None
        self.discriminator = None

        if promo_code_record_id is not None:
            self.promo_code_record_id = promo_code_record_id
        if promo_code_id is not None:
            self.promo_code_id = promo_code_id
        if table_id is not None:
            self.table_id = table_id
        if table_name is not None:
            self.table_name = table_name
        if security_user_id is not None:
            self.security_user_id = security_user_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def promo_code_record_id(self):
        """Gets the promo_code_record_id of this PromoCodeRecordItem.  # noqa: E501

        Promo Code Record  # noqa: E501

        :return: The promo_code_record_id of this PromoCodeRecordItem.  # noqa: E501
        :rtype: int
        """
        return self._promo_code_record_id

    @promo_code_record_id.setter
    def promo_code_record_id(self, promo_code_record_id):
        """Sets the promo_code_record_id of this PromoCodeRecordItem.

        Promo Code Record  # noqa: E501

        :param promo_code_record_id: The promo_code_record_id of this PromoCodeRecordItem.  # noqa: E501
        :type: int
        """

        self._promo_code_record_id = promo_code_record_id

    @property
    def promo_code_id(self):
        """Gets the promo_code_id of this PromoCodeRecordItem.  # noqa: E501

        Promo Code  # noqa: E501

        :return: The promo_code_id of this PromoCodeRecordItem.  # noqa: E501
        :rtype: int
        """
        return self._promo_code_id

    @promo_code_id.setter
    def promo_code_id(self, promo_code_id):
        """Sets the promo_code_id of this PromoCodeRecordItem.

        Promo Code  # noqa: E501

        :param promo_code_id: The promo_code_id of this PromoCodeRecordItem.  # noqa: E501
        :type: int
        """

        self._promo_code_id = promo_code_id

    @property
    def table_id(self):
        """Gets the table_id of this PromoCodeRecordItem.  # noqa: E501

        Table  # noqa: E501

        :return: The table_id of this PromoCodeRecordItem.  # noqa: E501
        :rtype: int
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this PromoCodeRecordItem.

        Table  # noqa: E501

        :param table_id: The table_id of this PromoCodeRecordItem.  # noqa: E501
        :type: int
        """

        self._table_id = table_id

    @property
    def table_name(self):
        """Gets the table_name of this PromoCodeRecordItem.  # noqa: E501

        Table Name  # noqa: E501

        :return: The table_name of this PromoCodeRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this PromoCodeRecordItem.

        Table Name  # noqa: E501

        :param table_name: The table_name of this PromoCodeRecordItem.  # noqa: E501
        :type: str
        """
        if table_name is not None and len(table_name) > 100:
            raise ValueError("Invalid value for `table_name`, length must be less than or equal to `100`")  # noqa: E501

        self._table_name = table_name

    @property
    def security_user_id(self):
        """Gets the security_user_id of this PromoCodeRecordItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this PromoCodeRecordItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this PromoCodeRecordItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this PromoCodeRecordItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def date_modified(self):
        """Gets the date_modified of this PromoCodeRecordItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this PromoCodeRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this PromoCodeRecordItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this PromoCodeRecordItem.  # noqa: E501
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
        if not isinstance(other, PromoCodeRecordItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
