import random
n=(input('enter ur name:'))
print('hello '+n )
list=['strawberry','madan gowri','excellent','welcome']
word = random.choice(list)  
print("Guess the characters") 
guesses = '' 
turns=10
while (turns > 0 ):
  failed=0
  for char in word:
    if char in guesses:
      print(char)
    else:
      print("")
      failed=failed+1
  if (failed==0) :
    print('u have won')     
    print('the word is',word)
    break
guess=(input('guess a word'))
guesses=guesses+guess
if guess not in word:
  turn-=1
  print ('wrong')
  print("You have", + turns, 'more guesses') 
if turns==0:
  print('u loose')