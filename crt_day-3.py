#dt=1-02-23
#crt_day-3

#list
#list access

'''l = [3,62,7.37,73,'vamsi',]
print(l)
print(l[3])
print(l[1:3])
print(l[1:])
print(l[:4])
print(l[::-1])
print()

#list operations
l = [3,62,7.37,73,'vamsi',]
print("printing the created list:",l)
print("appedning value 38 to l:",l.append(38))
print(l)
print("lenght of l is:",len(l))
l.extend([23,63,12])
print("after extending,the list looks like:",l)
l.insert(2,'apple')
print("after inserting 'apple' at postio 2:",l)
print("poping the element:",l.pop())
print("poping the element using index:",l.pop(4))
print("printing the count of a number 62:",l.count(62))
print("removing an element from the list l:",l.remove(3))
print(l)

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


#list comprehension
    
numbers = [numbers for elements in "great afternoon"]
print(numbers)
print()

l1 = [2**x for x in range(2,10)]
print(l1)
print()

l2 = [a for a in range(100,201,20)]
print(l2)
print()

#creating a new list from old list

l3 = [1,3,2,4,5,6,7]
l4 = [i for i in l3 if(i<5)]
print(l4)
print()


l = ['hyd','vizag','chennai','vijayawada']
city =[]
for i in l:
    if 'v' in i:
        city.append(i)
print(city)
print()

#set data_type

#creation of set

s = {3,52,35.4,'vam',23,52}
print(s)
print()

#adding an element to set

s.add(38.26)
print(s)
print()

#updating a created list
s.update(['ika',32])
print(s)
print()

#deleting elements in set

#using discard
s.discard(3)
print(s)
print()

#using remove
s.remove(1)
print(s)
print()

#set operations

s1 = {2,42,'vam',82,92}
s2 = {82,'vam',42}

print(s1)
print()
print(s2)
print()

a = s1.union(s2)
print("the union of s1 and s2:",a)
print()

b = s1.intersection(s2)
print("the intersection of s1 and s2:",b)
print()

c = s1.difference(s2)
d = s2.difference(s1)
print("the difference of s1 and s2:",c)
print("the difference of s2 and s1:",d)
print()

print("superset of two sets:",s1.issuperset(s2))


#tuple

#creation of a tuple
t = (23,5.23,'cam',35,82)
print(t)
print()

c = t.count(23)
print(c)

i = t.index(35)
print(i)
print()
#dictionary'''

#creation of a dictionary

dic = {1:'one',2:'two',3:'three',8:33}
print(dic)
print()

print(type(dic))

#printing the items of dictionary

print(dic.items())

print()

#printing the keys in dictionary

print(dic.keys())

#printing the values of dictionary
print(dic.values())
print()

#printing values using keys

print(dic[2])
print()

#poping an element from dictionary
dic.pop(1)
print(dic)
print()

dic.popitem()
print(dic)
print()

#creating a new key-value
dic['name']='vamsi'

print(dic)
