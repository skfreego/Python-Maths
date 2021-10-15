## Python Math
### HackerRank Challenges
#### Domain:Python
#### Sub Domain:Math


### Polar Coordinates
Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
z = x + yj
A complex number z is completely determined by its real part x and imaginary part y 
Here, j is the imaginary unit.
A polar coordinate (r,theta) is completely determined by modulus r and phase angle theta.
If we convert complex number z to its polar coordinate, we find:
r: Distance from z to origin, i.e., root of (x2 + y2)(squared)
theta: Counter clockwise angle measured from the positive x-axis to the line segment that joins z to the origin.
Python's cmath module provides access to the mathematical functions for complex numbers.
cmath.phase
This tool returns the phase of complex number z(also known as the argument of z).
>>> phase(complex(-1.0, 0.0))
    3.1415926535897931
abs
This tool returns the modulus (absolute value) of complex number z.
>>> abs(complex(-1.0, 0.0))
    1.0

#### Find Angle MBC
ABC is a right triangle, at 90 degree at B.
Therefore, angle ABC = 90 degree
Point M is the midpoint of hypotenuse AC
You are given the lengths AB and  BC.
Your task is to find MBC(angle) in degrees.

#### Triangle Quest 2 
For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321
You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.
Note:
Using anything related to strings will give a score of 0.
Using more than one for-statement will give a score of 0.

#### Mod Divmod
One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing the quotient of a/b first and then the remainder a.
For example:
>>> print divmod(177,10)
	(17, 7)
Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.


#### Power-Mod Power
So far, we have only heard of Python's powers. Now, we will witness them!
Powers or exponents in Python can be calculated using the built-in power function. Call the power function a^b as shown below:
>>> pow(a,b) 
or
>>> a**b
It's also possible to calculate a^b mod m.
>>> pow(a,b,m)  
This is very helpful in computations where you have to print the resultant % mod.
Note: Here, a and b can be floats or negatives, but, if a third argument is present, b cannot be negative.
Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. Frankly speaking, we will never use math.


#### Triangle Quest
You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:
1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.
Note: Using anything related to strings will give a score of 0.


#### Integer Come In All Sizes
Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: 2^31-1 (c++ int) or 2^63-1 (C++ long long int).
As we know, the result of a^b grows really fast with increasing b.
Let's do some calculations on very large integers.
