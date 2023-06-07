# For This Problem we need to use Binary Search 
# Here you can use iterative or recursive approach.
#----------------------------------------------------
#creating the function BinarySearch to search the element in the given list
def BinarySearch(arr,search_element):
    #keeping low and high to track the useful list.
    low,high = 0, len(arr)-1
    # As per the given question the array is in increasing order
    while low <= high :
        # we use mid value to break the list into half and 
        #decide where the element is present based on conditions 
        mid= (low + high) // 2
        # if the value is present in the middle then we can simply 
        # return the mid value 
        if (arr[mid]== search_element):
            return mid
        # if the mid element in the list is less than search_element
        # then our required search_element will be in right side of list
        elif (arr[mid]<search_element):
            # keeping low to the mid+1 element
            low= mid+1 
        # if not the above two cases then it will be in left side of list 
        else:
            # keeping high to the mid-1 
            high= mid-1
    # if the search_element is Not present in the list we need to return -1 
    return -1
#---------------Main Function ------------------

#Taking the input value as N.
N= int(input())
# Taking the input as the list 
arr = list(map(int, input().split(" ")))
#Taking input for the search element
search_element = int(input())
# Now we are calling the function to search the element in arr.
print(BinarySearch(arr, search_element))
