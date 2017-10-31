import random

class MarkovChain(object):
    def __init__(self, delimeter = ' ', windowSize=1):
        self.rawData = []
        self.delimeter = delimeter #Empty = character mode
        self.tokenAssociations = {} #{"a b":{a:2, b:#}}
        self.windowSize = windowSize

    def addData(self, data):
        self.rawData.append(str(data))

    def generateAssociations(self):
        for entry in self.rawData:
            if self.delimeter == '':
                splitEntry = list(entry)
            else:
                splitEntry = entry.split(self.delimeter)

            splitEntry.insert(0, 0)
            splitEntry.append(1)

            nextToken = ''
            window = []
            index = 0
            while nextToken != 1:
                window.append(splitEntry[index])
                while len(window) > self.windowSize:
                    window.pop(0)
                index += 1
                nextToken = splitEntry[index]
                if tuple(window) in self.tokenAssociations.keys():
                    if nextToken in self.tokenAssociations[tuple(window)]:
                        self.tokenAssociations[tuple(window)][nextToken]+=1
                    else:
                        self.tokenAssociations[tuple(window)][nextToken]=1
                else:
                    self.tokenAssociations[tuple(window)] = {nextToken: 1}

    def generateData(self):
        token = [0]
        data = ''
        value = 0
        while value != 1:
            values = [list(x) for x in self.tokenAssociations[tuple(token)].items()]
            values = [[x[0]]*x[1] for x in values]
            options=[]
            for v in values:
                for x in v:
                    options.extend(v)

            value = random.choice(options)

            if value == 1:
                continue

            data += value+' '
            token.append(value)
            while len(token) > self.windowSize:
                token.pop(0)
        return data
