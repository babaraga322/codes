def print_place(places, i, p1, p2):
    letter = {0: 'A', 1: "B", 2: "C", 4: "D", 5: "E", 6: "F"}
    num = i + 1
    for k in range(p1, p2-1):
        print(str(num) + letter[k], end=' ')
    print(str(num) + letter[p2-1])
    for j in range(len(places)):
        if i == j:
            print(places[i][:p1] + 'X' * (p2 - p1) + places[i][p2:])
        else:
            print(str(places[j]))


n = int(input())
places = []
for i in range(n):
    places.append(input())

m = int(input())
group = []
for i in range(m):
    group.append(input().split())

for i in range(m):
    x = '.' * int(group[i][0])
    if group[i][1] == 'left':
        p1, p2 = 0, int(group[i][0])
        if group[i][2] == 'aisle':
            x += '_'
            p1 = 4 - (int(group[i][0]) + 1)
            p2 = 4
    else:
        p1, p2 = 7 - int(group[i][0]), 7
        if group[i][2] == 'aisle':
            x = '_' + x
            p1 = 3
            p2 = 4 + int(group[i][0])

    chk = False

    for j in range(n):
        if places[j][p1:p2] == x:
            if group[i][1] == 'left' and group[i][2] == 'aisle':
                p2 -= 1
            elif group[i][1] == 'right' and group[i][2] == 'aisle':
                p1 += 1

            chk = True
            print("Passengers can take seats:", end=' ')
            print_place(places, j, p1, p2)
            places[j] = places[j][:p1] + '#' * (p2 - p1) + places[j][p2:]
            break

    if not chk:
        print("Cannot fulfill passengers requirements")

