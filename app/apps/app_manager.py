
#  Project Libraries
from config                import Configuration
from utilities.lvgl_styles import Style_Manager

#  Applications
from apps.calculator.Application import App as Calculator_App
from apps.editor.Application     import App as Editor_App
from apps.geo_coord.Application  import App as GeoCoord_App
from apps.settings.Application   import App as Settings_App
from apps.terminal.Application   import App as Terminal_App

class App_Manager:

    def __init__( self,
                  app_configs,
                  style_manager,
                  driver ):
        
        self.app_configs   = app_configs
        self.style_manager = style_manager
        self.driver        = driver

        self.app_loaders = { 'calculator': Calculator_App,
                             'geocoord':   GeoCoord_App,
                             'editor':     Editor_App,
                             'settings':   Settings_App ,
                             'terminal':   Terminal_App }

    def get_icon_data( self ):
        return self.app_configs
    
    def get_app_instance( self, tag ):

        #  get the folder
        app_cfg = self.app_configs[tag]

        #  Create instance
        return self.app_loaders[tag]

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