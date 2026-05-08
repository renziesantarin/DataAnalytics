# if, elif, else
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
print("Done")

# while loop
num = 5
while num > 0:
    print("Hello")
    num -=1

# for loop
for item in [1, 2, 3, 4]:
    if item == 2:
        break
    print(item)

for item in [1, 2, 3, 4]:
    if item == 2:
        continue
    print(item)

for item in [1, 2, 3, 4]:
    pass

