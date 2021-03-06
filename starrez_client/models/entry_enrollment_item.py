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


class EntryEnrollmentItem(object):
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
        'entry_enrollment_id': 'int',
        'entry_id': 'int',
        'enrollment_type_enum': 'str',
        'course_id': 'int',
        'term_id': 'int',
        'enrollment_order': 'int',
        'enrollment_field': 'str',
        'sequence': 'int',
        'institution': 'str',
        'campus': 'str',
        'faculty': 'str',
        'department': 'str',
        'major': 'str',
        'major_category': 'str',
        'minor': 'str',
        'is_enrolled': 'bool',
        'full_time': 'bool',
        'post_grad': 'bool',
        'graduation_date': 'str',
        'subjects': 'str',
        'years': 'str',
        'comments': 'str',
        'date_start': 'str',
        'date_end': 'str',
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
        'entry_enrollment_id': 'EntryEnrollmentID',
        'entry_id': 'EntryID',
        'enrollment_type_enum': 'EnrollmentTypeEnum',
        'course_id': 'CourseID',
        'term_id': 'TermID',
        'enrollment_order': 'EnrollmentOrder',
        'enrollment_field': 'EnrollmentField',
        'sequence': 'Sequence',
        'institution': 'Institution',
        'campus': 'Campus',
        'faculty': 'Faculty',
        'department': 'Department',
        'major': 'Major',
        'major_category': 'MajorCategory',
        'minor': 'Minor',
        'is_enrolled': 'IsEnrolled',
        'full_time': 'FullTime',
        'post_grad': 'PostGrad',
        'graduation_date': 'GraduationDate',
        'subjects': 'Subjects',
        'years': 'Years',
        'comments': 'Comments',
        'date_start': 'DateStart',
        'date_end': 'DateEnd',
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

    def __init__(self, entry_enrollment_id=None, entry_id=None, enrollment_type_enum=None, course_id=None, term_id=None, enrollment_order=None, enrollment_field=None, sequence=None, institution=None, campus=None, faculty=None, department=None, major=None, major_category=None, minor=None, is_enrolled=None, full_time=None, post_grad=None, graduation_date=None, subjects=None, years=None, comments=None, date_start=None, date_end=None, custom_bit1=None, custom_bit2=None, custom_string1=None, custom_string2=None, custom_string3=None, custom_string4=None, custom_string5=None, custom_string6=None, custom_date1=None, custom_date2=None, date_modified=None):  # noqa: E501
        """EntryEnrollmentItem - a model defined in Swagger"""  # noqa: E501

        self._entry_enrollment_id = None
        self._entry_id = None
        self._enrollment_type_enum = None
        self._course_id = None
        self._term_id = None
        self._enrollment_order = None
        self._enrollment_field = None
        self._sequence = None
        self._institution = None
        self._campus = None
        self._faculty = None
        self._department = None
        self._major = None
        self._major_category = None
        self._minor = None
        self._is_enrolled = None
        self._full_time = None
        self._post_grad = None
        self._graduation_date = None
        self._subjects = None
        self._years = None
        self._comments = None
        self._date_start = None
        self._date_end = None
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

        if entry_enrollment_id is not None:
            self.entry_enrollment_id = entry_enrollment_id
        if entry_id is not None:
            self.entry_id = entry_id
        if enrollment_type_enum is not None:
            self.enrollment_type_enum = enrollment_type_enum
        if course_id is not None:
            self.course_id = course_id
        if term_id is not None:
            self.term_id = term_id
        if enrollment_order is not None:
            self.enrollment_order = enrollment_order
        if enrollment_field is not None:
            self.enrollment_field = enrollment_field
        if sequence is not None:
            self.sequence = sequence
        if institution is not None:
            self.institution = institution
        if campus is not None:
            self.campus = campus
        if faculty is not None:
            self.faculty = faculty
        if department is not None:
            self.department = department
        if major is not None:
            self.major = major
        if major_category is not None:
            self.major_category = major_category
        if minor is not None:
            self.minor = minor
        if is_enrolled is not None:
            self.is_enrolled = is_enrolled
        if full_time is not None:
            self.full_time = full_time
        if post_grad is not None:
            self.post_grad = post_grad
        if graduation_date is not None:
            self.graduation_date = graduation_date
        if subjects is not None:
            self.subjects = subjects
        if years is not None:
            self.years = years
        if comments is not None:
            self.comments = comments
        if date_start is not None:
            self.date_start = date_start
        if date_end is not None:
            self.date_end = date_end
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
    def entry_enrollment_id(self):
        """Gets the entry_enrollment_id of this EntryEnrollmentItem.  # noqa: E501

        Entry Enrollment  # noqa: E501

        :return: The entry_enrollment_id of this EntryEnrollmentItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_enrollment_id

    @entry_enrollment_id.setter
    def entry_enrollment_id(self, entry_enrollment_id):
        """Sets the entry_enrollment_id of this EntryEnrollmentItem.

        Entry Enrollment  # noqa: E501

        :param entry_enrollment_id: The entry_enrollment_id of this EntryEnrollmentItem.  # noqa: E501
        :type: int
        """

        self._entry_enrollment_id = entry_enrollment_id

    @property
    def entry_id(self):
        """Gets the entry_id of this EntryEnrollmentItem.  # noqa: E501

        Entry  # noqa: E501

        :return: The entry_id of this EntryEnrollmentItem.  # noqa: E501
        :rtype: int
        """
        return self._entry_id

    @entry_id.setter
    def entry_id(self, entry_id):
        """Sets the entry_id of this EntryEnrollmentItem.

        Entry  # noqa: E501

        :param entry_id: The entry_id of this EntryEnrollmentItem.  # noqa: E501
        :type: int
        """

        self._entry_id = entry_id

    @property
    def enrollment_type_enum(self):
        """Gets the enrollment_type_enum of this EntryEnrollmentItem.  # noqa: E501

        Enrollment Type  # noqa: E501

        :return: The enrollment_type_enum of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_type_enum

    @enrollment_type_enum.setter
    def enrollment_type_enum(self, enrollment_type_enum):
        """Sets the enrollment_type_enum of this EntryEnrollmentItem.

        Enrollment Type  # noqa: E501

        :param enrollment_type_enum: The enrollment_type_enum of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """

        self._enrollment_type_enum = enrollment_type_enum

    @property
    def course_id(self):
        """Gets the course_id of this EntryEnrollmentItem.  # noqa: E501

        Course  # noqa: E501

        :return: The course_id of this EntryEnrollmentItem.  # noqa: E501
        :rtype: int
        """
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        """Sets the course_id of this EntryEnrollmentItem.

        Course  # noqa: E501

        :param course_id: The course_id of this EntryEnrollmentItem.  # noqa: E501
        :type: int
        """

        self._course_id = course_id

    @property
    def term_id(self):
        """Gets the term_id of this EntryEnrollmentItem.  # noqa: E501

        Term  # noqa: E501

        :return: The term_id of this EntryEnrollmentItem.  # noqa: E501
        :rtype: int
        """
        return self._term_id

    @term_id.setter
    def term_id(self, term_id):
        """Sets the term_id of this EntryEnrollmentItem.

        Term  # noqa: E501

        :param term_id: The term_id of this EntryEnrollmentItem.  # noqa: E501
        :type: int
        """

        self._term_id = term_id

    @property
    def enrollment_order(self):
        """Gets the enrollment_order of this EntryEnrollmentItem.  # noqa: E501

        Enrollment Order  # noqa: E501

        :return: The enrollment_order of this EntryEnrollmentItem.  # noqa: E501
        :rtype: int
        """
        return self._enrollment_order

    @enrollment_order.setter
    def enrollment_order(self, enrollment_order):
        """Sets the enrollment_order of this EntryEnrollmentItem.

        Enrollment Order  # noqa: E501

        :param enrollment_order: The enrollment_order of this EntryEnrollmentItem.  # noqa: E501
        :type: int
        """

        self._enrollment_order = enrollment_order

    @property
    def enrollment_field(self):
        """Gets the enrollment_field of this EntryEnrollmentItem.  # noqa: E501

        Enrollment Field  # noqa: E501

        :return: The enrollment_field of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._enrollment_field

    @enrollment_field.setter
    def enrollment_field(self, enrollment_field):
        """Sets the enrollment_field of this EntryEnrollmentItem.

        Enrollment Field  # noqa: E501

        :param enrollment_field: The enrollment_field of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if enrollment_field is not None and len(enrollment_field) > 20:
            raise ValueError("Invalid value for `enrollment_field`, length must be less than or equal to `20`")  # noqa: E501

        self._enrollment_field = enrollment_field

    @property
    def sequence(self):
        """Gets the sequence of this EntryEnrollmentItem.  # noqa: E501

        Sequence  # noqa: E501

        :return: The sequence of this EntryEnrollmentItem.  # noqa: E501
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this EntryEnrollmentItem.

        Sequence  # noqa: E501

        :param sequence: The sequence of this EntryEnrollmentItem.  # noqa: E501
        :type: int
        """

        self._sequence = sequence

    @property
    def institution(self):
        """Gets the institution of this EntryEnrollmentItem.  # noqa: E501

        Institution  # noqa: E501

        :return: The institution of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this EntryEnrollmentItem.

        Institution  # noqa: E501

        :param institution: The institution of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if institution is not None and len(institution) > 50:
            raise ValueError("Invalid value for `institution`, length must be less than or equal to `50`")  # noqa: E501

        self._institution = institution

    @property
    def campus(self):
        """Gets the campus of this EntryEnrollmentItem.  # noqa: E501

        Campus  # noqa: E501

        :return: The campus of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._campus

    @campus.setter
    def campus(self, campus):
        """Sets the campus of this EntryEnrollmentItem.

        Campus  # noqa: E501

        :param campus: The campus of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if campus is not None and len(campus) > 50:
            raise ValueError("Invalid value for `campus`, length must be less than or equal to `50`")  # noqa: E501

        self._campus = campus

    @property
    def faculty(self):
        """Gets the faculty of this EntryEnrollmentItem.  # noqa: E501

        Faculty  # noqa: E501

        :return: The faculty of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._faculty

    @faculty.setter
    def faculty(self, faculty):
        """Sets the faculty of this EntryEnrollmentItem.

        Faculty  # noqa: E501

        :param faculty: The faculty of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if faculty is not None and len(faculty) > 50:
            raise ValueError("Invalid value for `faculty`, length must be less than or equal to `50`")  # noqa: E501

        self._faculty = faculty

    @property
    def department(self):
        """Gets the department of this EntryEnrollmentItem.  # noqa: E501

        Department  # noqa: E501

        :return: The department of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this EntryEnrollmentItem.

        Department  # noqa: E501

        :param department: The department of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if department is not None and len(department) > 50:
            raise ValueError("Invalid value for `department`, length must be less than or equal to `50`")  # noqa: E501

        self._department = department

    @property
    def major(self):
        """Gets the major of this EntryEnrollmentItem.  # noqa: E501

        Major  # noqa: E501

        :return: The major of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this EntryEnrollmentItem.

        Major  # noqa: E501

        :param major: The major of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if major is not None and len(major) > 50:
            raise ValueError("Invalid value for `major`, length must be less than or equal to `50`")  # noqa: E501

        self._major = major

    @property
    def major_category(self):
        """Gets the major_category of this EntryEnrollmentItem.  # noqa: E501

        Major Category  # noqa: E501

        :return: The major_category of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._major_category

    @major_category.setter
    def major_category(self, major_category):
        """Sets the major_category of this EntryEnrollmentItem.

        Major Category  # noqa: E501

        :param major_category: The major_category of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if major_category is not None and len(major_category) > 50:
            raise ValueError("Invalid value for `major_category`, length must be less than or equal to `50`")  # noqa: E501

        self._major_category = major_category

    @property
    def minor(self):
        """Gets the minor of this EntryEnrollmentItem.  # noqa: E501

        Minor  # noqa: E501

        :return: The minor of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this EntryEnrollmentItem.

        Minor  # noqa: E501

        :param minor: The minor of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if minor is not None and len(minor) > 50:
            raise ValueError("Invalid value for `minor`, length must be less than or equal to `50`")  # noqa: E501

        self._minor = minor

    @property
    def is_enrolled(self):
        """Gets the is_enrolled of this EntryEnrollmentItem.  # noqa: E501

        Is Enrolled  # noqa: E501

        :return: The is_enrolled of this EntryEnrollmentItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_enrolled

    @is_enrolled.setter
    def is_enrolled(self, is_enrolled):
        """Sets the is_enrolled of this EntryEnrollmentItem.

        Is Enrolled  # noqa: E501

        :param is_enrolled: The is_enrolled of this EntryEnrollmentItem.  # noqa: E501
        :type: bool
        """

        self._is_enrolled = is_enrolled

    @property
    def full_time(self):
        """Gets the full_time of this EntryEnrollmentItem.  # noqa: E501

        Full Time  # noqa: E501

        :return: The full_time of this EntryEnrollmentItem.  # noqa: E501
        :rtype: bool
        """
        return self._full_time

    @full_time.setter
    def full_time(self, full_time):
        """Sets the full_time of this EntryEnrollmentItem.

        Full Time  # noqa: E501

        :param full_time: The full_time of this EntryEnrollmentItem.  # noqa: E501
        :type: bool
        """

        self._full_time = full_time

    @property
    def post_grad(self):
        """Gets the post_grad of this EntryEnrollmentItem.  # noqa: E501

        Post Grad  # noqa: E501

        :return: The post_grad of this EntryEnrollmentItem.  # noqa: E501
        :rtype: bool
        """
        return self._post_grad

    @post_grad.setter
    def post_grad(self, post_grad):
        """Sets the post_grad of this EntryEnrollmentItem.

        Post Grad  # noqa: E501

        :param post_grad: The post_grad of this EntryEnrollmentItem.  # noqa: E501
        :type: bool
        """

        self._post_grad = post_grad

    @property
    def graduation_date(self):
        """Gets the graduation_date of this EntryEnrollmentItem.  # noqa: E501

        Graduation Date  # noqa: E501

        :return: The graduation_date of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._graduation_date

    @graduation_date.setter
    def graduation_date(self, graduation_date):
        """Sets the graduation_date of this EntryEnrollmentItem.

        Graduation Date  # noqa: E501

        :param graduation_date: The graduation_date of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """

        self._graduation_date = graduation_date

    @property
    def subjects(self):
        """Gets the subjects of this EntryEnrollmentItem.  # noqa: E501

        Subjects  # noqa: E501

        :return: The subjects of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        """Sets the subjects of this EntryEnrollmentItem.

        Subjects  # noqa: E501

        :param subjects: The subjects of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if subjects is not None and len(subjects) > 250:
            raise ValueError("Invalid value for `subjects`, length must be less than or equal to `250`")  # noqa: E501

        self._subjects = subjects

    @property
    def years(self):
        """Gets the years of this EntryEnrollmentItem.  # noqa: E501

        Years  # noqa: E501

        :return: The years of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._years

    @years.setter
    def years(self, years):
        """Sets the years of this EntryEnrollmentItem.

        Years  # noqa: E501

        :param years: The years of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if years is not None and len(years) > 10:
            raise ValueError("Invalid value for `years`, length must be less than or equal to `10`")  # noqa: E501

        self._years = years

    @property
    def comments(self):
        """Gets the comments of this EntryEnrollmentItem.  # noqa: E501

        Comments  # noqa: E501

        :return: The comments of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this EntryEnrollmentItem.

        Comments  # noqa: E501

        :param comments: The comments of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if comments is not None and len(comments) > 200:
            raise ValueError("Invalid value for `comments`, length must be less than or equal to `200`")  # noqa: E501

        self._comments = comments

    @property
    def date_start(self):
        """Gets the date_start of this EntryEnrollmentItem.  # noqa: E501

        Date Start  # noqa: E501

        :return: The date_start of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """Sets the date_start of this EntryEnrollmentItem.

        Date Start  # noqa: E501

        :param date_start: The date_start of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """

        self._date_start = date_start

    @property
    def date_end(self):
        """Gets the date_end of this EntryEnrollmentItem.  # noqa: E501

        Date End  # noqa: E501

        :return: The date_end of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """Sets the date_end of this EntryEnrollmentItem.

        Date End  # noqa: E501

        :param date_end: The date_end of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """

        self._date_end = date_end

    @property
    def custom_bit1(self):
        """Gets the custom_bit1 of this EntryEnrollmentItem.  # noqa: E501

        Custom Flag 1  # noqa: E501

        :return: The custom_bit1 of this EntryEnrollmentItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit1

    @custom_bit1.setter
    def custom_bit1(self, custom_bit1):
        """Sets the custom_bit1 of this EntryEnrollmentItem.

        Custom Flag 1  # noqa: E501

        :param custom_bit1: The custom_bit1 of this EntryEnrollmentItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit1 = custom_bit1

    @property
    def custom_bit2(self):
        """Gets the custom_bit2 of this EntryEnrollmentItem.  # noqa: E501

        Custom Flag 2  # noqa: E501

        :return: The custom_bit2 of this EntryEnrollmentItem.  # noqa: E501
        :rtype: bool
        """
        return self._custom_bit2

    @custom_bit2.setter
    def custom_bit2(self, custom_bit2):
        """Sets the custom_bit2 of this EntryEnrollmentItem.

        Custom Flag 2  # noqa: E501

        :param custom_bit2: The custom_bit2 of this EntryEnrollmentItem.  # noqa: E501
        :type: bool
        """

        self._custom_bit2 = custom_bit2

    @property
    def custom_string1(self):
        """Gets the custom_string1 of this EntryEnrollmentItem.  # noqa: E501

        Custom String 1  # noqa: E501

        :return: The custom_string1 of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string1

    @custom_string1.setter
    def custom_string1(self, custom_string1):
        """Sets the custom_string1 of this EntryEnrollmentItem.

        Custom String 1  # noqa: E501

        :param custom_string1: The custom_string1 of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if custom_string1 is not None and len(custom_string1) > 50:
            raise ValueError("Invalid value for `custom_string1`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string1 = custom_string1

    @property
    def custom_string2(self):
        """Gets the custom_string2 of this EntryEnrollmentItem.  # noqa: E501

        Custom String 2  # noqa: E501

        :return: The custom_string2 of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string2

    @custom_string2.setter
    def custom_string2(self, custom_string2):
        """Sets the custom_string2 of this EntryEnrollmentItem.

        Custom String 2  # noqa: E501

        :param custom_string2: The custom_string2 of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if custom_string2 is not None and len(custom_string2) > 50:
            raise ValueError("Invalid value for `custom_string2`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string2 = custom_string2

    @property
    def custom_string3(self):
        """Gets the custom_string3 of this EntryEnrollmentItem.  # noqa: E501

        Custom String 3  # noqa: E501

        :return: The custom_string3 of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string3

    @custom_string3.setter
    def custom_string3(self, custom_string3):
        """Sets the custom_string3 of this EntryEnrollmentItem.

        Custom String 3  # noqa: E501

        :param custom_string3: The custom_string3 of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if custom_string3 is not None and len(custom_string3) > 50:
            raise ValueError("Invalid value for `custom_string3`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string3 = custom_string3

    @property
    def custom_string4(self):
        """Gets the custom_string4 of this EntryEnrollmentItem.  # noqa: E501

        Custom String 4  # noqa: E501

        :return: The custom_string4 of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string4

    @custom_string4.setter
    def custom_string4(self, custom_string4):
        """Sets the custom_string4 of this EntryEnrollmentItem.

        Custom String 4  # noqa: E501

        :param custom_string4: The custom_string4 of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if custom_string4 is not None and len(custom_string4) > 50:
            raise ValueError("Invalid value for `custom_string4`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string4 = custom_string4

    @property
    def custom_string5(self):
        """Gets the custom_string5 of this EntryEnrollmentItem.  # noqa: E501

        Custom String 5  # noqa: E501

        :return: The custom_string5 of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string5

    @custom_string5.setter
    def custom_string5(self, custom_string5):
        """Sets the custom_string5 of this EntryEnrollmentItem.

        Custom String 5  # noqa: E501

        :param custom_string5: The custom_string5 of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if custom_string5 is not None and len(custom_string5) > 50:
            raise ValueError("Invalid value for `custom_string5`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string5 = custom_string5

    @property
    def custom_string6(self):
        """Gets the custom_string6 of this EntryEnrollmentItem.  # noqa: E501

        Custom String 6  # noqa: E501

        :return: The custom_string6 of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_string6

    @custom_string6.setter
    def custom_string6(self, custom_string6):
        """Sets the custom_string6 of this EntryEnrollmentItem.

        Custom String 6  # noqa: E501

        :param custom_string6: The custom_string6 of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """
        if custom_string6 is not None and len(custom_string6) > 50:
            raise ValueError("Invalid value for `custom_string6`, length must be less than or equal to `50`")  # noqa: E501

        self._custom_string6 = custom_string6

    @property
    def custom_date1(self):
        """Gets the custom_date1 of this EntryEnrollmentItem.  # noqa: E501

        Custom Date 1  # noqa: E501

        :return: The custom_date1 of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date1

    @custom_date1.setter
    def custom_date1(self, custom_date1):
        """Sets the custom_date1 of this EntryEnrollmentItem.

        Custom Date 1  # noqa: E501

        :param custom_date1: The custom_date1 of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """

        self._custom_date1 = custom_date1

    @property
    def custom_date2(self):
        """Gets the custom_date2 of this EntryEnrollmentItem.  # noqa: E501

        Custom Date 2  # noqa: E501

        :return: The custom_date2 of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._custom_date2

    @custom_date2.setter
    def custom_date2(self, custom_date2):
        """Sets the custom_date2 of this EntryEnrollmentItem.

        Custom Date 2  # noqa: E501

        :param custom_date2: The custom_date2 of this EntryEnrollmentItem.  # noqa: E501
        :type: str
        """

        self._custom_date2 = custom_date2

    @property
    def date_modified(self):
        """Gets the date_modified of this EntryEnrollmentItem.  # noqa: E501

        Date Modified  # noqa: E501

        :return: The date_modified of this EntryEnrollmentItem.  # noqa: E501
        :rtype: str
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this EntryEnrollmentItem.

        Date Modified  # noqa: E501

        :param date_modified: The date_modified of this EntryEnrollmentItem.  # noqa: E501
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
        if not isinstance(other, EntryEnrollmentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
