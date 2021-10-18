"""Main entry point for donation matching platform

"""
__author__ = 'Arsalan Akhter'

import logging
import sys

from DMPlatform import DMPlatform


# Currently, we are setting up logger at one place only
debug = True
# noinspection PyArgumentList
# Added above comment to suppress logging.basicConfig warning.
# See https://stackoverflow.com/questions/61226587/
# pycharm-does-not-recognize-logging-basicconfig-handlers-argument
logging.basicConfig(
    level=logging.INFO if debug is not True else logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('debug.log', mode='w'),
        # logging.FileHandler(datetime.now().strftime('UB_log_%Y_%m_%d_%H_%M_%S.log')),
        logging.StreamHandler(sys.stdout)
    ]
)


def main():
    logging.debug('Hello UB World!')
    platform = DMPlatform()


if __name__ == "__main__":
    main()
