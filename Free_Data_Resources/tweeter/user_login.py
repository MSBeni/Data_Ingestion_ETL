import constants
import oauth2
import urllib.parse as urlparse
import json
from user import User
from database import Database

# Initializing the DB
MY_PASS = json.loads(open('../../../secretfiles.json', 'r').read())['web']['user_pw']

Database.initialize(database='learning', user='i-sip_iot', password=MY_PASS, host='localhost')

# check if the user is subscribed in the DB or not
email = input("Please enter your valid email address: ")
user_check = User.load_from_db_by_email(email)

# pip install oauth2
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)
client = oauth2.Client(consumer)

if user_check:
    print(user_check)

# Use the client to perform a request for the request token
response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
if response.status != 200:
    print('There is a Problem with the Response Body ...')

# Get the request token parsing the query string returned
requested_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

# Ask the user to authorize our app and
print("Go to thw following site in your browser...")
print("{}?oauth_token={}".format(constants.AUTHORIZATION_URL, requested_token['oauth_token']))

oauth_verifier = input("What is the TOKEN? Please enter it here --> ")

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

print(access_token)



# create user

name = input("Please enter your name: ")
family_name = input("Please enter last name: ")
user_ = User(email, name, family_name, access_token['oauth_token'], access_token['oauth_token_secret'])
# 'muli@Uniofcode.me'

# create the user table and save the user information here
User.create_table()

# Adding the user information to the table
User.save_to_db(user_)

# fetch usersauth table data
User.fetch_data()

# Create an 'authorized_token' Token object and use that to perfoem Twitter API calls on behalf of the user
authorized_token = oauth2.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
authorized_client = oauth2.Client(consumer, authorized_token)

# Make Twitter API calls!
response, content = authorized_client.request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images'
                                              , 'GET')
if response.status != 200:
    print('An error occurred while searching in twitter ...')

tweets = json.loads(content.decode('utf-8'))

for tweet in tweets['statuses']:
    print(tweet['text'])


