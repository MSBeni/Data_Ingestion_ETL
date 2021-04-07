import requests
import json

secrets = json.loads(open('../../../facebook_app_credential.json', 'r').read())
token = secrets['auth']['access_token']


me = 'https://graph.facebook.com/v10.0/Bituniex?access_token='+token
friends = 'https://graph.facebook.com/v10.0/Bituniex/friends?access_token='+token

me1 = requests.get(friends)

print(me1.text)
