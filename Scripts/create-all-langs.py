import json         #Json
import os           #Files in folder
import filecmp      #Compare files to find empties
import sys          #Debugging

allLangs = []


folderPath = '/home/bolhuis/Projects/P9'
folderName = '5krepos'


for filename in os.listdir(folderName):
    filePath = os.path.join(folderPath, folderName, filename)

    with open(filePath) as file:
        data = json.load(file)


        print(data.keys())
        for k in data.keys():
            print("K: " + k)
            if(k not in allLangs):
                allLangs.append(k)


print(allLangs)
#Load list of all languages
with open("allLangs.txt", "w" ) as all:
    for lang in allLangs:
        all.write(lang)
        all.write("\n")
