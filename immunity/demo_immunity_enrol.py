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
    'identity': {
        'first_name': 'ANGELA ZOE',
        'last_name': 'UK SPECIMEN',
        'selfie_base64_encoded': selfie_base64_encoded,
        'email_address': 'angela.zoe@gov.uk', # optional
        'phone_number': '00447700123456',     # optional
        'date_of_birth': '19881204'           # optional
    },
    'test': {
        'test_type': 'Molecular Swab Test',
        'test_result': 'Negative',
        'package_id': '1234567890987654'
    },
    'issuer': {
        'issuer_email': 'dev@eyn.vision',
        'issuer_location': 'RESERVED_KEY'
    }
}
response = requests.post('https://immunity.eyn.ninja/immunity_enrol', json=data)
print(response.text)
