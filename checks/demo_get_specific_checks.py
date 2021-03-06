# -*- coding: utf-8 -*-
#
# Demo Get Specific Check Info
#   Author: robin@eyn.vision
#   web:    https://eyn.vision
#
#   Requirements:
#       * warrant-lite (pip install warrant-lite)
#
# Eyn API is available at https://api.eyn.ninja. Documentation of the API is
# available at https://ayn-ai.github.io/eyn-api-doc/.
# (c) 2020 EYN Ltd

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

def get_specific_check_info(req_auth_headers, check_id, api_key):
    """ queries the EYN API's /checks/{id} endpoint to retrieve specific
        information about a check with id = {id}

        params:
            req_auth_headers (dict): authentication headers containing
                                     autorisation token
            check_id (str): id of the specific check we want to extract
                                information from
            api_key (str): the api key from eyn

        returns:
            (dict): specific check information
    """
    parameters = {'api_key': api_key}
    response = requests.get('https://api.eyn.ninja/api/v1/prod/checks/' + check_id,
                            params=parameters, headers=req_auth_headers)
    check_info = json.loads(response.content)
    return check_info

if __name__ == '__main__':
    print('[eyn-api-demo] Demo Get Specific Check Info.')

    # TODO: Demo parameters - replace with your eyn credentials
    username = "demo@api.eyn.ninja" # replace with your username
    password = "Def4ultP4ssw0rd!"   # replace with your password
    cognito_pool_id = "eu-west-2_ENTzGy2No"            # replace with your cognito pool id
    cognito_client_id = "3ogsvfd39d6r5jg9rcf7nv9lt6"          # replace with your cognito client id
    api_key = "api_key_dc0dce7e-52c8-4072-bc4a-743a335970c7"                    # replace with your api key
    check_id = "d1088995-6b98-4a40-bb07-77d27f3f1c68"                   # replace with a valid check_id (eg. retrieved via /checks)
    
    # First, we have to authenticate to AWS Cognito
    tokens = do_authentication(username, password, cognito_pool_id, cognito_client_id)
    
    req_auth_headers = {'Accept': '*/*',
                        'Content-Type': 'application/json; charset=UTF-8',
                        'Authorization': tokens['AuthenticationResult']['IdToken']}

    # Now, we can query EYN API to get specific information about a check
    check_info = get_specific_check_info(req_auth_headers, check_id, api_key)

    # Let's print the information that we retrieved
    print('[eyn-api-demo] Results of querying /checks/{id}:')
    print('other_names: ' + check_info["other_names"])
    print('family_name: ' + check_info["family_name"])
    print('date_of_birth: ' + check_info["date_of_birth"])
    print('check_state: ' + check_info["check_state"])
    print('time_stamp: ' + str(check_info["time_stamp"]))
    print('duration: ' + str(check_info["duration"]))
    print('user_confirmed: ' + str(check_info["user_confirmed"]))
    print('site_id: ' + check_info["site_id"])
    print('enrolment_id: ' + check_info["enrolment_id"])
