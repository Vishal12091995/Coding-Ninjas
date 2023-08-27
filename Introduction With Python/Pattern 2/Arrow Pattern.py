'''
Arrow pattern
Send Feedback
Print the following pattern for the given number of rows.
Assume N is always odd.
Note : There is space after every star.
Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
11
Sample Output :
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*
'''

n=int(input())
n1=(n+1)//2
n2=n//2
i=1
while i<=n1:
    space=n2
    while space>=2*i+1:
        print(' ',end='')
        space+=1
    star=1
    while star<=i:
        print('*',end=' ')
        star+=1
    i+=1
    print()
z=1
while z<=n2:
    space=n2+2
    while space>=z:
        print(' ',end='')
        space-=2
    k=n2
    while k>=z:
        print('*',end=' ')
        k-=1
    z+=1
    print()
    
