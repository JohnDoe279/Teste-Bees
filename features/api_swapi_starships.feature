@api
Feature: Testing Starships SWAPI endpoint

  API testing using python to validate the return of SWAPI API GET method

  @starships_api
  Scenario Outline: Verify GET response from Starships SWAPI endpoint
    Given a SWAPI endpoint
    When I send a GET request to the SWAPI endpoint with "<endpoint>"
    Then I expect the response status code to be "<status_code>"
    And I expect the response body to match the "<expected_payload>"
  Examples:
    | endpoint                                            | status_code | expected_payload                    |
    | starships/9/                                        | 200         | starships_deathstar_payload.json    |
    | starships/                                          | 200         | starships_payload.json              |
    | starships/?search=X-wing                            | 200         | starships_search_name_payload.json  |
    | starships/?search=DS-1%20Orbital%20Battle%20Station | 200         | starships_search_model_payload.json |
    | starships/?search=Sovereign                         | 200         | not_found_search_payload.json       |
    | starships/schema/                                   | 404         | starships_schema.json               |
    | starships/99/                                       | 404         | info_not_found_payload.json         |