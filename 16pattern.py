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
n=6
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):   # decrease range from i+1 - 1 =  i
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()