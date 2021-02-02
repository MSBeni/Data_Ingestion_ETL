import constants
import oauth2
import urllib.parse as urlparse

# pip install oauth2
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)
client = oauth2.Client(consumer)

# Use the client to perform a request for the request token
response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
if response.status != 200:
    print('There is a Problem with the Response Body ...')

# Get the request token parsing the query string returned
requested_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

print("Go to thw following site in your browser...")
print("{}?oauth_token={}".format(constants.AUTHORIZATION_URL, requested_token['oauth_token']))

oauth_verifier = input("What is the TOKEN? ")

token = oauth2.Token(requested_token['oauth_token'], requested_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)

# More known client for twitter
client = oauth2.Client(consumer, token)
response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

print(access_token)

