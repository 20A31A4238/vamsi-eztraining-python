#dt=30-01-23
#crt day-1

#printing names using unicode in telugu

print("hello world")
print(chr(3700)+chr(3077))
print(chr(3125)+chr(3174)+chr(3126)+chr(3136))
print(chr(3098)+chr(3144)+chr(3108)+chr(3112)+chr(3181))
print(chr(3129)+chr(3120)+chr(3135)+chr(3093))
print(chr(3117)+chr(3120)+chr(3176)+chr(3125)+chr(3097)+chr(3149))
print(chr(3125)+chr(3144)+chr(3126)+chr(3149)+chr(3107)+chr(3125)+chr(3135))

#varible declaration

v = "38"
_x = 38
v_38 = "vamsi"

#printing the various types of data types

print("enter integers values:")
a= int(input("enter first integer:"))
b = int(input("enter second integer:"))
c = int(input("enter third integer:"))
print()
print("the value of 'a' is :",a)
print("the value of 'b' is :",b)
print("the value of 'c' is :",c)

print()
print()

print("enter strings values:")
a=input("enter first string:")
b =input("enter second string:")
c =input("enter third string:")
print()
print("the value of 'a' is :",a)
print("the value of 'b' is :",b)
print("the value of 'c' is :",c)

print()
print()

print("enter float values:")
a= float(input("enter first float:"))
b = float(input("enter second float:"))
c = float(input("enter third float:"))
print()
print("the value of 'a' is :",a)
print("the value of 'b' is :",b)
print("the value of 'c' is :",c)

print()
print()

print("enter complex values:")
a= complex(input("enter first complex:"))
b = complex(input("enter second complex:"))
c = complex(input("enter third complex:"))
print()
print("the value of 'a' is :",a)
print("the value of 'b' is :",b)
print("the value of 'c' is :",c)


#programs

k = int(input("enter no of sugar canes:"))
s = k/2
k = s+s/2
print("the no of sugara canes wirh kumar is:",k)
print("the no of sugarcanes with sam is:",s/2)

print()
print()

n = float(input("enter a value:"))
n *= 3
n += 56.19
n -= 10
print(n)

print()
print()

p = int(input("enter a positive number:"))
n = float(input("enter a negative number:"))
print(p*n)

print()
print()


print(3.5/1.5)


print()
print()

#swapping the numbers

#with temprory variable

a,b =input("enter a and b values:").split()
a = int(a)
b = int(b)
temp = b
b = a
a = temp
print(a,b)


print()
print()

#with out temprory variable

a,b = input("enter a and b values:").split()
a,b = b,a
print(a,b)


print()
print()

#area and perimeter of rectangle

l,b = input("enter the lenght and breth value:").split()
l = int(l)
b = int(b)
print("area of rectangle is :",l*b)
print()
print("perimeter of rectangle is :",2*(l+b))

