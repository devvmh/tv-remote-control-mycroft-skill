from mycroft import MycroftSkill, intent_file_handler


class TvRemoteControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.remote.tv.intent')
    def handle_control_remote_tv(self, message):
        self.speak_dialog('control.remote.tv')


def create_skill():
    return TvRemoteControl()

