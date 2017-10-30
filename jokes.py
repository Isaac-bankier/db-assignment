import requests
import hashlib
import time

amount = int(input("How many blocks do you want to inport?"))

dataBaseId=0
dadaBase = [["id", "title", "punchline", "time", "upvotes", "user", "hash"]]
dadaBaseReact = [["id","upvotes", "edited", "uncle joke", "archived", "comments", "hash"]]
nextRequest=''
userAgent = {'User-agent': 'DadJokeFinder v1.4'}
count = 0

def jokeHash(title, punchline, date, user):
	hasher = hashlib.sha512()
	hasher.update(title.encode('ascii', 'ignore') + punchline.encode('ascii', 'ignore') + str(date).encode('ascii', 'ignore') + user.encode('ascii', 'ignore'))
	return 	hasher.hexdigest()

for count in range(amount):
	r = requests.get('http://www.reddit.com/r/dadjokes/top/.json?sort=top&t=all&after='+nextRequest, headers=userAgent)
	data = r.json()
	data=data['data']['children']
	nextRequest=['data']['children']['after']

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

	time.sleep(2)

print(dadaBase)
print(dadaBaseReact)
