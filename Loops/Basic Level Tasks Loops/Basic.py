# Print numbers from 1 to 10

'''for x in range(10):
   print(x + 1)'''

# Print even numbers from 1 to 50

'''for x in range(0, 51, 2):
   print(x)'''

# Print multiplication table of a number

'''a = int(input("Enter a number to print its multiplication table: "))
for x in range(1, 11):
   print(x, "x", a, "=", a * x)'''

# Print all characters in a string

'''for x in "python":
   print(x)'''

# Sum of numbers from 1 to user-entered number

'''a = 0
b = int(input("Enter a number to sum from 1 to that number: "))
c = 1
while c <= b:
   a += c
   c += 1
print("Sum of", b, "=", a)'''

# Count the number of vowels in a string

'''a = input("Enter a text: ")
vowels = "aAeEiIoOuU"
c = 0
for b in a:
   if b in vowels:
      c += 1
print("Number of vowels:", c)'''

# Factorial of a number using while loop

'''a = int(input("Enter a number to find factorial: "))
fact = 1
while a > 0:
   fact *= a
   a -= 1
print("Factorial is:", fact)'''

# Print all elements of a list

'''name = ["fayis", "fawas", "anas"]
for x in name:
   print(x)'''

# Check if a number is prime

'''num = int(input("Enter a number to check if it's prime: "))
if num <= 1:
   print(num, "is not a prime number")
else:
   for i in range(2, num):
      if num % i == 0:
         print(num, "is not a prime number")
         break
   else:
      print(num, "is a prime number")'''