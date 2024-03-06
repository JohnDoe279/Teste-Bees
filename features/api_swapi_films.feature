@api
Feature: Testing Film SWAPI endpoint

  API testing using python to validate the return of SWAPI API GET method

  @films_api
  Scenario Outline: Verify GET response from Film SWAPI endpoint
    Given a SWAPI endpoint
    When I send a GET request to the SWAPI endpoint with "<endpoint>"
    Then I expect the response status code to be "<status_code>"
    And I expect the response body to match the "<expected_payload>"
  Examples:
    | endpoint             | status_code | expected_payload                |
    | films/1/             | 200         | films_new_hope_payload.json     |
    | films/               | 200         | films_payload.json              |
    | films/?search=Empire | 200         | films_search_title_payload.json |
    | films/?search=Senate | 200         | not_found_search_payload.json   |
    | films/schema/        | 404         | films_schema.json               |
    | films/99/            | 404         | info_not_found_payload.json     |