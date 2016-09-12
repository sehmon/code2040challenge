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
array = [word for word in json_response['array'] if not word.startswith(prefix)]


validation_data = {
    'token': config.token,
    'array': array 
    }

# Cross validating the answer below shows that 'array' contains all the words
# that don't begin with the prefix. Server still doesn't accecpt answer as
# correct
print json_response['array']
print prefix
print validation_data

validation_response = requests.post(validation_endpoint, data=validation_data)
print validation_response.text
