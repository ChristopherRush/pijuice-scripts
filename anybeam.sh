#!/bin/bash

function mode_select()
{
  echo "Select one of the options below:"
  echo "Mode 1 - RGB 888 (Default)"
  echo "Mode 2 - RGB 666"
  echo "Mode 3 - RGB 666 + GPIO26"
  echo "Mode 4 - RGB 666 + GPOI26 + GPIO27"
  while true; do
          read -r -p 'Option: ' mode < /dev/stdin
          if [[ "$mode" == 1 ]] || [[ "$mode" == 2 ]] || [[ "$mode" == 3 ]] || [[ "$mode" == 4 ]]; then
                  break
          fi
  done
}


function configure_mode()
{
  if grep -Fxq "#AnyBeam" /boot/config.txt; then
    sed -i '/#AnyBeam/,$d' /boot/config.txt
  fi

  case $mode in
    1)
    cat >> /boot/config.txt <<EOF
#AnyBeam
dtoverlay=dpi24
overscan_left=0
overscan_right=0
overscan_top=0
overscan_bottom=0
framebuffer_width=1280
framebuffer_height=720
enable_dpi_lcd=1
display_default_lcd=1
dpi_group=2
dpi_mode=85
dpi_output_format=0x070027
EOF
    ;;
    2)
    cat >> /boot/config.txt <<EOF
#AnyBeam
dtoverlay=dpi24
overscan_left=0
overscan_right=0
overscan_top=0
overscan_bottom=0
framebuffer_width=1280
framebuffer_height=720
enable_dpi_lcd=1
display_default_lcd=1
dpi_group=2
dpi_mode=85
dpi_output_format=0x070026
EOF
    ;;
    3)
    cat >> /boot/config.txt <<EOF
#AnyBeam
dtoverlay=dpi24
overscan_left=0
overscan_right=0
overscan_top=0
overscan_bottom=0
framebuffer_width=1280
framebuffer_height=720
enable_dpi_lcd=1
display_default_lcd=1
dpi_group=2
dpi_mode=85
dpi_output_format=0x070026
EOF
    ;;
    4)
    cat >> /boot/config.txt <<EOF
#AnyBeam
dtoverlay=dpi24
overscan_left=0
overscan_right=0
overscan_top=0
overscan_bottom=0
framebuffer_width=1280
framebuffer_height=720
enable_dpi_lcd=1
display_default_lcd=1
dpi_group=2
dpi_mode=85
dpi_output_format=0x070026
dtoverlay=i2c-gpio,i2c_gpio_delay_us=1,i2c_gpio_sda=26,i2c_gpio_scl=27
EOF
    ;;
  esac
}

function reboot()
{
  echo "Rebooting system now......."
  sleep 3
  reboot
  exit 0
}

#Main function
mode_select
configure_mode
reboot
