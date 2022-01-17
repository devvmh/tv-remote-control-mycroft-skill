from mycroft import MycroftSkill, intent_handler
import subprocess

class TvRemoteControl(MycroftSkill):
    NOT_SET_UP = 'You need to setup the {} command at https://home.mycroft.ai/skills'

    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('control.remote.tv.turnon.intent')
    def handle_turn_on_tv(self, message):
        self.execute_remote_control_command('turnon')

    @intent_handler('control.remote.tv.turnoff.intent')
    def handle_turn_off_tv(self, message):
        self.execute_remote_control_command('turnoff')

    """
      Because there are so many ways we could name inputs, we just make a generic handler for all of them.
      You can add logic to your shell script to handle the various inputs.
      We need to pass two extra arguments to execute_remote_control_command:
        - dialog_data: a key-value map that lets Mycroft acknowledge back what you just said
           - e.g. if you say "Switch to HDMI 1", Mycroft can say "OK, switching to HDMI 1"
        - extra_args: we pass that same value (e.g. "HDMI 1") as an argument to the shell command specified in settings
    """
    @intent_handler('control.remote.tv.switchto.intent')
    def handle_switch_switchto(self, message):
        input_name = message.data.get('input_name')
        self.execute_remote_control_command(
                'switchto',
                {
                    'input_name': input_name
                },
                [
                    input_name
                ])

    """
     Command code for all the handler functions. The key will match settingsmeta.json and the file names in intents/dialogs folders.

     For example, if key were "turnon", we would:
       - speak the dialog from "control.remote.tv.turnon.dialog"
       - fetch the shell command "turnon_shell_command" from the settings
       - If it's not set up, tell the user "You need to setup the turnon command..."
    """
    def execute_remote_control_command(self, key, dialog_data = {}, extra_args = []):
        self.speak_dialog('control.remote.tv.{}'.format(key), dialog_data)
        settings_key = "{}_shell_command".format(key)
        cmd = self.settings.get(settings_key)
        if cmd:
            self.log.debug("Command is: {}".format(cmd))
            subprocess.run(cmd.split(' ') + extra_args)
        else:
            self.log.warn(self.NOT_SET_UP.format(key))

def create_skill():
    return TvRemoteControl()
