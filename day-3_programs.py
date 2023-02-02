#dt=01-02-23
#crt_day-3_programs


#qestion 1:

#methods for printing the list using for loop

#using range function

l = [32,62.2,'vamsi',38]
print("printing list l elements:")
for i in range(len(l)):
    print(l[i])
print()

#with out using range function

print("printing the list li elements:")
li = [24,63,'pyp',52]
for j in li:
    print(j)
print()

#taking input from user to create a list
lis = list(map(int,input("enter values to create a list:").split()))
print(lis)

print()

#question 2

#finding sum and average for floating numbers in a list

lf = [24.2,74.32,12.0,52.45]
s = sum(lf)
l = len(lf)
a = s/l
print("sum of elements of list is:",s)
print("average of elements of list is:",a)
print()

#question 3

#finding the even elements from the list

le = list(map(int,input("enter any 5 elemets:").split()))
for i in le:
    if i%2==0:
        print(i)
print()


#question 4

#finding neon numbers

n = int(input("enter a number:"))
ns = n*n
nsl = list(str(ns))
s=0
for i in nsl:
    s += int(i)
if s==n:
    print("the given number is neon number")
else:
    print("the given number is not a neon number")

print()

#question 5

#return  product if product of list elements is less than 750
#else return sum of elements

li = list(map(int,input("enter elements to the list:").split()))
m = 1
for i in li:
          m=m*i
if m<750:
          print(m)
else:
    print(sum(li))
