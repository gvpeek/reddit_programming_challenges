import os
import re
import wave

from struct import pack
from math import sin

RATE = 44100
base_duration = .1
max_vol = 2**15 - 1.0
hertz = 5000.0

def generate_tone(length_multiplier, volume):
    tone = ''
    for i in xrange(0, int(RATE * (base_duration * length_multiplier))):
        tone += pack('h', volume * sin(i * hertz / RATE))
    return tone

def long_tone():
    return generate_tone(3, max_vol)
        
def short_tone():
    return generate_tone(1, max_vol)

def tone_space():
    return generate_tone(1, 0)
    
def letter_space():
    return generate_tone(3, 0)

def word_space():
    return generate_tone(7, 0)

def translate(input):
    tone_types = {'.' : short_tone(),
                  '-' : long_tone()}

    translation = {'a' : ['.','-'],
                   'b' : ['-', '.', '.', '.'],
                   'c' : ['-', '.','-', '.'],
                   'd' : ['-', '.', '.'],
                   'e' : ['.'],
                   'f' : ['.', '.','-', '.'],
                   'g' : ['-', '-', '.'],
                   'h' : ['.', '.', '.', '.'],
                   'i' : ['.', '.'],
                   'j' : ['.','-', '-', '-'],
                   'k' : ['-', '.','-'],
                   'l' : ['.','-', '.', '.'],
                   'm' : ['-', '-'],
                   'n' : ['-', '.'],
                   'o' : ['-', '-', '-'],
                   'p' : ['.','-', '-', '.'],
                   'q' : ['-', '-', '.','-'],
                   'r' : ['.','-', '.'],
                   's' : ['.', '.', '.'],
                   't' : ['-'],
                   'u' : ['.', '.','-'],
                   'v' : ['.', '.', '.','-'],
                   'w' : ['.','-', '-'],
                   'x' : ['-', '.', '.','-'],
                   'y' : ['-', '.','-', '-'],
                   'z' : ['-', '-', '.', '.'],
                   '1' : ['.','-', '-', '-', '-'],
                   '2' : ['.', '.','-', '-', '-'],
                   '3' : ['.', '.', '.','-', '-'],
                   '4' : ['.', '.', '.', '.','-'],
                   '5' : ['.', '.', '.', '.', '.'],
                   '6' : ['-', '.', '.', '.', '.'],
                   '7' : ['-', '-', '.', '.', '.'],
                   '8' : ['-', '-', '-', '.', '.'],
                   '9' : ['-', '-', '-', '-', '.'],
                   '0' : ['-', '-', '-', '-', '-'],
                   '.' : ['.','-', '.','-', '.','-'],
                   ',' : ['-', '-', '.', '.','-', '-'],
                   '/' : ['-', '.', '.','-', '.'],
                   '+' : ['.','-', '.','-', '.'],
                   '=' : ['-', '.', '.', '.','-'],
                   '?' : ['.', '.','-', '-', '.', '.'],
                   '(' : ['-', '.','-', '-', '.'],
                   ')' : ['-', '.','-', '-', '.','-'],
                   '-' : ['-', '.', '.', '.', '.','-'],
                   '"' : ['.','-', '.', '.','-', '.'],
                   '_' : ['.', '.','-', '-', '.','-'],
                   "'" : ['.','-', '-', '-', '-', '.'],
                   ':' : ['-', '-', '-', '.', '.', '.'],
                   ';' : ['-', '.','-', '.','-', '.'],
                   '$' : ['.', '.', '.','-', '.', '.','-']}
               
    execution_dir = os.path.dirname(os.path.realpath(__file__))
    wave_file = wave.open(os.path.join(execution_dir, 'morse_translation.wav'), 'w')
    ## params = nchannels, sampwidth, framerate, nframes, comptype, compname
    wave_file.setparams((1, 2, RATE, 0, 'NONE', 'not compressed'))
    wave_data = ''

    words = re.split('\W+', user_input.strip())

    morse_text =[]
    for word in words:
        dot_notation = ''
        for i, letter in enumerate(word.lower()):
            for tone in translation[letter]:
                dot_notation += tone
                wave_data += tone_types[tone]
                wave_data += tone_space()
            wave_data += letter_space()
            if not len(word) == i+1:
                dot_notation += ' '
        wave_data += word_space()
        morse_text.append(dot_notation)

    wave_file.writeframes(wave_data)
    wave_file.close()
    
    print morse_text

if __name__ == '__main__':
    while True:
        user_input = raw_input('Enter a phrase to be translated to morse code: ')
        break
    translate(user_input)