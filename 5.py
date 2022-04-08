src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique = []
tmp = []
for el in src:
    if el not in tmp:
        unique.append(el)
    else:
        if el in unique:
            unique.remove(el)
    tmp.append(el)
print(unique)
