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
    username = "demo@eyn-api.com"   # replace with your username
    password = "Def4ultP4ssw0rd!"   # replace with your password
    cognito_pool_id = ""            # replace with your cognito pool id
    cognito_client_id = ""          # replace with your cognito client id
    api_key = ""                    # replace with your api key
    
    # First, we have to authenticate to AWS Cognito
    tokens = do_authentication(username, password, cognito_pool_id, cognito_client_id)
    
    req_auth_headers = {'Accept': '*/*',
                        'Content-Type': 'application/json; charset=UTF-8',
                        'Authorization': tokens['AuthenticationResult']['IdToken']}

    # Now, we can query EYN API to get specific information about a check
    check_info = get_specific_check_info(req_auth_headers, '<REPLACE WITH YOUR ID>', api_key)

    # Let's print the information that we retrieved
    print('[eyn-api-demo] Results of querying /checks/{id}:')
    print('other_names: ' + check_info["other_names"])
    print('family_name: ' + check_info["family_name"])
    print('date_of_birth: ' + check_info["date_of_birth"])
    print('check_state: ' + check_info["check_state"])
    print('time_stamp: ' + check_info["time_stamp"])
    print('duration: ' + check_info["duration"])
    print('user_confirmed: ' + check_info["user_confirmed"])
    print('site_id: ' + check_info["site_id"])
    print('enrolment_id: ' + check_info["enrolment_id"])
