Feature: Product Search on Google

  Scenario: User can search for products on Google
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown