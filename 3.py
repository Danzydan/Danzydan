3.
num = int(input('input the number: '))


if num in range(1,11):
    for i in range(1,11):
        print(str(num) + ' x ' + str(i) + ' = ' + str(num*i))
else:
    print('Invalid number')