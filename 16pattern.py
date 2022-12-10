'''
Pattern #16: Equilateral Triangle with Stars (Asterisk Symbol)
Pattern:
      *   
     * *   
    * * *   
   * * * *   
  * * * * *   
 * * * * * *   
* * * * * * *
 


'''
# print("             *             ")
# n=6
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):   # decrease range from i+1 - 1 =  i
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
    
    
    


# # print("             *             ")
# n=6
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):   # decrease range from i+1 - 1 =  i
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
    # print()
    
    
    
    
    
# n=int(input("Enter your number which need to print: "))
n=7
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()