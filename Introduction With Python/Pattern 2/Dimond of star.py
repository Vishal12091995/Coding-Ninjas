'''
Code : Diamond of stars
Send Feedback
Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5



The dots represent spaces.



Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *
Sample Input 2:
3
Sample Output 2:
  *
 ***
 '''

n=int(input())
n1=(n+1)//2
n2=n1-1
i=1
while i<=n1:
    sp=1
    while sp<=n1-i:
        print(' ',end='')
        sp+=1
    star=1
    while star<=2*i-1:
            print('*',end='')
            star+=1
    print()
    i+=1
i=n2
while i>=1:
    sp=n2
    while sp>=i:
        print(' ',end='')
        sp-=1
    star=1
    while star<=(2*i)-1:
        print('*',end='')
        star+=1
    print()
    i-=1



