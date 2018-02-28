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


class SurveyItem(object):
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
        'survey_id': 'int',
        'description': 'str',
        'term_session_id': 'int',
        'survey_type_id': 'int',
        'code': 'str',
        'record_type_enum': 'str',
        'date_created': 'datetime',
        'security_user_id': 'int',
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
        'date_modified': 'str'
    }

    attribute_map = {
        'survey_id': 'SurveyID',
        'description': 'Description',
        'term_session_id': 'TermSessionID',
        'survey_type_id': 'SurveyTypeID',
        'code': 'Code',
        'record_type_enum': 'RecordTypeEnum',
        'date_created': 'DateCreated',
        'security_user_id': 'SecurityUserID',
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
        'date_modified': 'DateModified'
    }

    def __init__(self, survey_id=None, description=None, term_session_id=None, survey_type_id=None, code=None, record_type_enum=None, date_created=None, security_user_id=None, custom_bit1=None, custom_bit2=None, custom_string1=None, custom_string2=None, custom_string3=None, custom_string4=None, custom_string5=None, custom_string6=None, custom_date1=None, custom_date2=None, date_modified=None):  # noqa: E501
        """SurveyItem - a model defined in Swagger"""  # noqa: E501

        self._survey_id = None
        self._description = None
        self._term_session_id = None
        self._survey_type_id = None
        self._code = None
        self._record_type_enum = None
        self._date_created = None
        self._security_user_id = None
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
        self._date_modified = None
        self.discriminator = None

        if survey_id is not None:
            self.survey_id = survey_id
        if description is not None:
            self.description = description
        if term_session_id is not None:
            self.term_session_id = term_session_id
        if survey_type_id is not None:
            self.survey_type_id = survey_type_id
        if code is not None:
            self.code = code
        if record_type_enum is not None:
            self.record_type_enum = record_type_enum
        if date_created is not None:
            self.date_created = date_created
        if security_user_id is not None:
            self.security_user_id = security_user_id
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
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def survey_id(self):
        """Gets the survey_id of this SurveyItem.  # noqa: E501

        Survey  # noqa: E501

        :return: The survey_id of this SurveyItem.  # noqa: E501
        :rtype: int
        """
        return self._survey_id

    @survey_id.setter
    def survey_id(self, survey_id):
        """Sets the survey_id of this SurveyItem.

        Survey  # noqa: E501

        :param survey_id: The survey_id of this SurveyItem.  # noqa: E501
        :type: int
        """

        self._survey_id = survey_id

    @property
    def description(self):
        """Gets the description of this SurveyItem.  # noqa: E501

        Description  # noqa: E501

        :return: The description of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SurveyItem.

        Description  # noqa: E501

        :param description: The description of this SurveyItem.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501

        self._description = description

    @property
    def term_session_id(self):
        """Gets the term_session_id of this SurveyItem.  # noqa: E501

        Term Session  # noqa: E501

        :return: The term_session_id of this SurveyItem.  # noqa: E501
        :rtype: int
        """
        return self._term_session_id

    @term_session_id.setter
    def term_session_id(self, term_session_id):
        """Sets the term_session_id of this SurveyItem.

        Term Session  # noqa: E501

        :param term_session_id: The term_session_id of this SurveyItem.  # noqa: E501
        :type: int
        """

        self._term_session_id = term_session_id

    @property
    def survey_type_id(self):
        """Gets the survey_type_id of this SurveyItem.  # noqa: E501

        Survey Type  # noqa: E501

        :return: The survey_type_id of this SurveyItem.  # noqa: E501
        :rtype: int
        """
        return self._survey_type_id

    @survey_type_id.setter
    def survey_type_id(self, survey_type_id):
        """Sets the survey_type_id of this SurveyItem.

        Survey Type  # noqa: E501

        :param survey_type_id: The survey_type_id of this SurveyItem.  # noqa: E501
        :type: int
        """

        self._survey_type_id = survey_type_id

    @property
    def code(self):
        """Gets the code of this SurveyItem.  # noqa: E501

        Code  # noqa: E501

        :return: The code of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SurveyItem.

        Code  # noqa: E501

        :param code: The code of this SurveyItem.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) > 20:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `20`")  # noqa: E501

        self._code = code

    @property
    def record_type_enum(self):
        """Gets the record_type_enum of this SurveyItem.  # noqa: E501

        Record Type  # noqa: E501

        :return: The record_type_enum of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._record_type_enum

    @record_type_enum.setter
    def record_type_enum(self, record_type_enum):
        """Sets the record_type_enum of this SurveyItem.

        Record Type  # noqa: E501

        :param record_type_enum: The record_type_enum of this SurveyItem.  # noqa: E501
        :type: str
        """

        self._record_type_enum = record_type_enum

    @property
    def date_created(self):
        """Gets the date_created of this SurveyItem.  # noqa: E501

        Date Created  # noqa: E501

        :return: The date_created of this SurveyItem.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SurveyItem.

        Date Created  # noqa: E501

        :param date_created: The date_created of this SurveyItem.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def security_user_id(self):
        """Gets the security_user_id of this SurveyItem.  # noqa: E501

        Security User  # noqa: E501

        :return: The security_user_id of this SurveyItem.  # noqa: E501
        :rtype: int
        """
        return self._security_user_id

    @security_user_id.setter
    def security_user_id(self, security_user_id):
        """Sets the security_user_id of this SurveyItem.

        Security User  # noqa: E501

        :param security_user_id: The security_user_id of this SurveyItem.  # noqa: E501
        :type: int
        """

        self._security_user_id = security_user_id

    @property
    def custom_bit1(self):
        """Gets the custom_bit1 of this SurveyItem.  # noqa: E501

        Custom Flag 1  # noqa: E501

        :return: The custom_bit1 of this SurveyItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit1

    @custom_bit1.setter
    def custom_bit1(self, custom_bit1):
        """Sets the custom_bit1 of this SurveyItem.

        Custom Flag 1  # noqa: E501

        :param custom_bit1: The custom_bit1 of this SurveyItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit1 = custom_bit1

    @property
    def custom_bit2(self):
        """Gets the custom_bit2 of this SurveyItem.  # noqa: E501

        Custom Flag 2  # noqa: E501

        :return: The custom_bit2 of this SurveyItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit2

    @custom_bit2.setter
    def custom_bit2(self, custom_bit2):
        """Sets the custom_bit2 of this SurveyItem.

        Custom Flag 2  # noqa: E501

        :param custom_bit2: The custom_bit2 of this SurveyItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit2 = custom_bit2

    @property
    def custom_string1(self):
        """Gets the custom_string1 of this SurveyItem.  # noqa: E501

        Custom String 1  # noqa: E501

        :return: The custom_string1 of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string1

    @custom_string1.setter
    def custom_string1(self, custom_string1):
        """Sets the custom_string1 of this SurveyItem.

        Custom String 1  # noqa: E501

        :param custom_string1: The custom_string1 of this SurveyItem.  # noqa: E501
        :type: str
        """
        if custom_string1 is not None and len(custom_string1) > 50:
            raise ValueError("Invalid value for `custom_string1`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string1 = custom_string1

    @property
    def custom_string2(self):
        """Gets the custom_string2 of this SurveyItem.  # noqa: E501

        Custom String 2  # noqa: E501

        :return: The custom_string2 of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string2

    @custom_string2.setter
    def custom_string2(self, custom_string2):
        """Sets the custom_string2 of this SurveyItem.

        Custom String 2  # noqa: E501

        :param custom_string2: The custom_string2 of this SurveyItem.  # noqa: E501
        :type: str
        """
        if custom_string2 is not None and len(custom_string2) > 50:
            raise ValueError("Invalid value for `custom_string2`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string2 = custom_string2

    @property
    def custom_string3(self):
        """Gets the custom_string3 of this SurveyItem.  # noqa: E501

        Custom String 3  # noqa: E501

        :return: The custom_string3 of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string3

    @custom_string3.setter
    def custom_string3(self, custom_string3):
        """Sets the custom_string3 of this SurveyItem.

        Custom String 3  # noqa: E501

        :param custom_string3: The custom_string3 of this SurveyItem.  # noqa: E501
        :type: str
        """
        if custom_string3 is not None and len(custom_string3) > 50:
            raise ValueError("Invalid value for `custom_string3`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string3 = custom_string3

    @property
    def custom_string4(self):
        """Gets the custom_string4 of this SurveyItem.  # noqa: E501

        Custom String 4  # noqa: E501

        :return: The custom_string4 of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string4

    @custom_string4.setter
    def custom_string4(self, custom_string4):
        """Sets the custom_string4 of this SurveyItem.

        Custom String 4  # noqa: E501

        :param custom_string4: The custom_string4 of this SurveyItem.  # noqa: E501
        :type: str
        """
        if custom_string4 is not None and len(custom_string4) > 50:
            raise ValueError("Invalid value for `custom_string4`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string4 = custom_string4

    @property
    def custom_string5(self):
        """Gets the custom_string5 of this SurveyItem.  # noqa: E501

        Custom String 5  # noqa: E501

        :return: The custom_string5 of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string5

    @custom_string5.setter
    def custom_string5(self, custom_string5):
        """Sets the custom_string5 of this SurveyItem.

        Custom String 5  # noqa: E501

        :param custom_string5: The custom_string5 of this SurveyItem.  # noqa: E501
        :type: str
        """
        if custom_string5 is not None and len(custom_string5) > 50:
            raise ValueError("Invalid value for `custom_string5`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string5 = custom_string5

    @property
    def custom_string6(self):
        """Gets the custom_string6 of this SurveyItem.  # noqa: E501

        Custom String 6  # noqa: E501

        :return: The custom_string6 of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string6

    @custom_string6.setter
    def custom_string6(self, custom_string6):
        """Sets the custom_string6 of this SurveyItem.

        Custom String 6  # noqa: E501

        :param custom_string6: The custom_string6 of this SurveyItem.  # noqa: E501
        :type: str
        """
        if custom_string6 is not None and len(custom_string6) > 50:
            raise ValueError("Invalid value for `custom_string6`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string6 = custom_string6

    @property
    def custom_date1(self):
        """Gets the custom_date1 of this SurveyItem.  # noqa: E501

        Custom Date 1  # noqa: E501

        :return: The custom_date1 of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date1

    @custom_date1.setter
    def custom_date1(self, custom_date1):
        """Sets the custom_date1 of this SurveyItem.

        Custom Date 1  # noqa: E501

        :param custom_date1: The custom_date1 of this SurveyItem.  # noqa: E501
        :type: str
        """

        self._custom_date1 = custom_date1

    @property
    def custom_date2(self):
        """Gets the custom_date2 of this SurveyItem.  # noqa: E501

        Custom Date 2  # noqa: E501

        :return: The custom_date2 of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date2

    @custom_date2.setter
    def custom_date2(self, custom_date2):
        """Sets the custom_date2 of this SurveyItem.

        Custom Date 2  # noqa: E501

        :param custom_date2: The custom_date2 of this SurveyItem.  # noqa: E501
        :type: str
        """

        self._custom_date2 = custom_date2

    @property
    def date_modified(self):
        """Gets the date_modified of this SurveyItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this SurveyItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SurveyItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this SurveyItem.  # noqa: E501
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
        if not isinstance(other, SurveyItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other