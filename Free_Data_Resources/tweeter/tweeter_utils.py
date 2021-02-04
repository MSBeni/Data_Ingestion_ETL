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