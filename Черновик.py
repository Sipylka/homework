str_ = ''
for i in range (3, 21):
    for j in range (1, i):
        for k in range (1, i):
            # print(i,j,k, j+k)
            #x = (j + k) % i
             if (j + k) % i == 0:
                 str_ += str(str_[j]) + ' '
                 #print(f'{i} - {j}{k}')
            #print(f'{i} | {j} + {k} / {i}= {x}')