""" 
For a given two-dimensional integer array/list of size (N x M),
you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.
Note :
If there are more than one rows/columns with maximum sum, consider the row/column that comes first. 
And if ith row and jth column has the same largest sum, consider the ith row as answer.
Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. 
They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

Second line onwards, the next 'N' lines or rows represent the ith row values.

Each of the ith row constitutes 'M' column values separated by a single space.
Output Format :
For each test case, If row sum is maximum, then print: "row" <row_index> <row_sum>
OR
If column sum is maximum, then print: "column" <col_index> <col_sum>
It will be printed in a single line separated by a single space between each piece of information.

Output for every test case will be printed in a seperate line.
 Consider :
If there doesn't exist a sum at all then print "row 0 -2147483648", where -2147483648 or -2^31 is the smallest value for the range of Integer.
Constraints :
1 <= t <= 10^2
1 <= N <= 10^3
1 <= M <= 10^3
Time Limit: 1sec


"""
'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    MIN_VALUE= -2147483648
    max_sumc=-1
    max_inc=-1
    max_sumr=-1
    max_inr=-1
    for i in range(mCols):
        sumc=0
        for ele in arr:
            sumc+=ele[i]
        
        if sumc>max_sumc:
            max_sumc=sumc
            max_inc=i
    
    for i in range(nRows):
        sumr=0
        for j in range(mCols):
            sumr+=arr[i][j]
        
        if sumr>max_sumr:
            max_sumr=sumr
            max_inr=i

    if nRows==0 and mCols==0:
        print("row 0"+" "+str(MIN_VALUE))

    elif max_sumr>=max_sumc:
        print("row"+" "+str(max_inr)+" "+str(max_sumr))
    elif max_sumr<max_sumc:
        print("column"+" "+str(max_inc)+" "+str(max_sumc))