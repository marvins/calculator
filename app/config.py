#
#


#  Python Libraries
import json
import sys
import time


class Configuration:
    '''
    Stores application configuration information
    '''

    def __init__( self,
                  cmd_args: dict[str],
                  cfg_args: dict[str] ):
        
        self.cmd_args = cmd_args
        self.cfg_args = cfg_args

        self.global_styles = {}

        self.load_image_list()

    def get_global( self, key: str ):
        return self.cfg_args[key]
    
    def get_section( self, section: str, key: str ):

        return self.cfg_args[section][key]

    def load_image_list(self):

        with open( self.cfg_args['image_lut'], 'r' ) as fin:
            self.image_list = json.loads( fin.read() )


    def get_image_path( self, tag: str ):
        return self.image_list[tag]
    
    #  Add a global font
    def add_global_style( self, name, style ):
        self.global_styles[name] = style
    
    def get_global_style( self, name ):
        return self.global_styles[name]

    @staticmethod
    def print_usage( app_name ):

        output  = f'usage: {app_name} -c <json> [optional args]\n'
        output += '\n'
        output += '-h | --help          : Print this menu and exit.\n'
        output += '\n'
        output += '-c | --config-path <json> : Path to configuration file.\n'
        output += '             Stores information about system setup.\n'
        output += '\n'
        output += '-g | --gen-config : Create config-file and exit\n.'
        output += '          Note: -c still required as this is dest path.\n'
        output += '\n'

    @staticmethod
    def default_cmd_config():
        
        return { 'app_name':   'calculator',
                 'gen_config': False }
        
    @staticmethod
    def parse_command_line( args ):

        config = Configuration.default_cmd_config()

        #  The application name is always arg 1
        config['app_name'] = args.pop(0)

        #  Parse remaining arguments
        while len(args) > 0:

            #  Get next param
            arg = args.pop(0)

            #  If help
            if arg == '-h' or arg == '--help':
                Configuration.print_usage( config['app_name'] )
                sys.exit(0)

            #  If config-path
            elif arg == '-c' or arg == '--config-path':
                config['config_path'] = args.pop(0)

            #  If generate-config
            elif arg == '-g' or arg == '--gen-config':
                config['gen_config'] = True
            
            #  otherwise, exit
            else:
                raise Exception( f'Unsupported argument: {arg}' )

        return config
    
    @staticmethod
    def generate_config_file( pathname: str ):

        #  Get current date and time
        dtinfo = time.localtime()

        #  Create the dictionary
        data = {  'config_file': { 'date_written': f'{dtinfo[0]}/{dtinfo[1]}/{dtinfo[2]} {dtinfo[3]}:{dtinfo[4]}:{dtinfo[5]}' },
                  'screen': { 'width': 320,
                             'height': 320  },
                  'app': { 'header_height': 30,
                           'footer_height': 30 },
                  'image_lut': '../data/image_list.json',
                  'style_config': '../data/style_config.json',
                  'font_catalog': '../data/font_list.json' }
        with open( pathname, 'w' ) as fout:
        
            fout.write( json.dumps( data ) )


    @staticmethod
    def parse_config_file( pathname = '../data/options.picocalc.json' ):

        #  Open file
        with open( pathname, 'r' ) as fd:
            cfg = json.loads( fd.read() )
            return cfg

    @staticmethod
    def parse( args ):

        #  Parse the command-line
        cmd_args = Configuration.parse_command_line( args )
        
        #  Generate a config-file and exit if requested
        if cmd_args['gen_config']:
            Configuration.generate_config_file( pathname = cmd_args['config_path'] )
            sys.exit(0)

        #  Parse the configuration file
        cfg_args = Configuration.parse_config_file( pathname = cmd_args['config_path'] )

        return Configuration( cmd_args = cmd_args,
                              cfg_args = cfg_args )
