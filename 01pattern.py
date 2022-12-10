'''Pattern #1: Simple Number Triangle Pattern
Pattern:
1  
2 2  
3 3 3  
4 4 4 4  
'''


n = 4
for i in range(n+1):
    for j in range(1, i+1):
        print(i, end=' ')
    print()