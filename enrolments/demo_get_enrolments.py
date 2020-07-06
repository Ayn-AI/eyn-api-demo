# -*- coding: utf-8 -*-
#
# Demo Get Enrolments
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
import datetime

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


def get_enrolments(req_auth_headers, eyn_api_key):
    """ queries the EYN API's /enrolments endpoint to retrieve a list of
        enrolment ids

        params:
            req_auth_headers (dict): authentication headers containing
                                     authorisation token
            eyn_api_key (str): the api key from eyn

        returns:
            (dict): a list of enrolment ids
    """
    parameters = {'start_time': str((int(datetime.datetime.now().strftime('%s'))- 10000)*1000),
                  'end_time': str(int(datetime.datetime.now().strftime('%s'))*1000),
                  'eyn_api_key': eyn_api_key}
    response = requests.get('https://api.eyn.ninja/api/v1/prod/enrolments',
                            params=parameters, headers=req_auth_headers)
    body = json.loads(response.content)
    print(response.content)
    print(response.status_code)
    enrolment_ids = body["enrolment_ids"]
    return enrolment_ids


if __name__ == '__main__':
    print('[eyn-api-demo] Demo Get Enrolments')

    # TODO: Demo parameters - replace with your eyn credentials
    username = "demo@api.eyn.ninja"   # replace with your username
    password = "Def4ultP4ssw0rd!"   # replace with your password
    cognito_pool_id = "eu-west-2_ENTzGy2No"            # replace with your cognito pool id
    cognito_client_id = "3ogsvfd39d6r5jg9rcf7nv9lt6"          # replace with your cognito client id
    eyn_api_key = "api_key_dc0dce7e-52c8-4072-bc4a-743a335970c7"                # replace with your eyn api key
    
    # First, we have to authenticate to AWS Cognito
    tokens = do_authentication(username, password, cognito_pool_id, cognito_client_id)

    req_auth_headers = {'Accept': '*/*',
                        'Content-Type': 'application/json; charset=UTF-8',
                        'Authorization': tokens['AuthenticationResult']['IdToken']}

    # Now, we can query EYN API to get a list of enrolments
    enrolment_ids = get_enrolments(req_auth_headers, eyn_api_key)

    # Let's print the list of enrolments that we retrieved
    print('[eyn-api-demo] Results of querying /enrolments')
    for enrolment_id in enrolment_ids:
        print('enrolment_id :' + enrolment_id["enrolment_id"])

