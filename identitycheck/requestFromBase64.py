import requests
import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "passport_base64.txt"), "r") as file:
    document_front_base64_encoded = file.read()
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "selfie_base64.txt"), "r") as file:
    selfie_base64_encoded = file.read()

data = {'document_front_base64_encoded': document_front_base64_encoded,
        'selfie_base64_encoded': selfie_base64_encoded,
        'eyn_ocr_token': '<EYN OCR TOKEN>'}
response = requests.post('https://api.eyn.ninja/api/v1/prod/identitycheck', json=data)
print(response.text)
