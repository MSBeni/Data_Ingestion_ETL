from functools import wraps
import json
from os import environ as env
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

app = Flask(__name__)

oauth = OAuth(app)

secrets = json.loads(open('../../../snapchat_mine.json', 'r').read())

auth0 = oauth.register(
    'auth0',
    client_id=secrets['auth']['Confidential_Client_ID'],
    client_secret=secrets['auth']['Confidential_Client_Secret'],
    api_base_url='https://accounts.snapchat.com/accounts/oauth2/auth',
    # access_token_url='https://YOUR_DOMAIN/oauth/token',
    # authorize_url='https://YOUR_DOMAIN/authorize',
    client_kwargs={
        'scope': 'https://auth.snapchat.com/oauth2/api/story-studio',
    },
)


# Here we're using the /callback route.
@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return redirect('/dashboard')


@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri='http://localhost:50000/snapchat_auth')


def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      # Redirect to Login page here
      return redirect('/')
    return f(*args, **kwargs)

  return decorated


if "__main__" == __name__:
    app.run(port=4495)
