"""
Input Format:- A single line containing integer, N.
Output Format:- Print N-1 lines as explained above.
"""

"""
5
"""

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i)//9)*i)