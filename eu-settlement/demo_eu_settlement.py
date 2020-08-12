import requests

data = {
    'api_secret': '9b7539bc-5f62-420d-ba4d-2241ade8f4b6',
    'share_code': 'JP7LFW2FP',
    'date_of_birth': '04/12/1988',
    'company_name': 'EYN',
}
response = requests.post('https://api.eyn.ninja/api/v1/prod/eu-settlement', json=data)
print(response.text)
