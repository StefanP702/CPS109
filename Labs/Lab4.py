#1 

def NoColors(picture): 
 for pixel in getPixels(picture): 
  value = getRed(pixel) 
  setRed(pixel, value * 0)
  value = getBlue(pixel) 
  setBlue(pixel, value * 0)
  value = getGreen(pixel) 
  setGreen(pixel, value * 0)  
 show(picture) 
  
#2 
def NoColors2(picture): 
 for pixel in getPixels(picture): 
   setRed(pixel, 255) 
   setBlue(pixel, 255) 
   setGreen(pixel, 255) 
 show(picture)  
 
#3 

def test1() :
 f_statue = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\statue-tower.jpg"
 picture = makePicture(f_statue)
 for pixel in getPixels(picture) :
  setRed(pixel, getRed(pixel) * 0.5)
 show(picture)
 
def test2() :
  f_statue = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\statue-tower.jpg"
  picture = makePicture(f_statue)
  for pixel in getPixels(picture) :
    setBlue(pixel, getBlue(pixel) * 1.5)
  show(picture) 

def test3() :
  f_statue = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\statue-tower.jpg"
  picture = makePicture(f_statue)
  for pixel in getPixels(picture) :
    setGreen(pixel, 0)
  show(picture) 

def test4() :
   f_statue = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\statue-tower.jpg"
   picture = makePicture(f_statue)
   for pixel in getPixels(picture) :
     red = getRed(pixel) + 10
     green = getGreen(pixel) + 10
     blue = getBlue(pixel) + 10
     color = makeColor(red, green, blue)
     setColor(pixel, color)
   show(picture) 

def test5() :
  f_statue = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\statue-tower.jpg"
  picture = makePicture(f_statue)
  for pixel in getPixels(picture) :
    r = max(0, getRed(pixel) - 20)
    g = max(0, getGreen(pixel) - 20)
    b = max(0, getBlue(pixel) - 20)
    color = makeColor(r, g, b)
    setColor(pixel, color)
  show(picture)

def test6() :
  f_statue = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\statue-tower.jpg"
  picture = makePicture(f_statue)
  for pixel in getPixels(picture) :
   red = getRed(pixel) 
   green = getGreen(pixel) 
   blue = getBlue(pixel) 
   color = makeColor(red, green, blue)
   setColor(pixel, color)
  show(picture)


def test7() :
  f_statue = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\statue-tower.jpg"
  picture = makePicture(f_statue)
  for pixel in getPixels(picture) :
   red = getRed(pixel) / 2
   green = getGreen(pixel) / 2 
   blue = getBlue(pixel) / 2
   color = makeColor(red, green, blue)
   setColor(pixel, color)
  show(picture)

def test8() :
  f_statue = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\statue-tower.jpg"
  picture = makePicture(f_statue)
  for pixel in getPixels(picture) :
   red = getRed(pixel) / 3
   green = getGreen(pixel) / 3 
   blue = getBlue(pixel) / 3
   color = makeColor(red, green, blue)
   setColor(pixel, color)
  show(picture)

def test9() :
  f_statue = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\statue-tower.jpg"
  picture = makePicture(f_statue)
  for pixel in getPixels(picture) :
    red = getRed(pixel) * 2
    green = getGreen(pixel) * 2 
    blue = getBlue(pixel) * 2
    color = makeColor(red, green, blue)
    setColor(pixel, color)
  show(picture) 

#4 
def blueify(): 
 f_jenny = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\jenny-red.jpg"
 picture = makePicture(f_jenny)
 for pixel in getPixels(picture): 
  value = getBlue(pixel) 
  if value<150: 
   setColor(pixel, white) 
 show(picture) 

#5 
def blueify2(): 
 f_jenny = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\jenny-red.jpg"
 picture = makePicture(f_jenny)
 for pixel in getPixels(picture): 
   blue = getBlue(pixel) * 2 
   red = getRed(pixel) * 2 
   green = getGreen(pixel) * 2 
   color = makeColor(red,green,blue) 
   setColor(pixel,color)
 show(picture) 
 
#6 
def blueify3(): 
 f_jenny = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\jenny-red.jpg"
 picture = makePicture(f_jenny)
 for pixel in getPixels(picture): 
  blue = getBlue(pixel) * 2 
  red = getRed(pixel) / 2 
  green = getGreen(pixel) / 2 
  color = makeColor(red,green,blue) 
  setColor(pixel,color) 
 show(picture) 

#7 
def greyScaleAndNegate():  
   f_caterpillar = "C:\Users\Stefan\Desktop\Python\mediasources-4ed\caterpillar.jpg"
   picture = makePicture(f_caterpillar )
   for pixel in getPixels(picture):
      red = getRed(pixel) 
      green = getGreen(pixel)
      blue = getBlue(pixel) 
      #changing to greyScale
      intensity = (red+blue+green)/3 
      setColor(pixel,makeColor(intensity,intensity,intensity)) 
      #Negating 
      luminance = 255 - (0.3 * red + 0.6 * green + 0.1 * blue)
      setColor(pixel,makeColor(luminance,luminance,luminance))
   show(picture) 

#8 
def greyScaleAndNegate2(picture): 
  grayScale(picture) 
  negate(picture) 
  show(picture) 
  
  #>>> picture = makePicture(pickAFile())
  #>>> caterpillar.jpg
  #>>> greyScaleAndNegate2(picture) 
  
def grayScale(picture): 
 for pixel in getPixels(picture): 
   red = getRed(pixel) 
   blue = getBlue(pixel) 
   green = getGreen(pixel) 
   intensity = (red+blue+green)/3 
   setColor(pixel,makeColor(intensity,intensity,intensity)) 
 
def negate(picture): 
 for pixel in getPixels(picture): 
   red = getRed(pixel) 
   blue = getBlue(pixel) 
   green = getGreen(pixel) 
   color = makeColor(255-red,255-green,255-blue) 
   setColor(pixel,color) 
 
#9  
def lightenGrayScale(picture):
  for pixel in getPixels(picture):
    red = getRed(pixel)+75
    green = getGreen(pixel)+75 
    blue = getBlue(pixel)+75  
    intensity = (red+green+blue)/3
    setColor(pixel,makeColor(intensity,intensity,intensity))
    newRed = getRed(pixel) * 0.3
    newGreen = getGreen(pixel) * 0.6
    newBlue = getBlue(pixel) * 0.1
    luminance = newRed+newGreen+newBlue
    setColor(pixel,makeColor(luminance,luminance,luminance))
  show(picture) 

  #>>>picture = makePicture(pickAFile())
  #>>>butterfly2.jpg 
  #>>>lightenGrayScale(picture)  
  
#10 
def lightenGrayScale2(picture): 
 for pixel in getPixels(picture): 
  color = getColor(pixel) 
  color = makeLighter(color) 
  setColor(pixel,color) 
  red = getRed(pixel)
  blue = getBlue(pixel) 
  green = getGreen(pixel) 
  intensity = (red+blue+green)/3 
  setColor(pixel,makeColor(intensity,intensity,intensity)) 
 show(picture)
 #>>>picture = makePicture(pickAFile())
 #>>>butterfly2.jpg 
 #>>>lightenGrayScale2picture) 
 
