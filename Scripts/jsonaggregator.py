import json         #Json
import csv          #For csv writing
import os           #Files in folder
import filecmp      #Compare files to find empties
import sys          #Debugging

dictOfDict = {}
tmpDict = {}
allLangs = []


folderPath = '/home/bolhuis/Projects/P9'
folderName = '5krepos'

#emptyFile = 'empty.json' #For Deleting files with no languages specified on github

#Load list of all languages
with open( "allLangs.txt", "r" ) as all:
    for line in all:
        allLangs.append(line.strip())

#Reset the per-file dict and set it to all zeroes
def resetTmp():
    global tmpDict
    tmpDict = {}
    for l in allLangs:
        tmpDict[l] = 0

for filename in os.listdir(folderName):
    filePath = os.path.join(folderPath, folderName, filename)

    #if(filecmp.cmp(emptyFile, filePath)): #Delete files with no languages specified on github
    #    print(filePath)

    with open(filePath) as file:
        data = json.load(file)
        dictOfDict[filename] = data



with open('all.csv', 'w') as csvfile:
    fields = ["Repo"] + allLangs
    #writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    wroteHeader = False

    for k, v in dictOfDict.items():
        tmpDict["Repo"] = k
        if(not wroteHeader):
            writer.writeheader()
            wroteHeader = True

        for deepK, deepV in v.items():
            tmpDict[deepK] = deepV
        writer.writerow(tmpDict)
        resetTmp()


