#
#


import lvgl as lv

from config import Configuration


class Main_Footer:

    def __init__( self, config, parent ):

        self.config = config
        self.parent = parent

    def initialize( self ):
        
        #  Create body
        self.body = lv.obj( self.parent )
        self.body.center()
        self.body.set_layout( lv.LAYOUT.FLEX )
        self.body.set_flex_flow( lv.FLEX_FLOW.ROW )
        self.body.set_size( self.config.get('screen','width')-10,
                            self.config.get('app','footer_height') )