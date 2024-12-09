list_ = []
for i in range(3, 21):
    a = []
    for j in range(1, i):
        for k in range(1, i):
            if j == k:
                break
            elif i % (j + k) == 0:
                a.append(j)
                a.append(k)

    print(f'{i}','-', *a)



