
#  Micropython Libraries
import logging

#  Project Libraries
from config                 import Configuration
from core                   import Action, Icon_Set
from apps.app_base          import App_Base
from utilities.lvgl_events  import get_event_name
from utilities.lvgl_styles  import Style_Manager
from widgets.main_header    import Main_Header
from widgets.main_footer    import Main_Footer

#  LVGL
import lvgl as lv


class App:

    def __init__( self,
                  config:        Configuration,
                  style_manager: Style_Manager,
                  parent ):

        self.name          = 'Terminal'

        self.logger = logging.getLogger( 'Terminal_App' )

        super().__init__( config,
                          style_manager,
                          parent )


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
        self.footer.add_command( Icon_Set.ENTER, 'Execute' )
        self.footer.add_command( Icon_Set.ESCAPE, 'Back' )
        self.footer.initialize()

        #  Setup Callbacks
        self.init_callbacks()

    def init_callbacks( self ):

        #  Callback
        def keyboard_callback( event, name ):
            
            #  Skip if we are not active
            if self.is_active == False:
                return
            
            self.logger.debug( f'[Terminal] Event: {event.code}, Button Name: {name}' )
            
            #  Look for escape key
            print( f'Event: {event.code}, Type: {get_event_name(lv.EVENT, event.code)}, Context: {name}' )
            if event.code == lv.KEY.ESC:
                self.parent.notify_action( Action.KEY_ESC )
        
        #  Setup Event Monitor
        self.body.add_event_cb( lambda event, event_name = self.name: keyboard_callback(event, event_name), lv.EVENT.ALL, None)

    @staticmethod
    def create( config:         Configuration,
                style_manager:  Style_Manager,
                parent ):
        
        app = App( config,
                   style_manager,
                   parent )

        app.initialize()

        return app
    