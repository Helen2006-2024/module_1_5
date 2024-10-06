immutable_var = 2, 4, 6, 'apple', ['cat, dog']
print(immutable_var)
# immutable_var[2] = 50  # при изменении элемента выдает ошибку, т.к. в tuple отсутствует данный объект.
mutable_list = ([1, 3, 5, 7, 'doll', 'ball', True])
print(mutable_list)
mutable_list[2] = 1
print(mutable_list)
mutable_list[True] = False
print(mutable_list)