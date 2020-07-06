#!/bin/bash

PASSPORT="$(base64 passport.jpg)"
SELFIE="$(base64 selfie.jpg)"

payload=$(cat <<EOF
{
    "selfie_base64_encoded": "${SELFIE}",
    "document_front_base64_encoded": "${PASSPORT}",
    "eyn_ocr_token": "<EYN OCR TOKEN>"
}
EOF
)

echo ${payload}

echo ${payload} | 
curl --header "Content-Type:application/json" -d @- https://api.eyn.ninja/api/v1/prod/identitycheck 
