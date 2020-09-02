if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    a=max(arr)
    b= set(arr)
    b.remove(a)
    c=max(b)
    if(c<a):
        print(c)
