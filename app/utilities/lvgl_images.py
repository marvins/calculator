

import lvgl as lv



def compute_xy_scale( image: lv.image,
                      dest_size ):
    
    x_scale = int( 256 * float( dest_size[0] ) / image.get_self_width() )
    y_scale = int( 256 * float( dest_size[1] ) / image.get_self_height() )

    return (x_scale, y_scale)