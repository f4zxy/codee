# for x in range(1,11):
#    print(x)

# for x in range(0,52,2):
#    print(x)

# num=int(input("Enter A Number :"))
# for x in range(1,11):
#    print(x,"x",num,"=",num*x)

# num=int(input("Enter a number :"))
# for x in range(1,11):
#    print(x,"x",num,"=",num*x)

# for x in "fayis":
#    print(x)

# sum=1
# for x in range(1,101):
#    count=1
#    while count<=x:
#       sum=sum+count
#       count=count+1
#       print("Sum Of",x,"=",sum)

# a = 0
# b = int(input("Enter a number to sum from 1 to that number: "))
# c = 1
# while c <= b:
#    a += c
#    c += 1
# print("Sum of", b, "=", a) 

# sum=0
# num=5
# count=1
# while count<=num:
#    sum+=count
#    count+=1
# print("sum of",num,"=",sum)

# sum=0
# num=int(input("Enter a Numbr :"))
# count=1
# while count<=num:
#    sum+=count
#    count+=1
# print("sum of",num,"=",sum)

# num=(input("Enter A Word :"))
# count=0
# Vowels="aeiouAEIOU"
# for x in num:
#    if x in Vowels:
#       count+=1
# print("Vowels in",num,":",count)

# num=int(input("Enter a number :"))
# fact=1
# while num>0:
#    fact*=num
#    num-=1
# print("Factorial of",num,"is",fact)  # Output: Factorial of

# num=int(input("Enter A Number :"))
# fact=1
# while num>0:
#    fact*=num
#    num-=1
# print(f"{num} factorial is {fact}")



# name=(input("Enter your name :"))
# while name=="":
#    print("You Not Enterd Your Name")
#    name=(input("Enter your name :"))
# print(f"{name} Its A Sweet Name")

# age=int(input("Enter Your Age :"))
# while age<18:
#    print("You Are Not Eligible To Use This Web")
#    break
# else:
#    print("You Are Eligible To Use This Web")


# num=int(input("Enter a Number (Between 1 to 100) :"))

# while num <1 or num >100:
#    print("You Enterd A Wrong Number,Enter a Valid Number")
#    num=int(input("Enter a Number (Between 1 to 100) :"))
# else:
#    print("Good boy")

# num = int(input("Enter a number to check if it's prime: "))
# if num <= 1:
#    print(num, "is not a prime number")
# else:
#    for i in range(2, num):
#       if num % i == 0:
#          print(num, "is not a prime number")
#          num = int(input("Enter a number to check if it's prime: "))
#          break
#    else:
#       print(num, "is a prime number")

import time

#timer
num=int (input("Enter A Number :"))
while num>0:
   print(num)
   num-=1
   time.sleep(1)
print("Time Is Over")