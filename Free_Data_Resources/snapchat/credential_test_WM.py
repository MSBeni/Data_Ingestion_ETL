import json

secrets = json.loads(open('../../../snapchat_Test_App_new.json', 'r').read())

# print(secrets['auth']['Confidential_Client_Secret'])


# client_id = secrets['auth']['Confidential_Client_ID_auth']
# client_id = secrets['auth']['Confidential_Client_ID']
# client_secret = secrets['auth']['Confidential_Client_Secret_auth']
# client_secret = secrets['auth']['Confidential_Client_Secret']
########################## Test App 1 #########################################
# client_id = secrets['auth']['Snap_Kit_App_ID']    # Error: Invalid Client
# client_secret = secrets['auth']['Confidential_Production_Client_Secret']
#############################################################################
########################## Test App 2 #########################################
# client_id = secrets['auth']['Snap_Kit_App_ID']      # Error: Invalid Client
# client_secret = secrets['auth']['OAuth2_Staging_Client_Secret']
#############################################################################
########################## Test App 3 #########################################
# client_id = secrets['auth']['OAuth2_Staging_Client_ID']    # Error: Invalid redirect_uri.
# client_secret = secrets['auth']['OAuth2_Staging_Client_Secret']
#############################################################################
########################## Test App 4 #########################################
client_id = secrets['auth']['Confidential_Staging_Client_ID']   # Error: Invalid redirect_uri.
client_secret = secrets['auth']['OAuth2_Staging_Client_Secret']
#############################################################################
########################## Test App 5 #########################################
# client_id = secrets['auth']['OAuth2_Production_Client_ID']   # Error: Invalid redirect_uri.
# client_secret = secrets['auth']['Confidential_Production_Client_Secret']
#############################################################################
########################## Test App 6 #########################################
# client_id = secrets['auth']['Confidential_Production_Client_ID']    # Error: Invalid redirect_uri.
# client_secret = secrets['auth']['Confidential_Production_Client_Secret']
#############################################################################
########################## Test App #########################################
# client_id = secrets['auth']['OAuth2_Staging_Client_ID']   # Error: Invalid redirect_uri.
# client_secret = secrets['auth']['Confidential_Staging_Client_ID']
#############################################################################
redirect_uri = 'https://localhost:50000/aftereffectsauth'

from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session


# Note that these are Google specific scopes
scope = ['https://auth.snapchat.com/oauth2/api/story-studio'
         # 'snapchat-marketing-api'
         ]
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
authorization_url, state = oauth.authorization_url(
        'https://accounts.snapchat.com/accounts/oauth2/auth',
        # 'https://accounts.snapchat.com/login/oauth2/authorize',
        # access_type and prompt are Google specific extra
        # parameters.
        # access_type="offline", prompt="select_account"
        # response_type="code"
        )

print('Please go to %s and authorize access.' % authorization_url)
# authorization_response = raw_input('Enter the full callback URL')

