import sys
import os
import requests

__session : requests.Session = None
  
def session(token=None):
    global __session
    if token is not None or __session is None:
        token = os.environ['ESIOS_TOKEN'] if token is None else token
        if __session is not None:
            __session.close()
        __session = requests.Session()
        headers = {
        'Accept': 'application/json; application/vnd.esios-api-v1+json',
        'Content-Type': 'application/json',
        'Host': 'api.esios.ree.es',
        'Authorization' : f'Token token={token}'
        }
        __session.headers.update(headers)

    return __session


def indicator_list():

    response = session().get('https://api.esios.ree.es/indicators')
    return response.json()
