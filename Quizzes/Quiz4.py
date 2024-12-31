#1 
#find max number in an array of lists 
def find_max(numbers): 
 max = numbers[0] 
 for item in numbers: 
  if item > max: 
   max = item 
 return max 
  
#>>> find_max([1,2,44,5,60])
#          60
#>>> find_max([3,6,29,5,45,2])
#          45
#>>> find_max([-3,6,29,5,45,2])
#          45
#>>> find_max([-3,-6,-29,-5,-45,-2])
#          -2 

#2
#sum of numbers from a list 
def sumOfNum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
    print sum 

#>>> sumOfNum([-2,3,4,5]) 
#      10
#>>> sumOfNum([-2,3,4,6]) 
#      11
#>>> sumOfNum([-2,3,4,4])
#      9    

#3
#prints out string symbol n by n grid 
def grid(n):
    for i in range(n):
        for j in range(n):
            if(i+j == n-1 or i==j):
                print("X"),
            else:
                print("0"),
        print 
# prints out string symbol n by n grid 
#>>> grid(5) 
#>>> grid(5) 
#>>> X 0 0 0 X
#>>> 0 X 0 X 0
#>>> 0 0 X 0 0
#>> >0 X 0 X 0

#4 
#This program offset the pixel 
def pixel_offset(n): 
 file = 'C:\\Users\\Stefan\\Desktop\\Python\\mediasources-4ed\\beach.jpg'
 picture = makePicture(file)
 for pixel in getPixels(picture): 
  value = getRed(pixel) 
  setRed(pixel, value + n) 
  value= getBlue(pixel)
  setBlue(pixel, value + n) 
  value = getGreen(pixel) 
  setGreen(pixel, value + n) 
 explore(picture) 
 
