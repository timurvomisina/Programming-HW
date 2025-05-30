#1
a = "Hello World!"
print(a)

#2
b = int(input("Enter some number: "))
c = int(input("Enter another number: "))
print(b + c)
print(b - c)
print(b * c)
print(b / c)

#3
str1 = input("Enter some text: ")
str2 = input("Enter some more text: ")
linetogether = str1 + str2
print(linetogether)
print(f"The length of both strokes: {len(linetogether)}")

#4
somenumber = int(input("Enter random number: "))
if somenumber%2 == 0:
    print("Парне!")
else:
    print("Непарне!")

#5
for i in range(10):
    print(i+1)

#6 
num = int(input("Enter some number: "))
if num > 0:
    print("POSITIVE")
elif num < 0:
    print("NEGATIVE ")
else:
    print("IT'S ZERO!")

#7
for i in range(10):
    if (i+1)%2 == 0:
        print(i+1)

#8
n = int(input("Enter a number: "))
thesum = 0
for i in range(n):
    thesum += i+1
    i+=1
print(thesum)

#9
somenumber = 10
for i in range(somenumber):
    print(somenumber-i)

#10
for i in range(10):
    if i+1 == 5:
        continue
    elif i+1 == 7:
        print(i+1)
        break
    else:
        print(i+1)

