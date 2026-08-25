Feature: Dropdown
  Scenario: User can control dropdown feature
    Given Go to the-internet.herokuapp.com
    When Click on Dropdown link
    And Select "Option1" from dropdown option
    Then Verify selected dropdown option is "Option 1"


