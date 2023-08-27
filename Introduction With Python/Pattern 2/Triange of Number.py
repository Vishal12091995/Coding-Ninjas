'''
Code : Triangle of Numbers
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4



The dots represent spaces.



Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
           1
         232
       34543
     4567654
   567898765
Sample Input 2:
4
Sample Output 2:
           1
         232
       34543
     4567654
     '''

n=int(input())
i=1
while i<=n:
    space=1
    while space<=n-i:
        print(" ",end="")
        space+=1
    j=1
    num=i
    while j<=i:
        print(num,end="")
        j+=1
        num+=1
    k=1
    num2=2*i-2
    while k<=i-1:
        print(num2,end="")
        k+=1
        num2-=1
    print()
    i+=1