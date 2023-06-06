
#--------------------BuBBLE SORT ------------------------------------# 
# Creating the bubble_sort function 
def bubble_sort(arr,N):
    # iterate the loop from zeroth index to the last element of the list .
    for i in range(0,N):
    # Keeping the variable swapped to keep track the boolean value 
        swapped = False
        # use another loop to eliminate the last element of the loop.
        # we already know that for every iteration last element is maximum element.
        #so we are iterating from j to n-i-1
        # here "-i" is used to remove the last element of the list
        for j in range(0,N-i-1):
            # if the value of the jth index is greater than the j+1 th index element 
            #Then we need to swap the two index elements 
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped= True
        # if the value of the swapped is false then we can break the current iteration
        if swapped==False:
            break
    # As the final step we can return the sorted array 
    return arr
                
#----------------------MAIN FUNCTION------------------------------------#
# Taking the input as N 
N= int(input())
# Taking the list as the input .
arr =  list(map(int, input().split(" ")))
# Calling the bubble_sort function to get the sorted array
print(*bubble_sort(arr,N))
