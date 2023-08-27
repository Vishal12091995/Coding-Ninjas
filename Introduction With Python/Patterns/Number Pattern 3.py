'''
Number Pattern 3
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
121
1221
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
1
11
121
1221
12221'''

# Using for Loop
# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         if j==0 or j==i-1:
#             print(1,end='')
#         else:
#             print(2,end='')
#     print()

#USing while Loop

n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        if i==1:
            print(1,end='')
        elif j==i or j==1:
            print(1,end='')
        else:
            print(2,end='')
        j+=1
    print()
    i+=1