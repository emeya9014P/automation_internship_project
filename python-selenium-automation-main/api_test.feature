Feature: ReqRes API CRUD Test
    Verify the CRUD operations of ReqRes API
    So that I can ensure user data management works as expected

  Scenario: Get user list vis Get request
      When I send a GET request to "/api/users?page=2"
      Then The response status code should be 200
      And The response body should contain "page" as 2

    Scenario: Create a new user via POST request
      When I send a POST request to "/api/users" with name "Eme" and job "QA Automation Engineer"
      Then The response status code should be 201
      And The response body should contain "id" and "createdAt"

    Scenario: Update existing user details via PUT request
      When I send a PUT request to "/api/users/2" with name "Eme" and job "Senior QA Automation Engineer"
      Then The response status code should be 200
      And The response body field "job" should be "Senior QA Automation Engineer"

    Scenario: Delete a user via DELETE request
      When I send a DELETE request to "/api/users/2"
      Then The response status code should be 204