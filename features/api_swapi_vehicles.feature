@api
Feature: Testing Vehicles SWAPI endpoint

  API testing using python to validate the return of SWAPI API GET method

  @vehicles_api
  Scenario Outline: Verify GET response from Vehicles SWAPI endpoint
    Given a SWAPI endpoint
    When I send a GET request to the SWAPI endpoint with "<endpoint>"
    Then I expect the response status code to be "<status_code>"
    And I expect the response body to match the "<expected_payload>"
  Examples:
    | endpoint                         | status_code | expected_payload                   |
    | vehicles/37/                     | 200         | vehicles_C9979_payload.json        |
    | vehicles/                        | 200         | vehicles_payload.json              |
    | vehicles/?search=AT-ST           | 200         | vehicles_search_name_payload.json  |
    | vehicles/?search=TIE/sa%20bomber | 200         | vehicles_search_model_payload.json |
    | vehicles/?search=Sovereign       | 200         | not_found_search_payload.json      |
    | vehicles/39/                     | 404         | info_not_found_payload.json        |
    | vehicles/schema/                 | 404         | vehicles_schema.json               |