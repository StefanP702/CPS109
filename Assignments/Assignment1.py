#Assignment 1 

#1
def removeRed(picture): 
 for pixel in getPixels(picture): 
   newRed = getRed(pixel) 
   setRed(pixel, newRed * 0) 
 show(picture) 
#>>> picture = makePicture(pickAFile())  
#>>> removeRed(picture)


#2 
def removeBlue(picture): 
 for pixel in getPixels(picture): 
  newBlue = getBlue(pixel) 
  setBlue(pixel, newBlue * 0) 
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> removeBlue(picture) 


#3 
def removeGreen(picture): 
 for pixel in getPixels(picture): 
  newGreen = getGreen(pixel) 
  setGreen(pixel, newGreen * 0) 
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> removeGreen(picture) 


#4
def makePicBlack(picture): 
 for pixel in getPixels(picture): 
   setRed(pixel, 0) 
   setBlue(pixel, 0) 
   setGreen(pixel, 0) 
 show(picture)  
#>>> picture = makePicture(pickAFile()) 
#>>> makePicBlack(picture) 


#5 
def makePicWhite(picture): 
 for pixel in getPixels(picture): 
   setRed(pixel, 250) 
   setBlue(pixel, 250) 
   setGreen(pixel, 250) 
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> makePicWhite(picture)  

#6
def addBox(picture): 
 pixels = getPixels(picture) 
 for pixel in pixels: 
  x = getX(pixel) 
  y = getY(pixel) 
  if 160< x < 220 and 150 < y < 180: 
   setColor(pixel,red) 
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> addBox(picture)  


#7 
def addCircle(picture, xc, yc, radius, color): 
 pixels = getPixels(picture) 
 for pixel in pixels: 
  x = getX(pixel) 
  y = getY(pixel) 
  distance = math.sqrt((x-xc)**2 + (y-yc)**2) 
  if distance < radius: 
    setColor(pixel,color) 
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> addCircle(picture,200, 100, 30 , blue) 


#8
def addLine(picture,x1,y1,x2,y2): 
 pixels = getPixels(picture) 
 m = 1.0*(y2 - y1)/(x2-x1) 
 b = y1 - m * x1 
 for pixel in pixels: 
  x = getX(pixel) 
  y = getY(pixel) 
  y_line = m * x + b 
  if y == y_line: 
   setColor(pixel,green) 
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> addLine(picture,100,100,300,300) 


#9
def addLine2(picture, x1, y1, x2, y2, thickness, color): 
 pixels = getPixels(picture) 
 m = 1.0 *(y2-y1)/(x2-x1) 
 b = y1 - m * x1 
 for pixel in pixels: 
  x = getX(pixel) 
  y = getY(pixel) 
  y_line = m * x + b 
  distance = int(abs(y_line - y) + 0.5) 
  if distance < thickness / 2: 
   setColor(pixel,color) 
 show(picture) 
#>>> picture = makePicture(pickAFile())  
#>>> addLine2(picture,100,100,300,300,2 ,blue) 
 
#10 
def swappingColor(picture): 
 for pixel in getPixels(picture): 
   red = getGreen(pixel)  
   green = getRed(pixel)
   setRed(pixel,red) 
   setGreen(pixel,green)  
 show(picture) 

#>>> picture = makePicture(pickAFile()) 
#>>> swappingColor(picture)  

#11 
def pictureParameter(picture,n): 
 for pixel in getPixels(picture): 
  red = getRed(pixel)
  blue = getBlue(pixel)
  green = getGreen(pixel)
  setRed(pixel, red - n) 
  setBlue(pixel,blue - n) 
  setGreen(pixel,green - n)
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> pictureParameter(picture,4)  

#12 
def pictureParameter2(picture,n): 
 for pixel in getPixels(picture): 
  newRed = getRed(pixel) 
  setRed(pixel, newRed * n) 
 show(picture) 
#>>> picture = makePicture(pickAFile())  
#>>> pictureParameter2(picture,50)  

#13 
def pictureParameter3(picture,n): 
 for pixel in getPixels(picture): 
  newBlue = getBlue(pixel) 
  setBlue(pixel, newBlue + n) 
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> pictureParameter3(picture,50)  

#14 
def grayScaleWeights(picture,n1,n2,n3): 
 for pixel in getPixels(picture): 
  red = getRed(pixel)* n1
  green = getGreen(pixel) * n2
  blue = getBlue(pixel)* n3 
  luminance = red + green + blue 
  setColor(pixel,makeColor(luminance,luminance,luminance)) 
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> grayScaleWeights(picture,0.299,0.587,0.114)   

#15 
def IncreaseGreenIndex(picture,n): 
  pixels = getPixels(picture)
  for index in range(0,len(pixels)): 
   pixel = pixels[index] 
   newGreen = getGreen(pixel) 
   setGreen(pixel, newGreen * n) 
  show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> IncreaseGreenIndex(picture,40)  

#16
def addCircle2(picture, xc, yc, radius, color): 
 pixels = getPixels(picture) 
 for pixel in pixels: 
  x = getX(pixel) 
  y = getY(pixel) 
  distance = math.sqrt((x-xc)**2 + (y-yc)**2) 
  if (radius - 5 < distance < radius): 
    setColor(pixel,color) 
 show(picture)  
#>>> picture = makePicture(pickAFile()) 
#>>> addCircle2(picture,200, 100, 30 , yellow) 
 
 
#17 
def addCircle3(picture, xc, yc, radius, circleThickness,color): 
 pixels = getPixels(picture)
 for pixel in pixels: 
  x = getX(pixel) 
  y = getY(pixel) 
  distance = math.sqrt((x-xc)**2 + (y-yc)**2)
  if (radius - circleThickness < distance < radius): 
   setColor(pixel,color) 
 show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> addCircle3(picture,200, 100, 30, 10 ,yellow)  

  
#18 
def rectangleFrame(picture,xc,yc,length,width,thick,color): 
 pixels = getPixels(picture) 
 for pixel in pixels: 
  x = getX(pixel) 
  y = getY(pixel) 
  if (xc < x < xc+ length and yc < y < yc + thick): 
   setColor(pixel,color) 
  if( xc < x < xc + length and yc + width - thick < y < yc + width): 
   setColor(pixel,color)
  if( xc < x < xc + thick and  yc < y < yc + width): 
   setColor(pixel,color)
  if( xc + length - thick < x < xc + length and yc < y < yc + width): 
   setColor(pixel,color)
 show(picture) 
#>>> rectangleFrame(picture,200, 120, 120, 250,20,yellow) 

#19
def drawTriangle(picture,xc,yc,a,color): 
 pixels = getPixels(picture) 
 for pixel in pixels: 
  x = getX(pixel) 
  y = getY(pixel) 
  if (xc -(y - yc)* tan(pi/6) < x < xc + (y- yc)*tan(pi/6) and y <= yc + a/2):
   setColor(pixel,color) 
 show(picture) 

#>>> drawTriangle(picture,400,200,500,green)  

#20 
def drawTriangleFrame(picture,xc,yc,a,thick,color): 
  pixels = getPixels(picture) 
  for pixel in pixels: 
   x = getX(pixel) 
   y = getY(pixel)  
   if((xc -(y - yc)* tan(pi/6) < x < (xc - (y- yc)*tan(pi/6) + thick) or (xc +(y - yc)* tan(pi/6) - thick) < x < xc + (y- yc)*tan(pi/6)) and  yc<y<(yc+a*math.sqrt(3)/2) ):
     setColor(pixel,color) 
  
   if(xc -(y - yc)* tan(pi/6) < x < xc + (y - yc)*tan(pi/6) and  yc + a * math.sqrt(3)/2 -thick < y < yc + a * math.sqrt(3)/2 ):
     setColor(pixel,color)

  show(picture) 
#>>> picture = makePicture(pickAFile()) 
#>>> drawTriangleFrame(picture,200,200,100,7,green)  