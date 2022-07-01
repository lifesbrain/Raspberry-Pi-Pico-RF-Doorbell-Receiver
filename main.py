from audio.longwave import LongWave

lw = LongWave() # Default uses DAC1 and Timer4
lw.play("audio/haiya.wav")

lw.play('hisnibs.wav', 200) # 120% speed