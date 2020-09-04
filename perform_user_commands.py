if __name__ == '__main__':
    N = int(input())
    arr_of_commands=[]
    required_list=[]
    for i in range(N):
        arr=input().split()
        arr_of_commands.append(arr)

    for i in arr_of_commands:
        for j in range(len(i)):
            if j==0:
                if i[j] == "insert":
                    i[1]=int(i[1])
                    i[2]=int(i[2])
                    required_list.insert(i[1],i[2])
                elif i[j] == "print":
                    print(required_list)
                elif i[j] == "remove":
                    i[1]=int(i[1])
                    required_list.remove(i[1])
                elif i[j] == "append":
                    i[1]=int(i[1])
                    required_list.append(i[1])
                elif i[j] == "sort":
                    required_list.sort()
                elif i[j] == "pop":
                    required_list.pop()
                elif i[j] == "reverse":
                    required_list.reverse()
    
