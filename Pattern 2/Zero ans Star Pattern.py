'''
Zeros and Stars Pattern
Send Feedback
Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000
Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Sample Input 1 :
3
Sample Output 1 :
*00*00*
0*0*0*0
00***00
Sample Input 2 :
5
Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
'''

n=int(input())
row=2*n+1
i=1
while i<=n:
    j=1
    while j<=row:
        if(j==i or j==(row+1)//2 or j==row-i+1):
            print("*",end='')
        else:
            print(0,end='')
        j+=1
    print()
    i+=1