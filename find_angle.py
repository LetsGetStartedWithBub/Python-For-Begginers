# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

a = int(input())
b = int(input())

if (a>0 and a<=100 and b>0 and b <=100) :
    c = math.hypot(a,b)

d=round(math.degrees(math.acos(b/c)))
degree=chr(176)
print(d,degree,sep='')
