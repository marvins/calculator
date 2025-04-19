


import fs_driver
import json

import lvgl as lv


class Font_Manager:

    def __init__( self, font_list ):

        #  Only load fonts on request
        self.font_list = font_list
        self.loaded_fonts = {}

    def font( self, tag ):

        #  Check the list of loaded fonts
        if tag in self.loaded_fonts.keys():
            return self.loaded_fonts[tag]
        
        #  Otherwise, load the font
        return self.load_font( tag )

    def load_font( self, tag ):

        #  Check the list of fonts
        if tag in self.font_list.keys():
            fs_drv = lv.fs_drv_t()
            fs_driver.fs_register(fs_drv, 'S')
            print( f'Loading font: {self.font_list[tag]}' )
            self.loaded_fonts[tag] = lv.binfont_create("S:" + self.font_list[tag])
            return self.loaded_fonts[tag]

        raise Exception( f'No font registered to tag: {tag}' )
    
    @staticmethod
    def create( font_path ):
        
        #  Load the config file
        conf = {}
        with open( font_path, 'r' ) as fin:
            conf = json.loads( fin.read() )
        
        return Font_Manager( conf )
    
