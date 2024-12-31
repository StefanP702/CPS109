#>>> setMediaPath() 
setMediaPath('C:\\Users\\Stefan\\Desktop\\Python\\mediasources-4ed\\')
jenny = makePicture('jenny-red.jpg')
beach = makePicture('beach.jpg')
waikiki = makePicture('waikiki.jpg')
caterpillar = makePicture('caterpillar.jpg')
statue = makePicture('statue-tower.jpg')
graves = makePicture('graves.jpg')
llama = makePicture('llama.jpg')
eiffel = makePicture('eiffel.jpg')
butterfly1 = makePicture('butterfly1.jpg')
butterfly = makePicture('butterfly.jpg')
katie = makePicture('katie.jpg') 
statueTower = makePicture('statue-tower.jpg') 
moon = makePicture('moon-surface.jpg') 
horse = makePicture('horse.jpg')
house = makePicture('House.jpg')

#1
def addSunset(picture,x1,y1,width,height,startangle,degrees,color): 
 addArcFilled(picture,x1,y1,width,height,startangle,degrees,color) 
 explore(beach)
#>>>addSunset(beach,200,155,90,80,0,170,yellow) 

#2 
def addBullseye(picture,x1,y1,width): 
  pixels = getPixels(picture) 
  for pixel in pixels:  
   x = getX(pixel) 
   y = getY(pixel) 
   distance = math.sqrt((x-x1)**2 + (y-y1)**2) 
   if(width - 8 < distance < width): 
    setColor(pixel,red) 
   elif(width - 18 < distance < width): 
    setColor(pixel,blue) 
   elif(width - 32 < distance < width): 
    setColor(pixel,yellow) 
  explore(caterpillar) 
#>>> addBullseye(caterpillar,160, 100, 30)   


#3 
def addHouse(picture,x1,y1):  
  WidthPoint = 1000 
  HeightPoint = 1000
  canvas = makeEmptyPicture(WidthPoint,HeightPoint)
  for y in range(y1,HeightPoint,138): 
   for x in range(x1,WidthPoint,110):
    addRectFilled(canvas,x,y + 28,100,100,green)  
    addLine(canvas,x,y + 28,x + 49,y,black)
    addLine(canvas,x + 49, y, x + 99, y + 28,black) 
    addRectFilled(canvas,x + 19, y + 37,30,30,yellow)
    addRectFilled(canvas,x + 67, y + 37,30, 30,yellow) 
    addRectFilled(canvas,x + 51, y + 86,30, 40,red)  
  show(canvas) 
#>>> addHouse(llama,0,0)   

  
#4
def grid(picture, step):
  horizontalLines(picture, step)
  verticalLines(picture, step)
  explore(caterpillar) 

def horizontalLines(picture,step): 
  W = getWidth(picture) 
  H = getHeight(picture) 
  for x in range(0,W,1): 
   for y in range(0,H,step): 
    pixel = getPixel(picture,x,y) 
    setColor(pixel,black) 
  

def verticalLines(picture,step): 
 W = getWidth(picture)
 H = getHeight(picture) 
 for x in range(0,W,step): 
   for y in range(0,H,1): 
    pixel = getPixel(picture,x,y) 
    setColor(pixel,black) 

#>>> grid(caterpillar,5) 

#5 
def grawGrid2(picture): 
  canvas = makeEmptyPicture(1000,1000)
  horizontalLines2(canvas)
  verticalLines2(canvas)
  explore(canvas) 

def horizontalLines2(picture): 
  t = 5
  x = 5 
  y = 0 
  cnt = 1
  W = getWidth(picture) 
  H = getHeight(picture) 
  while(x < H): 
   while(y < W): 
    setColor(getPixel(picture,y,x),black) 
    y = y + 1 
   y = 0 
   cnt = cnt + 2 
   x = x + t + 2 * cnt
  
def verticalLines2(picture): 
  t = 5
  x = 5 
  y = 0 
  cnt = 1
  W = getWidth(picture) 
  H = getHeight(picture)
  while(x < W): 
   while(y < H): 
    setColor(getPixel(picture,x,y),black)
    y = y + 1 
   y = 0
   cnt = cnt + 2 
   x = x + t + 2 * cnt
#>>> grawGrid2(caterpillar)    

#6 
def flipHorizontally(picture): 
  W = getWidth(picture)
  H = getHeight(picture)
  flipPoint = W/2
  for x in range(0,flipPoint) : 
    for y in range(0,H) :
     rightPixel = getPixel(picture,x,y) 
     leftPixel = getPixel(picture,W - x - 1,y)
     rightColor = getColor(rightPixel)
     leftColor = getColor(leftPixel) 
     setColor(rightPixel,leftColor)
     setColor(leftPixel,rightColor)
  explore(llama)
#>>> flipHorizontally(llama)  

#7 
def scaleup(picture):
  W = getWidth(picture)
  H = getHeight(picture)
  canvas = makeEmptyPicture(2 * W, 2 * H)
  pixels = getPixels(picture)
  canvaspixels = getPixels(canvas)
  index = 0 
  for pixel1 in pixels:
   pixel2 = canvaspixels[index]
   setColor(pixel2,getColor(pixel1))
   pixel3 = canvaspixels[index + 1]
   setColor(pixel3,getColor(pixel1))
   index = index + 2
  show(canvas)
  return canvas
#>>> scaleup(caterpillar)       

#8  
def scaledown(picture): 
 W = getWidth(picture)  
 H = getHeight(picture)
 canvas = makeEmptyPicture(W/2,H/2)
 for x in range(0,W): 
  for y in range(0,H): 
   pixel1 = getPixel(picture,x,y) 
   pixel2 = getPixel(canvas,x/2,y/2) 
   setColor(pixel2,getColor(pixel1))
 show(canvas)
 
#>>> scaledown(llama)   

#9 
def mirror20(picture): 
  mirrorPoint = 20 
  for y in range(0,getHeight(picture)): 
   for x in range(0,20): 
    leftPixel = getPixel(picture,x,y)
    rightPixel = getPixel(picture,40 - x - 1,y)
    color = getColor(leftPixel)
    setColor(rightPixel,color) 
  show(caterpillar) 
  
#>>> mirror20(caterpillar)   
