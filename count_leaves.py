lines = []
input = open("hard1.out", "r")
print(input)
#input = input.splitlines("\n")
for line in input:
    lines.append(line[0:len(line)-1])

#print(lines)
leaves1 = []
i = 0
while i < (len(lines)):
    leaf, edges = lines[i].split()
    leaves1.append(leaf)
    i += (int)(edges) + 1

print(leaves1)

lines = []
input = open("hard (1).out", "r")
print(input)
#input = input.splitlines("\n")
for line in input:
    lines.append(line[0:len(line)-1])

#print(lines)
leaves2 = []
i = 0
while i < (len(lines)):
    leaf, edges = lines[i].split()
    leaves2.append(leaf)
    i += (int)(edges) + 1

print(leaves2)
count = 0
count1=0
for i in range(len(leaves1)):
    if (int)(leaves1[i]) < (int)(leaves2[i]):
        print("worse", i)
        print("original:", leaves2[i])
        print("current:", leaves1[i])
        print("------------------------")
        count1+=1
    elif (int)(leaves1[i]) - (int)(leaves2[i]) >=  1:
        # print("better", i)
        # print("original:", leaves2[i])
        # print("current:", leaves1[i])
        # print("------------------------")
        count+=1
print("worse", count1)
print(count)