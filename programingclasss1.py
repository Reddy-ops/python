
for num in  range(1, 11):

    sortednumbers = sorted(numbers, key=lambda x: (bin(x).count('1'), x))

print(list(sorted_numbers))
