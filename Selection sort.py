#-------------SELECTION-SORT-----------------------------#
# Creating the selection sort function
def selection_sort(arr,N):
    # iterating the loop from the first index of the list 
    for i in range(0,N):
        # Setting the minimum index to the i . . i.e 0,1,2,3....N-1
        min_index=i
        # iterate from i+1 to N-1 
        # Suppose if i is 1 we need to iterate from i+1 = 2 ...N-1.
        for j in range(i+1,N):
            # check the condition if element in the minimum index is greater than arr[j]
            if arr[min_index] > arr[j]:
                # If the condition is satisfied then we need to update minimum index to j
                min_index =j
        # Swap Both minimum index and arr[i]
        arr[i],arr[min_index] = arr[min_index],arr[i]
    # As the final step we need to return the sorted array.
    return arr

#-----------------MAIN FUNCTION -------------------------#
#Taking the  number of values in the list as a input 
N = int(input())
# Taking the whole list as the array 
arr = list(map(int,input().split(" ")))
# calling the selection sort function 
print(*selection_sort(arr,N))
