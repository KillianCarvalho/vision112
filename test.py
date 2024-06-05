j = 1


def generateur(n):
    for i in range(n):
        if i == 5:
            j = 2
            print("La 5eme iteration", j)
        yield i + 1


i = generateur(10)
for v in i:
    print(j, v)
