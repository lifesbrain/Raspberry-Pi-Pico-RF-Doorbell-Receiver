import os as uos
from wavePlayer import wavePlayer

def playAudio():
    player = wavePlayer()
    wavName= "haiya"
    try:
        player.play(f"/audio/{wavName}.wav")
    except KeyboardInterrupt:
        player.stop()
    player.stop()

if __name__ == "__main__":
    pass
    #playAudio()