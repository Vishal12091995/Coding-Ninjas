'''
Code : Reverse Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
21
321
4321
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
1
21
321
4321
54321
Sample Input 2:
6
Sample Output 2:
1
21
321
4321
54321
654321'''

# Using for loop

# n=int(input())
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()

#using While loop
n=int(input())
i=1
while i<=n:
    j=1
    p=i
    while j<=i:
        print(p,end="")
        j+=1
        p-=1
    print("")
    i+=1
