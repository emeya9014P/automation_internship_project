Feature: Handling multiple windows

  Scenario: User can handle multiple windows
    Given Go to the-internet.herokuapp.com
    When Click on Multiple Windows link
    And Click on Click Here link to open new window
    Then Verify text "New Window" opened in the new window
    And Switch back to original window
    Then Verify original window header "Opening a new window" is displayed