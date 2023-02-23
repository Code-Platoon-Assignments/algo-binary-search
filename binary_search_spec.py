from random import seed, sample
from binary_search import binary_search

seed(1)  # this forces our 'random' numbers to be the same every time

test_array = list(range(1, 10))
test_big_array = sample(list(range(1, 1000000)), 1000)
test_big_array.sort()  # binary_search only works on sorted lists

print(binary_search(1, test_array) == 0)
print(binary_search(4, test_array) == 3)
print(binary_search(7, test_array) == 6)
print(binary_search(8, test_array) == 7)
print(binary_search(42, test_array) == -1)

print(binary_search(991189, test_big_array) == 993)
print(binary_search(991190, test_big_array) == -1)
