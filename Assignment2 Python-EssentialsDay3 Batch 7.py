print("question 1 solution")
s=int(input("enter the height from land"))
if s<=1000:
	print("Safe to Land")
elif s>1000 and s<5000:
	print("Bring down to 1000")
elif s>5000:
	print("Turn around!!!")
else:
	print("Keep Flying")
print("__________________________")
print("question 2 solution")
lower = 1 
upper = 200  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 
print("______________________")