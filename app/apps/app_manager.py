
#  Project Libraries
from config                import Configuration
from utilities.lvgl_styles import Style_Manager

class App_Manager:

    def __init__( self,
                  app_configs,
                  style_manager,
                  driver ):
        
        self.app_configs   = app_configs
        self.style_manager = style_manager
        self.driver        = driver

    def get_icon_data( self ):
        return self.app_configs

    @staticmethod
    def create( config,
                style_manager,
                driver ):
        
        app_configs = config.cfg_args['apps']
        for app in app_configs.keys():
            app_configs[app]['icon_path'] = config.get_image_path( app_configs[app]['icon'] )

        #  Load application config
        return App_Manager( app_configs,
                            style_manager,
                            driver )