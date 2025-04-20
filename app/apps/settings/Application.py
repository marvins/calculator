

#  Project Libraries
from config import Configuration
from core   import Icon_Set
from utilities.lvgl_styles import Style_Manager
from widgets.main_header import Main_Header
from widgets.main_footer import Main_Footer

#  LVGL
import lvgl as lv


class App:

    def __init__( self,
                  config: Configuration,
                  style_manager: Style_Manager,
                  app_manager: App_Manager,
                  parent ):
        
        self.config        = config
        self.style_manager = style_manager
        self.app_manager   = app_manager
        self.parent        = parent


    def initialize( self ):

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

        #  Build Window


        #  Create Footer
        self.footer = Main_Footer( self.config,
                                   self.style_manager,
                                   self.body )
        
        self.footer.add_command( Icon_Set.ARROWS_ALL, 'Navigate' )
        self.footer.add_command( Icon_Set.ENTER, 'Select' )
        self.footer.initialize()

        return lv.screen_load( self.body )
    
    @staticmethod
    def create( config:         Configuration,
                style_manager:  Style_Manager,
                app_manager:    App_Manager,
                parent ):
        
        app = App( config,
                   style_manager,
                   app_manager,
                   parent )

        app.initialize()

        return app
    