#!/usr/bin/python

class GeneratorService:
	bpm = 60

	def getRandomNumber(min, max, preferedMin, preferedMax):
		return

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
	generatorService = GeneratorService()

	randomNumber = generatorService.getRandomNumber(3, 5)
	print("randomNumber", randomNumber)
