if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    count=0
    average=0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for key in student_marks.keys():
        if key==query_name:
            value=student_marks[key]
            for j in value:
                count+=1
                average += j
    
    print("{:.2f}".format(average/count))
           
