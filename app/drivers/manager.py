#
#    File:    manager.py
#    Author:  Marvin Smith
#    Date:    4/19/2025
#

#  Project Libraries
from config import Configuration
from drivers.unix import Driver as unix_driver

class Driver_Manager:

    @staticmethod
    def load( config: Configuration ):

        # Try the unix port
        try:
            driver = unix_driver( config )
            return driver
        except Exception as e:
            print( f'Unix Driver Failed: ', e )
            pass

