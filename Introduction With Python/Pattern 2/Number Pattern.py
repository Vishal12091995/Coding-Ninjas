'''
Number Pattern
Send Feedback
Print the following pattern for n number of rows.
Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1
For eg. N = 5 

Sample Input 1 :
5
Sample Output 1 :
1        1
12      21 
123    321
1234  4321
1234554321
'''
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j+=1
    space=1
    while space <=2*n-2*i:
        print(' ',end='')
        space+=1
    k=i
    z=1
    while z<=i:
        print(k,end='')
        k-=1
        z+=1
    i+=1
    print()
    
