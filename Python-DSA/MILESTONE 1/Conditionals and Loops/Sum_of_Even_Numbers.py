""" 
Given a number N, print sum of all even numbers from 1 to N.

Input Format :
Integer N

Output Format :
Required Sum 

Sample Input 1 :
 6
 
Sample Output 1 :
12

"""

n = int(input())
sum = 0
for i in range(2,n,2):
    sum += i

print(sum)