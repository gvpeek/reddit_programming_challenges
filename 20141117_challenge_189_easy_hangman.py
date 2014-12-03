#!/usr/bin/env python
import sys
import string

from random import choice

 #  |----
 #  O   |
 # -|-  |
 # / \  |

with open(sys.path[0] + '/20141117_challenge_189_easy_hangman_wordlist.txt', 'rb') as word_file:
    wordlist = [word.strip() for word in word_file]

valid_guesses = set()
for word in wordlist:
    for letter in word:
        valid_guesses.add(letter)
print 'Valid Letters: ', valid_guesses

word_to_be_guessed = choice(wordlist)
guesses = []
incorrect = 0 
puzzle_solved = False
hangman_display = [
'''  
  |----
      |
      |
      |
                   ''',
'''  
  |----
  O   |
      |
      |
                   ''',
'''  
  |----
  O   |
  |   |
      |
                   ''',
'''  
  |----
 \O   |
  |   |
      |
                   ''',
'''  
  |----
 \O/  |
  |   |
      |
                   ''',
'''  
  |----
 \O/  |
  |   |
 /    |
                   ''',
'''  
  |----
 \O/  |
  |   |
 / \  |
                   ''']
                   
max_incorrect = len(hangman_display) - 1

while incorrect < max_incorrect and not puzzle_solved:
    guess = None
    while not guess:
        user_input = raw_input("Guess a letter: ").lower()
        if user_input in valid_guesses and len(user_input) == 1 and not user_input in guesses:
            guess = user_input
            break
        print 'Your guess was invalid.'
        
    guesses.append(guess)
    if guess in word_to_be_guessed:
        print 'Right! That letter is in the word.'
    else:
        incorrect += 1
        
    display_word = ''
    for letter in word_to_be_guessed:
        if letter in guesses:
            display_word = display_word + letter
        else:
            display_word = display_word + '_'
            
    print display_word
    print guesses
    print hangman_display[incorrect]
    print

    if display_word == word_to_be_guessed:
        print 'You guessed the word!'
        puzzle_solved = True
        
if incorrect >= max_incorrect:
    print 'Sorry. You lose. The word was ' + word_to_be_guessed
        