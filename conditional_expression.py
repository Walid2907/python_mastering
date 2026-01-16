# conditional expression is an one line shortcut for the if statement 
# it's also called ternary operator 
# syntaxe is : X if (condition) else Y
#example :
age = int(input("entre your age: "))

print("you're old enough" if age > 18 else "you're not old enough")
#in this example after u entre ur age it should print you're old enough if ur age is bigger than 18
# and prints you're not old enough if ur age is less than 18
#we can do the same in a ariable to assign a value to it 
#example
old_enough = True if age > 18 else False
print(old_enough)