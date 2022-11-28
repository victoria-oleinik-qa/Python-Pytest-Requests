import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/5')
    assert response.status_code == 200
def test_string():
    response = requests.get('https://petstore.swagger.io/v2/pet/11')
    assert response.json()['name'] == 'teroSr'