"""  
Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
Fibonacci Series is defined by the recurrence
    F(n) = F(n-1) + F(n-2)
where F(0) = 0 and F(1) = 1


Input Format :
Integer N
Output Format :
true or false
Constraints :
0 <= n <= 10^4
Sample Input 1 :
5
Sample Output 1 :
true
Sample Input 2 :
14
Sample Output 2 :
false    

"""
def checkMember(n):
    a=1
    b=1
    s=0
    if(n==0 or n==1):
        return True
    elif n>=2:
        while s<=n:
            s=a+b
            a=b
            b=s
            if(s==n):
                return True

    return False

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")