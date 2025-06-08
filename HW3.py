# starter lvl

#1
numbers = [1, 4, 16, 222]
print(sum(numbers))

#2
numbers = [1, 4, 16, 222]
print(min(numbers))

#3
numbers = [1, 4, 16, 222]
print(numbers[::-1])

#4
numbers = [1, 2, 3, 4, 5, 7, 8, 9]
for i in numbers:
    if not i%2 == 0:
        print(i)

#5
numbers = [1, 4, 16, 222]
a = int(input("Enter sumting: "))
numbers_multiplied = []
for bruh in numbers:
    numbers_multiplied.append(bruh * 2)
numbers = numbers_multiplied
print(numbers)

# easy lvl

#1
x = int(input("Enter: "))
numbers = [1, 4, 16, 222]
new_numbers = []
for bruh in numbers:
    if bruh > x:
        new_numbers.append(bruh)
numbers = new_numbers
print(numbers)

#2
numbers = [1, 4, 16, 222, -2, -300, -228, 1000]
positivchiki = []
for bruh in numbers:
    if bruh > 0:
        positivchiki.append(bruh)
if len(positivchiki) > 0:
    average = sum(positivchiki) / len(positivchiki)
print(average)

#3
numbers = [1, 4, 16, 222, -2, -300, -228, 1000]
x = int(input("Enter sumting: "))
howmany = 0
filtered_numbers = []
for bruh in numbers:
    if bruh < x:
        filtered_numbers.append(bruh)
print(max(filtered_numbers))

#4
numbers = [1, 4, 16, 222, -2, -300, -228, 1000]
x = int(input("Enter sumting: "))
y = int(input("Enter sumting: "))
total_sum = 0
for bruh in numbers:
    if bruh%y == 0:
        total_sum += bruh
print(total_sum)

#5
numbers = [1, 4, 16, 222, -2, -300, -228, 1000]
newnew = []
for i in numbers:
    newnew.append(i**2)
print(newnew)

#6
numbers = [1, 4, 16, 222, -2, -300, -228, 1000]
newnew = []
for hello in numbers:
    if hello > 0:
        newnew.append(hello)
print(newnew)

#7
words = ["apple", "banana", "apricot", "cherry", "avocado"]
the_prefix = "ap"
words_w_prefix = []
for word in words:
    if word.startswith(the_prefix):
        words_w_prefix.append(word)
print(words_w_prefix)

#8
numbers = [1, 4, 16, 222, -2, -300, -228, 1000]
n = int(input("Enter sumting: "))
newnew = 0
for bruh in range(n):
    newnew += numbers[bruh]
print(newnew)

#9
words = ["level", "python", "madam", "racecar", "hello"]
polindromes = []
for word in words:
    if word == word[::-1]:
        polindromes.append(word)
print(polindromes)

#10
numbers = [1, 4, 16, 222, -2, -300, -228, 1000]
divisor = int(input("Enter the divisor: "))
thelist = []
for bruh in numbers:
    if bruh % divisor == 0:
        thelist.append(True)
    elif not bruh % divisor == 0:
        thelist.append(False)
print(thelist)

# middle LVL

#1
numbers = [1, 2, 123, 123123, 123123123, 9000]
fnums = []
X = 2
Y = 1
for i in numbers:
    if i%X == 0 and i%Y == 0:
        fnums.append (i)  
print(fnums)

#2
nums = [[1, 2], [3, 4, 5], [6]]
numsfinal = []
for sublist in nums:
    for item in sublist:
        numsfinal.append(item)
print(numsfinal)

#3
string_list = ["Hello World", "Python Is Fun", "Keep Calm"]
capitals_list = []
for text in string_list:
    capitals = ""
    for char in text:
        if char.isupper():
            capitals = capitals + char
    capitals_list.append(capitals)
print(capitals_list)

#4
from collections import Counter
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
counts = Counter(numbers)
sorted_list = sorted(numbers, key=lambda x: (counts[x], x), reverse=True)
print(sorted_list)

#5
list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10, 11, 12]
merged_list = []
for num in list1:
    if num % 2 == 0:
        merged_list.append(num)
for num in list2:
    if num % 2 != 0:
        merged_list.append(num)
print(merged_list)

#6
data = [
    {'category': 'A', 'value': 10},
    {'category': 'B', 'value': 5},
    {'category': 'A', 'value': 15},
    {'category': 'B', 'value': 20},
    {'category': 'C', 'value': 12}
]
result_dict = {}
for item in data:
    key = item['category']
    value = item['value']
    if key in result_dict:
        result_dict[key] = result_dict[key] + value
    else:
        result_dict[key] = value
print(result_dict)

#7
numbers = [5, 12, 8, 25, 3]
replaced_list = []
for num in numbers:
    if num > 10:
        replaced_list.append('high')
    else:
        replaced_list.append('low')
print(replaced_list)

#8
words = ["one", "two", "three", "four", "five", "six"]
X = 3
count = 0
for word in words:
    if len(word) > X:
        count = count + 1
print(count)

#9
list1 = ['A', 'B', 'C']
list2 = ['1', '2', '3', '4', '5']
result = []
max_len = max(len(list1), len(list2))
for i in range(max_len):
    if i < len(list1):
        result.append(list1[i])
    if i < len(list2):
        result.append(list2[i])
print(result)

#10
numbers = [5, 15, 8, 20, 10]
X = 12
Y = 10
new_list = []
for num in numbers:
    if num > X:
        new_list.append(num * Y)
    else:
        new_list.append(num)
print(new_list)