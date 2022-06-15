#Online wordle solver

import numpy as np
import string

print("Welcome to the solver")

with open('words.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

all_words = lines

all_words.sort()

ord_words = ['first', 'second','third','fourth','fifth'];

letters = [[],[],[],[],[]] #possible letters for each location


for i in range(0,5):
  letters[i] = list(string.ascii_lowercase) 

contains = list() #list of all contained letters
doubles = list() #list of doubled letters
does_not_contain = list() #list of all letters that are not contained

live_words = list(all_words)



#Start Loop
for attempts in range(0,5):

  number_of_live_words = len(live_words)
  print(f"There are {number_of_live_words} possible 5 letter words.\n")

  if len(live_words) < 1:
    print("I have failed you.")
  
    exit()
  elif len(live_words) < 2:
    
    print(f"\nI've got it!\nThe word is {live_words}\n")
    exit("Have a nice day")

  doubles_counter =0
  rand = np.random.randint(len(live_words))
  randWord = str(live_words[rand])
  while(len(set(randWord)) < len(randWord) and doubles_counter < 20):
    rand = np.random.randint(len(live_words))
    doubles_counter+=1
    randWord = str(live_words[rand])


  print(f"You should guess: {randWord}")

  colour = ['','','','','']
  possible_colours = ["green", "grey", "yellow"]

  print("Please enter the colour of each letter. They can be green, grey, or yellow.")


  for i in range(0,5):
    answer = ''
    while answer not in possible_colours:
      answer = input(f"What colour is the {ord_words[i]} letter? ")
    colour[i] = answer
  #Echo
  print(colour)


  for i in range(0,5):
    if colour[i] == "green":
      for let in letters[i]:
        if  let != randWord[i]:
          letters[i].remove(let)
      letters[i] = randWord[i]
      
    elif colour[i] == "yellow":
      if randWord[i] in randWord[:i]:
        doubles.append(randWord[i])
      contains.append(randWord[i])
      try:
        letters[i].remove(randWord[i])
      except ValueError:
        pass
    elif colour[i] == "grey": 
      if randWord[i] not in randWord[:i] and randWord[i] not in randWord[i+1:]:
        does_not_contain.append(randWord[i])
        for l in letters:
          try:
            l.remove(randWord[i])
          except ValueError:
            pass
          except AttributeError:
            pass
      else:
        try:
          letters[i].remove(randWord[i])
        except ValueError:
          pass
      

  #Update live Words

  #Match green letters
  for i in range(0,5):
    if len(letters[i]) == 1:
      rm = list()
      for w in live_words:
        if w[i] != letters[i]:
          rm.append(w)

      for w in rm:
        try:
          live_words.remove(w)
        except ValueError:
          pass
    
  #Ensure all letters are still live. Remove words containing dead letter/position combos.
  rm = list()
  for word in live_words:
    for i in range(0,5):
      if word[i] not in letters[i]:
        rm.append(word)
  for w in rm:
        try:
          live_words.remove(w)
        except ValueError:
          pass

  #ensure not containing greys
  for letter in does_not_contain:
    rm = list()
    for word in live_words:
      if letter in word:
        rm.append(word)
    for w in rm:
        try:
          live_words.remove(w)
        except ValueError:
          pass

  #ensure containing yellows
  for letter in contains:
    for word in live_words:
      if letter not in word:
        live_words.remove(word)

  for letter in doubles:
    for word in live_words:
      tempW = word.replace(letter,'',1)
      if letter not in tempW:
        live_words.remove(word)

  print("\n\n\n")
  #Debug echos
  #print(letters)
print("We weren't able to narrow it down completely. The ramaining possibilities are:")
print(live_words)