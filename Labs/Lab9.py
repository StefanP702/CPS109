setMediaPath('C:\\Users\\Stefan\\Desktop\\Python\\mediasources-4ed\\')
croak = makeSound('croak.wav')
preamble = makeSound('preamble.wav')
airplane = makeSound('airplane.wav')
yesterday = makeSound('yesterday.wav')
test = makeSound('test.wav')



#3 
def twoscomplement(binarystring):
  complement = list(binarystring) 
  i = 0 
  size = len(binarystring) 
  while i < size: 
    if ord(complement[i]) == 49: 
      complement[i] = '0' 
    else: 
      complement[i] = '1' 
    i += 1   
  size -= 1 
  carry = 1 
  while size >=0: 
     if complement[size] == '1' and carry == 1: 
       complement[size] = '0' 
     elif complement[size] == '0' and carry == 1: 
       complement[size] = '1' 
       carry = 0 
     size -= 1 
  return "".join(complement)  
 
#4 
def intToBinary(n): 
 s = '' 
 while n > 0: 
  s = str(n % 2) + s 
  n //= 2
 return (16 - len(s)) * '0' + s 
 print intToBinary
  
  
  
#5 
def doubleAmplitude(soundfile): 
  samples = getSamples(soundfile) 
  for sample in samples: 
   value = getSample(sample) 
   setSampleValue(sample,2 * value) 
  explore(croak) 
  
#6 
def doublehalf(sound):  
 for sample in getSamples(sound):
  value = getSampleValue(sample) 
  if value < 0:
   setSampleValue(sample,value/2)
  if value > 0: 
   setSampleValue(sample,value * 2)  
 explore(test) 

def zeronegative(sound): 
 for sample in getSamples(sound): 
  value = getSampleValue(sample) 
  if value < 0: 
   setSampleValue(sample,value * 0)
  else: 
   setSampleValue(sample,value) 
 explore(test)

#7 
def minValue(sound):
  samples = getSamples(sound)
  minvalue = getSampleValue(samples[0])
  for sample in samples: 
   value = getSampleValue(sample) 
   if value < minvalue: 
    minvalue = value 
  return minvalue 
   
#>>> minValue(test) 
# -18004  
 
#8 
def countZeros(sound): 
 count = 0
 for sample in getSamples(sound):
  value = getSampleValue(sample) 
  if value == 0: 
   count += 1
 return count 
 
 
#9 
def clip(sound,maxvalue): 
 for sample in getSamples(sound): 
  value = getSampleValue(sample) 
  if value > maxvalue: 
   setSampleValue(sample,maxvalue) 
  if value < -maxvalue: 
   setSampleValue(sample,-maxvalue) 
 explore(test) 

#10  
def falseIncreaseVolume(sound,increment): 
 for sample in getSamples(sound): 
  value = getSample(sample) 
  setSample(sample,value + increment) 
 explore(test)