#
#    File:    main.py
#    Author:  Marvin Smith
#    Date:    4/19/2025
#

#  Micropython Libraries
import sys

#  Project Libraries
from config import Configuration

def main():

    config = Configuration.parse( sys.argv )
    print( config.cfg_args )



if __name__ == '__main__':
    main()