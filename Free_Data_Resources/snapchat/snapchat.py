import json
import pytz
from datetime import datetime, timedelta, timezone
import requests
import pandas as pd
import argparse

snap_credentials = json.loads(open('../../../snapchat_WM_App_2.json', 'r').read())
SNAP_CREDENTIALS = {
    "client_id": snap_credentials['auth']['Confidential_Staging_Client_ID'],
    "client_secret": snap_credentials['auth']['OAuth2_Staging_Client_Secret'],
    "refresh_token": snap_credentials['auth']['refresh_token']
}

def day_diff_strptime(start, end):
    """Calculate the number of days between two dates."""
    s = datetime.strptime(start, '%Y-%m-%d')
    e = datetime.strptime(end, '%Y-%m-%d')
    return (e - s).days


def get_snapchat_access_token(snap_credentials):
    """Retrieve snapchat access token using credentials."""
    # Initialize
    access_url = 'https://accounts.snapchat.com/login/oauth2/access_token'
    access_params = {
        'client_id': snap_credentials['client_id'],
        'client_secret': snap_credentials['client_secret'],
        'code': snap_credentials['refresh_token'],
        'grant_type': 'refresh_token',
    }

    # Get
    res = requests.post(
        access_url,
        params=access_params
    )

    return res.json()['access_token']

###########################################
def get_all_publishers(access_token):
    publishers_url = 'https://api.snapkit.com/v1/stories/studio/publishers'
    headers = {'Authorization': 'Bearer %s' % (access_token)}
    # Get
    res = requests.get(
        publishers_url,
        headers=headers
    )

    return res

#################################################

def main(snap_credentials, start_date, end_date):
    # Initialize
    snap = pd.DataFrame()

    # Get access token from refresh token
    access_token = get_snapchat_access_token(snap_credentials)
    print('Access Token is: {}'.format(access_token))

    # Get all publishers
    publishers = get_all_publishers(access_token)
    return publishers



if __name__ == '__main__':
    # Parsing args
    # Use python snapchat.py -start YYYY-mm-dd  -end YYYY-mm-dd
    parser = argparse.ArgumentParser()
    parser.add_argument('-start', action='store', dest='start', type=str,
                        help='Start date of the report in the following format: YYYY-mm-dd')
    parser.add_argument('-end', action='store', dest='end', type=str,
                        help='End date of the report in the following format: YYYY-mm-dd')
    args = parser.parse_args()

    # Check that time period is not too large
    if day_diff_strptime(args.start, args.end) >= 30:
        raise Exception('The difference between start and end date must be less than 31 days')

    # Retrieve snapchat data
    snap = main(SNAP_CREDENTIALS, args.start, args.end)

    print(snap)

