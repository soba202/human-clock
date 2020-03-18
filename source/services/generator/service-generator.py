#!/usr/bin/python

import random
import datetime

class generatorService:
    def __init__(self, alarmTime, alarmDate, weather, energyLevel):
        self.alarmTime = alarmTime
        self.alarmDate = alarmDate
        self.weather = weather
        self.energyLevel = energyLevel

    def getRandomNumber(min, max):
        return random.randint(min, max)

    def getSongKey(energyLevel):
        keyMaj = ("CM", "CsM", "DM", "DsM", "EM", "FM", "FsM", "GM", "GsM","AM", "AsM", "BM")
        keyMin = ("Cm", "Csm", "Dm", "Dsm", "Em", "Fm", "Fsm", "Gm", "Gsm","Am", "Asm", "Bm")
        allkeys = keyMaj + keyMin
        if energyLevel == "depressed":
            return random.choice(keyMin)
        elif energyLevel == "chill":
            return random.choice(allkeys)
        elif energyLevel == "pumped up":
            return random.choice(keyMaj)

    def getSongBPM(energyLevel):
        if energyLevel == "depressed":
            return random.randrange(69, 104, 1)
        elif energyLevel == "chill":
            return random.randrange(104, 137, 1)
        elif energyLevel == "pumped up":
            return random.randrange(137, 170, 1)

    def getBuildUpTime(alarmTime):
        if alarmTime <= 5:
            return random.randrange(6, 8, 1)  # slow build up
        elif 5 < alarmTime <= 8:
            return random.randrange(4, 6, 1)
        elif 8 < alarmTime <= 10:
            return random.randrange(2, 4, 1)
        else:
            return random.randrange(1, 2, 1)  # wake up now

    def dateType(alarmDate):
        day = datetime.datetime.strptime(alarmDate, "%d %m %Y").weekday()
        if day < 5:
            return "Weekday"
        else:
            return "Weekend"

    #def getWeather(weather): https://code.google.com/archive/p/python-weather-api/ ???





    # def getBlockTime(bpm, timestamp):

    # def generate(self):




randomNumber = generatorService.getRandomNumber(69, 421)
print(randomNumber)

songkey = generatorService.getSongKey("chill")
print(songkey)

bpm = generatorService.getSongBPM("depressed")
print(bpm)

buildup = generatorService.getBuildUpTime(9)
print(buildup)

date = generatorService.dateType("20 03 2020")
print(date)

