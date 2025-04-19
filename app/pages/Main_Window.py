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
from apps.app_manager import App_Manager
from config import Configuration
from core   import Icon_Set
from utilities.lvgl_styles import Style_Manager
from widgets.main_header import Main_Header
from widgets.main_footer import Main_Footer
from widgets.main_menu   import Main_Menu

class Main_Window:

    def __init__( self, 
                  config: Configuration,
                  driver,
                  style_manager,
                  app_manager ):
        
        self.config        = config
        self.driver        = driver
        self.style_manager = style_manager
        self.app_manager   = app_manager

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

        #  Build main menu
        self.main_menu = Main_Menu( self.config,
                                    self.style_manager,
                                    self.app_manager,
                                    self.body )
        self.main_menu.initialize()

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
                style_manager: Style_Manager,
                app_manager: App_Manager ):

        #  Build new instance
        window = Main_Window( config, 
                              driver,
                              style_manager,
                              app_manager )

        window.initialize()

        return window
    

    def run( self ):

        return lv.screen_load( self.screen )
