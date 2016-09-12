import config
import requests

initial_endpoint = 'http://challenge.code2040.org/api/register'

data = {
    'token': config.token,
    'github': config.github
    }

initial_response = requests.post(initial_endpoint, data=data)
print initial_response.text
