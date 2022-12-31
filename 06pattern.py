'''
Pattern #6: Reverse Pyramid of Numbers
Pattern:
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
'''

# n=5
# for i in range(n):
#     p=5
#     for j in range(i+1):
#         print(p+1,end=" ")
#         p-=1
#     print()

# n=5
# k=5
# for i in range(n):
#     p=1
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()
n=5
for i in range(n):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print()