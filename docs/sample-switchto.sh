#!/bin/bash

switchto_hdmi1() {
  irsend send_once scepter KEY_CHANNELUP
  irsend send_once scepter KEY_MODE
}

switchto_hdmi2() {
  irsend send_once scepter KEY_HOME
}

switchto_hdmi3() {
  irsend send_once scepter KEY_HOME
  irsend send_once scepter KEY_MODE
}

main() {
  EXTRA_ARGS=${@,,}
  case "${EXTRA_ARGS}" in
    'hdmi 1') switchto_hdmi1 ;;
    'hdmi 2') switchto_hdmi2 ;;
    'hdmi 3') switchto_hdmi3 ;;
    'chromecast') switchto_hdmi2 ;;
    'media player') switchto_hdmi2 ;;
    'computer') switchto_hdmi3 ;;
    'dvd player') switchto_hdmi3 ;;
    *) echo "No matches. Args were: ${EXTRA_ARGS}" ;;
  esac
}
main $@
