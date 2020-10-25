def conv_to_binary(n):
    result = 0
    base = 1
    while n>0:
        rem = n%10
        result = result+rem*base        
        n = n//10
        base *= 2
    return result
if __name__=='__main__':
    n = int(input())
    print(conv_to_binary(n))
