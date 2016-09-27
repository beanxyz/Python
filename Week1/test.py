newDict = {}
with open('China', 'r') as f:
    for line in f:
        splitLine = line.split()
        newDict[splitLine[0]] = ",".join(splitLine[1:])

print(newDict)

City="LuoHe"

newDict2=[]