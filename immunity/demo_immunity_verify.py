import requests
import os
import json
import base64

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "certificate.jpeg"), "rb") as file:
    blob = base64.encodebytes(file.read())
    file.close()
    blob = blob.decode("ascii")
    certificate_base64_encoded = blob.replace("\n", "")

data = {
    'api_secret': '676bc3ca-e2b9-4161-85a4-1dc8592916a5',
    'certificate': certificate_base64_encoded,
}
response = requests.post('https://immunity.eyn.ninja/immunity_verify', json=data)
print(response.text)
