#!/usr/bin/env python

import time

from audioEngine import AudioEngine

'''
Playout of audio files on Windows is a bit complicated. That is, Python doesn't
have out-of-the-box support for audio playout on all platforms.

OrchestraService uses AudioEngine class which is a wrapper for platform
specific abstraction of FFMPEG.
'''
TAG = "[OrchestraService]"

class OrchestraService:
    oneMinute = 60              # Duration of minute in seconds
    beatQuantizer = 8           # Number of steps (actions) during every beat
    bpm = 69                    # Beats per minute

    songLength = 0              # Song length in beats
    songSteps = 0               # Number of steps, beats * quantizer

    beatDuration = 0            # Beat length in seconds
    stepDuration = 0            # Step length in seconds
    instrumentSheet = list()    # List of instruments

    audioEngine = None

    def __init__(self, songStructure):
        # General settings
        self.oneMinute = self.oneMinute
        self.beatQuantizer = self.beatQuantizer
        self.bpm = songStructure["bpm"]

        # Song parameters
        self.songLength = songStructure["length"]
        self.songSteps = self.songLength * self.beatQuantizer
 
        self.beatDuration = self.oneMinute / self.bpm
        self.stepDuration = self.beatDuration / self.beatQuantizer

        # Instruments
        self.instrumentSheet = songStructure["instrument"]

        # Control output
        print(TAG, "__init__: self.oneMinute", self.oneMinute)
        print(TAG, "__init__: self.beatQuantizer", self.beatQuantizer)
        print(TAG, "__init__: self.bpm", self.bpm)
        print(TAG, "__init__: self.songLength", self.songLength)
        print(TAG, "__init__: self.songSteps", self.songSteps)
        print(TAG, "__init__: self.beatDuration", self.beatDuration)
        print(TAG, "__init__: self.stepDuration", self.stepDuration)

        # Audio engine
        self.audioEngine = AudioEngine()

    def play(self):
        currentStep = 0
        instrumentSheetLength = len(self.instrumentSheet)

        while currentStep < self.songSteps:
            indexInstrumentStep = currentStep % instrumentSheetLength
            instrumentStep = self.instrumentSheet[indexInstrumentStep]

            if instrumentStep > 0:
                print(TAG, "play: playing drum sample", instrumentStep)

                volume = instrumentStep
                self.audioEngine.play("kick-sample.wav", 3, volume)

            currentStep += 1
            time.sleep(self.stepDuration)

        # Wait for all sounds to finish
        time.sleep(self.beatDuration * 3)
        self.audioEngine.clearCache()

if __name__ == "__main__":
    # First song structure, duration: 4 seconds
    firstSongStructure = {
        "bpm": 120,
        "length": 32,
        "instrument": [ 100, 0, 0, 0, 0, 0, 0, 0 ]
    }

    realSongStructure = {
        "bpm": 120,
        "length": 32,
        "instrument": {
            "drums": {
                "kick": [
                    { "velocity": 100, "tone": "C7" },
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None
                ]
            },
            "guitar": {
                "chords": [
                    { }
                ]
            }
        }
    }

    firstOrchestraService = OrchestraService(firstSongStructure)
    firstOrchestraService.play()

    # Second song structure, duration: 8 seconds
    secondSongStructure = {
        "bpm": 69,
        "length": 8,
        "instrument": [ 100, 0, 0, 0, 50, 0, 50, 0 ]
    }

    #secondOrchestraService = OrchestraService(secondSongStructure)
    #secondOrchestraService.play()
