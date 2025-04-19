

#  Micropython Libraries
import json

# LVGL
import lvgl as lv

#  Project Libraries
from config import Configuration
from utilities import lvgl_fonts

class Style_Manager:
    '''
    This class stores styles for different use cases. 
    
    Styles consist of the following:
    - Fonts
    '''

    def __init__( self, 
                  style_config: dict,
                  font_manager: lvgl_fonts.Font_Manager ):
        
        self.style_config = style_config
        self.font_manager = font_manager

        self.loaded_styles = {}


    def style( self, tag ):

        if tag in self.loaded_styles.keys():
            return self.loaded_styles[tag]
        
        #  Otherwise, load from scratch
        #  - Step 1:  Get config info
        cfg = self.style_config[tag]

        new_style = lv.style_t()

        new_style.set_text_font( self.font_manager.font( cfg['text_font'] ) )

        self.loaded_styles[tag] = new_style

        return new_style
    

    @staticmethod
    def create( config: Configuration ):

        #  Get the style config
        style_path = config.get_global( 'style_config' )
        style_conf = json.loads( open( style_path, 'r' ).read() )

        #  Get the font config
        font_path = config.get_global( 'font_catalog' )
        font_mgr  = lvgl_fonts.Font_Manager.create( font_path )

        return Style_Manager( style_conf, font_mgr )
    
