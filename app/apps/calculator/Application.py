

#  Project Libraries
from config                 import Configuration
from core                   import Icon_Set
from utilities.lvgl_styles  import Style_Manager
from widgets.main_header    import Main_Header
from widgets.main_footer    import Main_Footer

#  LVGL
import lvgl as lv
from lv_utils import event_loop


member_name_cache = {}

def get_member_name(obj, value):
    try:
        return member_name_cache[id(obj)][id(value)]
    except KeyError:
        pass

    for member in dir(obj):
        if getattr(obj, member) == value:
            try:
                member_name_cache[id(obj)][id(value)] = member
            except KeyError:
                member_name_cache[id(obj)] = {id(value): member}
            return member

class App:

    def __init__( self,
                  config:        Configuration,
                  style_manager: Style_Manager,
                  parent ):
        
        self.config        = config
        self.style_manager = style_manager
        self.parent        = parent


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
        self.footer.add_command( Icon_Set.ESCAPE, 'Back' )
        self.footer.initialize()

        #  Setup Callbacks
        self.init_callbacks()

        return lv.screen_load( self.body )
    
    def init_calbacks( self ):

        #  Callback
        def button_callback( event, name ):
            
            event_name = get_member_name(lv.EVENT, event.code)
            print( f'Event: {event_name}, Button Name: {name}' )
            
            #  Look for escape key
            if event.code == lv.KEY.ESC:
                lv.sceen_load( self.parent )

                

    @staticmethod
    def create( config:        Configuration,
                style_manager: Style_Manager,
                parent ):
        
        app = App( config,
                   style_manager,
                   parent )

        app.initialize()

        return app
    