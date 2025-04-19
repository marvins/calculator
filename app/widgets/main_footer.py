#
#


import lvgl as lv

from config    import Configuration
from core      import Icon_Set
from utilities.lvgl_debug import debug_print

class Main_Footer:

    def __init__( self, config, style_manager, parent ):

        self.config = config
        self.style_manager = style_manager
        self.parent = parent

        self.commands = []

    def initialize( self ):
        
        #  Create body
        self.body = lv.obj( self.parent )
        self.body.set_flex_flow( lv.FLEX_FLOW.ROW )
        self.body.set_flex_align(lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.START, lv.FLEX_ALIGN.CENTER)
        self.body.set_style_pad_all(0, lv.PART.MAIN)
        self.body.set_style_pad_gap(0, lv.PART.MAIN)
        
        self.body.set_size( self.config.get_section('screen','width')-10,
                            self.config.get_section('main','footer_height') )
        
        #  Add each icon
        for cmd in self.commands:

            #  Get the icon
            icon_path = self.config.get_image_path( Icon_Set.icon_tag( cmd['icon'] ) )
            print( f'Loading icon: ', icon_path )

            png_data = None
            with open( icon_path, 'rb') as f:
                png_data = f.read()

            png_image_dsc = lv.image_dsc_t({
                'data_size': len(png_data),
                'data': png_data 
            })

            # Create an image using the decoder
            img = lv.image(self.body)
            img.set_src(png_image_dsc)

            #  Add label
            lbl = lv.label(self.body)
            lbl.set_text( cmd['title'] )
            lbl.add_style( self.style_manager.style('footer_text_normal'),
                           lv.PART.MAIN )
        
    #  Add icons
    def add_command( self, icon: Icon_Set, title: str ):

        self.commands.append( { 'icon': icon, 'title': title } )


