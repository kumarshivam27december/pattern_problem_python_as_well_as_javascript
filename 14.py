'''Pattern #14: Pyramid Pattern of Alternate Numbers
Pattern:
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
'''


a=5
p=1
for i in range(a):
    for j in range(i+1):
        print(p,end=" ")
    p+=2
    print()