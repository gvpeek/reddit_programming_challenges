import wave

from struct import pack
from math import sin

RATE=44100

wave_file = wave.open('test_mono.wav', 'w')
## params = nchannels, sampwidth, framerate, nframes, comptype, compname
wave_file.setparams((1, 2, RATE, 0, 'NONE', 'not compressed'))
max_vol=2**15-1.0 #maximum amplitude
wave_data = ''

for i in xrange(0, RATE*3):
    print sin(i * 500.0 / RATE)
    wave_data += pack('h', max_vol * sin(i * 500.0 / RATE)) #500Hz

wave_file.writeframes(wave_data)
wave_file.close()
