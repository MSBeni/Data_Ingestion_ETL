import oauth2
import constants
import urllib.parse as urlparse

consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)


def get_request_token():
    client = oauth2.Client(consumer)
    # Use the client to perform a request for the request token
    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
    if response.status != 200:
        print('There is a Problem with the Response Body ...')

    # Get the request token parsing the query string returned
    # requested_token
    return dict(urlparse.parse_qsl(content.decode('utf-8')))


def get_oauth_verifier(requested_token):
    # Ask the user to authorize our app and
    print("Go to thw following site in your browser...")
    print("{}?oauth_token={}".format(constants.AUTHORIZATION_URL, requested_token['oauth_token']))

    # oauth_verifier
    return input("What is the TOKEN? Please enter it here --> ")


def get_access_token(requested_token, oauth_verifier):
    # Create the Token object which contains the request token and the verifier
    token = oauth2.Token(requested_token['oauth_token'], requested_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)

    # Create a client with our consumer (our app) and newly created (and verified) token
    client = oauth2.Client(consumer, token)

    # Ask Twitter for an access token, and Twitter knows it should give us it since we've verified the request token
    response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
    if response.status != 200:
        print('A problem faced during the access token process ...')
    access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

    return access_token


