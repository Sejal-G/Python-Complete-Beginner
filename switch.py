'''
Unlike most programming languages, Python doesn’t have a built-in implementation of a switch statement. 
In general, a switch statement is to evaluate an expression or a variable against a list of values to check for equality. 
When the case matches the evaluation result or the variable, the corresponding operations will run under that case. 
When no case is found, the default operations will run instead.
'''

#Print first letter of alphabet <- 'a'
#Print Python <- 'p'
#Print Last letter of alphabet <- 'z'

switcher = {
  "a": "Print first letter of alphabet",
  "p": "Print Python",
  "z": "Last letter of alphabet"
}

if __name__ == "__main__":
  character=input("Input a letter")
  print(switcher.get(character, "Invalid Letter"))
