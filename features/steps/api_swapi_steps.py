import json
from behave import *
from Utilities.api_Utils import API_Utils

api_utils = API_Utils()


@given('a SWAPI endpoint')
def step_given_swapi_endpoint(context):
    context.api_url = api_utils.get_api()


@when('I send a GET request to the SWAPI endpoint with "{endpoint}"')
def step_when_send_get_request(context, endpoint):
    global response
    response = api_utils.get_request(endpoint)


@then('I expect the response status code to be "{status_code}"')
def step_then_expect_status_code(context, status_code):
    actual_status = response.status_code
    assert actual_status == int(status_code)


@then('I expect the response body to match the "{expected_payload}"')
def step_then_expect_payload(context, expected_payload):
    response_payload = response.json()
    with open('resources/' + expected_payload, 'r') as files:
        expected_payload_data = json.load(files)
    assert response_payload == expected_payload_data
