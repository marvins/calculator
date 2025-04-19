import lvgl

def find_lvgl_info( value ):
    for entry in dir( lvgl ):
        if value in str(entry):
            print( entry )

