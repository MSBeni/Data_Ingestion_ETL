# Using OAuth1Session
from requests_oauthlib import OAuth1Session

# Using OAuth1 auth helper
import requests
from requests_oauthlib import OAuth1

client_key = ''
client_secret = ''

request_token_url = 'https://accounts.snapchat.com/accounts/oauth2/auth'


# Using OAuth1 auth helper
oauth = OAuth1(client_key, client_secret=client_secret, callback_uri='http://localhost:8000')
r = requests.post(url=request_token_url, auth=oauth)
print(r.content)
