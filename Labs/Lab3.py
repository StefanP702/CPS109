#1

def buildCipher(key) :
  alpha1 = "abcdefghijklmnopqrstuvwxyz"
  alpha2 = key
  for letter in alpha1 :
    if letter not in key :
     alpha2 = alpha2 + letter
  return alpha2

def encode2(message, key) :
# change message to lower case
  message = message.lower()
# First build alpha2
  alpha1 = 'abcdefghijklmnopqrstuvwxyz'
  alpha2 = ''
  for letter in alpha1 :
    if letter not in key :
      alpha2 = alpha2 + letter
    # put the key word at the end of alpha2
  alpha2 = alpha2 + key
# Second encript the message
  pile = ''
  for letter in message :
    i = alpha1.find(letter)
    if i >= 0 :
      pile = pile + alpha2[i]
  return pile

#2

def encode3(message, key) :
# change message to lower case
  message = message.lower()
# The normal alphabet:
  alpha1 = "abcdefghijklmnopqrstuvwxyz"
# First reverse alpha1 to make alpha2
  reverse1 = ""
  for letter in alpha1 :
    reverse1 = letter + reverse1
  alpha2 = key
  for letter in reverse1 :
    if letter not in key :
      alpha2 = alpha2 + letter
  alpha2 = alpha2 + key
# Second encript the message
  pile = ''
  for letter in message :
    i = alpha1.find(letter)
    if i >= 0 :
      pile = pile + alpha2[i]
  return pile

#3
def dupTimes3(something) :
  dup = '_'
  for index in range(0, len(something)) :
    dup = dup + something
  return dup 
  
#4 
def findem4(n) :
 letters = "abcdefghijklmnopqrstuvwxyz"
 pile = ""
 for index in range(0, len(letters)) :
   pile = pile + letters[index % n]
 return pile 
    
#5 
def spaceitout(string,n): 
  pile = ''
  for letter in string :
    pile = pile + letter + n * ' '
  return pile
  
 

#6 

def spaceitout2(string,n): 
   pile = ''
   for word in string.split() :
    pile = pile + word + n * ' '
   return pile



#8 
def decreaseRed(picture): 
 for pixel in getPixels(picture): 
  value = getRed(pixel) 
  setRed(pixel, value * 0.8) 
  
  
#9 
def increaseRed2(picture) :
 for pixel in getPixels(picture) :
  setRed(pixel, 1.2 * getRed(pixel))
  show(picture)
  
#10 
def swapRedGreen(picture) :
  for pixel in getPixels(picture) :
    red = getRed(pixel)
    green = getGreen(pixel)
    temp = red
    red = green
    green = temp
    setRed(pixel, red)
    setGreen(pixel, green) 
  show(picture) 
 
 
    
