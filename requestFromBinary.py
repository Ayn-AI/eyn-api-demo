import requests
import os
import json
import base64

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "passport.jpg"), "rb") as file:
    blob = base64.encodebytes(file.read())
    file.close()
    blob = blob.decode("ascii")
    document_front_base64_encoded = blob.replace("\n", "")
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "selfie.jpg"), "rb") as file:
    blob = base64.encodebytes(file.read())
    file.close()
    blob = blob.decode("ascii")
    selfie_base64_encoded = blob.replace("\n", "")

data = {'document_front_base64_encoded': document_front_base64_encoded,
        'selfie_base64_encoded': selfie_base64_encoded,
        'eyn_ocr_token': '<EYN OCR TOKEN>'}
response = requests.post('https://api.eyn.ninja/api/v1/prod/identitycheck', json=data)
print(response.text)
