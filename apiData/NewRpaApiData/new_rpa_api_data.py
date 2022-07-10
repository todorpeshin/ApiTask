

__author__ = 'TodorPeshin'

import requests


class Rpa_api:
    def __init__(self, **options):

        self._rpa_fqdn = "vmc-07-07-46-06.kryonaws.com"
        self._access_token = ""
        self._rpa_url = ""
        self._user = "dev"
        self._password = "OneRedRosse!_?"



    #seeter and getters
    def set_access_token(self, access_token):
        self._access_token = access_token

    def get_access_token(self):
        return self._access_token

    def set_rpa_fqdn(self, rpa_fqdn):
        self._rpa_fqdn = rpa_fqdn

    def get_rpa_fqdn(self):
        return self._rpa_fqdn




    #functions

    def acces_token(self, fqdn):
        body = {'grant_type': 'password',
                'client_id': 'kryon-console',
                'username': 'dev',
                'password': 'OneRedRosse!_?'}

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.post(('http://{}/auth/realms/kryon/protocol/openid-connect/token'.format(fqdn)),
                                 data=body, headers=headers)

        token = response.json().get('access_token')
        return token

    def get_triggers(self, token, fqdn):
        query = """
        query {
      triggers(queryInput:{
          sort: [],
          filter: {},
          take: 25,
          skip: 0
          }) {
            items {
                id
                name
                type
                creationUser
                tenantId
                active
                priority
                running
                queueId
                queueName
                scriptId
                scriptName
                metadata
            }
            totalRecords
          }
        }
        """

        headers = {
            'kryon-auth-provider': 'aerobase',
            'kryon-client-id': 'kryon-public-api',
            'Authorization': ('Bearer {}'.format(token))
        }

        response = requests.post(('http://{}/public-api/graphql').format(fqdn), {'query': query}, headers=headers)
        return response








