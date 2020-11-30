"""Query GitHub API"""

import requests


def creation_time(username):
    """
    Receive a username and return the creation time of a github account
    :param username: the github user username you want to seee the results
    :return: the request status and the creation time
    """
    url = 'https://api.github.com/users/' + username
    x = requests.get(url)
    return x.status_code, x.json()['created_at']


print(creation_time('MSBeni'))
