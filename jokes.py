import requests
import hashlib

usera = {'User-agent': 'DadJokeFinder v1.1'}
r = requests.get('http://www.reddit.com/r/dadjokes/top/.json', headers=usera)
data = r.json()

title=""
punchline=""
data=data['data']['children']
dataBaseId=0
edited


dadaBase = [["id", "title", "punchline", "time", "upvotes", "user", "hash"]]
dadaBaseReact = [["id","upvotes", "edited", "uncle joke", "archived", "comments", "hash"]]

def jokeHash(title, punchline, date, user):
	hasher = hashlib.sha512()
	hasher.update(title + punchline + date + user)
	return 	hasher.hexdigest()

for joke in data:
	title=joke['data']['title']
	punchline=joke['data']['selftext']
	dataBaseId+=1
	edited=joke['data']['edited']
	over_18=joke['data']['over_18']
	user=joke['data']['author']
	postTime=joke['data']['created_utc']
	upvotes=joke['data']['score']
	archived=joke['data']['archived']
	comments=joke['data']['num_comments']
	hash = jokeHash(title, punchline, postTime, user)

	databasePush = [dataBaseId, title, punchline, postTime, upvotes, user, hash]
	database2Push = [dataBaseId, upvotes, edited, over_18, archived, comments, hash]
	dadaBase.append(databasePush)
	dadaBaseReact.append(database2Push)

print(dadaBase)
print(dadaBaseReact)
