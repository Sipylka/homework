for i in range (3,21):
    list1 = []
    list2 = []
    s = list1[i] + list2[i]
    for j in range(1, i + 1):
        list1.append(j)
        print(list1)
        for k in range(1, j + 1):
            list2.append(k)