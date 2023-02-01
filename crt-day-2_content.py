#bitwise operators
print("bitwise and")
print(10&4)
print()
print(12&7)
print()
print("bitwise or")
print(10|4)
print()
print(12|7)
print()
print("negation")
print(~10)
print()
print("bitwise xor")
print(5^6)
print()
print(9^8)
print()
print("bitwise left shift")
print(10<<2)
print()
print("bitwise right shift")
print(10>>2)
print()

#bitwise operators programs

print("input should be less than 15")
a,b = input("enter a and b values:").split()
a=int(a)
b=int(b)
print("a&b:",a&b)
print()
print("a|b:",a|b)
print()
print("~a:",~a)
print()
print("~b:",~b)
print()
print("a^b:",a^b)
print()
print("a<<b:",a<<b)
print()
print("a>>b:",a>>b)
print()

#taking input using list,map functions

#using strip function
n = int(input("size:"))
li = list(map(int,input("enter numbers:").strip().split()))
print(li)

#use without strip
n = int(input("size:"))
li = list(map(int,input("enter numbers:").split()))
print(li)

#product of any 10 numbers using list function

n = list(map(int,input("enter 10 numbers:").split()))
print(n)
p=1
for i in n:
    p *= i
print("the produvt of 10 numberes:",p)

#usage of sep and end

print("its","a","good","daY")
print("all","is","good")

print()

print("its","a","good","daY",end=" ")
print("all","is","good")

print()

print("its","a","good","daY",end="***")
print("all","is","good")

print()

print("its","a","good","daY",sep="##")
print("all","is","good")

print()
print("its","a","good","daY",sep="##",end="")
print("all","is","good",sep="@@")


#printing patterns
print()
print("@@@@@@@@@")
print(" @@@@@@@ ")
print("  @@@@@  ")
print("   @@@   ")
print("    @    ")



print()
print()
print()

  
print("  @       @    ")
print(" @  @   @  @   ")
print(" @    @    @   ")
print(" @         @   ")
print("  @       @    ")
print("   @     @     ")
print("    @   @      ")
print("     @ @       ")
print("      @        ")



#conditional statements
1.if
2.if-else
3.elif
4.ladder if

#weather prediction program

t = int(input("enter the current temprature:"))
if t<10:
    print("weather is coldest")
elif t>10 and t<=25:
    print("weather is cold")
elif t>25 and t<=35:
    print("weather is warm")
elif t>35 and t<=40:
    print("weather is hot")
else:
    print("wheather is hottest")


#control statements
#while loop
#printing 1-10 integers
i=1
while i<11:
    print(i)
    i+=1

print()

#printing 2-20 even numbers
i=2
while i<=20:
    if i%2==0:
        print(i)
    i+=1
print()

#printing 1-30 odd numbers

i=1
while i<=30:
    if i%2!=0:
        print(i)
    i+=1
    
#for loops
#printing 1-10 numbers
n=10
for i in range(1,n):
    print(i)
    
print()

#printing numbers with step-2

n = 20
for i in range(1,n,2):
    print(i)


#working with Random module

import random
n = random.randrange(1,50)
guess = int(input("enter a number between 1,50:"))
while n!=guess:
    if n<guess:
        print("its too high")
        guess = int(input("enter the number again:"))
    elif n>guess:
        print("its too low")
        guess = int(input("enter the number again:"))
    else:
        break
print("you guessed the correct number")
        
