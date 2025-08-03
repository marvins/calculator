
cmake_minimum_required(VERSION 4.0.0 FATAL_ERROR)

# Setup board for Pico
#  Pico 1:  pico
#  Pico 1W: pico_w
#  Pico 2:  pico2
#  Pico 2W: pico2_w
set(PICO_BOARD pico2_w)

include( $ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)

project( pico_lvgl_display_demo
    LANGUAGES CXX C
)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()

include_directories(
  ${CMAKE_CURRENT_LIST_DIR}
)

#  Add in each sub-project
add_subdirectory(i2ckbd)
add_subdirectory(lcdspi)

#  Add in LVGL Library
add_subdirectory(./lib/lvgl)


add_executable(pico_lvgl_display_demo
    src/main.cpp
    src/picocalc/lv_port_indev_picocalc_kb.c
    src/picocalc/lv_port_disp_picocalc_ILI9488.c
)

target_compile_options(pico_lvgl_display_demo
    PRIVATE
    -DPICOMITE
    -DPICO_HEAP_SIZE=0x1000
    -DGUICONTROLS
    -DPICO_CORE0_STACK_SIZE=0x1000 )

target_compile_definitions(pico_lvgl_display_demo PRIVATE LV_USE_DEMO_WIDGETS=1)

target_include_directories(pico_lvgl_display_demo PRIVATE
    ${CMAKE_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/lib
    ${CMAKE_SOURCE_DIR}/lib/lvgl
    ${CMAKE_SOURCE_DIR}/lib/lvgl/lvgl/src
    ${CMAKE_SOURCE_DIR}/lib/lvgl/lvgl/demos
)


target_link_libraries(pico_lvgl_display_demo
  pico_stdlib
  hardware_flash
  hardware_irq
  hardware_adc
  hardware_pwm
  hardware_i2c
  hardware_spi
  hardware_dma
  hardware_exception
  hardware_pio
  pico_multicore
  i2ckbd
  lcdspi
  lvgl
  lvgl_demos
)

pico_enable_stdio_usb(pico_lvgl_display_demo 0)
pico_enable_stdio_uart(pico_lvgl_display_demo 1)
pico_add_extra_outputs(pico_lvgl_display_demo)
