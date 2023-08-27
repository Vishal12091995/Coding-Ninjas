6
'''
Pyramid Number Pattern
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
    1
   212
  32123
 4321234
543212345
'''

n=int(input())
i=1
while i<=n:
    space=n
    while space>i:
        print(' ',end='')
        space-=1
    j=1
    n1=i
    while j<=i:
        print(n1,end='')
        j+=1
        n1-=1
    k=1
    n2=2
    while k<=i-1:
        print(n2,end='')
        k+=1
        n2+=1
    print()
    i+=1
