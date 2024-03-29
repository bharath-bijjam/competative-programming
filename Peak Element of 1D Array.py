# Taking input as N 
N = int(input())
# Taking list as The input 
List = list(map(int, input().split(" ")))
# The list will create as [1, 2, -1, 3, 1, 10, 1]
#Taking Empty list to store the peak ELements of 1D Array
Peak_elements=[]
# Now We need to iterate on the loop from index 0 to the last element of the list.
for each in range (0,N):
    # Now we need to consider the edge case .
    # if the element is at zeroth index then we need to check 
    # the 1 st index element is less than zeroth index or not 
    if each == 0 and List[each] > List[each+1]:
        Peak_elements.append(each)
    # Now we need to consider the second edge case which is the last element of the list.
    # if the element is at the end of the index we need to check the 
    # Before element of the last index element .
    # if last element is greater than before element . we need to append it to Peak_elements.
    elif each == N-1 and List[each] > List[N-2] :
        Peak_elements.append(each)
    # Now we need to consider the last edge case in the given problem 
    else:
        if List[each] > List[each-1] and List[each] > List[each+1] :
            Peak_elements.append(each)
            
# As Per the given question if no peak elements are there we need to return -1 
if Peak_elements==[]:
    print("-1")
else:
    # The output is in list . So, we need to unpack the lsit using keyword argument.
    print(*Peak_elements) 
    

       
        
    
