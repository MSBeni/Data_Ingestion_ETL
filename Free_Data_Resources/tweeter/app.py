from flask import Flask, render_template, session, redirect
from Free_Data_Resources.tweeter.tweeter_utils import get_request_token, auth_twitter_url

app = Flask(__name__)
app.secret_key = '1234'


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/login/twitter')
def twitter_login():
    request_token = get_request_token()
    # add the request_token to the cookie to keep it from being remove after terminating the request
    session['request_token'] = request_token

    return redirect(auth_twitter_url(session['request_token']))


if "__main__" == __name__:
    app.run(port=4495)

