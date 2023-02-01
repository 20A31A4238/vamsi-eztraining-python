#dt:31-01-23
#crt_day-2_prog-5

#biggest of three numbers

a,b,c = map(int,input("enter a , b and c values:").split())
if a>b:
    if a>c:
        print("the biggest of a,b,c is 'a'")
    else:
        print("the biggest of a,b,c is 'c'")
else:
    if b>c:
        print("the biggest of a,b,c is 'b'")
    else:
        print("the biggest of a,b,c is 'c'")
