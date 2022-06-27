inf = 9999999999


class car:
    def __init__(self, x, y, v) -> None:
        self.head = max(x, y)
        self.tail = min(x, y)
        self.ver = v
        self.checked = False


def find_minimum_moves(start_cell, temp_ans, temp_str):
    global answer
    global ans_str

    current_car_number = mat[start_cell]

    temp_str += str(current_car_number + 1)
    temp_str += ","

    if current_car_number < 0:
        return False

    if current_car_number == car_number and temp_ans > 0:
        return False

    current_car = car_list[current_car_number]

    if start_cell == current_car.tail:
        head_type = True    # This means car's head have to move
    else:
        head_type = False   # This means car's tail have to move

    if head_type:
        if current_car.ver:
            if current_car.head + x < x*y:
                if mat[current_car.head + x] == -1:
                    if temp_ans < answer:
                        answer = temp_ans
                        ans_str = temp_str
                    return True
                elif mat[current_car.head + x] == -2:
                    return False
                else:
                    find_minimum_moves(current_car.head + x,
                                       temp_ans + 1, temp_str)
            else:
                return False
        else:
            if (current_car.head + 1) // x == current_car.head // x:
                if mat[current_car.head + 1] == -1:
                    if temp_ans < answer:
                        answer = temp_ans
                        ans_str = temp_str
                    return True
                elif mat[current_car.head + 1] == -2:
                    return False
                else:
                    find_minimum_moves(current_car.head + 1,
                                       temp_ans + 1, temp_str)
            else:
                return False
    else:   # Tail type
        if current_car.ver:
            if current_car.tail - x >= 0:
                if mat[current_car.tail - x] == -1:
                    if temp_ans < answer:
                        answer = temp_ans
                        ans_str = temp_str
                    return True
                elif mat[current_car.tail - x] == -2:
                    return False
                else:
                    find_minimum_moves(current_car.tail - x,
                                       temp_ans + 1, temp_str)
            else:
                return False
        else:
            if (current_car.tail - 1) // x == current_car.tail // x:
                if mat[current_car.tail - 1] == -1:
                    if temp_ans < answer:
                        answer = temp_ans
                        ans_str = temp_str
                    return True
                elif mat[current_car.tail - 1] == -2:
                    return False
                else:
                    find_minimum_moves(current_car.tail - 1,
                                       temp_ans + 1, temp_str)
            else:
                return False


# Opens testcase file for reading information
file = open("testcase2.txt", "r")

x, y = [int(i) for i in file.readline().split(",")]     # Finding parking size

car_list = list()
tl = list()

mat = list()

for i in range(0, x*y):
    mat.append(-1)

car_counter = 0

for line in file:   # Reading information from testcase file
    tl = [int(item)-1 for item in line.split(",")]
    if len(tl) == 1:    # Specifying camera position
        cam_position = tl[0]
        mat[cam_position] = -2
    else:
        hpos, tpos, ver = tl[0], tl[1], abs(tl[0] - tl[1]) != 1
        car_list.append(car(hpos, tpos, ver))   # Filling car_list
        mat[hpos] = car_counter
        mat[tpos] = car_counter
        car_counter += 1

file.close()

target = int(input("Enter Cell Number: ")) - 1  # Reading target cell number

answer = inf
ans_str = str()

car_number = mat[target]

find_minimum_moves(target, 0, "")   # Calling the function

if mat[target] == -1:   # This means that cell is already empty
    print(0)
elif target == cam_position or answer == inf:   # This means this cell can not be free
    print("Impossible!")
else:
    print(answer+1, "Move(s)")  # Print required moves to make target cell free

al = ans_str.split(",")

for i in range(len(al)-2, -1, -1):  # Print cars
    print("Car", al[i])
