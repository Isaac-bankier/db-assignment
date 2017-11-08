import requests
import hashlib
import time
import csv
import string

amount = int(input("How many blocks do you want to inport? "))

dataBaseId=0
dadaBase = [["id", "title", "punchline", "time", "upvotes", "user", "hash"]]
dadaBaseReact = [["id","upvotes", "edited", "uncle joke", "archived", "comments", "hash"]]
nextRequest=''
userAgent = {'User-agent': 'DadJokeFinder v1.6'}
count = 0

translator = str.maketrans('', '', ",.;:'\"\\/\n")

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

		for joke in data:
			title=joke['data']['title'].translate(translator)
			punchline=joke['data']['selftext'].translate(translator)
			dataBaseId+=1
			edited= (joke['data']['edited'] != False if time.gmtime((joke['data']['edited'])) else (False))
			over_18=joke['data']['over_18']
			user=joke['data']['author'].translate(translator)
			postTime=time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(joke['data']['created_utc']))
			upvotes=joke['data']['score']
			archived=joke['data']['archived']
			comments=joke['data']['num_comments']
			hash = jokeHash(title, punchline, postTime, user).translate(translator)

			databasePush = [dataBaseId, title, punchline, postTime, upvotes, user, hash]
			database2Push = [dataBaseId, upvotes, edited, over_18, archived, comments, hash]
			dadaBase.append(databasePush)
			dadaBaseReact.append(database2Push)

		time.sleep(2)

finally:
	writer = csv.writer(open("/home/isaac/Documents/code/database-assignment-year-9/dadaBase2.csv", "w"), dialect="excel")
	for row in dadaBase:
		writer.writerow(row)

	writer = csv.writer(open("/home/isaac/Documents/code/database-assignment-year-9/dadaBaseReact2.csv", "w"), dialect="excel")
	for row in dadaBaseReact:
		writer.writerow(row)

	print("Wrote data on "+str(len(dadaBase)-1)+" dad jokes.")
	print("Done.")
