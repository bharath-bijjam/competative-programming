#Creating the fibonacci function 
def fibonacci(N):
    # if the user is below two then the value 2 will return
    if N <= 2 :
        return 1 
    else:
        # if the user value is grater than 2 then recursively it will add 
        return fibonacci(N-1) + fibonacci (N-2)

#--------Main Function ------------#        
# Taking input as N 
N= int(input())
# calling the fibonacci function to get Nth fibonacci number
print(fibonacci(N))
