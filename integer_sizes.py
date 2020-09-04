# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b,c,d=int(input()),int(input()),int(input()),int(input())
if (a>0 and a<=1000) and (b>0 and b<=1000) and (c>0 and c<=1000) and (d>0 and d<=1000):
    print(pow(a,b)+pow(c,d))
