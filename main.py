import os as uos
import time
from array import array
from utime import ticks_us, ticks_diff
import ujson

from machine import Pin
from wavePlayer import wavePlayer

class Bell():
    def __init__(self, code="code"):
        self._code = {}
        self.loadCode(f"{code}.json")

    def __call__(self): # Runs doorbell
        pass

    def loadCode(self, jsonFile):  # Import json code file
        try:
            with open(jsonFile, 'r') as f:
                self._code.update(ujson.load(f))
        except OSError:
            print(f"Can't open {self._code} for reading.")

    def listenRF(self): # Listens for saved code on RF
        pass

    def playAudio():
        player = wavePlayer()
        wavName= "haiya"
        try:
            player.play(f"/audio/{wavName}.wav")
        except KeyboardInterrupt:
            player.stop()
        player.stop()

    def readVol():
        pin = Pin(17, Pin.IN, Pin.PULL_UP)
        print(f"Checking pin for change")
        currentPinVal = pin.value()
        print(f"Pin = {currentPinVal}")
        while True:
            newPinVal = pin.value()
            if newPinVal != currentPinVal:
                print(f"Pin = {newPinVal}")
                currentPinVal = newPinVal


if __name__ == "__main__":
    pass
    #playAudio()

    #Import RX, 
    #constantly sample data, compare low/highs against json,
    #if match, pause sampling and play audio, inform others
    #return to samping