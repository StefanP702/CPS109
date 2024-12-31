#Quiz5 
#Assuming that X is the width of the picture and Y is the height of the picture. 
#Create a function that takes in a picture as an input and does:
#Make the red brighter by 40% if X<Y
#Otherwise, make the green brighter by 33.3%



def pictureRedorGreen(picture):
  w = getHeight(picture)
  h = getHeight(picture)
  for pixel in getPixels(picture):
   x = getX(pixel)+ w
   y = getY(pixel)+ h
   if(x<y):
     setRed(pixel, getRed(pixel) * 1.4)
   else:
     setGreen(pixel, getGreen(pixel) * 1.3333)
  show(picture)

#>>> picture = makePicture(pickAFile()) 
#>>> pictureRedorGreen(picture)