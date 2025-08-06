"""name = "fayis";
age = 12;
place= "vengad";

print(name)
print(age)
print(place)
"""
'''a=int(input("enter 1st number :"))
b=int(input("enter 2nd number :"))

c=a+b
x=a*b
print(c,x)'''


'''a=(input("Enter a fistname :"))
b=(input("Enter a lastname :"))
c=(input("Enter your place :"))
#print("your fullname is",a+" "+b,"place is",c)
print(f"your name is {a}{b}\nplace is {c}")

'''
'''x="fayis";
y="p";
print("your sweet name is ",x+y)
'''

'''a=50
b=25
if a > b:
   print(" a is largest")
else:
   print("b is largst");
'''
'''
# Ask how many numbers to compare
n = int(input("Enter how many numbers: "))

# Initialize largest to a very small number or None
largest = None

# Loop to take input n times
for i in range(n):
   num = float(input(f"Enter number {i+1}: "))
   if largest is None or num > largest:
      largest = num

print("The largest number is:", largest)
'''



'''for i in range(0, 21, 1):
   print(i)'''

#factorial
'''
def fact(x):
   if x==1:
      return 1
   else:
      return x*fact(x-1)
a=(input("Enter a number:"))
ans=fact(a)
print(ans)'''


# 
'''name = input ("Entr your name:")
try:
   age=int (input("enter your age:"))
except ValueError:
   print("invalid age entered. please enter a numbr.")
   exit()
   
print(f"Hello,{name}!")
if age <18:
   print("you are a minor")
elif 18 <= age <65:
   print (" you are an adult")
elif 65<= age <100:
   print ("You are a senior citizen")
else:
   print("your deaath is soooon")'''
   
#print(sum([15,85]))

'''num =1
while num <+5:
   print(num)
   num+=1'''
   
'''for a in range(1,100):
   if a % 2==1:
      print(a)'''
'''num = 10
while num >= 1:
   print(num)
   num -= 1
'''
"""bh=10
while bh <=50:
   print(bh)
   bh+=5
   
"""
'''a=15
while a>2:
   print(a)
   a-=1
   '''
   
#for looop exambls

'''for x in range(1,10):
   print(x)
'''

'''for x in range(0,52,5):
   print(x)'''

'''for x in "letter":
   print(x)'''

'''for x in range(1,15):
   print("5x",x,"=",5*x)'''
   
'''sum=0
for i in range(1,50):
   sum += i
   print("sum of",sum)'''
   
'''for x in range (1,20):
   if x %2==1:
      print(x)'''
      
'''for x in range(1,10):
   print("square of",x,"=",x*x)
'''
'''for x in "rentease":
   print(x)
   '''   
