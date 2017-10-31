import markov_chain
import requests
import time

amount = int(input("How many blocks do you want to inport? "))
jokeAmount = int(input("How many jokes do you want? "))

dadaBase = []#["title", "punchline","user"]
nextRequest=''
userAgent = {'User-agent': 'DadJokeFinder v1.6'}
count = 0

try:
	for count in range(amount):
		r = requests.get('http://www.reddit.com/r/dadjokes/top/.json?sort=top&t=all&after='+nextRequest, headers=userAgent)
		rawData = r.json()
		data=rawData['data']['children']
		nextRequest=rawData['data']['after']

		for joke in data:
			title=joke['data']['title']
			punchline=joke['data']['selftext']
			user=joke['data']['author']
			databasePush = [title, punchline, user]
			dadaBase.append(databasePush)

		time.sleep(2)

finally:
    chain1 = markov_chain.MarkovChain()
    chain2 = markov_chain.MarkovChain()
    for row in dadaBase:
        chain1.addData(row[0])
        chain2.addData(row[1])

    chain1.generateAssociations()
    chain2.generateAssociations()
    for joke in range(0,jokeAmount):
        print("------------------------------------------------")
        print(chain1.generateData())
        print("\n")
        print(chain2.generateData())
        print("------------------------------------------------")
        print("\n\n")

print("Done.")
