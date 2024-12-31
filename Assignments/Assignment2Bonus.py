# ------------------------------------------------------------
#        Assignment Bonus a2 
#        by Stefan Pribisic 
#        500699080
# --------------------------------------------------------------
setMediaPath('C:\\Users\\Stefan\\Desktop\\Python\\mediasources-4ed\\') 
scene = makePicture('scene.jpg') 
waldo = makePicture('waldo.jpg')
tinyscene = makePicture('tinyscene.jpg')
tinywaldo = makePicture('tinywaldo.jpg')


#1
#1
def compareOneFast(template,searchImage,x1,y1): 
    #Width and Height of template denoted as Width small(Ws) and Height small(Hs)
    Ws = getWidth(template)
    Hs = getHeight(template) 
    #Width and Height of searchImage denoted as Width big(Wb) and Height big(Hb)
    Hb = getHeight(searchImage)
    Wb = getWidth(searchImage)
    sum = 0
    #Limit pixel x1 and y1 position not to get out of searchImage
    if(x1 + Ws > Wb): 
     x1 = Wb - Ws 
    if(y1 + Hs > Hb): 
     y1 = Hb - Hs 
    
    for y in range(y1,y1 + 1): #Scan only one line per waldo frame to get faster
     for x in range(x1,x1 + Ws): 
       #Ps(Pixel small) = pixel of template
       #Pb(Pixel big) = pixel of searchImage
       Ps = getPixel(template,x - x1,y - y1) 
       Pb = getPixel(searchImage,x,y) 
       #Ls = luminance of template
       #Lb = luminance of searchImage 
       Ls = (getRed(Ps) + getGreen(Ps) + getBlue(Ps))/3 
       Lb = (getRed(Pb) + getGreen(Pb) + getBlue(Pb))/3  
       DiffLum = abs(Ls - Lb) 
       sum += DiffLum
    return sum  
    
#2 
def compareAllFast(template,searchImage): 
  #Width and Height of template
  Ws = getWidth(template)
  Hs = getHeight(template) 
  #Width and Height of searchImage
  Hb = getHeight(searchImage)
  Wb = getWidth(searchImage)
  # declare and initialize BIG number to 10000
  matrix = [[10000 for y in range(Hb)] for x in range(Wb)]
  
  for y in range(0,Hb - Hs): 
    for x in range(0,Wb - Ws):   
      matrix [x][y] = compareOneFast(template,searchImage,x,y)
      #debugging info
      #print (x,y,matrix [x][y]) 
  return matrix  
  
#3 
def find2Dmin(matrix): 
 col = 0 
 row = 0 
 for i in range(0,len(matrix)): 
  for j in range(0,len(matrix[i])): 
   if matrix[i][j] < matrix[row][col]: 
    row = i 
    col = j 
 return(row,col) 
#find2Dmin(compareAllFast(tinywaldo,tinyscene))
  
#4 
def displayMatch(searchImage,x1,y1,w1,h1,color): 
  pixels = getPixels(searchImage) 
  for pixel in pixels: 
   x = getX(pixel) 
   y = getY(pixel) 
   if(x1 < x < x1 + w1 and y1 < y < y1 + 3): 
    setColor(pixel,color) 
   if( x1 < x < x1 + w1 and y1 + h1 - 3 < y < y1 + h1): 
    setColor(pixel,color)
   if( x1 < x < x1 + 3 and y1 < y < y1 + h1): 
    setColor(pixel,color)
   if( x1 + w1 - 3 < x < x1 + w1 and y1 < y < y1 + h1): 
    setColor(pixel,color)
  explore(searchImage)   
#>>> displayMatch(tinyscene,54,13,57,110,cyan) 
  
  
#5 
def grayscale(picture): 
 for pixel in getPixels(picture): 
  r = getRed(pixel)
  g = getGreen(pixel)
  b = getBlue(pixel) 
  Luminance = (r + g + b)/3  
  setColor(pixel,makeColor(Luminance,Luminance,Luminance)) 
 explore(picture) 
 
   
#6 
def findWaldo(targetJPG,searchJPG): 
  #Width and Height of targetJPG
  Ws = getWidth(targetJPG)
  Hs = getHeight(targetJPG) 
  matrix = compareAllFast(targetJPG,searchJPG)
  (x1,y1) = find2Dmin(matrix)
  displayMatch(searchJPG,x1,y1,Ws,Hs,cyan) 
 
  
#findWaldo(waldo,scene) 
  
