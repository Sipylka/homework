immutable_va = (1, 2, 'a', 'b')
print(immutable_va)
#immutable_va[0] = 5
#TypeError: 'tuple' object does not support item assignment
#нельзя изменить элементы кортежа, но можно изменить содержимое, если в кортеже есть список

mutable_list = [1,2,3,4,5]
mutable_list[1] = 321
print(mutable_list)