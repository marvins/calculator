
// C++ Standard Libraries
#include <cstdio>
#include <cstring>
#include <filesystem>
#include <iostream>
#include <sstream>
#include <string>

// PICO APIs
#include "hardware/gpio.h"
#include "pico/stdlib.h"

// LVGL
#include <lv_conf.h>
#include <lvgl/lvgl.h>

// PicoCalc Drivers
#include <picocalc/lv_port_indev_picocalc_kb.h>
#include <picocalc/lv_port_disp_picocalc_ILI9488.h>


#include <resources/images/logo_235_65.hpp>

#define ILI9488 1
#define USE_DEFAULT_DEMO 1

#define BYTE_PER_PIXEL (LV_COLOR_FORMAT_GET_SIZE(LV_COLOR_FORMAT_RGB565)) /*will be 2 for RGB565 */

const unsigned int LEDPIN = 25;

// The event handler
static void textarea_event_handler(lv_event_t *e) {
    auto textarea = reinterpret_cast<lv_obj_t*>( lv_event_get_target( e ) );
    printf("Textarea: '%s'\n", lv_textarea_get_text(textarea));
}


int main()
{
    // Initialize standard I/O
    stdio_init_all();

    // Initialize LED
    gpio_init(LEDPIN);
    gpio_set_dir(LEDPIN, GPIO_OUT);

    // Initialize LVGL
    lv_init();

    // Initialize the custom display driver
    lv_port_disp_init();

    // Initialize the keyboard input device (implementation in lv_port_indev_kbd.c)
    lv_port_indev_init();


    // Create a screen
    lv_obj_t *screen = lv_obj_create(NULL);

    // Parent Column
    lv_obj_t* cont_col = lv_obj_create(screen);
    lv_obj_set_size(cont_col, 315, 315);
    lv_obj_align(cont_col, LV_ALIGN_TOP_MID, 0, 5);
    lv_obj_set_flex_flow(cont_col, LV_FLEX_FLOW_COLUMN);

    // The textarea
    lv_obj_t *input = lv_textarea_create(cont_col);
    lv_obj_set_width(input, 280);
    lv_obj_set_height(input, LV_SIZE_CONTENT);
    lv_obj_center(input);

    // Image
    //LV_IMAGE_DECLARE( logo_235_65 );
    //lv_obj_t * img1 = lv_image_create(cont_col);
    //lv_image_set_src(img1, &logo_235_65);


    // Enable keyboard input for the text box
    lv_textarea_set_placeholder_text(input, "Input:");
    lv_textarea_set_one_line(input, true);

    lv_obj_set_style_anim_time(input, 5000, LV_PART_CURSOR|LV_STATE_FOCUSED);

    // Textarea event handler
    lv_obj_add_event_cb(input, textarea_event_handler, LV_EVENT_READY, input);

    /// File Lister
    lv_obj_t *file_lister = lv_textarea_create(cont_col);
    lv_obj_set_size( file_lister, 300, 270 );
    lv_obj_center(file_lister);

    std::stringstream file_text;
    file_text << "Content\n";
    for (auto const& dir_entry : std::filesystem::recursive_directory_iterator{"/"} ) {
        file_text << dir_entry << std::endl;
    }

    lv_textarea_set_text( file_lister, file_text.str().c_str() );

    // Load the screen
    lv_scr_load(screen);

    // Main loop
    while (1)
    {
        lv_timer_handler();
        lv_tick_inc(20); // Increment LVGL tick by 5 milliseconds
        sleep_ms(5); // Sleep for 5 milliseconds}
    }
}
