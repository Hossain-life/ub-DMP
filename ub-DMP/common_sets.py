"""Sets of attributes common against Donors, Recipients and Restaurants

This file contains those sets and parameters that are common across
donors, recipients and restaurants
"""
__author__ = 'Arsalan Akhter'

age_ranges_dict = {'<18': (0, 17),
                   '18-24': (18, 24),
                   '25-49': (25, 49),
                   '50-64': (50, 64),
                   '>65': (65, 140),
                   'All': (0, 140)}

ethnicity_set = {'African American',
                 'Hispanics',
                 'Native Americans',
                 'Others',
                 'All'}

gender_set = {'Female',
              'Male',
              'Non-Binary',
              'All'}

donation_loctions_set = {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC",
                         "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
                         "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN",
                         "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
                         "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
                         "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
                         "WV", "WI", "WY", "All"}  # States in US

donation_pools_set = {(i, j, k, l)
                      for i in age_ranges_dict
                      for j in ethnicity_set
                      for k in gender_set
                      for l in donation_loctions_set}
