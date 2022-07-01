# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
"""
import board
import audiomp3
import audiopwmio

def playMP3(file="slow"):
    audio = audiopwmio.PWMAudioOut(board.GP0)
    decoder = audiomp3.MP3Decoder(open(f"audio/{file}.mp3", "rb"))

    audio.play(decoder)
    while audio.playing:
        pass

    print("Done playing!")

if __name__ == "__main__":
    playMP3()
