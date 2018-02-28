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


class ConcernEntryItem(object):
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
        'concern_entry_id': 'int',
        'concern_id': 'int',
        'entry_id': 'int',
        'identity_known': 'bool',
        'name': 'str',
        'demographic': 'str',
        'gender_enum': 'str',
        'race': 'str',
        'religion': 'str',
        'ethnicity': 'str',
        'height': 'str',
        'weight': 'str',
        'hair_colour': 'str',
        'eye_colour': 'str',
        'age': 'str',
        'comments': 'str',
        'involvement_type': 'str',
        'involvement_comments': 'str',
        'workflow_step_id': 'int',
        'assigned_to_security_user_id': 'int',
        'current_workflow_history_id': 'int',
        'previous_workflow_history_id': 'int',
        'date_modified': 'str'
    }

    attribute_map = {
        'concern_entry_id': 'ConcernEntryID',
        'concern_id': 'ConcernID',
        'entry_id': 'EntryID',
        'identity_known': 'IdentityKnown',
        'name': 'Name',
        'demographic': 'Demographic',
        'gender_enum': 'GenderEnum',
        'race': 'Race',
        'religion': 'Religion',
        'ethnicity': 'Ethnicity',
        'height': 'Height',
        'weight': 'Weight',
        'hair_colour': 'HairColour',
        'eye_colour': 'EyeColour',
        'age': 'Age',
        'comments': 'Comments',
        'involvement_type': 'InvolvementType',
        'involvement_comments': 'InvolvementComments',
        'workflow_step_id': 'WorkflowStepID',
        'assigned_to_security_user_id': 'AssignedTo_SecurityUserID',
        'current_workflow_history_id': 'Current_WorkflowHistoryID',
        'previous_workflow_history_id': 'Previous_WorkflowHistoryID',
        'date_modified': 'DateModified'
    }

    def __init__(self, concern_entry_id=None, concern_id=None, entry_id=None, identity_known=None, name=None, demographic=None, gender_enum=None, race=None, religion=None, ethnicity=None, height=None, weight=None, hair_colour=None, eye_colour=None, age=None, comments=None, involvement_type=None, involvement_comments=None, workflow_step_id=None, assigned_to_security_user_id=None, current_workflow_history_id=None, previous_workflow_history_id=None, date_modified=None):  # noqa: E501
        """ConcernEntryItem - a model defined in Swagger"""  # noqa: E501

        self._concern_entry_id = None
        self._concern_id = None
        self._entry_id = None
        self._identity_known = None
        self._name = None
        self._demographic = None
        self._gender_enum = None
        self._race = None
        self._religion = None
        self._ethnicity = None
        self._height = None
        self._weight = None
        self._hair_colour = None
        self._eye_colour = None
        self._age = None
        self._comments = None
        self._involvement_type = None
        self._involvement_comments = None
        self._workflow_step_id = None
        self._assigned_to_security_user_id = None
        self._current_workflow_history_id = None
        self._previous_workflow_history_id = None
        self._date_modified = None
        self.discriminator = None

        if concern_entry_id is not None:
            self.concern_entry_id = concern_entry_id
        if concern_id is not None:
            self.concern_id = concern_id
        if entry_id is not None:
            self.entry_id = entry_id
        if identity_known is not None:
            self.identity_known = identity_known
        if name is not None:
            self.name = name
        if demographic is not None:
            self.demographic = demographic
        if gender_enum is not None:
            self.gender_enum = gender_enum
        if race is not None:
            self.race = race
        if religion is not None:
            self.religion = religion
        if ethnicity is not None:
            self.ethnicity = ethnicity
        if height is not None:
            self.height = height
        if weight is not None:
            self.weight = weight
        if hair_colour is not None:
            self.hair_colour = hair_colour
        if eye_colour is not None:
            self.eye_colour = eye_colour
        if age is not None:
            self.age = age
        if comments is not None:
            self.comments = comments
        if involvement_type is not None:
            self.involvement_type = involvement_type
        if involvement_comments is not None:
            self.involvement_comments = involvement_comments
        if workflow_step_id is not None:
            self.workflow_step_id = workflow_step_id
        if assigned_to_security_user_id is not None:
            self.assigned_to_security_user_id = assigned_to_security_user_id
        if current_workflow_history_id is not None:
            self.current_workflow_history_id = current_workflow_history_id
        if previous_workflow_history_id is not None:
            self.previous_workflow_history_id = previous_workflow_history_id
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def concern_entry_id(self):
        """Gets the concern_entry_id of this ConcernEntryItem.  # noqa: E501

        Concern Entry  # noqa: E501

        :return: The concern_entry_id of this ConcernEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._concern_entry_id

    @concern_entry_id.setter
    def concern_entry_id(self, concern_entry_id):
        """Sets the concern_entry_id of this ConcernEntryItem.

        Concern Entry  # noqa: E501

        :param concern_entry_id: The concern_entry_id of this ConcernEntryItem.  # noqa: E501
        :type: int
        """

        self._concern_entry_id = concern_entry_id

    @property
    def concern_id(self):
        """Gets the concern_id of this ConcernEntryItem.  # noqa: E501

        Concern  # noqa: E501

        :return: The concern_id of this ConcernEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._concern_id

    @concern_id.setter
    def concern_id(self, concern_id):
        """Sets the concern_id of this ConcernEntryItem.

        Concern  # noqa: E501

        :param concern_id: The concern_id of this ConcernEntryItem.  # noqa: E501
        :type: int
        """

        self._concern_id = concern_id

    @property
    def entry_id(self):
        """Gets the entry_id of this ConcernEntryItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this ConcernEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this ConcernEntryItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this ConcernEntryItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def identity_known(self):
        """Gets the identity_known of this ConcernEntryItem.  # noqa: E501

        Identity Known  # noqa: E501

        :return: The identity_known of this ConcernEntryItem.  # noqa: E501
        :rtype: bool
        """
        return self._identity_known

    @identity_known.setter
    def identity_known(self, identity_known):
        """Sets the identity_known of this ConcernEntryItem.

        Identity Known  # noqa: E501

        :param identity_known: The identity_known of this ConcernEntryItem.  # noqa: E501
        :type: bool
        """

        self._identity_known = identity_known

    @property
    def name(self):
        """Gets the name of this ConcernEntryItem.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConcernEntryItem.

        Name  # noqa: E501

        :param name: The name of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def demographic(self):
        """Gets the demographic of this ConcernEntryItem.  # noqa: E501

        Demographic  # noqa: E501

        :return: The demographic of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._demographic

    @demographic.setter
    def demographic(self, demographic):
        """Sets the demographic of this ConcernEntryItem.

        Demographic  # noqa: E501

        :param demographic: The demographic of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if demographic is not None and len(demographic) > 30:
            raise ValueError("Invalid value for `demographic`, length must be less than or equal to `30`")  # noqa: E501

        self._demographic = demographic

    @property
    def gender_enum(self):
        """Gets the gender_enum of this ConcernEntryItem.  # noqa: E501

        Gender  # noqa: E501

        :return: The gender_enum of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._gender_enum

    @gender_enum.setter
    def gender_enum(self, gender_enum):
        """Sets the gender_enum of this ConcernEntryItem.

        Gender  # noqa: E501

        :param gender_enum: The gender_enum of this ConcernEntryItem.  # noqa: E501
        :type: str
        """

        self._gender_enum = gender_enum

    @property
    def race(self):
        """Gets the race of this ConcernEntryItem.  # noqa: E501

        Race  # noqa: E501

        :return: The race of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._race

    @race.setter
    def race(self, race):
        """Sets the race of this ConcernEntryItem.

        Race  # noqa: E501

        :param race: The race of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if race is not None and len(race) > 20:
            raise ValueError("Invalid value for `race`, length must be less than or equal to `20`")  # noqa: E501

        self._race = race

    @property
    def religion(self):
        """Gets the religion of this ConcernEntryItem.  # noqa: E501

        Religion  # noqa: E501

        :return: The religion of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._religion

    @religion.setter
    def religion(self, religion):
        """Sets the religion of this ConcernEntryItem.

        Religion  # noqa: E501

        :param religion: The religion of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if religion is not None and len(religion) > 20:
            raise ValueError("Invalid value for `religion`, length must be less than or equal to `20`")  # noqa: E501

        self._religion = religion

    @property
    def ethnicity(self):
        """Gets the ethnicity of this ConcernEntryItem.  # noqa: E501

        Ethnicity  # noqa: E501

        :return: The ethnicity of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._ethnicity

    @ethnicity.setter
    def ethnicity(self, ethnicity):
        """Sets the ethnicity of this ConcernEntryItem.

        Ethnicity  # noqa: E501

        :param ethnicity: The ethnicity of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if ethnicity is not None and len(ethnicity) > 20:
            raise ValueError("Invalid value for `ethnicity`, length must be less than or equal to `20`")  # noqa: E501

        self._ethnicity = ethnicity

    @property
    def height(self):
        """Gets the height of this ConcernEntryItem.  # noqa: E501

        Height  # noqa: E501

        :return: The height of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ConcernEntryItem.

        Height  # noqa: E501

        :param height: The height of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if height is not None and len(height) > 20:
            raise ValueError("Invalid value for `height`, length must be less than or equal to `20`")  # noqa: E501

        self._height = height

    @property
    def weight(self):
        """Gets the weight of this ConcernEntryItem.  # noqa: E501

        Weight  # noqa: E501

        :return: The weight of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ConcernEntryItem.

        Weight  # noqa: E501

        :param weight: The weight of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if weight is not None and len(weight) > 20:
            raise ValueError("Invalid value for `weight`, length must be less than or equal to `20`")  # noqa: E501

        self._weight = weight

    @property
    def hair_colour(self):
        """Gets the hair_colour of this ConcernEntryItem.  # noqa: E501

        Hair Colour  # noqa: E501

        :return: The hair_colour of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._hair_colour

    @hair_colour.setter
    def hair_colour(self, hair_colour):
        """Sets the hair_colour of this ConcernEntryItem.

        Hair Colour  # noqa: E501

        :param hair_colour: The hair_colour of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if hair_colour is not None and len(hair_colour) > 20:
            raise ValueError("Invalid value for `hair_colour`, length must be less than or equal to `20`")  # noqa: E501

        self._hair_colour = hair_colour

    @property
    def eye_colour(self):
        """Gets the eye_colour of this ConcernEntryItem.  # noqa: E501

        Eye Colour  # noqa: E501

        :return: The eye_colour of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._eye_colour

    @eye_colour.setter
    def eye_colour(self, eye_colour):
        """Sets the eye_colour of this ConcernEntryItem.

        Eye Colour  # noqa: E501

        :param eye_colour: The eye_colour of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if eye_colour is not None and len(eye_colour) > 20:
            raise ValueError("Invalid value for `eye_colour`, length must be less than or equal to `20`")  # noqa: E501

        self._eye_colour = eye_colour

    @property
    def age(self):
        """Gets the age of this ConcernEntryItem.  # noqa: E501

        Age  # noqa: E501

        :return: The age of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this ConcernEntryItem.

        Age  # noqa: E501

        :param age: The age of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if age is not None and len(age) > 20:
            raise ValueError("Invalid value for `age`, length must be less than or equal to `20`")  # noqa: E501

        self._age = age

    @property
    def comments(self):
        """Gets the comments of this ConcernEntryItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ConcernEntryItem.

        Comments  # noqa: E501

        :param comments: The comments of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 500:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `500`")  # noqa: E501

        self._comments = comments

    @property
    def involvement_type(self):
        """Gets the involvement_type of this ConcernEntryItem.  # noqa: E501

        Involvement Type  # noqa: E501

        :return: The involvement_type of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._involvement_type

    @involvement_type.setter
    def involvement_type(self, involvement_type):
        """Sets the involvement_type of this ConcernEntryItem.

        Involvement Type  # noqa: E501

        :param involvement_type: The involvement_type of this ConcernEntryItem.  # noqa: E501
        :type: str
        """
        if involvement_type is not None and len(involvement_type) > 50:
            raise ValueError("Invalid value for `involvement_type`, length must be less than or equal to `50`")  # noqa: E501

        self._involvement_type = involvement_type

    @property
    def involvement_comments(self):
        """Gets the involvement_comments of this ConcernEntryItem.  # noqa: E501

        Involvement Comments  # noqa: E501

        :return: The involvement_comments of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._involvement_comments

    @involvement_comments.setter
    def involvement_comments(self, involvement_comments):
        """Sets the involvement_comments of this ConcernEntryItem.

        Involvement Comments  # noqa: E501

        :param involvement_comments: The involvement_comments of this ConcernEntryItem.  # noqa: E501
        :type: str
        """

        self._involvement_comments = involvement_comments

    @property
    def workflow_step_id(self):
        """Gets the workflow_step_id of this ConcernEntryItem.  # noqa: E501

        Workflow Step  # noqa: E501

        :return: The workflow_step_id of this ConcernEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._workflow_step_id

    @workflow_step_id.setter
    def workflow_step_id(self, workflow_step_id):
        """Sets the workflow_step_id of this ConcernEntryItem.

        Workflow Step  # noqa: E501

        :param workflow_step_id: The workflow_step_id of this ConcernEntryItem.  # noqa: E501
        :type: int
        """

        self._workflow_step_id = workflow_step_id

    @property
    def assigned_to_security_user_id(self):
        """Gets the assigned_to_security_user_id of this ConcernEntryItem.  # noqa: E501

        Assigned To Security User  # noqa: E501

        :return: The assigned_to_security_user_id of this ConcernEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_security_user_id

    @assigned_to_security_user_id.setter
    def assigned_to_security_user_id(self, assigned_to_security_user_id):
        """Sets the assigned_to_security_user_id of this ConcernEntryItem.

        Assigned To Security User  # noqa: E501

        :param assigned_to_security_user_id: The assigned_to_security_user_id of this ConcernEntryItem.  # noqa: E501
        :type: int
        """

        self._assigned_to_security_user_id = assigned_to_security_user_id

    @property
    def current_workflow_history_id(self):
        """Gets the current_workflow_history_id of this ConcernEntryItem.  # noqa: E501

        Current Workflow History  # noqa: E501

        :return: The current_workflow_history_id of this ConcernEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._current_workflow_history_id

    @current_workflow_history_id.setter
    def current_workflow_history_id(self, current_workflow_history_id):
        """Sets the current_workflow_history_id of this ConcernEntryItem.

        Current Workflow History  # noqa: E501

        :param current_workflow_history_id: The current_workflow_history_id of this ConcernEntryItem.  # noqa: E501
        :type: int
        """

        self._current_workflow_history_id = current_workflow_history_id

    @property
    def previous_workflow_history_id(self):
        """Gets the previous_workflow_history_id of this ConcernEntryItem.  # noqa: E501

        Previous Workflow History  # noqa: E501

        :return: The previous_workflow_history_id of this ConcernEntryItem.  # noqa: E501
        :rtype: int
        """
        return self._previous_workflow_history_id

    @previous_workflow_history_id.setter
    def previous_workflow_history_id(self, previous_workflow_history_id):
        """Sets the previous_workflow_history_id of this ConcernEntryItem.

        Previous Workflow History  # noqa: E501

        :param previous_workflow_history_id: The previous_workflow_history_id of this ConcernEntryItem.  # noqa: E501
        :type: int
        """

        self._previous_workflow_history_id = previous_workflow_history_id

    @property
    def date_modified(self):
        """Gets the date_modified of this ConcernEntryItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this ConcernEntryItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ConcernEntryItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this ConcernEntryItem.  # noqa: E501
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
        if not isinstance(other, ConcernEntryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
