if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list_of_i = [i for i in range(x+1)]
    list_of_j = [i for i in range(y+1)]
    list_of_k = [i for i in range(z+1)]
    
    list_of_all_permutations = [[i,j,k] for i in list_of_i for j in list_of_j for k in list_of_k if (i+j+k != n)]

    
    print(list_of_all_permutations)
