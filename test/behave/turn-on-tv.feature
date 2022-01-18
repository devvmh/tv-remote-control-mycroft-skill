Feature: turn-on-tv
  Scenario: Turning on the TV
    Given an English speaking user
    When the user says "turn on the tv"
    Then "tv-remote-control-skill" should reply with dialog from "control.remote.tv.turnon.dialog"
