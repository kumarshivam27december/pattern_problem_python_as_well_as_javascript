'''Pattern #5: Inverted Pyramid of the Same Digit
Pattern:
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
 '''
 
 
n=5
for i in range(n):
    for j in range(n-i):
        print(5,end=" ")
    print()