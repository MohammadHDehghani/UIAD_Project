inf = 9999999999


def floyd(mat):     # Floyd algorithm for finding shortest path between any two vertexes of matrix
    dist = list(map(lambda i: list(map(lambda j: j, i)), mat))

    for k in range(len(mat)):
        for i in range(len(mat)):
            for j in range(len(mat)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


# The seller person algorithm for finding lightest hamiltonian cycle in selected node's graph
def tsp(graph, v, currPos, n, count, cost, str_temp):
    global answer
    global str_ans
    str_temp += str(currPos)
    str_temp += ","
    if count == n and graph[currPos][0] and cost + graph[currPos][0] < answer:
        answer = cost + graph[currPos][0]
        str_ans = str_temp
        str_temp = ""
        return
    for i in range(n):
        if (v[i] == False and graph[currPos][i]):

            v[i] = True
            tsp(graph, v, i, n, count + 1,
                cost + graph[currPos][i], str_temp)

            v[i] = False


alphabet_to_place = dict()
place_to_alphabet = dict()
alphabet_to_number = dict()
number_to_alphabet = dict()

# Opens tesetcase file for reading information
file = open("testcase1.txt", "r")
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

floyd_ans = floyd(mat)

translate = dict()  # This dictionary will use in translating final answer path

source = input("Enter source: ")    # Getting source node from user

translate[0] = source

source = alphabet_to_number[place_to_alphabet[source]]

passes = input("Enter places to be passed: ").split(
    ",")     # Getting places to be passed from user

for i in range(1, len(passes) + 1):
    translate[i] = passes[i-1]

for i in range(len(passes)):
    passes[i] = alphabet_to_number[place_to_alphabet[passes[i]]]

# selected_nodes include source node and nodes to be passed
selected_nodes = [source]

for item in passes:
    selected_nodes.append(item)

new_adj_mat = list(list())

for i in range(len(selected_nodes)):    # Initializing new_adj_mat
    new_adj_mat.append([inf] * len(selected_nodes))

for i in range(len(selected_nodes)):    # Filling new_adj_mat
    for j in range(len(selected_nodes)):
        new_adj_mat[i][j] = floyd_ans[selected_nodes[i]][selected_nodes[j]]

answer = inf    # The shortest lenght path
str_ans = ""    # The shortest path 

v = [False] * place_number
v[0] = True

tsp(new_adj_mat, v, 0, len(new_adj_mat), 1, 0, "")

print("The shortest lenght path:", answer)

temp_list = str_ans.split(",")

temp_list = temp_list[:len(temp_list)-1]

for item in temp_list:  # Translating 
    print(translate[int(item)], end=" ")

print(translate[0])
