Feature: switch-inputs
  Scenario Outline: Switching inputs
    Given an English speaking user
    When the user says "switch the tv to <input_name>"
    Then "tv-remote-control-skill" should reply with dialog from "control.remote.tv.switchto.dialog"
    Examples: input names
      | input_name  |
      | hdmi 1     |
      | chromecast |

