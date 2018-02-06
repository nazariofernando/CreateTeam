from math import sqrt

def find(array, solution):
    best = 0
    newRole = 0
    newPerson = 0

    best = max(array)
    indexOfMax = array.index(best)

    result = solution

    if best == -1:
        return result
    else:
        if indexOfMax <= 2:
            newRole = 0
        elif 3 <= indexOfMax <= 5:
            newRole = 1
        else:
            newRole = 2
        newPerson = indexOfMax % 3
        i = 0
        for element in array:
            if newPerson == i % 3 or ((newRole % 3) * 3 <= i <= ((newRole+1)*3-1)):
                array[i] = -1
            i+=1
        solution += best**2
        return find(array, solution)


fi = open('./input.txt', 'r')

a = map(int, fi.readline().split())
b = map(int, fi.readline().split())
c = map(int, fi.readline().split())

group = [a, b, c]

transpose = [
    [0,0,0], #code
    [0,0,0], #math
    [0,0,0]  #test
]

for role in range(0,3):
    for person in range(0,3):
        transpose[role][person] = group[person][role]

allList = []

for role in transpose:
    for person in role:
        allList.append(person)

solution = sqrt(find(allList, 0))

fo = open('./output.txt', 'w')
fo.write(str(solution))
