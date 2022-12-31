'''Pattern #4: Inverted Pyramid of Descending Numbers
Pattern:
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
'''

n=5
p=5
for i in range(n):
    for j in range(n-i):
        print(p,end=" ")
    p-=1
    print()