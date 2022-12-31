'''Pattern #17: Downward Triangle Pattern of Stars
Pattern:
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
 '''



# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(n-i-1):
#         print("*",end=" ")   
#     print()


# n=7
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
    
    

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")