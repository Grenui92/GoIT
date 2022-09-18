points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coor):
    return sum(points[(min(coor[i], coor[i+1]), max(coor[i], coor[i+1]))] for i in range(len(coor)-1))

print(calculate_distance([0, 1, 3, 2, 0]))