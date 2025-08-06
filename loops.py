# 1. Countdown from 5 using while loop
c = 5
while c >= 1:
    print(c)
    c -= 1

print("-----")

# 2. Print all items in a list using for loop
num = [1, 45, 26, 45, 85, 35, 5, 2, 6, 8, 5]
for x in num:
    print(x)

print("-----")

# 3. Break loop when 85 is found
mm = [1, 45, 26, 45, 85, 35, 55, 74]
for x in mm:
    if x == 85:
        break
    print(x)

print("-----")

# 4. Skip 45 using continue in for loop
ink = [1, 45, 26, 45, 85, 35, 55, 74]
for x in ink:
    if x == 45:
        continue
    print(x)

print("-----")

# 5. Print numbers from 1 to 100 using for loop
for y in range(1, 101):
    print(y)

print("-----")

# 6. Store 5 valid numbers (5 to 25) in list using for loop
valid_nums = []
for i in range(5):
    x = int(input("Enter a number between 5 and 25: "))
    if 5 <= x <= 25:
        valid_nums.append(x)
    else:
        print("Enter a valid number")
print("Collected numbers:", valid_nums)

print("-----")

# 7. Store 5 valid numbers (10 to 50) in list using while loop
count = 0
num_list = []
while count < 5:
    num = int(input("Enter a number between 10 and 50: "))
    if 10 <= num <= 50:
        num_list.append(num)
        count += 1
    else:
        print("Enter a correct number")
print("Collected numbers:", num_list)

print("-----")

# 8. Print list of fruits using for loop
lop = ["apple", "orange", "grape"]
for x in lop:
    print(x)

print("-----")

# 9. Print each character of a string using for loop
for x in "apple":
    print(x)

print("-----")

# 10. Check if number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("-----")

# 11. Compare two input numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
if a > b:
    print("1st number is bigger")
elif a < b:
    print("2nd number is bigger")
else:
    print("Both are equal")

print("-----")

# 12. Print 1 to 100 using while loop
i = 1
while i <= 100:
    print(i)
    i += 1
print("Your output is here")

print("-----")

# 13. Countdown from 100 to 1 by 5 using while loop
i = 100
while i >= 1:
    print(i)
    i -= 5

print("-----")

# 14. Right-aligned triangle pattern (incomplete logic originally)
i = 1
while i <= 5:
    j = 5
    while j > i:
        print(" ", end="")
        j -= 1
    print("*" * i)
    i += 1

print("-----")

# 15. Countdown from 20 to 1
i = 20
while i >= 1:
    print(i)
    i -= 1

print("-----")

# 16. FIXED: Print numbers from 1 to 49 (step 5 missing fixed)
a = 1
while a < 50:
    print(a)
    a += 5

print("-----")

# 17. FIXED: Print numbers with dot using f-string
for num in range(10):
    print(f"{num}.")
