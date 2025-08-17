
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

# Where folder for binary data
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

#  Define Language Standards
set( CMAKE_C_STANDARD   11 )
set( CMAKE_CXX_STANDARD 20 )
set( CMAKE_CXX_STANDARD_REQUIRED ON )

#  Setup the Pico SDK
pico_sdk_init()

#----------------------------------------#
#-          Update Version File         -#
#----------------------------------------#

# Get the current date
string(TIMESTAMP PROJECT_BUILD_DATE "%Y-%m-%d %H:%M:%S" )

configure_file( ${CMAKE_SOURCE_DIR}/templates/version.hpp.in
                ${CMAKE_BINARY_DIR}/include/terminus/version.hpp )

include_directories(
  ${CMAKE_CURRENT_LIST_DIR}
)

#  Add in each driver API
add_subdirectory( src/drivers/i2ckbd )
add_subdirectory( src/drivers/lcdspi )

#  Add in LVGL Library
add_subdirectory( ./lib/lvgl )

add_executable(calculator
    src/main.cpp
    src/picocalc/lv_port_indev_picocalc_kb.c
    src/picocalc/lv_port_disp_picocalc_ILI9488.c
    src/resources/images/logo_235_65.hpp
)

target_compile_options(calculator
    PRIVATE
    -DPICOMITE
    -DPICO_HEAP_SIZE=0x1000
    -DGUICONTROLS
    -DPICO_CORE0_STACK_SIZE=0x1000 )

target_include_directories( calculator PRIVATE
    ${CMAKE_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/lib
    ${CMAKE_SOURCE_DIR}/lib/lvgl
    ${CMAKE_SOURCE_DIR}/lib/lvgl/lvgl/src
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_SOURCE_DIR}/src/drivers
)


target_link_libraries(calculator
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
  FatFs_SPI
)

pico_enable_stdio_usb(calculator 0)
pico_enable_stdio_uart(calculator 1)
pico_add_extra_outputs(calculator)
