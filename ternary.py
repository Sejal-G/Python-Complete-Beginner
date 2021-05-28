#Ternary operators are also selectors just like if-else

#Convert if-else to Ternary

age=input("Input your age")
if age>=18:
  print("Can vote")
else:
  print("Cannot vote")
  
#Ternary
age>=18 ? print("Can vote") : print("Cannot vote")
 

'''ASSIGNMENT QUESTIONS:
1. Print "Learning DL" if age is greater than 15 but less than 18, print "DL" if age is above 18, and print "Not eligible" if age is less than or equal to 15.
2. Print pass if marks greater than 40% and print fail otherwise.
3. Print Grade A if marks > 90%, Grade B if marks > 80%, and Grade C if marks >70%
4. Print Grade A if marks > 90%, Grade B if marks > 80%, and Grade C if marks >70% and print D if marks>60%
5. Print Grade A if marks > 90%, Grade B if marks > 80% and marks<60%, Grade C if marks<60% and marks>40%
6. Print Grade A if marks > 90%, Grade B if marks > 80% and marks<60%, Grade C if marks<60% and marks>40% else print fail.
'''
  
  
