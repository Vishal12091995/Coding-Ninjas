'''
Code : Triangle Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
22
333
4444
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
22
333
4444
55555
Sample Input 2:
6
Sample Output 2:
1
22
333
4444
55555
666666'''
#Using for loop
# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end='')
#     print()

#Using While Loop
n=int(input())
i=1
while i<=n:
       j=1
       while j<=i:
              print(i,end="")
              j+=1
       print("")
       i+=1
