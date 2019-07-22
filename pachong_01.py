n = int(input("请输入："))
a = 0
b = 1
print(a)
print(b)
while(1):
    a = a + b
    if a > n:
        break
    print(a)
    b = a + b
    if b > n:
        break
    print(b)