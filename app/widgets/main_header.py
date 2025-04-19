#
#


import lvgl as lv

from config import Configuration


class Main_Header:

    def __init__( self, config, style_manager, parent ):

        self.config = config
        self.style_manager = style_manager
        self.parent = parent

    def initialize( self ):
        
        #  Create body
        self.body = lv.obj( self.parent )
        self.body.set_flex_flow( lv.FLEX_FLOW.ROW )
        self.body.set_flex_align(lv.FLEX_ALIGN.SPACE_EVENLY, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER)
        self.body.set_style_pad_all(0, lv.PART.MAIN)
        self.body.set_style_pad_gap(0, lv.PART.MAIN)
        self.body.add_style( self.style_manager.style('header_normal'),
                             lv.PART.MAIN )
        
        self.body.set_size( self.config.get_section('screen','width')-10,
                            self.config.get_section('app','header_height') )
        
        #  Add label
        self.title = lv.label( self.body )
        self.title.set_text( 'Calculator' )
        self.title.set_style_pad_gap(0, lv.PART.MAIN )
        #self.title.set_height( self.body.get_height()-5 )
        self.title.center()

