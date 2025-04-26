
from django.http import HttpResponse
from django.template import loader

def index( request ):
    template = loader.get_template('coord_convert/main.html')
    return HttpResponse(template.render())

def main_window( request ):
    
    print( 'HERE!!!!!!!!!!!' )
    template = loader.get_template('coord_convert/geo_panel.html')

    return HttpResponse( template.render() )


def convert_coordinates( request ):

    print( request )