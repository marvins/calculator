
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


class App( App_Base ):

    def __init__( self,
                  config:        Configuration,
                  style_manager: Style_Manager,
                  parent ):

        self.name          = 'Coord Convert'

        self.group = lv.group_create()

        self.logger = logging.getLogger( 'Coordinate_Converter' )

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
        self.body.set_style_pad_gap( 0, lv.PART.MAIN )
        self.body.set_style_pad_all( 0, lv.PART.MAIN )

        #  Create Header
        self.header = Main_Header( self.config,
                                   self.style_manager,
                                   self.body )
        self.header.initialize()

        #  Build Window
        self.main_panel = lv.obj( self.body )
        self.main_panel.set_layout( lv.LAYOUT.FLEX )
        self.main_panel.set_flex_flow( lv.FLEX_FLOW.COLUMN )
        self.main_panel.set_size( lv.SIZE_CONTENT,
                                  lv.SIZE_CONTENT )

        #  Build geographic coordinate window
        self.build_geo_pane()
        

        #  Create Footer
        self.footer = Main_Footer( self.config,
                                   self.style_manager,
                                   self.body )
        
        self.footer.add_command( Icon_Set.ARROWS_ALL, 'Navigate' )
        self.footer.add_command( Icon_Set.ESCAPE, 'Back' )
        self.footer.initialize()

        #  Setup Callbacks
        self.init_callbacks()

    def build_geo_pane(self):

        #  Main widget will be a big grid layout
        col_desc = [ 100, 100, 100, lv.GRID_TEMPLATE_LAST ]
        row_desc = [ 40, 25, 25, 25, lv.GRID_TEMPLATE_LAST ]
        geo_pane = lv.obj( self.main_panel )
        geo_pane.set_grid_dsc_array( col_desc, row_desc )
        geo_pane.set_size( lv.SIZE_CONTENT,
                           lv.SIZE_CONTENT )

        #  Primary Header Label
        geo_label = lv.label( geo_pane )
        geo_label.set_text( 'Geographic Coordinate:' )
        geo_label.set_grid_cell( lv.GRID_ALIGN.START, 0, 4,
                                 lv.GRID_ALIGN.CENTER, 0, 1 )
        geo_label.set_size( lv.SIZE_CONTENT,
                           lv.SIZE_CONTENT )
        geo_label.add_style( self.style_manager.style('app_text_header'),
                             lv.PART.MAIN )
        geo_label.center()


        #  2nd Row (Latitude, Longitude, Format Labels)
        lat_label = lv.label( geo_pane )
        lat_label.set_text( 'Latitude: ' )
        lat_label.set_grid_cell( lv.GRID_ALIGN.START, 0, 1,
                                 lv.GRID_ALIGN.CENTER, 1, 1 )
        lat_label.set_size( 80, 25 )
        lat_label.add_style( self.style_manager.style('app_text_normal'),
                             lv.PART.MAIN )


        lon_label = lv.label( geo_pane )
        lon_label.set_text( 'Longitude: ' )
        lon_label.set_grid_cell( lv.GRID_ALIGN.START, 1, 1,
                                 lv.GRID_ALIGN.CENTER, 1, 1 )
        lon_label.set_size( 80, 25 )
        lon_label.add_style( self.style_manager.style('app_text_normal'),
                             lv.PART.MAIN )
        
        fmt_label = lv.label( geo_pane )
        fmt_label.set_text( 'Format: ' )
        fmt_label.set_grid_cell( lv.GRID_ALIGN.START, 2, 1,
                                 lv.GRID_ALIGN.CENTER, 1, 1 )
        fmt_label.set_size( 80, 25 )
        fmt_label.add_style( self.style_manager.style('app_text_normal'),
                             lv.PART.MAIN )
        
        #  3rd Row (Latitude, Longitude, Format Entries)
        lat_text = lv.textarea( geo_pane )
        lat_text.set_one_line( True )
        lat_text.set_grid_cell( lv.GRID_ALIGN.START, 0, 1,
                                lv.GRID_ALIGN.CENTER, 2, 2 )
        lat_text.set_size( 100, 25 )

        
        lon_text = lv.textarea( geo_pane )
        lon_text.set_one_line( True )
        lon_text.set_grid_cell( lv.GRID_ALIGN.START, 1, 1,
                                lv.GRID_ALIGN.CENTER, 2, 2 )
        lon_text.set_size( 100, 25 )


        fmt_chk_d = lv.checkbox( geo_pane )
        fmt_chk_d.set_text( 'Degrees' )
        fmt_chk_d.set_grid_cell( lv.GRID_ALIGN.START, 2, 1,
                                 lv.GRID_ALIGN.CENTER, 2, 1 )
        fmt_chk_d.add_style( self.style_manager.style('app_text_normal'),
                             lv.PART.MAIN )

        fmt_chk_r = lv.checkbox( geo_pane )
        fmt_chk_r.set_text( 'Radians' )
        fmt_chk_r.set_grid_cell( lv.GRID_ALIGN.START, 2, 1,
                                 lv.GRID_ALIGN.CENTER, 3, 1 )
        fmt_chk_r.add_style( self.style_manager.style('app_text_normal'),
                             lv.PART.MAIN )

    def init_callbacks( self ):

        #  Callback
        def keyboard_callback( event, name ):
            
            #  Skip if we are not active
            if self.is_active == False:
                return
            
            #  Look for escape key
            self.logger.debug( f'Event: {event.code}, Type: {get_event_name(lv.EVENT, event.code)}, Context: {name}, Key: {event.get_key()}' )
            if event.code == lv.KEY.ESC:
                self.logger.info( f'Escape Detected: Moving back to parent page.' )
                self.parent.notify_action( Action.KEY_ESC )

            if event.code == lv.EVENT.KEY:
                action = Action.keyboard_to_action( event.get_key() )
                if action == Action.KEY_ESC:
                    self.logger.info( f'Escape Detected: Moving back to parent page.' )
                    self.parent.notify_action( Action.KEY_ESC, 'main' )

        #  Setup Event Monitor
        self.body.add_event_cb( lambda event,
                                       event_name = self.name: keyboard_callback(event,
                                                                                 event_name),
                                       lv.EVENT.ALL,
                                       None )

    @staticmethod
    def create( config:         Configuration,
                style_manager:  Style_Manager,
                parent ):
        
        app = App( config,
                   style_manager,
                   parent )

        app.initialize()

        return app
    