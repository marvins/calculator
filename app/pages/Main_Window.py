#
#    File:    Main_Window.py
#    Author:  Marvin Smith
#    Date:    4/19/2025
#
#    Main Window for demo app.
#

#  Python Libraries
import logging

#  LVGL
import lvgl as lv

#  Project Libraries
from apps.app_manager import App_Manager
from config import Configuration
from core   import Action, Icon_Set
from utilities.lvgl_styles import Style_Manager
from widgets.main_header import Main_Header
from widgets.main_footer import Main_Footer
from widgets.main_menu   import Main_Menu

class Main_Window:

    def __init__( self, 
                  config: Configuration,
                  driver,
                  style_manager: Style_Manager,
                  app_manager: App_Manager ):
        
        self.config        = config
        self.driver        = driver
        self.style_manager = style_manager
        self.app_manager   = app_manager

        self.active_pages = {}

        self.logger = logging.getLogger( 'Main_Window' )

    def initialize( self ):

        self.build_main_page()
        self.active_pages['main'] = self.body

        self.build_app_pages()


    def build_main_page( self ):

        #  Main Body Widget
        self.body = lv.obj()
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
                                    self )
        self.main_menu.initialize()

        #  Create Footer
        self.footer = Main_Footer( self.config,
                                   self.style_manager,
                                   self.body )
        
        self.footer.add_command( Icon_Set.ARROWS_ALL, 'Navigate' )
        self.footer.add_command( Icon_Set.ENTER, 'Select' )
        self.footer.initialize()

    def build_app_pages( self ):

        for app_id in self.app_manager.get_icon_data().keys():

            new_inst = self.app_manager.get_app_instance( app_id )

            self.logger.info( f'Adding App Page: {app_id}' )
            self.active_pages[app_id] = new_inst.create( self.config,
                                                         self.style_manager,
                                                         self )

    def notify_action( self, action, context ):
        '''
        Process the action, likely changing the screen
        '''
        self.logger.info( f'Action Requested: {action}, Context: {context}' )

        if action == Action.APP_LAUNCH:

            self.set_active( False )
            self.logger.info( f'Launching app: {context}' )
            self.driver.reset_group()
            self.active_pages[context].set_active( True )
            lv.screen_load( self.active_pages[context].body )

        elif action == Action.KEY_ESC:

            if context == 'main':
                self.logger.info( f'Turning ourselves back on!' )
                self.set_active( True )

                self.driver.reset_group()
                lv.screen_load( self.body )

    def set_active( self, value ):
        self.is_active = value
        self.main_menu.is_active = value

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

        return lv.screen_load( self.body )
