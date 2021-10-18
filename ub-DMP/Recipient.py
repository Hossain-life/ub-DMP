"""Recipient class to define the recipient behavior

"""
__author__ = 'Arsalan Akhter'

from common_sets import age_ranges_dict, ethnicity_set, gender_set


class Recipient:
    """
    The Recipient class defines the recipient and all the associated
    parameters.
    """

    def __init__(self, id):
        self._id = id
        self._gender = ''
        self._need_score = 0.0
        self._age_range = tuple()
        self._ethnicity = ''
        self._restaurants_set = set()
        self._home_location = tuple()

    def set_gender(self, gender):
        """
        Sets the gender of the recipient.
        :param gender: Gender, as defined in gender_set
        """
        if gender in gender_set:
            self._gender = gender
        else:
            raise ValueError(f'Gender {gender} is not a previously '
                             f'defined gender.')

    def set_need_score(self, need_score):
        """
        Sets the need score for the recipient. We assume that need
        score is \in [0, 1]
        :param need_score: The need score float value to be set
        """
        if 0 <= need_score <= 1:
            self._need_score = need_score
        else:
            raise ValueError(f'Need Score {need_score} is not within'
                             f'defined range.')

    def set_age_range(self, age_range):
        """
        Set age_range, as defined in age_ranges_dict in common_sets
        :param age_range: The identifier for each age range
        """
        if age_range in list(age_ranges_dict.keys()):
            self._age_range = age_ranges_dict[age_range]
        else:
            raise ValueError(f'Age Range {age_range} is not in '
                             f'previously defined age ranges.')

    def set_ethnicity(self, ethnicity):
        """
        Set ethnicity, as defined in the ethnicity_set
        :param ethnicity: The ethnicity of the recipient
        """
        if ethnicity in ethnicity_set:
            self._ethnicity = ethnicity
        else:
            raise ValueError(f'Ethnicity {ethnicity} is not in '
                             f'previously defined ethnicity sets.')

    def set_home_location(self, home_loc):
        """
        Sets the home location of the recipient. We assume the format
        (lat, long) for the locations through out DMPlatform
        :param home_loc: Home location of the recipient
        """
        if -90 <= home_loc[0] <= 90 and -180 <= home_loc[1] <= 180:
            self._home_location = (home_loc[0], home_loc[1])
        else:
            raise ValueError(f'Recipient Home location {home_loc} is '
                             f'not valid.')

    def get_home_location(self):
        """
        Returns the home location of the recipient
        :return: A tuple in the format (lat, long)
        """
        return self._home_location

    def get_gender(self):
        """
        Returns the gender of the recipient.
        :return: A gender string as defined in gender_set
        """
        return self._gender

    def get_id(self):
        """
        Returns the ID of the recipient
        :return: String or number containing the ID
        """
        return self._id
