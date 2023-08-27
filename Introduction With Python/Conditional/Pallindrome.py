'''
Palindrome number
Send Feedback
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
Sample Input 1 :
121
Sample Output 1 :
true
Sample Input 2 :
1032
Sample Output 2 :
false'''

n=int(input())
temp=n
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp==rev):
    print("true")
else:
    print("false")