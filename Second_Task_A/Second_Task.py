inf = 9999999999

def dijkstra(mat, size, source, dest):      # Dijkstra algorithm for finding shortest path between source and destination

    dist = [inf] * size
    dist[source] = 0
    ischecked = [False] * size

    mini = -1

    for i in range(size):
        minimum = inf
        for u in range(size):
            if dist[u] < minimum and ischecked[u] == False:
                minimum = dist[u]
                mini = u

        x = mini

        ischecked[x] = True

        for y in range(size):
            if mat[x][y] > 0 and ischecked[y] == False and dist[y] > dist[x] + mat[x][y]:
                dist[y] = dist[x] + mat[x][y]

    return dist[dest]


def print_all_minimum_pathes(mat, check, source, dest, minimum, current_value, current_str):
    check[source] = True
    current_str += number_to_alphabet[source]

    if source == dest and current_value == minimum:
        for c in current_str:
            print(alphabet_to_place[c], end=" ")
        print()
    else:
        for i in range(len(mat)):
            if not check[i] and mat[source][i] > 0 and current_value + mat[source][i] <= minimum:
                print_all_minimum_pathes(
                    mat, check, i, dest, minimum, current_value+mat[source][i], current_str)

    current_str = current_str[:len(current_str)-1]
    check[source] = False


alphabet_to_place = dict()
place_to_alphabet = dict()
alphabet_to_number = dict()
number_to_alphabet = dict()

# Opens tesetcase file for reading information
file = open("testcase2.txt", "r")
place_number = int(file.readline())     # Finds number of places in the city
temp_list = list()
mat = list(list())  # Initializing matrix
for i in range(place_number):
    temp_list = []
    for j in range(place_number):
        if i == j:
            temp_list.append(0)
        else:
            temp_list.append(-1)
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

source = alphabet_to_number[place_to_alphabet["Parking"]]
source = int(source)

dest = input("Enter Your Destination: ")

dest = alphabet_to_number[place_to_alphabet[dest]]

minimum = dijkstra(mat, place_number,
                   alphabet_to_number[place_to_alphabet["Parking"]], dest)


check = [False] * place_number
print("Mimimum length path:", minimum)
print_all_minimum_pathes(
    mat, check, alphabet_to_number[place_to_alphabet["Parking"]], dest, minimum, 0, "")
