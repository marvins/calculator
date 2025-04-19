#
#    File:    unix.py
#    Author:  Marvin Smith
#    Date:    4/19/2025
#
#    Initialize the SDL-based unix port
#

#  LVGL
import lvgl as lv
import lv_utils

#  Project Libraries
from config import Configuration

#  Unix Driver
class Driver:

    #  Initialize
    def __init__( self, config: Configuration ):

        self.event_loop = lv_utils.event_loop()
        self.disp_drv   = lv.sdl_window_create( config.get_section('screen','width'), 
                                                config.get_section('screen','height') )
        self.indev_drv  = lv.sdl_mouse_create()

