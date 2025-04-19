#
#    File:    Main_Window.py
#    Author:  Marvin Smith
#    Date:    4/19/2025
#
#    Main Window for demo app.
#

#  LVGL
import lvgl as lv

#  Project Libraries
from config import Configuration
from widgets.main_header import Main_Header
from widgets.main_footer import Main_Footer

class Main_Window:

    def __init__(self, config: Configuration, driver ):
        self.config = config
        self.driver = driver

    def initialize( self ):

        #  Setup the underlying screen
        self.screen = lv.obj()

        #  Main Body Widget
        self.body = lv.obj( self.screen )
        self.body.set_size( self.config.get('screen','width'),
                            self.config.get('screen','height') )
        self.body.center()
        self.body.set_layout( lv.LAYOUT.FLEX )
        self.body.set_flex_flow( lv.FLEX_FLOW.COLUMN )
        self.body.set_style_pad_gap(0, lv.PART.MAIN)
        self.body.set_style_pad_all(0, lv.PART.MAIN)

        #  Create Header
        self.header = Main_Header( self.config,
                                   self.body )
        self.header.initialize()


        #  Create Footer
        self.footer = Main_Footer( self.config,
                                   self.body )
        self.footer.initialize()
        

    @staticmethod
    def create( config: Configuration, driver ):

        #  Build new instance
        window = Main_Window( config, driver )

        window.initialize()

        return window
    

    def run( self ):

        return lv.screen_load( self.screen )
