'''Pattern #7: Inverted Half Pyramid Number Pattern
Pattern:
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
 
 '''


n=6
for i in range(n):
    p=0
    for j in range(n-i):
        print(p,end=" ")
        p+=1
    print()