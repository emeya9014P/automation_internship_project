Feature: ActionChain - Hovers
  Scenario: User can hover element
    Given Go to the-internet.herokuapp.com for actionchain test
    When Click on "Hovers" link
    And Hover over the first user avatar
    And Click on "View profile" link
    Then Verify "Not Found" text is displayed