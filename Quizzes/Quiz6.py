def sumMatrix(matrix):
  output = []
  for row in matrix:
    total = 0
    for item in row:
     total += item
    output.append(total)
  return output

#>>> matrix = [[8,3,4], [4,0,6] , [7,8,1]]
#>>> sumMatrix(matrix)
#[15, 10, 16] 

# The append() method takes a single item and adds it to the end of the list.