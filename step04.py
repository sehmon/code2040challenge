import config
import requests

initial_endpoint = 'http://challenge.code2040.org/api/prefix'
validation_endpoint = 'http://challenge.code2040.org/api/prefix/validate'

initial_data = {
    'token': config.token
    }

initial_response = requests.post(initial_endpoint, data=initial_data)

json_response =  initial_response.json()
prefix = json_response['prefix']
# Filter the array and leave words that don't start with the given prefix
array = [word for word in json_response['array'] if not word.startswith(prefix)]

validation_data = {
    'token': config.token,
    'array': array
    }

validation_response = requests.post(validation_endpoint, json=validation_data)
print validation_response.text
