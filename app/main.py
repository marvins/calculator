#
#    File:    main.py
#    Author:  Marvin Smith
#    Date:    4/19/2025
#

#  Micropython Libraries
import sys

#  Project Libraries
from apps.app_manager import App_Manager
from config import Configuration
from drivers.manager import Driver_Manager
from pages.Main_Window import Main_Window
from utilities.lvgl_styles import Style_Manager

def main():

    #  Parse the configuration
    config = Configuration.parse( sys.argv )
    
    #  Determine our driver
    driver = Driver_Manager.load( config )

    #  Create font-manager
    style_manager = Style_Manager.create( config )

    #  Create app-manager
    app_manager = App_Manager.create( config,
                                      style_manager,
                                      driver )
    
    #  Build the main window
    window = Main_Window.create( config, 
                                 driver,
                                 style_manager,
                                 app_manager )

    return window.run()

if __name__ == '__main__':
    main()