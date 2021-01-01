# List of numbers
lst = [2, 3, 5, 8, 9, 10, 21, 24, 53]
print('List of numbers: ', lst)
print()

# Sorted list of numbers
sort_lst = sorted(lst)
print('Sorted list of numbers using function:\n', sort_lst)
print()

# Sorting list using sort method
lst.sort()
print('Sorted list of numbers using method:\n', lst)
print()

# Sorting list in descending order
sort_lst = sorted(lst, reverse=True)
print('Sorted list of numbers in descending order:\n', sort_lst)
print()

lst.sort(reverse=True)
print('Sorted list of numbers in descending order:\n', lst)
