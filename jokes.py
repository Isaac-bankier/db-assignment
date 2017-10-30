import requests
import sys
import time
import random

user = {'User-agent': 'DadJokeFinder v1.1'}
r = requests.get('http://www.reddit.com/r/dadjokes/top/.json', headers=user)
data = r.json()

title=""
punchline=""
data=data['data']['children']



for joke in data:
	title=joke['data']['title']
	punchline=joke['data']['selftext']
	print("------------------------------------")
	print(title)
	print("\n")
	print(punchline)
	print("------------------------------------")
