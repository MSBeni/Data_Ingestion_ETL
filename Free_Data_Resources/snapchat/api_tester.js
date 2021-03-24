var _qs = require("qs"); // Will need to 'npm install qs'

scopeList = ['https://auth.snapchat.com/oauth2/api/story-studio']
var getAuthCodeRedirectURL = function getAuthCodeRedirectURL(
  clientId,
  redirectUri,
  scopeList,
  state
) {
  var SNAP_ACCOUNTS_LOGIN_URL =
    "https://accounts.snapchat.com/accounts/oauth2/auth";
  var scope = scopeList.join(" ");
  var loginQS = {
    client_id: clientId,
    redirect_uri: redirectUri,
    response_type: "code",
    scope: scope,
    state: state,
  };

  var stringifyLoginQS = _qs.stringify(loginQS);
  return SNAP_ACCOUNTS_LOGIN_URL + "?" + stringifyLoginQS;
};


var express = require("express"); // Will need to 'npm install express'
var app = express();

var clientId = "";
var clientSecret = "";
var redirectUri = "http://localhost:8000";
var scopeList = [
  "https://auth.snapchat.com/oauth2/api/example.abc",
  "https://auth.snapchat.com/oauth2/api/example.xyz",];

app.get("/send-oauth-GET-request-step-two", function (req, res) {
  // Generate query parameters
  var state = generateClientState();

  // Build redirect URL
  var getRedirectURL = getAuthCodeRedirectURL(
    clientId,
    redirectUri,
    scopeList,
    state
  );

  // Redirect user to get consent
  res.redirect(getRedirectURL);
});

app.listen(3000);