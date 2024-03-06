@api
Feature: Testing People SWAPI endpoint

  API testing using python to validate the return of SWAPI API GET method

  @people_api
  Scenario Outline: Verify GET response from people SWAPI endpoint
    Given a SWAPI endpoint
    When I send a GET request to the SWAPI endpoint with "<endpoint>"
    Then I expect the response status code to be "<status_code>"
    And I expect the response body to match the "<expected_payload>"
  Examples:
    | endpoint              | status_code | expected_payload                |
    | people/1/             | 200         | people_luke_payload.json        |
    | people/               | 200         | people_payload.json             |
    | people/?search=luke   | 200         | people_search_name_payload.json |
    | people/?search=danilo | 200         | not_found_search_payload.json   |
    | people/schema/        | 404         | people_schema.json              |
    | people/99/            | 404         | info_not_found_payload.json     |