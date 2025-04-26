

#  Project Libraries
from config                 import Configuration
from utilities.lvgl_styles  import Style_Manager


class App_Base:

    def __init__( self,
                  config:         Configuration,
                  style_manager:  Style_Manager,
                  parent ):
        
        self.is_active = False
        
        self.config        = config
        self.style_manager = style_manager
        self.parent        = parent

    def set_active( self, value ):
        self.is_active = value