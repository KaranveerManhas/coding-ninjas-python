""" 
Print the following pattern for the given N number of rows.

Pattern for N = 4
4444
4444
4444
4444

Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Constraints
0 <= N <= 50

Sample Input 1:
7

Sample Output 1:
7777777
7777777
7777777
7777777
7777777
7777777
7777777

Sample Input 1:
6

Sample Output 1:
666666
666666
666666
666666
666666
666666

"""
## Read input as specified in the question
## Print the required output in given format
N=int(input())
i=1
while i<=N:
    j=1
    while j<=N:
        print(N, end='')
        j=j+1
       
    print()
    i=i+1