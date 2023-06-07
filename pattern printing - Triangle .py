# Taking the input value as N 
N=int(input())
#Using spaces to track How many spaces is needed for the specific iteration.
spaces =N-1
# Using stars with starting 1 .
stars=1
# iterating N times to print the stars.
for i in range(N):
    Needed_stars ="*" * stars
    Needed_spaces = " " * spaces
    # concatinating the Needed_spaces and Needed_stars
    print(Needed_spaces+Needed_stars)
    # keep on updating the stars and spaces based on the given problem
    spaces = spaces - 1 
    stars = stars + 2
    
