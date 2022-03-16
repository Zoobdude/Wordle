import random
from termcolor import colored

allWords = open('wordlist').read().splitlines()
theWord = random.choice(allWords)
print(theWord)
inWord = "0"

#print(colored('hello', 'red'), colored('world', 'green'))

# 1 = Not in word
# 2 = in word not right place
# 3 = in word right place

def coolColoredWords(ltrcorrectNum, i, inWord):
  if ltrcorrectNum == 1:
    return(colored(inWord[i], 'red'))
  elif ltrcorrectNum == 2:
    return(colored(inWord[i], 'yellow'))
  elif ltrcorrectNum == 3:
    return(colored(inWord[i], 'green'))
  else:
   print("somethin be broken")
      
while inWord != theWord:
  inWord = input("Enter your word: ")
  if len(inWord) == 5:
    for i in range(5):
      if inWord[i] == theWord[i]:
       exec(f"ltrcorrect{i} = 3")
      else:
        if inWord[i] in theWord:
          exec(f"ltrcorrect{i} = 2")
        else:  
          exec(f"ltrcorrect{i} = 1")
    print(coolColoredWords(ltrcorrect0, 0, inWord), coolColoredWords(ltrcorrect1, 1, inWord),     coolColoredWords(ltrcorrect2, 2, inWord),     coolColoredWords(ltrcorrect3, 3, inWord),     coolColoredWords(ltrcorrect4, 4, inWord) )
  else:
    print("thats not the right length")
#https://stackoverflow.com/questions/5036700/how-can-you-dynamically-create-variables
#for i in range(2):
#  exec(f"number{i} = {1}")
#  print(number0)

#https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b