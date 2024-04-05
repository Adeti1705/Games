import random
import csv
#wordslist
#53 elements
wordslist=['ant', 'bat', 'bear', 'camel' ,'cat' , 'cobra','crow', 'deer', 'dog', 'donkey',
        'duck' ,'eagle','fox', 'frog', 'goat', 'goose' ,'hawk','lion', 'lizard','llama' ,
        'mole' ,'monkey', 'moose' ,'mouse' ,'owl', 'panda','parrot', 'pigeon' ,'python',
       'rabbit','rat','rhino' ,'salmon', 'seal', 'shark','sheep','sloth', 'snake', 'spider',
       'swan' ,'tiger','turkey' ,'turtle','whale', 'wolf','zebra','octopus','snail','horse',
       'hummingbird','hippopotamus','crab','alpaca']

# 5 tries
tries=['''
  ---------|
   |       |
   O       |
           |
           | 
           |
        ---|---''','''

 ----------|
   |       |
   O       |
   |       |
   |       | 
           |
        ---|---''','''
 ----------|
   |       |
   O       |
  /|       |
   |       | 
           |
        ---|---''','''
 ----------|
   |       |
   O       |
  /|\      |
   |       | 
           |
        ---|---''','''
 ----------|
   |       |
   O       |
  /|\      |
   |       | 
  /        |
        ---|--- ''','''
 ----------|
   |       |
   O       |
  /|\      |
   |       | 
  / \      |
        ---|--- '''
        ]
guesslist=[]
#for selecting word, returns word
def selectword():
  global guesslist
  while True:
    word=random.choice(wordslist)
    if word in guesslist:
      continue
    else:break
  guesslist.append(word)
  return word
#for validation, returns the guessed letter
def chkguess():
  while True:
    g=input('enter a letter: ').lower()
    if not g.isalpha() or len(g)!=1:
      continue
    else:break
  return g
#prints the current status of the player
def currentstatus(guessedword,chance):
  global correctword
  for l in correctword:
    if l in guessedword:
      print(l,end='')
    else:
      print('_ ',end='')
  print(tries[chance])

while True:
  ans=input('do u want to play?(y/n)')
  if ans.lower()=='y':pass
  if ans.lower()=='n':
    #leaderboard()
    break
  print('\nH A N G M A N\n**************\n\nLets Begin')
  print('NOTE:You will have 5 tries\nHINT:All words are names of different animals')
  correctword=selectword()
  print('_ '*len(correctword),'\n',tries[0])
  #print(correctword)
  chance=0
  guessedword=''
  alreadyguessed=''
  while chance<5:
    gletter=chkguess()
    if gletter in alreadyguessed:
      print('you have already guessed the letter , please try again')
    elif gletter in correctword:
      print('correct!')
      alreadyguessed+=gletter
      guessedword+=gletter
      currentstatus(guessedword,chance)
      k = sum(l in guessedword for l in correctword)
      if k ==len(correctword):
        print('you WON!')
        break
    else:
      chance+=1
      currentstatus(guessedword,chance)
      alreadyguessed+=gletter
  else:print('sorry! try again','the word was',correctword)


