@api
Feature: Testing Planets SWAPI endpoint

  API testing using python to validate the return of SWAPI API GET method

  @planets_api
  Scenario Outline: Verify GET response from Planets SWAPI endpoint
    Given a SWAPI endpoint
    When I send a GET request to the SWAPI endpoint with "<endpoint>"
    Then I expect the response status code to be "<status_code>"
    And I expect the response body to match the "<expected_payload>"
  Examples:
    | endpoint                  | status_code | expected_payload                 |
    | planets/1/                | 200         | planets_tatooine_payload.json    |
    | planets/                  | 200         | planets_payload.json             |
    | planets/?search=Coruscant | 200         | planets_search_name_payload.json |
    | planets/?search=Terra     | 200         | not_found_search_payload.json    |
    | planets/schema/           | 404         | planets_schema.json              |
    | planets/99/               | 404         | info_not_found_payload.json      |