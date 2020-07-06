import requests
import os
import json
import base64

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "selfie.jpg"), "rb") as file:
    blob = base64.encodebytes(file.read())
    file.close()
    blob = blob.decode("ascii")
    selfie_base64_encoded = blob.replace("\n", "")

data = {
    'api_secret': 'e1131458-4664-4da7-855a-7ac3e5b9648d',
    'first_name': 'ANGELA ZOE',
    'last_name': 'UK SPECIMEN',
    'issue_date': '1592310965',
    'expiry_date': '1592310966',
    'selfie': selfie_base64_encoded,
    'test': {
        'test_type': 'Molecular Swab Test',
        'test_result': 'Negative',
        'issuer_email': 'robin@eyn.vision',
        'issuer_location': 'Test Site'
}}
response = requests.post('https://api.eyn.ninja/api/v1/prod/immunity_enrol', json=data)
print(response.text)
