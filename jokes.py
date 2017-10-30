import requests
import hashlib
import time
import csv

amount = int(input("How many blocks do you want to inport? "))

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
try:
	for count in range(amount):
		r = requests.get('http://www.reddit.com/r/dadjokes/top/.json?sort=top&t=all&after='+nextRequest, headers=userAgent)
		rawData = r.json()
		data=rawData['data']['children']
		nextRequest=rawData['data']['after']
		print(nextRequest)

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

finally:
	writer = csv.writer(open("/home/isaac/Documents/code/database-assignment-year-9/dadaBase.csv", "w"))
	for row in dadaBase:
		writer.writerow(row)

	writer = csv.writer(open("/home/isaac/Documents/code/database-assignment-year-9/dadaBaseReact.csv", "w"))
	for row in dadaBaseReact:
		writer.writerow(row)

	print("Wrote data on "+str(len(dadaBase)-1)+" dad jokes.")
	print("Done.")
