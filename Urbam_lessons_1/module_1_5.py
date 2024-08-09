immutable_var = (1, 2, False)
print(immutable_var)

#immutable_var[0] = 2
# Выдает ошибку, потому что кортежи не поддерживают функцию изменение своих переменных.
# Если это только не внутри списка

mutable_list = [0,1,2,3]
print(mutable_list)
mutable_list[1] = 99
print(mutable_list)