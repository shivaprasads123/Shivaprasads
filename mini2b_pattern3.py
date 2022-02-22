#problem2_pattern3
N = int(input("enter the number of rows: "))
for row in range(0,N):
     for col in range(0,N):
         if col == N-1 or row == 0 or col == row:
            print("*",end=" ")
         else:
             print(" ",end=" ")
     print()