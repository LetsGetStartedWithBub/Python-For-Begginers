#python 2
import string
def print_rangoli(size):
    # your code goes here
    s = size
    p = string.ascii_lowercase
    w = len('-'.join(p[size-1:0:-1]+p[0:size]))

    for i in range(1,size):
        n = '-'.join(p[size-1:size-i:-1]+p[size-i:size]).center(w,'-')
        print n
    
    for i in range(size,0,-1):
        n = '-'.join(p[size-1:size-i:-1]+p[size-i:size]).center(w,'-')
        print n

if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
