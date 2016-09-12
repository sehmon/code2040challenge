import config
import requests

initial_endpoint = 'http://challenge.code2040.org/api/haystack'
validation_endpoint = 'http://challenge.code2040.org/api/haystack/validate'

initial_data = {
    'token': config.token
    }

initial_response = requests.post(initial_endpoint, data=initial_data)

json_response =  initial_response.json()
needle = json_response['needle']
needle_index = None

for index, word in enumerate(json_response['haystack']):
  if needle == word:
    needle_index = index
    break;

validation_data = {
    'token': config.token,
    'needle': needle_index
    }

validation_response = requests.post(validation_endpoint, data=validation_data)
print validation_response.text
