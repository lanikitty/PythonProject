name = input('enter your name >> ')

print(len(name))

if(len(name)>5):
    print('valid name it has more than 4 characters')
    print('we shall store it in the database')
else:
    print('name should have at least 4 characters')