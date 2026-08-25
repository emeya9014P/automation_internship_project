Feature: JavaScript alert
  Scenario: User can close Javascript alert
    Given Go to the-internet.herokuapp.com
    When Click on JavaScript Alerts link
    And Click on "Click for JS Alert" button
    Then Click "Okay" button in the alert window
    Then Verify result "You successfully clicked an alert" shown

