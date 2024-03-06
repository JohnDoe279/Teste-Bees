@api
Feature: Testing Species SWAPI endpoint

  API testing using python to validate the return of SWAPI API GET method

  @species_api
  Scenario Outline: Verify GET response from Species SWAPI endpoint
    Given a SWAPI endpoint
    When I send a GET request to the SWAPI endpoint with "<endpoint>"
    Then I expect the response status code to be "<status_code>"
    And I expect the response body to match the "<expected_payload>"
  Examples:
    | endpoint                  | status_code | expected_payload                 |
    | species/2/                | 200         | species_droid_payload.json       |
    | species/                  | 200         | species_payload.json             |
    | species/?search=Sullustan | 200         | species_search_name_payload.json |
    | species/?search=Jambroba  | 200         | not_found_search_payload.json    |
    | species/schema/           | 404         | species_schema.json              |
    | species/99/               | 404         | info_not_found_payload.json      |