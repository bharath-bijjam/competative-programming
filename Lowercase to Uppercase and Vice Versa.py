
# Taking string as input 
String = input()
# Using viceversa variable to track the changed 
viceversa = ""
#Using The for loop to iterate every charecter on input
for each in String:
    #if the charecter is in lower case then we will change it into upper by using upper() string method.
    if each== each.lower():
        viceversa+=each.upper()
    # if the charecter is in uppercase then we will change it into lower by using lower() string method.
    else:
        viceversa+=each.lower()
# The last statement is used to print the output string.        
print(viceversa)
        
