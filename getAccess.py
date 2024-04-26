"""
Code for acquiring the reddit access token
"""
from flask import Flask, request
import requests
import json
import urllib.parse
import random

import requests.auth

CLIENT_ID = 'G9fsyjdmNdhVgArnCYjvaQ'
CLIENT_SECRET = 'Bb-kyFLsB8PX59Xx1OKHCAFNgbQc3Q'

# state variable is used to generate the url
state = str(random.randint(0, 65000))

redirect_uri = urllib.parse.quote("http://0.0.0.0:8000/")

URL = f'https://www.reddit.com/api/v1/authorize?client_id={CLIENT_ID}&&state={state}&redirect_uri={redirect_uri}&response_type=code&duration=permanent&scope=%2A'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_access():
    args = request.args.to_dict()

    if "code" in args:
        url = 'https://www.reddit.com/api/v1/access_token'
        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
        data = {'grant_type': 'authorization_code',
                'code': request.args['code'],
                'redirect_uri': "http://0.0.0.0:8000/"}
        headers = {'User-Agent': 'testscript by u/alexdelei'}

        respo = requests.post(url, auth=auth, data=data, headers=headers)
        r = respo.json()
        token = r['access_token']
        get_username(token)
        
        return r
    return f"Click on this <a href=\"{URL}\" target=\"_blank\">link</a>."

@app.route('/me', methods=['GET'])
def get_username(access_token):
    headers = {'Authorization': "bearer " + access_token}
    resp = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
    me = resp.json()
    return me['name']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)