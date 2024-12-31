#1
def bingoGame(name,money): 
  line1 = name+" was extremely lucky in Bingo and won "+str(money)+" dollars" 
  print line1 

#2  
def marathon(RunnerNumber,milesPassed,time): 
  line1 = " The Runner # "+str(RunnerNumber)+" passed mile "+str(milesPassed)+" at time "+time 
  print line1   

#3
def invertedpyramid(char): 
  space = " " 
  print 10*char 
  print space,7*char 
  print 2*space,5*char 
  print 3*space,3*char 
  print 4*space,char  
  
def invertedpyramid2(char): 
 space = " " 
 print 4*space,char 
 print 3*space,3*char 
 print 2*space,5*char 
 print space,7*char 
 print 9*char

#4
def textsquare(ch,n): 
  print(ch * n)
  for i in range(n-2):            
    print(ch + ' '*(n-2) + ch)
  print(ch * n)

#5
def justConsonants(string): 
  pile = ''
  for letter in string :
    if not (letter in 'AEIOUYaeiouy') :
      pile = pile + letter
  print pile

#6 
def justConsonants2(string): 
  pile = ''
  for letter in string :
    if not (letter.lower() in 'aeiouy') :
      pile = pile + letter
  print pile

#7    
def dup3(s) :
  target = ''
  for letter in s :
    target = letter + target + letter
  return target  
 
#8  
def dup5(s): 
 target = " " 
 for letter in s: 
  target = letter + "-" +target+ "-"+ letter 
 return target    
 
#9
def separate(string): 
  vowels = ''
  consonants = ''
  for letter in string :
    if letter.lower() in 'aeiouy' :
      vowels = vowels + letter
    if not (letter.lower() in 'aeiouy') :
      consonants = consonants + letter
  print 'Vowels: ' + vowels
  print 'Consonants: ' + consonants

#10    
def encode2(string, alpha2) :
  alpha1 = 'abcdefghijklmnopqrstuvwxyz'
  secret = ''
  for letter in string :
   i = alpha1.find(letter)
   if i >= 0 :
      secret = secret + alpha2[i]
  return secret

  


