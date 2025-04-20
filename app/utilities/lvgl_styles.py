

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

    COLOR_MAP = { 'white': lv.color_white(),
                  'black':  lv.color_black() }

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

        #  Text Font
        if len(cfg['text_font']) > 0:
            new_style.set_text_font( self.font_manager.font( cfg['text_font'] ) )
        
        #  Background Color
        if len(cfg['bg_color']) > 0:
            bg_color = cfg['bg_color']
            if bg_color in list(Style_Manager.COLOR_MAP.keys()):
                new_style.set_bg_color( Style_Manager.COLOR_MAP[bg_color] )

        #  Set the background gradient color
        if len(cfg['outline_color']) > 0:
            outline_color = cfg['outline_color']
            if outline_color in list(Style_Manager.COLOR_MAP.keys()):
                new_style.set_outline_color( Style_Manager.COLOR_MAP[outline_color] )
        
        #  Set the outline opacity
        if len(cfg['outline_opacity']) > 0:
            outline_opa = int(cfg['outline_opacity'])
            new_style.set_outline_opa( outline_opa )

        #  Set the outline width
        if len(cfg['outline_width']) > 0:
            outline_width = int(cfg['outline_width'])
            new_style.set_outline_width( outline_width )

        #  Set the text color
        if len(cfg['text_color']) > 0:
            text_color = cfg['text_color']
            if text_color in list(Style_Manager.COLOR_MAP.keys()):
                new_style.set_text_color( Style_Manager.COLOR_MAP[text_color] )
            

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
    
