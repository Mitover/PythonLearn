a = int(input())
b = a % 10 == a // 1000
c = a % 100 // 10 == a // 100 % 10
if b is True and c is True:
    print("YES")
else:
    print("NO")
#-------------------
b = input()
if b == b[::-1]:
    print("YES")
else:
    print("NO")

#-------------------

a = input()
b = a[0] == a[3]
c = a[1] == a[2]
if b is True and c is True:
    print("YES")
else:
    print("NO")