import json

secrets = json.loads(open('../../../tweeter_app_credential.json', 'r').read())

CONSUMER_KEY = secrets['auth']['api_key']
CONSUMER_SECRET = secrets['auth']['api_secret']

ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
