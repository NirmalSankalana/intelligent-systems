import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

def backtracking(assign, slots, depth):
    if (depth == len(assign)):
        return True
    global constrains
    global lecture_halls
    sub = constrains[depth][0]
    available = constrains[depth][2:]
    category = constrains[depth][1]
    if (category == "c"):
        for slot in available:
            if (slots[slot] == -1):
                assign[depth] = [sub, slot, lecture_halls[0]]
                slots[slot] = lecture_halls[0]
                if (backtracking(assign, slots, depth+1)):
                    return True
                else:
                    slots[slot] = -1
                    assign[depth] = [sub, -1, -1]
        else:
            return False

    elif (category == "o"):
        for slot in available:
            if (slots[slot] == -1):
                assign[depth] = [sub, slot, lecture_halls[0]]
                slots[slot] = [lecture_halls[0]]
                if (backtracking(assign, slots, depth+1)):
                    return True
                else:
                    slots[slot] = -1
                    assign[depth] = [sub, -1, -1]
            elif (type(slots[slot]) == list):
                asRooms = slots[slot]
                temp = asRooms[:]
                if (len(asRooms) == len(lecture_halls)):
                    continue
                asRooms.append(lecture_halls[len(asRooms)])
                assign[depth] = [sub, slot, asRooms[-1]]
                slots[slot] = asRooms
                if (backtracking(assign, slots, depth+1)):
                    return True
                else:
                    slots[slot] = temp
                    assign[depth] = [sub, -1, -1]
        else:
            return False


data = []
with open(input_file, 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        data.append(row)
lecture_halls = data[-1]
constrains = data[:-1]
# print(lecture_halls)
# print(constrains)

slots = {}
assign = []

for constrain in constrains:
    for slot in constrain[2:]:
        if slot not in slots:
            slots[slot] = -1
    assign.append([constrain[0], -1, -1])
backtracking(assign, slots, 0)
print(*assign, sep="\n")

with open(output_file22, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write multiple rows
    writer.writerows(assign)
