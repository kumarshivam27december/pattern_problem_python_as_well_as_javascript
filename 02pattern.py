'''
Pattern #2: Inverted Pyramid of Numbers
Pattern:
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

'''

n=5
for i in range(n+1):
    for j in range(n-i):
        print(i+1,end=" ")
    print()


