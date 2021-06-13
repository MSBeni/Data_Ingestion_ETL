import json
from requests_oauthlib import OAuth2Session
import requests

scope = ['https://auth.snapchat.com/oauth2/api/story-studio'
         # 'snapchat-marketing-api'
         ]
authorize_url = 'https://accounts.snapchat.com/login/oauth2/authorize'
access_token_url = 'https://accounts.snapchat.com/login/oauth2/access_token'
protected_url = 'https://adsapi.snapchat.com/v1/me/organizations'


snap_credentials = json.loads(open('../../../snapchat_WM_App_2.json', 'r').read())


oauth = OAuth2Session(
    # snap_credentials['client_id'],
    snap_credentials['auth']['Confidential_Staging_Client_ID'],
    redirect_uri=snap_credentials['auth']['Redirect_URI'],
    scope=scope
)

authorization_url, state = oauth.authorization_url(authorize_url)
print('Please go to %s and authorize access.' % authorization_url)


authorization_response = input('Enter the full callback URL: ')

token = oauth.fetch_token(
    access_token_url,
    authorization_response=authorization_response,
    client_secret=snap_credentials['auth']['OAuth2_Staging_Client_Secret'],
    scope=scope
)

snap_credentials['access_token'] = oauth.token['access_token']
snap_credentials['refresh_token'] = oauth.token['refresh_token']

print(snap_credentials['refresh_token'])








