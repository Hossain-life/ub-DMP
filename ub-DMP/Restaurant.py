"""Restaurant class to define the restaurant usage in UB

"""
__author__ = 'Arsalan Akhter'


class Restaurant:
    """
    The Restaurant class defines the restaurant and all the associated
    parameters.
    """

    def __init__(self, id):
        self._id = id
        self._lat = None
        self._lon = None
        self._location = (self._lat, self._lon)
        self._total_number_of_meals_available = 0.0
        self._meals_offered_list = []
        self._meals_availability_dict = {}

    def set_location(self, loc):
        """
        Sets the location of the restaurant. We assume the format
        (lat, long) for the locations through out DMPlatform
        :param loc: Location of the restaurant
        """
        if -90 <= loc[0] <= 90 and -180 <= loc[1] <= 180:
            self._lat = loc[0]
            self._lon = loc[1]
            self._location = (self._lat, self._lon)
        else:
            raise ValueError(f'Restaurant location {loc} is '
                             f'not valid.')

    def set_meals_offered_list(self, meals_offered_list):
        self._meals_offered_list = meals_offered_list

    def get_id(self):
        """
        Returns the ID of the restaurant
        :return: String or number containing the ID
        """
        return self._id
