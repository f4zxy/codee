# Fibonacci Series up to 'a' numbers

'''a = int(input("Enter how many Fibonacci numbers to print: "))
b = 0
c = 1
x = 1
while x <= a:
   print(b, end=" ")
   x += 1
   b, c = c, b + c  # Fibonacci logic: next = current + previous
'''
# Print star pattern 

'''for x in range(1, 50, 1):
   print(x * "*")'''

# Sum of digits of a number

'''a = 123
x = 0
while a > 0:
   x += a % 10     # get last digit
   a //= 10        # remove last digit
print("Sum of digits:", x)'''

# Check if a string is a palindrome

'''text = input("Enter a string to check if it's a palindrome: ")
if text == text[::-1]:
   print("Palindrome")
else:
   print("Not a palindrome")'''

# Find smallest and largest number from user input

'''numbers = input("Enter numbers separated by space: ")
numbers = list(map(int, numbers.split()))

smallest = numbers[0]
largest = numbers[0]

for x in numbers:
   if x < smallest:
      smallest = x
   if x > largest:
      largest = x

print("Smallest number is", smallest)
print("Largest number is", largest)'''

# Count words in a sentence

'''Word = input("Enter a sentence: ")
count = 0
for x in Word.split():
   count += 1
print("Word count:", count)'''

# Multiplication tables from 1 to 10

'''for x in range(1, 11):
   print(f"\nMultiplication table of {x}")
   for y in range(1, 11):
      print(y, "x", x, "=", x * y)'''

# Print only unique characters in a string (no repeats)

'''text = input("Enter a string: ")
print("Unique characters are:", end=" ")
for char in text:
   if text.count(char) == 1:
      print(char, end='')'''