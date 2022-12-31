'''Pattern #8: Pyramid of Natural Numbers Less Than 10
Pattern:
1 
2 3 4 
5 6 7 8 9
   
   
   '''
# n=3
# k=10
# p=1
# for i in range(n):
#     for j in range(i+2):
#         print(p,end=" ")
#         p+=1
#     print()



a=5
p=1
for i in range(1,a):
    for j in range(i+2):
        print(p,end=" ")
        p+=1
    print()