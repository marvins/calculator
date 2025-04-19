

#  LVGL Libraries
import lvgl as lv


def debug_print( value ):

    if isinstance( value, lv.font_t ):
        output  =  'lvgl.font_t\n'
        output += f'  - str: {value}\n'
        output += f'  - dir: {dir(value)}\n'
        output += f'  - base_line: {value.base_line}\n'
        output += f'  - dsc: {value.dsc}\n'
        output += f'  - line_height: {value.line_height}\n'

        #output += f'   -> {value.get_glyph_dsc()}\n'
        #output += f'   -> {value.get_glyph_dsc_fmt_txt()}\n'
        #output += f'   -> {value.get_glyph_width()}\n'
        #output += f'   -> {value.get_line_height()}\n'
        
        print(output)
