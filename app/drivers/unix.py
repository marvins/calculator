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

        self.group      = lv.group_create()
        self.group.set_default()

        self.event_loop = lv_utils.event_loop()
        self.disp_drv   = lv.sdl_window_create( config.get_section('screen','width'), 
                                                config.get_section('screen','height') )
        self.mouse    = lv.sdl_mouse_create()
        self.keyboard = lv.sdl_keyboard_create()
        self.keyboard.set_group( self.group )


    def update_keyboard(self, body):
        pass


    def reset_group(self):
        self.group.set_default()
        self.keyboard.set_group( self.group )