from flask import Flask, render_template, session, redirect, request, url_for, g
from Free_Data_Resources.tweeter.tweeter_utils import get_request_token, auth_twitter_url, get_access_token
from Free_Data_Resources.tweeter.user_app import UserApp
import json
from database import Database
import requests

app = Flask(__name__)
app.secret_key = '1234'


# Initializing the DB
MY_PASS = json.loads(open('../../../secretfiles.json', 'r').read())['web']['user_pw']
Database.initialize(database='learning', user='i-sip_iot', password=MY_PASS, host='localhost')


@app.before_request
def user_from_screen_name():
    if 'screen_name' in session:
        g.user = UserApp.load_from_db_by_screen_name(session['screen_name'])


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/login/twitter')
def twitter_login():
    request_token = get_request_token()
    if 'screen_name' in session:
        return redirect(url_for('profile'))
    # add the request_token to the cookie to keep it from being remove after terminating the request
    session['request_token'] = request_token

    return redirect(auth_twitter_url(session['request_token']))


@app.route('/logout')
def log_out():
    session.clear()
    return redirect(url_for('home_page'))


@app.route('/auth/twitter')
def auth_twitter():
    oauth_verifier = request.args.get('oauth_verifier')
    access_token = get_access_token(session['request_token'], oauth_verifier)
    UserApp.create_table()
    user = UserApp.load_from_db_by_screen_name(access_token['screen_name'])

    if not user:
        user = UserApp(access_token['screen_name'], access_token['oauth_token'], access_token['oauth_token_secret'],
                       None)
        user.save_to_db()

    session['screen_name'] = user.screen_name

    return redirect(url_for('profile'))
    # return redirect('http://127.0.0.1:4495/profile')


@app.route('/profile')
def profile():
    return render_template('profile.html', screen_name=g.user)


@app.route('/search')
def search():
    query = request.args.get('q')
    tweets = g.user.get_user_twitter_api_calls('https://api.twitter.com/1.1/search/tweets.json?q={}'.format(query))
    tweets_txt_lst = [{'tweet': tweet['text'], 'label': 'neutral'} for tweet in tweets['statuses']]
    for tweet in tweets_txt_lst:
        r = requests.post('http://text-processing.com/api/sentiment/', data={'text': tweet['tweet']})
        json_response = r.json()
        label = json_response['label']
        tweet['label'] = label

    return render_template('search.html', content=tweets_txt_lst)


if "__main__" == __name__:
    app.run(port=4495)

