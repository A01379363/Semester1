user_input = input()
print('The original string is', user_input)
print('Printing only even index chars...')

for i in range(0,len(user_input), 2):
    print(f'Index[{i}]',user_input[i])
