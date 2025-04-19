

import lvgl as lv

from apps.app_manager import App_Manager
from config import Configuration
from utilities.lvgl_styles import Style_Manager

class Main_Menu:

    PAD_ALL = 5
    PAD_GAP = 5

    def __init__( self,
                  config: Configuration,
                  style_manager: Style_Manager,
                  app_manager: App_Manager,
                  parent, ):
        
        self.config        = config
        self.style_manager = style_manager
        self.parent        = parent
        self.app_manager   = app_manager

    def initialize( self ):
        
        #  Create body
        self.body = lv.obj( self.parent )
        self.body.set_style_pad_all( Main_Menu.PAD_ALL, lv.PART.MAIN)
        self.body.set_style_pad_gap( Main_Menu.PAD_GAP, lv.PART.MAIN)
        self.body.add_style( self.style_manager.style('header_normal'), lv.PART.MAIN )

        menu_size = self.menu_size()
        self.body.set_size( menu_size[0], menu_size[1] )
        
        #  Get a list of objects to create
        icon_sets = self.app_manager.get_icon_data()

        #  Create the column and row descriptors
        print( 'Computing Descriptors' )
        col_desc, row_desc = self.create_icon_descriptors( len( icon_sets ) )
        self.body.set_style_grid_column_dsc_array( col_desc, 0 )
        self.body.set_style_grid_row_dsc_array( row_desc, 0 )
        
        icon_width  = self.config.get_section( 'main', 'menu_icon_width' )
        icon_height = self.config.get_section( 'main', 'menu_icon_height' )

        #  Build out the icons
        counter = 0
        for ic in icon_sets:
        
            icon_col = int( counter % ( len( col_desc ) - 1 ) )
            icon_row = int( counter / ( len( col_desc ) - 1 ) )

            #  Create the button
            btn = lv.button( self.body )
            btn.set_flex_flow( lv.FLEX_FLOW.COLUMN )
            btn.set_flex_align(lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
            btn.set_size( icon_width, icon_height )
            
            btn.set_grid_cell( lv.GRID_ALIGN.STRETCH, icon_col, 1,
                               lv.GRID_ALIGN.STRETCH, icon_row, 1 )

            counter += 1

            btn_image = lv.image( btn )
            print( f'Icon Col: {icon_col}, Row: {icon_row}' )
            print( 'Setting Path: ', icon_sets[ic]['icon_path'] )
            btn_image.set_src( icon_sets[ic]['icon_path'] )
        
            btn_label = lv.label( btn )
            print( 'Setting Text: ', icon_sets[ic]['title'] )
            btn_label.set_text( icon_sets[ic]['title'] )
    
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
        icons_per_row = int( ( window_width - icon_gap ) / ( icon_width + icon_gap ) )
        print( f'Icons Per Row: {icons_per_row}' )

        col_desc = [  icon_width,  icon_width, lv.GRID_TEMPLATE_LAST ]
        row_desc = [ icon_height, icon_height, lv.GRID_TEMPLATE_LAST ]

        return (col_desc, row_desc)
    
    def menu_size(self):

        win_x = self.config.get_section( 'screen', 'width' )
        win_y = self.config.get_section( 'screen', 'height' )

        hdr_y = self.config.get_section( 'main', 'header_height' )
        ftr_y = self.config.get_section( 'main', 'footer_height' )

        return ( win_x - Main_Menu.PAD_ALL, 
                 win_y - hdr_y - ftr_y - Main_Menu.PAD_GAP - Main_Menu.PAD_ALL )