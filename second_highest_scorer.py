if __name__ == '__main__':
    list_of_students=[]
    list_of_scores=[]
    
    #taking input and storing in nested loop
    for i in range(int(input())):
        name = input()
        score = float(input())
        list_of_students.append([name,score])
        list_of_scores.append(score)
    

    list_of_students.sort(key=lambda x: (x[1],x[0]))
    names = [i[0] for i in list_of_students]
    marks = [i[1] for i in list_of_students]
    min_val=min(marks)
    while marks[0]==min_val:
        marks.remove(marks[0])
        names.remove(names[0])    
    for x in range(0,len(marks)):
        if marks[x]==min(marks):
            print(names[x])         


        
