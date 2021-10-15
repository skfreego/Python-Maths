"""
Task:
You are given a complex z. Your task is to convert it to polar coordinates.
Input Format:
A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.
Output Format
Output two lines:
The first line should contain the value of r.
The second line should contain the value of y.
"""
"""
1+2j
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
a=complex(input())
print(abs(a))
print(cmath.phase(a))