fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')

print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))


print(fruits.index('banana', 4))  # Find next banana starting a position 4


fruits.reverse()

print(fruits)


fruits = ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape')

print(fruits)

fruits = ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()

print(fruits)

fruits = ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

fruits.pop()

print(fruits)
