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
0000***0000'''

n=int(input())
for i in range(1,n+1):
    for j in range(1,2*n+2):
        if j==i or j==(2*n+2)-i:
            print('*',end='')
        elif j== (2*n+2)//2:
            print('*',end='')
        else:
            print('0',end='')
    print()