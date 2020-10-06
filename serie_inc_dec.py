num = int(input())

for i in range(1,num+1):
    while i < num:
        print(i, end=',')
        i += 1

    while num > 1:
        print(num, end=',')
        num -= 1

    while num == 1:
        print(num)
        num -= 1
