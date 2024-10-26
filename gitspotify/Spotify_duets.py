import os
import random
import string
import requests
from flask import Flask, redirect, request, session, url_for
import base64

app = Flask(__name__)
app.secret_key ='50d790d571e843168f39d9214f2a4487'
client_id = '012d332ade524f0c9415dbc88ce5308b'
redirect_uri = 'Spotify_Duets-login://callback'
scope = 'user-read-private user-read-email'

def generate_random_string(length=16):
	return
''.join(random.choices(string.ascii_letters +string.digits, k=length))

@app.route('/login')
def login():
	state = generate_random_string(16)
	session['state']= state 
	auth_url = ('https://accounts.spotify.com/authorize?'f'response_type=code&client_id={client_id}&' 
		f'scope={scope}&redirect_url={redirect_url}&state={state}')
	return redirect(auth_url)

@app.route('/callback')
def callback():
	if request.args.get('state')!= session['state']:
		return 'State mismatch errror', 400

	code = requ3est.args.get('code')
	return 'Authorization Succesful!'


	##PREPARE TO EXCHANGE FOR TOKEN##

	token_url  = 'https://accounts.spotify.com/api/token'
	payload = {'code': code, 'redirect_url':redirect_url, 'grant_type':'authorization_code'}
	auth = f"{client_id}:{client_secret}"

	headers = {'Content-Type':'application/x-www-form-urlencoded','Authorization':'Basic' + base64.b64encode(auth.encode()).decode()}
	response = requests.post(token_url, data=payload, headers=headers)
	token_info = response.json()

	if 'access_token' in token_info: 
		access_token = token_info['access_token']

		return f'Authorization Succesful!! Access token:{access_token}'
	return 'Failed to retrieve access token', 400
if __name__ =='__main__':
	app.run(port=8888)
