# -*- coding: utf-8 -*-
#
# Demo Get Specific Enrolment Info
#   Author: robin@eyn.vision
#   web:    https://eyn.vision
#
#   Requirements:
#       * warrant-lite (pip install warrant-lite)
#
# Eyn API is available at https://api.eyn.ninja. Documentation of the API is
# available at https://ayn-ai.github.io/eyn-api-doc/.
# (c) 2019 eyn ltd

from warrant_lite import WarrantLite
import requests
import json

def do_authentication(username, password, cognito_pool_id, cognito_client_id):
    """ authenticates to AWS Cognito via eyn's credentials and returns
        authentication tokens

        params:
            username (str): username to authenticate (supplied by EYN)
            password (str): password to authenticate (supplied by EYN)
            cognito_pool_id (str): AWS cognito user pool id
            cognito_client_id (str): AWS cognito app client id

        returns:
            (dict): authentication tokens
    """
    wl = WarrantLite(username=username, password=password,
                     pool_id=cognito_pool_id, client_id=cognito_client_id,
                     client_secret=None, pool_region="eu-west-2")
    tokens = wl.authenticate_user()
    return tokens

def get_specific_enrolment_info(req_auth_headers, enrolment_id, eyn_api_key):
    """ queries the EYN API's /enrolments/{id} endpoint to retrieve specific
        information about an enrolment with id = {id}

        params:
            req_auth_headers (dict): authentication headers containing
                                     autorisation token
            enrolment_id (str): id of the specific enrolment we want to extract
                                information from
            eyn_api_key (str): the api key from eyn

        returns:
            (dict): specific enrolment information
    """
    parameters = {'eyn_api_key': eyn_api_key}
    response = requests.get('https://api.eyn.ninja/api/v1/prod/enrolments/' + enrolment_id,
                            params=parameters, headers=req_auth_headers)

    enrolment_info = json.loads(response.content)
    return enrolment_info

if __name__ == '__main__':
    print('[eyn-api-demo] Demo Get Specific Enrolment Info.')

    # TODO: Demo parameters - replace with your eyn credentials
    username = "demo@eyn-api.com"   # replace with your username
    password = "Def4ultP4ssw0rd!"   # replace with your password
    cognito_pool_id = ""            # replace with your cognito pool id
    cognito_client_id = ""          # replace with your cognito client id
    eyn_api_key = ""                # replace with your eyn api key
    
    # First, we have to authenticate to AWS Cognito
    tokens = do_authentication(username, password, cognito_pool_id, cognito_client_id)
    
    req_auth_headers = {'Accept': '*/*',
                        'Content-Type': 'application/json; charset=UTF-8',
                        'Authorization': tokens['AuthenticationResult']['IdToken']}

    # Now, we can query EYN API to get specific information about an enrolment
    enrolment_info = get_specific_enrolment_info(req_auth_headers, 'a987259c-bbbb-4b26-926e-b3e6ab64620d', eyn_api_key)

    # Let's print the information that we retrieved
    print('[eyn-api-demo] Results of querying /enrolments/a987259c-bbbb-4b26-926e-b3e6ab64620d:')
    print('other_names: ' + enrolment_info["other_names"])
    print('family_name: ' + enrolment_info["family_name"])
    print('date_of_birth: ' + enrolment_info["date_of_birth"])
    print('nationality: ' + enrolment_info["nationality"])
    print('document_type: ' + enrolment_info["document_type"])
    print('document_expiry_date: ' + enrolment_info["document_expiry_date"])
    if "images" in enrolment_info:
        if "link_identity_document_chip_face" in enrolment_info["images"]:
            print('link_identity_document_chip_face: ' + str(enrolment_info["images"]["link_identity_document_chip_face"]))
        if "link_identity_document_image_front" in enrolment_info["images"]:
            print('link_identity_document_image_front: ' + str(enrolment_info["images"]["link_identity_document_image_front"]))
        if "link_identity_document_image_mrz" in enrolment_info["images"]:
            print('link_identity_document_image_mrz: ' + str(enrolment_info["images"]["link_identity_document_image_mrz"]))
        if "link_user_selfie" in enrolment_info["images"]:
            print('link_user_selfie: ' + str(enrolment_info["images"]["link_user_selfie"]))
    print('right_to_work_status: ' + str(enrolment_info["right_to_work_status"]))
    if "biometric_checks" in enrolment_info:
        if "face_matching_score" in enrolment_info["biometric_checks"]:
            print('face_matching_score: ' + str(enrolment_info["biometric_checks"]["face_matching_score"]))
        if "face_matching_status" in enrolment_info["biometric_checks"]:
            print('face_matching_status: ' + str(enrolment_info["biometric_checks"]["face_matching_status"]))
        if "model_used" in enrolment_info["biometric_checks"]:
            print('model_used: ' + str(enrolment_info["biometric_checks"]["model_used"]))
    if "document_checks" in enrolment_info:
        if "mrz_check" in enrolment_info["document_checks"]:
            print('mrz_check: ' + str(enrolment_info["document_checks"]["mrz_check"]))
        if "chip_check" in enrolment_info["document_checks"]:
            print('chip_check: ' + str(enrolment_info["document_checks"]["chip_check"]))
    print('checked_by: ' + enrolment_info["checked_by"])
    if "checked_at" in enrolment_info:
        if "site_id" in enrolment_info["checked_at"]:
            print('site_id: ' + str(enrolment_info["checked_at"]["site_id"]))
        if "site_name" in enrolment_info["checked_at"]:
            print('site_name: ' + str(enrolment_info["checked_at"]["site_name"]))
