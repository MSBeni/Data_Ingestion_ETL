import constants
import oauth2
import urllib.parse as urlparse

# pip install oauth2
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)
client = oauth2.Client(consumer)

response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
if response.status != 200:
    print('There is a Problem with the Response Body ...')

requested_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

print("Go to thw following site in your browser...")
print("{}?oauth_token={}".format(constants.AUTHORIZATION_URL, requested_token['oauth_token']))
