phrases = {'lol' : 'laugh out loud',
           'dw' : 'don\'t worry',
           'hf' : 'have fun',
           'gg' : 'good game',
           'brb' : 'be right back',
           'g2g' : 'got to go',
           'wtf' : 'what the fuck',
           'wp' : 'well played',
           'gl' : 'good luck',
           'imo' : 'in my opinion'
}

def translate(phrase):
    words = phrase.split()
    output = ''
    for word in words:
        if word in phrases:
            output += phrases[word]
        else:
            output += ' ' + word
    print output
    
    
translate('wtf that was unfair')
translate('gl all hf')
translate('imo that was wp. Anyway I\'ve g2g')