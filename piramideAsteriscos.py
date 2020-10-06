def inverted_pyramid():
    num = int(input('How many levels should the pyramid have?: '))

    for i in range(num, 0, -1):
        print('* '*i)


def pyramid():
    num = int(input('How many levels should the pyramid have?: '))

    for i in range(1, num+1):
        print('* '*i)


pyramid_type = input('Which pyramid would you like (pyramid or inverted pyramid)? ')

if pyramid_type == 'pyramid':
    pyramid()

elif pyramid_type == 'inverted pyramid':
    inverted_pyramid()

else:
    print('Error')
