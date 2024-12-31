setMediaPath('C:\\Users\\Stefan\\Desktop\\Python\\mediasources-4ed\\')
croak = makeSound('croak.wav')
preamble = makeSound('preamble.wav')
airplane = makeSound('airplane.wav')
yesterday = makeSound('yesterday.wav')
test = makeSound('test.wav')
guzdial = makeSound('guzdial.wav')
isword = makeSound('is.wav')

#1 
def increaseAndDecrease(sound,position): 
  n = getLength(sound)
  n1 = int(position * n) 
  for i in range(0,n1):  
   value = getSampleValueAt(sound,i) 
   setSampleValueAt(sound,i,value * 2) 
  for i in range(n1,n): 
   value = getSampleValueAt(sound,i) 
   setSampleValueAt(sound,i,value * 0.2)
  explore(sound) 

#2 
def increaseDecrease2(sound) :
  rate = int(getSamplingRate(sound))
  n = getLength(sound)
  # find the max in the first second
  maxvalue = abs(getSampleValueAt(sound, 0))
  for i in range(rate) :
    maxvalue = max(maxvalue, abs(getSampleValueAt(sound, i)))
  factor = 32767.0/maxvalue
  for i in range(rate) :
    value = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, factor * value)
  factor = 0.8
  for i in range(rate, min(n, 2*rate)) :
    value = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, factor * value)
  factor = 0.6
  for i in range(2 * rate, min(n, 3*rate)) :
    value = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, factor * value)
  factor = 0.4
  for i in range(3*rate, min(n, 4*rate)) :
    value = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, factor * value)
  factor = 0.2
  for i in range(4*rate, min(n, 5*rate)) :
    value = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, factor * value)
  factor = 0.0
  for i in range(5*rate, n) :
    value = getSampleValueAt(sound, i)
    setSampleValueAt(sound, i, factor * value)

#3 
def copy(source, target, targetposition) :
  n = getLength(source)
  for i in range(n) :
    value = getSampleValueAt(source, i)
    setSampleValueAt(target, targetposition + i, value)
    
def clip(sound, start, end) :
  target = makeEmptySound(end - start)
  for i in range(start, end) :
    value = getSampleValueAt(sound, i)
    setSampleValueAt(target, i - start, value)
  return target

def thisistest(sound): 
 Wordtest = clip(test,50610,64575)
 start = clip(test,0,34020) 
 end = clip(test,34020,44310) 
 len = getLength(start) + getLength(Wordtest)+ getLength(end) 
 newTest = makeEmptySound(len)
 copy(start,newTest,0) 
 copy(Wordtest,newTest,25935)  
 return newTest
 
#4 
def reverse(sound) :
  n = getLength(sound)
  samples = getSamples(sound)
  target = makeEmptySound(n)
  targetsamples = getSamples(target)
  for i in range(n) :
    value = getSampleValue(samples[i])
    setSampleValue(targetsamples[n - 1 - i], value)
  return target

#>>> reversesound = reverse(croak) 
#>>> explore(reversesound) 


 
 