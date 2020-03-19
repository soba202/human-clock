import json

def createJson(inputDict, outputFile):
    targetFile = open(outputFile, "w")
    finalJson = json.dumps(inputDict, indent=4)
    targetFile.write(finalJson)
    return


testDict = {
    "key": "CM",
    "dateType": "Weekday",
    "bpm": 135
}

createJson(testDict, "test-song.json")