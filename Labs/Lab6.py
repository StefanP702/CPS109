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

#1 
def blueAndGold(picture): 
  H = getHeight(picture)
  W = getWidth(picture)
  gold = makeColor(255,215,0) 
  for pixel in getPixels(picture): 
   y = getY(pixel) 
   if y < 10 or y > H - 1 - 10: 
    setColor(pixel,blue) 
   x = getX(pixel) 
   if x < 10 or x > W - 1 - 10: 
    setColor(pixel,gold) 
  show(llama)
#>>>blueAndGold(llama) 

#2
def purpleTeeth(picture): 
 purple = makeColor(128,0,128) 
 #The white teeth in the katie photo has these rgb values
 white = makeColor(151,127,99) 
 for pixel in getPixels(picture): 
  x = getX(pixel)
  y = getY(pixel) 
  if 184 < x <217 and 183 < y < 191:  
    color = getColor(pixel) 
    if distance(color,white)< 50:     
     setColor(pixel,purple) 
 show(katie) 
#>>>purpleTeeth(katie)  
 
#3 
def checkLuminance(r,g,b): 
 for pixel in getPixels(picture):
   luminance = (r + g + b)/3
   if(luminance < 10): 
     print "Thats going to be awfully dark" 
   elif(50<= luminance <= 200):  
     print "Looks like a good range"  
   elif(luminance > 250): 
     print "Thats nearly white" 
   return 
#>>> checkLuminance(255,250,248) 
      
#4 
def chromakeyBlueAbove(picture, background, skyY):  
  for pixel in getPixels(picture): 
   x = getX(pixel)
   y = getY(pixel) 
   if (getRed(pixel) + getGreen(pixel)< getBlue(pixel) + 100) and y < skyY: 
    backgroundPixel = getPixel(background,x,y) 
    backgroundColor = getColor(backgroundPixel) 
    setColor(pixel,backgroundColor)  
  show(statueTower) 

#>>> chromakeyBlueAbove(statueTower,moon,200)       


   
#5 
def interleave(picture1,picture2): 
  toggle = false
  canvas = makeEmptyPicture(getWidth(picture1),getHeight(picture1))
  for x in range(0,getWidth(picture1)): 
   if x % 20 == 0 : 
    if toggle : 
     toggle = false 
    else: 
     toggle = true  
   if toggle: 
    for y in range(0,getHeight(picture2)): 
     setColor(getPixel(canvas,x,y),getColor(getPixel(picture1,x,y)))
   else: 
    for y in range(0,getHeight(picture2)): 
     setColor(getPixel(canvas,x,y),getColor(getPixel(picture2,x,y)))
  show(canvas) 
#>>> interleave(llama,eiffel)

#6 
def getRegion(picture, x1, y1, x2, y2) :
  (W, H) = (getWidth(picture), getHeight(picture))
  canvas = makeEmptyPicture(x2 - x1, y2 - y1)
  u0 = 0
  v0 = 0
  u = u0
  for x in range(x1, x2) :
    v = v0
    for y in range(y1, y2) :
      pixel1 = getPixel(picture, x, y)
      pixel2 = getPixel(canvas, u, v)
      setColor(pixel2, getColor(pixel1))
      v = v + 1
    u = u + 1
  show(canvas)     
  #>>> show(caterpillar) 
  #>>> >>> caterpillar1 = getRegion(caterpillar,25,4,96,60)
  #>>> explore(caterpillar1)
 
#7 
def getRegion2(picture,x1,y1,x2,y2): 
  newW = x2 - x1 
  H = (y2 - y1) 
  newH = H * 2
  nX = 0 
  nY = 0 
  canvas = makeEmptyPicture(newW,newH) 
  for x in range(x1,x2): 
   for y in range(y1,y2): 
    color = getColor(getPixel(picture,x,y))
    setColor(getPixel(canvas,nX,nY),color) 
    setColor(getPixel(canvas,nX,nY + H),color) 
    nY += 1 
   nY = 0
   nX += 1 
  show(canvas) 
#>>>getRegion2(caterpillar,25,4,96,60)
   
    
 