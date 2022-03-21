import random
from termcolor import colored
from art import *
import os
from replit import db
import time

highScoreTime = db["hS"]
#-----------------------------------------------------
#Picks random word from file
allWords = open('wordlist').read().splitlines()
theWord = "penis" #random.choice(allWords)
#-----------------------------------------------------
#Dels extra rubbish on variable
allWords = ""
#-----------------------------------------------------
okGuess = open("Wag").read().splitlines()
#Sets up list and variable
inWord = "0"
allText = []
#-----------------------------------------------------
#Removes the input line
def allTextPrint(inputStuff):
  global allText
  allText.append(inputStuff)
def allTextOutput():
  os.system('clear')
  for i in allText:
    for x in i:
      print(x,end='')   
#-----------------------------------------------------
#timer
startTime = time.time()
#input("Press Enter to stop")
#end_time = time.time()
#time_lapsed = end_time - start_time
#print(time_lapsed, "seconds")
#time.wait(1)

allTextPrint(colored(text2art("Wordle"), 'green'))
allTextOutput()
#-----------------------------------------------------------
# Converts numbers to the coloured letters:
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

#----------------------------------------------------------
#Actual program
while inWord != theWord:
    #guess input
  inWord = input("\nEnter your word: ")
  if len(inWord) == 5:
    #checks guess length
    if inWord in okGuess:
      #checks if word is on list (a real word)
      for i in range(5):
      #checks which letters are correct and gives them numbers
        if inWord[i] == theWord[i]:
         exec(f"ltrcorrect{i} = 3")
        else:
          if inWord[i] in theWord:
            exec(f"ltrcorrect{i} = 2")
          else:  
            exec(f"ltrcorrect{i} = 1")
    #calls subroutine to covert numbers to coloured leters and sends it to printer subroutine
      allTextPrint([coolColoredWords(ltrcorrect0, 0, inWord), coolColoredWords(ltrcorrect1, 1, inWord),     coolColoredWords(ltrcorrect2, 2, inWord),     coolColoredWords(ltrcorrect3, 3, inWord),     coolColoredWords(ltrcorrect4, 4, inWord),'\n'])
      allTextOutput()
    else:
      print("not on wordlist")
      time.sleep(1)
    allTextOutput()
  else:
    #If the word is not the correct length
    print("thats not the right length")
    time.sleep(1)
    allTextOutput()
endTime = time.time()
timeLapsed = endTime - startTime
print("You did it in", str(time_lapsed) +"s")

if highScoreTime > timeLapsed:
  db["hS"] = timeLapsed
  print("New quickest time")
else:
  print("The fastest time was", highScoreTime)