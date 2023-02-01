#dt:31-01-23
#crt_day-2_prog-7


#divisible by 2 and 5

n = int(input("enter a value:"))
if n%2==0:
    if n%5==0:
        print("the value is divisible by both 2&5")
    else:
        print("the value is divisible by 2 but not divisible by 5")
else:
    if n%5==0:
        print("the value is not divisble by 2 and divisible by 5")
    else:
        print("the value is not divisible by both 2&5")
    
