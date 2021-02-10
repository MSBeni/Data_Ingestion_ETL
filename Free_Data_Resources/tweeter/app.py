from flask import Flask, render_template, session, redirect
from Free_Data_Resources.tweeter.tweeter_utils import get_request_token

app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/login/twitter')
def twitter_login():
    request_token = get_request_token()
    session['request_token'] = request_token

    return redirect('http://youtube.com')


app.run(port=4495)

