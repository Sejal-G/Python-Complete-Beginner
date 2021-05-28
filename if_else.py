#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of 6 to 20, print Weird
#If  is even and greater than 20, print Not Weird




if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2 == 1: #ODD NUMBER
        print("WIERD")
    elif n<=5 and n>=2:   #NO NEED TO CHECK FOR EVEN NUMBER BECAUSE FOR ODD ALREADY CHECKED
        print("Not Wierd")
    elif n>=6 and n<=20:
        print("Wierd")
    else:
        print("Not Wierd")
      

      
