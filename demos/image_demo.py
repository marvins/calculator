

import lvgl as lv

import display_driver

base = lv.obj()

middle = lv.obj( base )


#  Load the PNG Image
png_data = None
with open('../app/apps/settings/assets/settings_96_96.png', 'rb') as f:
  png_data = f.read()

print( 'Image Size: ', len(png_data) )
png_image_dsc = lv.image_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})

# Create an image using the decoder

image1 = lv.image( middle )
image1.set_src(png_image_dsc)
print( image1.get_width(), ' x ', image1.get_height() )
print( image1.get_self_width(), ' x ', image1.get_self_height() )


lv.screen_load( base )