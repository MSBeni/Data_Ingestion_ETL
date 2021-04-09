import json

secrets = json.loads(open('../../../snapchat_mine.json', 'r').read())

CONSUMER_KEY = secrets['auth']['Confidential_Client_ID']

CONSUMER_SECRET = secrets['auth']['Confidential_Client_Secret']

# ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
REQUEST_TOKEN_URL = 'https://accounts.snapchat.com/accounts/oauth2/auth'
# AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
