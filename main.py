#Andrew Domonkos


def encode(password):
    encoded_password=""
    for num in password:
        num=(int(num)+3)%10
        num=str(num)
        encoded_password=encoded_password+num
    return encoded_password

def decode(password):
    decoded_password=""
    for num in password:
        num=(int(num)-3)%10
        num=str(num)
        decoded_password=decoded_password+num
    return decoded_password

Quit=1
while Quit!=None:
    print('''Menu
-------------
1. Encode
2. Decode
3. Quit''')
    option= int(input('\nPlease enter an option: '))

    if option==1:
        password = input('Please enter your password to encode: ')
        encoded_password=encode(password)
        #print(encoded_password)
        print("Your password has been encoded and stored!")
    elif option==2:
        print(f'The encoded password is: {encoded_password}, and the original password is: {decode(encoded_password)}.')
        #password = input('Please enter your password to encode: ')
        #print(decode(password))
        #print("")
    elif option==3:
        Quit=None