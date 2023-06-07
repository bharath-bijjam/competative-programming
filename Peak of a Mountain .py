#For The given constraints in the question.
# We can use the binary search for the given question.
#---------------------------------------------------------#
# creating a function Peak_of_a_mountain
def Peak_of_a_mountain(arr):
    # keeping low value to the first index of the list
    low=0
    # keeping high value to the last index of the list
    high=len(arr)-1 
    # Now We need to check every time low is less than high or not 
    while low < high:
        mid=(low+high)//2 
        # if the arr[mid] is less than arr[mid+1] then we can set low to mid+1
        if arr[mid] < arr[mid+1]:
            low = mid+1 
        # if arr[mid] > = arr[mid-1] then we can set high to the mid. 
        else:
            high = mid 
    # return the low element to get the peak element of an mountain
    return low
            
#----------------------Main Function ------------------------#
# Taking input as N 
N=int(input())
#Taking input list as arr 
arr = list(map(int,input().split()))
# Calling the function Peak_of_a_mountain
print(Peak_of_a_mountain(arr))
