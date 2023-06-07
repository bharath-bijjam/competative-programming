# This problem can be solved by usng binary search 
# Creating find_small_and_large function 
def find_small_and_large(arr,N):
    # initially keep the low to zero 
    low=0
    # initially keep the high to N-1 
    high =N-1 
    # We need to use a extra variable say find_index keep Zero at present 
    find_index = 0 
    while low <= high :
        # finding the mid element 
        mid=(low+high)//2
        # if the value at the mid is less than the last element then
        # we can say that minimun element can be found in left side of the list
        if arr[mid] <= arr[N-1]:
            find_index=mid 
            high=mid - 1 
        else:
            low=mid+1
    # return the find_index 
    return find_index


#----------------------MAIN FUNCTION -------------------------#
# Taking the input value as N 
N = int(input())
# Taking the list as the input 
arr = list(map(int,input().split(" ")))
# calling the function find_small_and_large by passing arr and N as parameters 
index=find_small_and_large(arr,N)
# if the returned value of the index is zero then we can the list is in  ascending order
if index==0:
    print(arr[0],arr[N-1])
else:
    # if element is other than zero then we can say it as minimun element 
    # Before the minimun element is the maximum element
    print(arr[index],arr[index-1])
