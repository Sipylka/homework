i = int(input('клю: '))
#for i in range (3,21):
list1 = []
list2 = []
list_o = []
print('')
for j in range(1, i + 1):
    list1.append(j)
    for k in range(1, j + 1):
        list2.append(k)
        if i % (j + k) == 0 and j != k:
            #print(f'{j}{k}', end = '')
            m = sorted([j,k])
            #print(not m in list_o, m)
            if not m in list_o:
                list_o.append(m)
#print(sorted(list_o))
for j in sorted(list_o):
    print(*j, end = '', sep = '')
