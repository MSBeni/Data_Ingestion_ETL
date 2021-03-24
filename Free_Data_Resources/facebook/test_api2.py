import sys
import json
sys.path.append('/opt/homebrew/lib/python2.7/site-packages')
sys.path.append('/opt/homebrew/lib/python2.7/site-packages/facebook_business-3.0.0-py2.7.egg-info')

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

secrets = json.loads(open('../../../facebook_app_credential.json', 'r').read())


my_app_id = secrets['auth']['api_id']
my_app_secret = secrets['auth']['api_secret']
my_access_token = secrets['auth']['access_token']
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount(secrets['auth']['ad_account_id'])
campaigns = my_account.get_campaigns()
print(campaigns)


#
# from facebookads.api import FacebookAdsApi
# from facebookads import adobjects
#
# secrets = json.loads(open('../../../facebook_app_credential.json', 'r').read())
# my_app_id = secrets['auth']['api_id']
# my_app_secret = secrets['auth']['api_secret']
# my_access_token = secrets['auth']['access_token']
# ad_account_id = secrets['auth']['ad_account_id']
# proxies = {'http': '<HTTP_PROXY>', 'https': '<HTTPS_PROXY>'} # add proxies if needed
# FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, proxies)