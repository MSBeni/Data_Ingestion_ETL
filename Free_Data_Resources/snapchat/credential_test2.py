from requests_oauthlib import OAuth1Session

# Using OAuth1 auth helper
import requests
from requests_oauthlib import OAuth1
import json


secrets = json.loads(open('../../../snapchat_final_test_app.json', 'r').read())

# client_key = ''
# client_secret = ''
client_key = secrets['auth']['Confidential_Client_ID_auth']
# client_id = ''
client_secret = secrets['auth']['Confidential_Client_Secret_auth']

request_token_url = 'https://accounts.snapchat.com/accounts/oauth2/auth'


# Using OAuth1 auth helper
oauth = OAuth1(client_key, client_secret=client_secret, callback_uri='http://localhost:50000/')
r = requests.post(url=request_token_url, auth=oauth)
print(r.content)