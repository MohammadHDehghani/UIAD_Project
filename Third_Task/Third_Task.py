inf = 9999999999

alphabet_to_place = dict()
place_to_alphabet = dict()
alphabet_to_number = dict()
number_to_alphabet = dict()

def prime(graph):
    key = [inf] * len(graph)
    parent = [None] * len(graph)
    key[0] = 0
    mstSet = [False] * len(graph)

    parent[0] = -1

    for cout in range(len(graph)):

        minimum = inf

        for v in range(len(graph)):
            if key[v] < minimum and mstSet[v] == False:
                minimum = key[v]
                min_index = v
        u = min_index

        mstSet[u] = True

        for v in range(len(graph)):

            if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    print_answer(graph, parent)


def print_answer(mat, parent):
    sum = 0
    for i in range(1, len(mat)):
        sum += mat[i][parent[i]]
        print(alphabet_to_place[number_to_alphabet[parent[i]]], "-",
              alphabet_to_place[number_to_alphabet[i]], " = ", mat[i][parent[i]])
    print("Required length:",sum)


# Opens tesetcase file for reading information
file = open("testcase.txt", "r")
place_number = int(file.readline())     # Finds number of places in the city
temp_list = list()
mat = list(list())  # Initializing matrix
for i in range(place_number):
    temp_list = []
    for j in range(place_number):
        if i == j:
            temp_list.append(0)
        else:
            temp_list.append(inf)
    mat.append(temp_list)

for i in range(place_number):   # Filling dictionaries
    line = file.readline()
    temp_list = line.split(" ")
    place_to_alphabet[temp_list[1][:len(temp_list[1])-1]] = temp_list[0]
    alphabet_to_place[temp_list[0]] = temp_list[1][:len(temp_list[1])-1]
    alphabet_to_number[temp_list[0]] = i
    number_to_alphabet[i] = temp_list[0]

file.readline()

for line in file:   # Filling matrix
    temp_list = line.split()
    mat[alphabet_to_number[temp_list[0]]
        ][alphabet_to_number[temp_list[1]]] = int(temp_list[2])
    mat[alphabet_to_number[temp_list[1]]
        ][alphabet_to_number[temp_list[0]]] = int(temp_list[2])

file.close()

prime(mat)
