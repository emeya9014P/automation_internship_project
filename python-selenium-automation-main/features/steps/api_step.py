import requests
from behave import when, then

BASE_URL = "https://reqres.in"

@when('I send a GET request to "/api/users?page=2"')
def step_impl(context, endpoint):
    context.response = requests.get(BASE_URL + endpoint)


@when('I send a POST request to "/api/users" with name "Eme" and job "QA Automation Engineer"')
def step_impl(context, endpoint, name, job):
    payload = {"name": name, "job": job}
    context.response = requests.post(BASE_URL + endpoint, json=payload)


@when('I send a PUT request to "/api/users/2" with name "Eme" and job "Senior QA Automation Engineer"')
def step_impl(context, endpoint, name, job):
    payload = {"name": name, "job": job}
    context.response = requests.put(BASE_URL + endpoint, json=payload)


@when('I send a DELETE request to "/api/users/2"')
def step_impl(context, endpoint):
    context.response = requests.delete(BASE_URL + endpoint)


@then('The response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)


@then('The response body should contain "{key}" as {value:d}')
def step_impl(context, key, value):
    response_json = context.response.json()
    assert response_json.get(key) == value, \
        f"Expected {key} to be {value}, but got {response_json.get(key)}"


@then('The response body field "{key}" should be "{value}"')
def step_impl(context, key, value):
    response_json = context.response.json()
    assert response_json.get(key) == value, \
        f"Expected {key} to be {value}, but got {response_json.get(key)}"


@then('The response body should contain "{key1}" and "{key2}"')
def step_impl(context, key1, key2):
    response_json = context.response.json()
    assert key1 in response_json, f"Missing key in response: {key1}"
    assert key2 in response_json, f"Missing key in response: {key2}"
