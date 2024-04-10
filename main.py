#Andrew Domonkos


def encode(password):
    encoded_password=""
    for num in password:
        num=(int(num)+3)%10
        num=str(num)
        encoded_password=encoded_password+num
    return encoded_password

Quit=1
while Quit!=None:
    print('''Menu
-------------
1. Encode
2. Decode
3. Quit''')
    option= int(input('Please enter an option: '))

    if option==1:
        password = input('Please enter your password to encode: ')
        encoded_password=encode(password)
        print(encoded_password)
        print("Your password has been encoded and stored!")
    elif option==2:
        password = input('Please enter your password to encode: ')
        decode(password)
        print("")
    elif option==3:
        Quit=None