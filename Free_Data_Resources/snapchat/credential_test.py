import json

secrets = json.loads(open('../../../snapchat_snap_ads.json', 'r').read())

# print(secrets['auth']['Confidential_Client_Secret'])


# client_id = secrets['auth']['Confidential_Client_ID_auth']
client_id = secrets['auth']['Confidential_Client_ID']
# client_id = '135459c5-275f-4567-b16f-ef2b79a4bd1e'
# client_secret = secrets['auth']['Confidential_Client_Secret_auth']
client_secret = secrets['auth']['Confidential_Client_Secret']
redirect_uri = 'http://localhost:3000/auth/snapchat/callback'

from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session


# Note that these are Google specific scopes
scope = ['https://auth.snapchat.com/oauth2/api/story-studio'
         # 'snapchat-marketing-api'
         ]
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
authorization_url, state = oauth.authorization_url(
        'https://accounts.snapchat.com/accounts/oauth2/auth',
        # 'https://accounts.snapchat.com/login/oauth2/authorize',
        # access_type and prompt are Google specific extra
        # parameters.
        # access_type="offline", prompt="select_account"
        # response_type="code"
        )

print('Please go to %s and authorize access.' % authorization_url)
# authorization_response = raw_input('Enter the full callback URL')


