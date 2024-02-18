from fractions import*
from math import *
x=420836439543564503900159637058347368195377088898408
print (', '.join(repr(i) for i in range(2, 101) if gcd(x, i) == 1))
