import wave

from struct import pack
from math import sin

RATE=44100
base_duration=.1
max_vol=2**15 - 1.0 #maximum amplitude

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

def tone_space():
    tone = ''
    for i in xrange(0, int(RATE * (base_duration))):
        tone += pack('h', 0) 
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

translation = {'a' : [short_tone(),long_tone()],
               'b' : [long_tone(),short_tone(),short_tone(),short_tone()],
               'c' : [long_tone(),short_tone(),long_tone(),short_tone()],
               'd' : [long_tone(),short_tone(),short_tone()],
               'e' : [short_tone()],
               'f' : [short_tone(),short_tone(),long_tone(),short_tone()],
               'g' : [long_tone(), long_tone(),short_tone()],
               'h' : [short_tone(),short_tone(),short_tone(),short_tone()],
               'i' : [short_tone(),short_tone()],
               'j' : [short_tone(),long_tone(), long_tone(), long_tone()],
               'k' : [long_tone(),short_tone(),long_tone()],
               'l' : [short_tone(),long_tone(),short_tone(),short_tone()],
               'm' : [long_tone(), long_tone()],
               'n' : [long_tone(),short_tone()],
               'o' : [long_tone(), long_tone(), long_tone()],
               'p' : [short_tone(),long_tone(), long_tone(),short_tone()],
               'q' : [long_tone(), long_tone(),short_tone(),long_tone()],
               'r' : [short_tone(),long_tone(),short_tone()],
               's' : [short_tone(),short_tone(),short_tone()],
               't' : [long_tone()],
               'u' : [short_tone(),short_tone(),long_tone()],
               'v' : [short_tone(),short_tone(),short_tone(),long_tone()],
               'w' : [short_tone(),long_tone(), long_tone()],
               'x' : [long_tone(),short_tone(),short_tone(),long_tone()],
               'y' : [long_tone(),short_tone(),long_tone(), long_tone()],
               'z' : [long_tone(), long_tone(),short_tone(),short_tone()],
               '1' : [short_tone(),long_tone(), long_tone(), long_tone(), long_tone()],
               '2' : [short_tone(),short_tone(),long_tone(), long_tone(), long_tone()],
               '3' : [short_tone(),short_tone(),short_tone(),long_tone(), long_tone()],
               '4' : [short_tone(),short_tone(),short_tone(),short_tone(),long_tone()],
               '5' : [short_tone(),short_tone(),short_tone(),short_tone(),short_tone()],
               '6' : [long_tone(),short_tone(),short_tone(),short_tone(),short_tone()],
               '7' : [long_tone(), long_tone(),short_tone(),short_tone(),short_tone()],
               '8' : [long_tone(), long_tone(), long_tone(),short_tone(),short_tone()],
               '9' : [long_tone(), long_tone(), long_tone(), long_tone(),short_tone()],
               '0' : [long_tone(), long_tone(), long_tone(), long_tone(), long_tone()],}

wave_file = wave.open('morse_translation.wav', 'w')
## params = nchannels, sampwidth, framerate, nframes, comptype, compname
wave_file.setparams((1, 2, RATE, 0, 'NONE', 'not compressed'))
wave_data = ''

for letter in 'Hello'.lower():
    for tone in translation[letter]:
        wave_data += tone
        wave_data += tone_space()
    wave_data += letter_space()


wave_file.writeframes(wave_data)
wave_file.close()
