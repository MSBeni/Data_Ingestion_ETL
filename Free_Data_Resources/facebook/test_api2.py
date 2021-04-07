import json
import facebook

secrets = json.loads(open('../../../facebook_app_credential.json', 'r').read())


def main():
    token = (secrets['auth']['access_token'])
    graph = facebook.GraphAPI(token)

    fields = ['email, gender']
    profile = graph.get_object('me', fields=fields)
    # profile = graph.get_object('me')


    print(json.dumps(profile, indent=4))


if __name__ == '__main__':
    main()


# import sys
# import json
# sys.path.append('/opt/homebrew/lib/python2.7/site-packages')
# sys.path.append('/opt/homebrew/lib/python2.7/site-packages/facebook_business-3.0.0-py2.7.egg-info')
#
# from facebook_business.api import FacebookAdsApi
# from facebook_business.adobjects.adaccount import AdAccount
#
# secrets = json.loads(open('../../../facebook_app_credential.json', 'r').read())
#
# # print(secrets['auth']['ad_account_id'])
#
# my_app_id = secrets['auth']['api_id']
# my_app_secret = secrets['auth']['api_secret']
# my_access_token = secrets['auth']['access_token']
# FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
# my_account = AdAccount(secrets['auth']['ad_account_id'])
# campaigns = my_account.get_campaigns()
# print(campaigns)

