import config
import requests
from dateutil import parser
from datetime import datetime, timedelta

initial_endpoint = 'http://challenge.code2040.org/api/dating'
validation_endpoint = 'http://challenge.code2040.org/api/dating/validate'

initial_data = {
    'token': config.token
    }

initial_response = requests.post(initial_endpoint, data=initial_data)
json_response = initial_response.json()


date = parser.parse(json_response['datestamp'])
delta = timedelta(seconds=json_response['interval'])
new_date = date+delta

# Python datetime is a bit clunky and requres some manual parsing for the 
# correct formatting
formatted_date = new_date.isoformat()
formatted_date = formatted_date[:-6]
formatted_date += 'Z'

print json_response
print formatted_date

validation_data = {
    'token': config.token,
    'datestamp': formatted_date
    }

validation_response = requests.post(validation_endpoint, data=validation_data)
print validation_response.text
