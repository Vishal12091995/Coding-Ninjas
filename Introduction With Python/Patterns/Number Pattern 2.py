'''
Number Pattern 2
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
Input format :
Integer N (Total no. of rows)
Constraints:
1 <= n <= 50
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
1
11
202
3003
40004'''

#Using For Loop
# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         if i>=3:
#             if j==0 or j==i-1:
#                 print(i-1,end='')
#             else:
#                 print(0,end='')
#         else:
#             print(1,end='')

#     print()

#using while Loop

n=int(input())
i=0
while i<=n:
    j=1
    while j<=i:
        if i==1:
            print(1,end='')
        elif j==1 or j==i:
            print(i-1,end='')
        else:
            print(0,end='')
        j+=1
    print()
    i+=1

