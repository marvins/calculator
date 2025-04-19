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
from core   import Icon_Set
from widgets.main_header import Main_Header
from widgets.main_footer import Main_Footer

class Main_Window:

    def __init__( self, 
                  config: Configuration,
                  driver,
                  style_manager ):
        self.config = config
        self.driver = driver
        self.style_manager = style_manager

    def initialize( self ):

        #  Setup the underlying screen
        self.screen = lv.obj()

        #  Main Body Widget
        self.body = lv.obj( self.screen )
        self.body.set_size( self.config.get_section('screen','width'),
                            self.config.get_section('screen','height') )
        self.body.center()
        self.body.set_layout( lv.LAYOUT.FLEX )
        self.body.set_flex_flow( lv.FLEX_FLOW.COLUMN )
        self.body.set_style_pad_gap(0, lv.PART.MAIN)
        self.body.set_style_pad_all(0, lv.PART.MAIN)

        #  Create Header
        self.header = Main_Header( self.config,
                                   self.style_manager,
                                   self.body )
        self.header.initialize()


        #  Create Footer
        self.footer = Main_Footer( self.config,
                                   self.style_manager,
                                   self.body )
        
        self.footer.add_command( Icon_Set.ARROWS_ALL, 'Navigate' )
        self.footer.add_command( Icon_Set.ENTER, 'Select' )
        self.footer.initialize()
        

    @staticmethod
    def create( config: Configuration,
                driver,
                style_manager ):

        #  Build new instance
        window = Main_Window( config, 
                              driver,
                              style_manager )

        window.initialize()

        return window
    

    def run( self ):

        return lv.screen_load( self.screen )
