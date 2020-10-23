def calculate_cord(s):
    c = 'R'
    x = 0
    y = 0
    distance = 10
    for i in range(s):
        if c=='R':
            x += distance
            distance += 10
            c = 'U'
        elif c=='U':
            y += distance
            distance += 10
            c = 'L'
        
        elif c=='L':
            x -= distance
            distance += 10
            c = 'D'
            
        elif c=='D':
            y-=distance
            distance += 10
            c = 'A'
        elif c=='A':
            x += distance
            distance += 10
            c ='R'
    return x,y
if __name__ == '__main__':
    s = int(input())
    x,y = calculate_cord(s)
    print x , y

