
n,m = input().split()
n = int(n)
m = int(m)
if n%2 != 0 and m==3*n:
    pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))  
