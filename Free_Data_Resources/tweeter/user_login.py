import json
from user import User
from database import Database
from Free_Data_Resources.tweeter.tweeter_utils import get_request_token, get_oauth_verifier, get_access_token

# Initializing the DB
MY_PASS = json.loads(open('../../../secretfiles.json', 'r').read())['web']['user_pw']

Database.initialize(database='learning', user='i-sip_iot', password=MY_PASS, host='localhost')

# check if the user is subscribed in the DB or not
email = input("Please enter your valid email address: ")
# user_check = User.load_from_db_by_email(email)
user_ = User.load_from_db_by_email(email)

if not user_:
    # Get the request token parsing the query string returned
    requested_token = get_request_token()

    # Ask the user to authorize our app and get token
    oauth_verifier = get_oauth_verifier(requested_token)

    # Ask Twitter for an access token
    access_token = get_access_token(requested_token, oauth_verifier)

    # create user
    name = input("Please enter your name: ")
    family_name = input("Please enter last name: ")
    user_ = User(email, name, family_name, access_token['oauth_token'], access_token['oauth_token_secret'])

    # create the user table and save the user information here
    User.create_table()

    # Adding the user information to the table
    User.save_to_db(user_)

    # fetch data from table
    User.fetch_data()


tweets = user_.get_user_twitter_api_calls('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images')

for tweet in tweets['statuses']:
    print(tweet['text'])


