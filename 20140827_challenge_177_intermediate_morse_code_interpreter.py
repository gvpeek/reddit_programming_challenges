import wave

from struct import pack
from math import sin

RATE=44100
base_duration=.1

def long_tone():
    tone = ''
    for i in xrange(0, int(RATE * (base_duration * 3))):
        tone += pack('h', max_vol * sin(i * 4000.0 / RATE))
    return tone
        
def short_tone():
    tone = ''
    for i in xrange(0, int(RATE * base_duration)):
        tone += pack('h', max_vol * sin(i * 4000.0 / RATE)) 
    return tone
    
def letter_space():
    tone = ''
    for i in xrange(0, int(RATE * (base_duration * 3))):
        tone += pack('h', 0) 
    return tone

def word_space():
    tone = ''
    for i in xrange(0, int(RATE * (base_duration * 7))):
        tone += pack('h', 0) 
    return tone

wave_file = wave.open('test_mono.wav', 'w')
## params = nchannels, sampwidth, framerate, nframes, comptype, compname
wave_file.setparams((1, 2, RATE, 0, 'NONE', 'not compressed'))
max_vol=2**15-1.0 #maximum amplitude
wave_data = ''

wave_data += short_tone()
wave_data += letter_space()
wave_data += long_tone()
wave_data += word_space()
wave_data += short_tone()


wave_file.writeframes(wave_data)
wave_file.close()
