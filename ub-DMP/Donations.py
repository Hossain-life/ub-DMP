"""Donation class to manage donations in UB

"""
__author__ = 'Arsalan Akhter'

from common_sets import age_ranges_dict, ethnicity_set, gender_set, \
    donation_loctions_set, donation_pools_set


class Donations:
    """
    The Donation class keeps track of all the funds in UB.

    """

    def __init__(self):
        self._donation_pool_funds = {i: 0 for i in donation_pools_set}
        self._total_funds_available = sum(
            list(self._donation_pool_funds.values()))
        self._total_meals_available = 0.0

    def refresh_total_funds_status(self):
        """
        Refreshes the parameter for total available funds
        """
        self._total_funds_available = sum(
            list(self._donation_pool_funds.values()))

    def add_donation_to_pool(self, pool_tuple, amount):
        """
        Adds a donation that was just received, in the respective pool
        :param pool_tuple: The pool/bucket to which the donation was
        allocated for preference
        :param amount: The amount to be allocated in the pool
        """
        if pool_tuple in donation_pools_set:
            self._donation_pool_funds[pool_tuple] += amount
        else:
            raise ValueError(f"{pool_tuple} not in donation pools set!")
        self.refresh_total_funds_status()

    def remove_donation_from_pool(self, pool_tuple, amount):
        """
        Removes amount from a specified donation pool
        :param pool_tuple: The pool/bucket from which the amount is
        to be subtracted
        :param amount: The amount to be subtracted.
        """
        if pool_tuple in donation_pools_set:
            if self._donation_pool_funds[pool_tuple] - amount >= 0:
                self._donation_pool_funds[pool_tuple] -= amount
            else:
                raise ValueError(
                    f"donation pool {pool_tuple} does not have enough"
                    f"funds such that amount {amount} could be "
                    f"subtracted!")
        else:
            raise ValueError(f"{pool_tuple} not in donation pools set!")
        self.refresh_total_funds_status()

    def get_funds_in_pool(self, pool_tuple):
        """
        Get how many funds are available in a specific pool
        :param pool_tuple: The pool for which the query is made
        :returns A float value representing the amount present in a
        specific pool
        """
        if pool_tuple in donation_pools_set:
            return self._donation_pool_funds[pool_tuple]
        else:
            raise ValueError(f"{pool_tuple} not in donation pools set!")

    def get_total_funds_available(self):
        """
        Get total funds available in DM Platform
        :returns A float value representing the total funds available
        in the DM Platform
        """
        self.refresh_total_funds_status()
        return self._total_funds_available
