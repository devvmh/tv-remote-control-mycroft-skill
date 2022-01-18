Feature: turn-off-tv
  Scenario: Turning off the TV
    Given an English speaking user
    When the user says "turn off the tv"
    Then "tv-remote-control-skill" should reply with dialog from "control.remote.tv.turnoff.dialog"
