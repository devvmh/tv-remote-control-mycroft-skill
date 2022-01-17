# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/tv.svg" card_color="#FD9E66" width="50" height="50" style="vertical-align:bottom"/> TV Remote Control
Mycroft AI voice interface to control a tv (e.g. using lirc)

## About
This skill defines voice commands for controlling a tv. how this actually works is up to you - you'll need to install lirc or something and then create a shell script or something to actually turn on the tv.

## Examples
* "Turn on the TV"
* "Turn off the TV"
* "Switch to HDMI 2"
* "Switch to HDMI 3"
* "Switch to media player"
* "Switch to computer"
* "Switch to dvd player"

## Required setup

Note: out of the box, this won't do much but say "OK, turning on the TV" back to you. You need to specify shell commands at https://home.mycroft.ai/skills.

You need to set up some functions that actually interact with your TV.  For example, you might set the "turn on" shell command there to send IR data using LIRC:

    irsend send_once samsung KEY_POWER

For more complex commands, you can write your own shell script and save it, then reference that shell command directly:

    /usr/local/bin/turnon.sh

For complex commands like "Switch to <input-name>" you'll almost certainly need a shell script. Mycroft will pass the name specified by the user to the shell script as an argument. For example, if you say "Hey Mycroft, switch the tv to hdmi 1", and you've set the shell command to `/usr/local/bin/switchto.sh`, then Mycroft will execute this command:

    /usr/local/bin/switchto.sh hdmi 1

So as long as your script can handle that argument, you'll be able to execute what you want. A sample switchto.sh is available at [docs/sample-switchto.sh](./docs/sample-switchto.sh).

## Credits
Devin Howard

## Category
**Entertainment**
Media

## Tags
#TV
#LIRC
#IR
#RemoteControl
#Television
