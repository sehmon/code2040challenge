import config
import requests

initial_endpoint = 'http://challenge.code2040.org/api/reverse'
validation_endpoint = 'http://challenge.code2040.org/api/reverse/validate'

initial_data = {
    'token': config.token
    }

initial_response = requests.post(initial_endpoint, data=initial_data)

validation_data = {
    'token': config.token,
    # Iterate through the string and go backwards (-1)
    'string': initial_response.text[::-1]
    }

validation_response = requests.post(validation_endpoint, data=validation_data)
print validation_response.text
