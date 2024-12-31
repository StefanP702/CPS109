#1
def changeColor(picture,amount,rgbNumber): 
 for pixel in getPixels(picture): 
  if(-0.99 < amount < 0.99): 
    currentRed = getRed(pixel)
    currentBlue = getBlue(pixel)
    currentGreen = getGreen(pixel)   
  else:
    print "Please enter right color change number."
    return
  if rgbNumber == 1: 
      red = currentRed * (1 + amount) 
      setRed(pixel,red)
  elif rgbNumber == 2: 
      green = int(currentGreen) * (1 + amount) 
      setGreen(pixel,green)
  elif rgbNumber == 3: 
      blue = int(currentBlue) * (1 + amount) 
      setBlue(pixel,blue)
 show(picture) 
             
#changeColor(picture, -0.10, 1) decreases red by 10%.
#changeColor(picture, 0.30, 2) increases green by 30%.
#changeColor(picture, 0, 3) makes no change.     
   
#2 
def posterize8(picture): 
 for pixel in getPixels(picture): 
  red = getRed(pixel) 
  green = getGreen(pixel)
  blue = getBlue(pixel) 
  if(red<100): 
   setRed(pixel,0) 
  else: 
   setRed(pixel,255) 
  if(green<100): 
   setGreen(pixel,0) 
  else: 
   setGreen(pixel,255) 
  if(blue<100): 
   setBlue(pixel,0) 
  else: 
   setBlue(pixel,255) 
 show(picture) 
   
#>>> picture = makePicture(pickAFile()) 
#>>> posterize8(picture) 

#3 
def pictureborder(picture,color,width): 
 bottom = getHeight(picture)- width 
 left = getWidth(picture) - width 
 for pixel in getPixels(picture): 
  x = getX(pixel) 
  y = getY(pixel) 
  if y < width: 
   setColor(pixel,color) 
  if y > bottom: 
   setColor(pixel,color) 
  if x < width: 
   setColor(pixel,color) 
  if x > left: 
   setColor(pixel,color) 
 show(picture) 
#>>> picture = makePicture(pickAFile())  
#>>> border(picture,black,5)

#4 
def drawXequalsYline(picture, color): 
 for pixel in getPixels(picture):
  x = getX(pixel) 
  y = getY(pixel) 
  if x == y : 
   setColor(pixel,color)  
 show(picture) 
 
#>>> picture = makePicture(pickAFile()) 
#>>> drawXequalsYline(picture,black)  

#5 
def drawQuadrants(picture, color): 
 w = getWidth(picture) 
 h = getHeight(picture)
 for pixel in getPixels(picture): 
  x = getX(pixel) 
  y = getY(pixel) 
  if(x == w/2): 
   setColor(pixel,color) 
  if(y == h/2): 
   setColor(pixel,color) 
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> drawQuadrants(picture,black) 
  
#6 
def drawDiagonalLine2(picture,color):  
  w = getWidth(picture) 
  for pixel in getPixels(picture): 
   x = getX(pixel) 
   y = getY(pixel)
   if x + y == w : 
    setColor(pixel,color) 
  show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> drawDiagonalLine2(picture,black)
    
#7 
def posterize3(picture): 
 for pixel in getPixels(picture): 
  red = getRed(pixel)
  green = getGreen(pixel)
  blue = getBlue(pixel) 
  if(red > 180): 
   setColor(pixel,red) 
  elif(blue > 180): 
   setColor(pixel,blue) 
  elif(green >180): 
   setColor(pixel,green) 
  else: 
   setColor(pixel,black) 
 show(picture)
#>>> picture = makePicture(pickAFile()) 
#>>> posterize3(picture) 

#8 
def pinkify(picture): 
 for pixel in getPixels(picture): 
  red = getRed(pixel) 
  green = getGreen(pixel) 
  blue = getBlue(pixel) 
  if(red>=100 and green >=100 and blue>= 100): 
   setColor(pixel,pink) 
 show(picture)  

#>>> picture = makePicture(pickAFile()) 
#>>> pinkify(picture)

#9 
def downupRed(picture): 
 lefthalf = getWidth(picture)/2 
 for pixel in getPixels(picture): 
  x = getX(pixel) 
  if x < lefthalf: 
   red = getRed(pixel) 
   red = red/2 
   setRed(pixel,red) 
  else: 
   red = getRed(pixel) 
   red = 3 * red 
   setRed(pixel,red) 
  show(picture) 

#>>> picture = makePicture(pickAFile()) 
#>>> downupRed(picture)


#10 
def thirds(picture): 
 topthird = getHeight(picture)/3 
 midthird = 2 * (getHeight(picture)/3) 
 bottomthird = getHeight(picture) 
 for pixel in getPixels(picture): 
  y = getY(pixel) 
  if y < topthird: 
   color = getColor(pixel) 
   setColor(pixel,makeLighter(color)) 
  elif y > topthird and y < midthird: 
   blue = getBlue(pixel) * 0.7 
   green = getGreen(pixel) * 0.7 
   setBlue(pixel,blue) 
   setGreen(pixel,green) 
  else: 
   red = getRed(pixel)
   blue = getBlue(pixel) 
   green = getGreen(pixel) 
   negativeColor = makeColor(255-red, 255-blue , 255-green)
   setColor(pixel,negativeColor) 
 show(picture) 
 
#>>> picture = makePicture(pickAFile()) 
#>>> thirds(picture)
   
   
  