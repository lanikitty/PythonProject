name = input('enter your name >> ')

print(len(name))

if(len(name)>5):
    print('valid name it has more than 4 characters')
    print('we shall store it in the database')
elif(len(name)==3 or len(name)==4):
    print('type confirm to store it into database')
    if 'confirm'==input():
        print('stored in the database')
    else:
        print('wrong input')
else:
    print('name should have at least 3 characters')