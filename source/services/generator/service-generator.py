#!/usr/bin/python

class GeneratorService:
	bpm = 60

	def __init__(self, time, energyLevel):
		return

	def getRandomNumber(min, max):
		return
	
	#random key, minor/major ovisno o energyLevel
	def getSongKey(energyLevel):
		return

	# Vraca broj izmedu 69 i 169
	def getSongBPM(energyLevel):
		return

	# Where hour is datetime type
	# Returns a number of beats representing duration of single block
	def getBlockTime(bpm, timestamp):
		return

'''
getRandomKey("depressed|chill|pumpedup")

getRandomKey() -> None
getRandomKey("random") -> None
getRandomKey("depressed|...") -> {
	"root": "C->C",
	"chord": ["D", "E"]
}
'''

if __name__ == "__main__":
	time = {
		"date": "31.01.2020", # DD.MM.YYYY
		"time": 16, # Time of the day, number between 0 and 24
		"weather": "sunny" # One of predefined values
	}
	generatorService = GeneratorService(time, energyLevel)

	generatedSong = generatorService.generate()

	# Generated song should look similar to example in serviceOrchestra.py
	print generatedSong

	randomNumber = generatorService.getRandomNumber(3, 5)
	print("randomNumber", randomNumber)
