""" 
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to return the answer.
Do this recursively.
Input format :
Two integers x and n (separated by space)
Output Format :
x^n (i.e. x raise to the power n)
Constraints :
0 <= x <= 30
0 <= n <= 30
Sample Input 1 :
 3 4
Sample Output 1 :
81
Sample Input 2 :
 2 5
Sample Output 2 :
32

"""
#Power of a number

def power(x,n):
    
    if n==0:
        return 1
    
    if n==1:
        return x
    helper = power(x, n//2)
    
    if n%2==0:
        return helper*helper
    else:
        return x*helper*helper
    
    
    
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))