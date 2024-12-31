from math import sqrt
def hypotenuse(a,b):
  c = sqrt(a**2 + b**2)
  return c 

#>>> hypotenuse(3,4) 
#>>> 5.0   

def encode(string,keyletters):
  alpha="abcdefghijklmnopqrstuvwxyz"
  secret = ""
  for letter in string:
    index = alpha.find(letter)
    secret = secret+keyletters[index]
  print secret 
  
def decode(secret,keyletters):
  alpha="abcdefghijklmnopqrstuvwxyz"
  clear = ""
  for letter in secret:
    index = keyletters.find(letter)
    clear = clear+alpha[index]
  print clear 
  
  
#>>> encode("helloworld","earthbcdfgijklmnopqsuvwxyz") 
#dhjjmwmpjt

#>>> decode("dhjjmwmpjt","earthbcdfgijklmnopqsuvwxyz") 
#helloworld
