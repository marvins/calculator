

import logging

import lvgl as lv

from apps.app_manager      import App_Manager
from config                import Configuration
from core                  import Action
from utilities.lvgl_events import get_event_name
from utilities.lvgl_images import compute_xy_scale
from utilities.lvgl_styles import Style_Manager

        
class Main_Menu:

    PAD_ALL = 5
    PAD_GAP = 5

    def __init__( self,
                  config: Configuration,
                  style_manager: Style_Manager,
                  app_manager: App_Manager,
                  parent ):
        
        self.config        = config
        self.style_manager = style_manager
        self.parent        = parent
        self.app_manager   = app_manager

        #  Flag if we are active
        self.is_active = True

        #  Information about widgets
        self.icons_per_row = 0
        self.num_icons     = 0

        #  List of buttons
        self.buttons = []

        self.button_info = {}

        self.logger = logging.getLogger( 'Main_Menu' )

    def initialize( self ):

        #  Get a list of objects to create
        icon_sets = self.app_manager.get_icon_data()
        col_desc, row_desc = self.create_icon_descriptors( len( icon_sets ) )
        self.logger.debug( 'Descriptors Cols: ', col_desc, 
                           ', Rows: ', row_desc )
        self.icons_per_row = len( col_desc ) - 1
        
        #  Create body
        self.body = lv.obj( self.parent.body )

        #  Set body size
        menu_size = self.menu_size()
        self.body.set_size( menu_size[0], menu_size[1] )
        self.body.center()

        icon_gap    = self.config.get_section( 'main', 'menu_icon_gap' )

        self.body.set_grid_align( lv.GRID_ALIGN.STRETCH,
                                  lv.GRID_ALIGN.START )
        self.body.set_grid_dsc_array(col_desc, row_desc)

        self.body.set_style_pad_all( icon_gap, lv.PART.MAIN)

        self.body.set_style_pad_gap( icon_gap, lv.PART.MAIN )
        self.body.add_style( self.style_manager.style('header_normal'), lv.PART.MAIN )
        
        icon_width  = self.config.get_section( 'main', 'menu_icon_width' )
        icon_height = self.config.get_section( 'main', 'menu_icon_height' )
                
        #  Callback
        def button_callback( event, name, button_id: int ):
            
            #  If we are not active, ignore us
            if self.is_active == False:
                return
            
            #  Otherwise, continue
            self.logger.info( f'Button Event: {get_event_name(lv.EVENT, event.code)}, Name: {name}, ID: {button_id}, Key: {event.get_key()}' )
            if event.code == lv.EVENT.CLICKED:
                self.logger.info( f'Button for {name} selected' )
                return self.parent.notify_action( Action.APP_LAUNCH, name )

            if event.code == lv.EVENT.KEY:
                action = Action.keyboard_to_action( event.get_key() )

                if action == Action.KEY_ARROW_LEFT:
                    self.bgroup.focus_prev()
                
                if action == Action.KEY_ARROW_RIGHT:
                    self.bgroup.focus_next()

        
        self.bgroup = lv.group_create()
            
        #  Build out the icons
        for ic in icon_sets:
        
            icon_col = int( self.num_icons % ( len( col_desc ) - 1 ) )
            icon_row = int( self.num_icons / ( len( col_desc ) - 1 ) )

            #  Create the button
            btn = lv.button( self.body )
            self.bgroup.add_obj( btn )

            #  Always set the first icon to focused
            focus_tag = 'menu_button'
            btn.add_style( self.style_manager.style( focus_tag ),
                           lv.PART.MAIN )

            #  Position in the parent widget  
            btn.set_grid_cell( lv.GRID_ALIGN.CENTER, icon_col, 1,
                               lv.GRID_ALIGN.START, icon_row, 1 )

            #  Setup layout for button itself
            btn.set_layout( lv.LAYOUT.FLEX )

            btn.set_flex_flow( lv.FLEX_FLOW.COLUMN )
            
            btn.set_flex_align( lv.FLEX_ALIGN.SPACE_EVENLY, 
                                lv.FLEX_ALIGN.CENTER,
                                lv.FLEX_ALIGN.CENTER )
            btn.set_style_pad_all( 10, lv.PART.MAIN )
            btn.set_style_pad_gap( 7, lv.PART.MAIN )

            btn.center()

            btn.set_size( icon_width, icon_height )
            
            

            #  Button Image
            btn_image = lv.image( btn )

            png_data = None
            with open( icon_sets[ic]['icon_path'], 'rb') as f:
                png_data = f.read()

            img_desc = lv.image_dsc_t({
                'data_size': len(png_data),
                'data': png_data 
            })

            btn_image.set_src( img_desc )
            
            img_scale = compute_xy_scale( btn_image,
                                          (icon_width  - icon_gap*2,
                                           icon_height - icon_gap*2 ) )
            btn_image.set_scale_x( img_scale[0] )
            btn_image.set_scale_y( img_scale[1] )
            btn_image.center()
            btn_image.set_flex_grow( 4 )

            #  Button Label
            btn_label = lv.label( btn )
            btn_label.set_text( icon_sets[ic]['title'] )
            btn_label.center()
            btn_label.set_flex_grow( 0 )
            btn_label.add_style( self.style_manager.style( 'menu_text' ),
                                 lv.PART.MAIN )
            
            self.button_info[self.num_icons] = { 'name': ic }
            
            #  Setup Event Monitor
            btn.add_event_cb( lambda event, 
                                     button_name = ic,
                                     button_id = self.num_icons: button_callback( event,
                                                                                  button_name, 
                                                                                  button_id), 
                             lv.EVENT.ALL,
                             None )
            btn.add_flag( lv.obj.FLAG.EVENT_BUBBLE )

            self.buttons.append( btn )
            self.num_icons += 1

        
        self.parent.driver.keyboard.set_group( self.bgroup )

    def create_icon_descriptors( self, num_icons ):

        col_desc = []
        row_desc = []

        #  Get width, height, and gap
        icon_width  = self.config.get_section( 'main', 'menu_icon_width' )
        icon_height = self.config.get_section( 'main', 'menu_icon_height' )
        icon_gap    = self.config.get_section( 'main', 'menu_icon_gap' )
        
        # Get screen info
        window_width  = self.config.get_section( 'screen', 'width' )
        window_height = self.config.get_section( 'screen', 'height' )

        #  Compute the amount of icons we can fit per row/col
        icons_per_col = int( ( window_width - icon_gap ) / ( icon_width + icon_gap ) )
        number_rows = num_icons / icons_per_col

        #  Align columns
        col_desc = []
        for x in range( icons_per_col ):
            col_desc.append( icon_width )
        col_desc.append( lv.GRID_TEMPLATE_LAST )

        #  Align rows
        row_desc = []
        for x in range( number_rows ):
            row_desc.append( icon_height )
        row_desc.append( lv.GRID_TEMPLATE_LAST )

        return (col_desc, row_desc)
    
    def menu_size(self):

        win_x = self.config.get_section( 'screen', 'width' )
        win_y = self.config.get_section( 'screen', 'height' )

        hdr_y = self.config.get_section( 'main', 'header_height' )
        ftr_y = self.config.get_section( 'main', 'footer_height' )

        return ( win_x - Main_Menu.PAD_ALL, 
                 win_y - hdr_y - ftr_y - Main_Menu.PAD_GAP - Main_Menu.PAD_ALL )