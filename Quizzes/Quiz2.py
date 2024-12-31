def add_numbers(numbers, sign):
  Total = 0
  for num in numbers:
    Value = int(num)
    Total += Value
  if sign == "-":
      Total = Total * -1
  print(Total)
  
  
#Python homework question. Create a function that takes two strings as parameters. 
#First string should contain a sequence of numbers (e.g. ???1234???) and the second string should be either ???+??? or ???-??? denoting whether the numbers should be positive or negative. 
#Your function should add all individual numbers (applying the sign first) within the first string and give us the output. 
#Here???s the skeleton code for you start with: 

#Def add_numbers(numbers, sign): 
	#Total = 0 
	#For num in numbers: 
		#Value = int(num)  
                        #???.. you do the rest 
		
                        #print total 

#example: add_numbers(???1234???, ???+???)should result in: 10 
#example: add_numbers(???123???, ???-???)should result in: - 6
 