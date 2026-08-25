Feature: iframe handling on the-internet.herokuapp.com

  Scenario: User can switch to iframe and enter text
    Given Go to the-internet.herokuapp.com
    When Click on the Frames
    And Click on the iFrame
    Then Enter text "Hello iFrame!"
    Then Verify the text inside iframe "Hello iFrame!"