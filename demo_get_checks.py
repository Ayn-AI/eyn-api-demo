# -*- coding: utf-8 -*-
#
# Demo Get Checks
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


def get_checks(req_auth_headers, api_key):
    """ queries the EYN API's /checks endpoint to retrieve a list of
        check ids

        params:
            req_auth_headers (dict): authentication headers containing
                                     authorisation token
            api_key (str): the api key from eyn

        returns:
            (dict): a list of enrolment ids
    """
    parameters = {'start_time': 0,
                  'end_time': str(int(datetime.datetime.now().strftime('%s'))*1000),
                  'api_key': api_key}
    response = requests.get('https://api.eyn.ninja/api/v1/prod/checks',
                            params=parameters, headers=req_auth_headers)
    body = json.loads(response.content)
    check_ids = body["check_ids"]
    return check_ids


if __name__ == '__main__':
    print('[eyn-api-demo] Demo Get Checks')

    # TODO: Demo parameters - replace with your eyn credentials
    username = "demo@api.eyn.ninja" # replace with your username
    password = "Def4ultP4ssw0rd!"   # replace with your password
    cognito_pool_id = ""            # replace with your cognito pool id
    cognito_client_id = ""          # replace with your cognito client id
    api_key = ""                    # replace with your api key
    
    # First, we have to authenticate to AWS Cognito
    tokens = do_authentication(username, password, cognito_pool_id, cognito_client_id)

    req_auth_headers = {'Accept': '*/*',
                        'Content-Type': 'application/json; charset=UTF-8',
                        'Authorization': tokens['AuthenticationResult']['IdToken']}

    # Now, we can query EYN API to get a list of enrolments
    check_ids = get_checks(req_auth_headers, api_key)

    # Let's print the list of checks that we retrieved
    print('[eyn-api-demo] Results of querying /checks')
    for check_id in check_ids:
        print('check_id :' + check_id["check_id"])

