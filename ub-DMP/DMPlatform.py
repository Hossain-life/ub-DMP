"""This is the main DMPlatform

"""
__author__ = 'Arsalan Akhter'

from Donations import Donations
from Recipient import Recipient
from Restaurant import Restaurant


class DMPlatform:
    """
       The DMPlatform class orchestrates the whole platform,
       and takes care of any task that is related to donation
       matching in Universal Basic.
    """

    def __init__(self):
        self._recipients_list = []
        self._restaurants_list = []

    def register_recipient(self, id, gender, need_score, age_range,
                           ethnicity, home_loc):
        """
        Register a recipient in the DMPlatform
        :param id: ID of the recipient
        :param gender: Gender of the recipient
        :param need_score: Need Score in [0, 1]
        :param age_range: String identifier for age range
        :param ethnicity: Ethnicity of the recipient
        :param home_loc: (lat, long) tuple for home location of
        recipient
        """
        r = Recipient(id)
        r.set_gender(gender)
        r.set_need_score(need_score)
        r.set_age_range(age_range)
        r.set_ethnicity(ethnicity)
        r.set_home_location(home_loc)
        self._recipients_list.append(r)

    def register_restaurant(self, id, location, meals_list):
        """
        Registers a restaurant in the DMPlatform
        :param id: ID of the restaurant
        :param location: Location of the platform (lat, lon)
        :param meals_list: List of meals offered by the restaurant
        """
        r = Restaurant(id)
        r.set_location(location)
        r.set_meals_offered_list(meals_list)
        self._restaurants_list.append(r)
