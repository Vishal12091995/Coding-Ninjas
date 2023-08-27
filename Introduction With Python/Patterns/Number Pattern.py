'''
Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1234
123
12
1
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
12345
1234
123
12
1
'''
#Using For Loop
# n=int(input())
# for i in range(0,n):
#     k=1
#     for j in range(n,i,-1):
#         print(k,end='')
#         k+=1
#     print()

#Using While Loop
n = int(input())
i=1
while i <= n:
       j=1
       k=1
       while j<=n-i+1:
              print(k,end="")
              j=j+1
              k=k+1
       print()
       i=i+1

