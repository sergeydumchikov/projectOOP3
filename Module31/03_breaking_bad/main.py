import requests
import json

my_request = requests.get('https://breakingbadapi.com/api/deaths/')
data = json.loads(my_request.text)

maxi = 0
result = {}
for i_dir in data:
    if i_dir['number_of_deaths']:
        if i_dir['number_of_deaths'] > maxi:
            maxi = i_dir['number_of_deaths']
            result = i_dir

with open('test.join', 'w') as file:
    json.dump(result, file, indent=2)

