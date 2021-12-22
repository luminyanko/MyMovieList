import pytest
import requests
import json
import logging
import subprocess
import sys

LOGGER = logging.getLogger(__name__)
URL = 'http://127.0.0.1:8000/'


def natural_numbers_generator():
    n = 0
    while True:
        n += 1
        yield n


natural_numbers = natural_numbers_generator()


@pytest.fixture
def token():
    url = URL + "api/login/"
    data = {'username': 'test@mail.com', 'password': 'password'}
    resp = requests.post(url, data=data)
    resp_json = json.loads(resp.text)
    return resp_json.get('token')


@pytest.mark.run(order=next(natural_numbers))
def test_registration():
    url = URL + "api/register/"
    data = {'username': 'test@mail.com', 'password': 'password'}
    resp = requests.post(url, data=data)
    resp_json = json.loads(resp.text)
    assert 'id' in resp_json
    assert resp.status_code == 201
    assert resp_json.get('username') == 'test@mail.com'


@pytest.mark.run(order=next(natural_numbers))
def test_failing_registration():
    url = URL + "api/register/"
    data = {'username': 'test@', 'password': '123'}
    resp = requests.post(url, data=data)
    resp_json = json.loads(resp.text)
    assert resp.status_code == 400
    assert resp_json.get('password') == [
        "Password must be at least 8 characters long, contain at least one digit"]


@pytest.mark.run(order=next(natural_numbers))
def test_login(token):
    assert token


@pytest.mark.run(order=next(natural_numbers))
def test_fail_login():
    url = URL + "api/login/"
    data = {'username': 'test@', 'password': '123'}
    resp = requests.post(url, data=data)
    resp_json = json.loads(resp.text)
    assert resp.status_code == 400
    assert resp_json.get('non_field_errors') == ["Unable to log in with provided credentials."]
