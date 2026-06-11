# Created by emeya at 6/10/2026
Feature: Test cases for off_plan menu

  Scenario: User can open the off-plan page and filter the result with "Out of Stock" option.
    Given Open the main page
    When Log in to the page
    And Click on the 'Off-plan' on the left side menu
    Then Verify the right page opens
    When Click on the 'Search & filters' button
    And Filter it to 'Out of Stock'
    Then Verify that the results show the 'Out of Stock' tag in the result