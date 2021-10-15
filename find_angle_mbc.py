"""
Input Format:
The first line contains the length of side AB.
The second line contains the length of side BC.
Output Format:
Output angle MBC in degrees.
"""

"""
10
10
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab=int(input())
bc=int(input())

ca=math.hypot(ab,bc)
mc=ca/2
bca=math.asin(1*ab/ca)
bm=math.sqrt((bc**2+mc**2)-(2*bc*mc*math.cos(bca)))
mbc=math.asin(math.sin(bca)*mc/bm)

print(int(round(math.degrees(mbc),0)),'\u00B0',sep='')