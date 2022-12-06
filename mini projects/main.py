import random as rnd
from twilio.rest import Client as clt
import sqlite3
from database import country_codes


def check_valid_string(x):
    if len(x) <= 0:
        return False
    for i in x:
        if i.isalpha() != True and i.issppace() != True:
            return ValueError
    return True

connection = sqlite3.connect('user_data.db')
c = connection.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user_data (
    name test, age integer, p_num blob PRIMARY KEY
)''')

generate_otp = rnd.randint(1000000,9999999)                         #access tokens
sid = 'AC0e00774f9d3f80d9e12dbc53bfbceb8a'
auth_token = 'ec09419b1caa61ade7a025285ea51130'
client = clt(sid,auth_token)

test_number = '+61455512511'
valid_genders = ['male', 'female']                              #list of valid gender inputs    
val_chars = '~`!@#£€$¢¥§%°^&*()-_+={}[]|\/:;\"\'<>,.?'                #valid characters for input
i = 0  
name = (input('Please enter your name: '))                      #prompt user's name and save under name

if check_valid_string(name) == ValueError:
    print('\nError: Name can only contain alphabetical characters or spaces')
elif check_valid_string(name) == False:
    print('\nError: Name cannot be empty or string')

while True:                                                     #initalize event-controlled loop
    try:
        age = int(input('\nPlease enter your age: '))           #save age under age
    except ValueError:                                          #check for value error
        print('Error: Please enter valid input')
        continue
    if age < 0 or age > 110:                                    #check for range
        print('Error: The age is a number between 0 to 110')
        continue
    else: 
        break

while True:
    try:
        phone_num = int(input('\nPlease enter your age: '))
    except ValueError:
        print('Error: Please enter a valid input')
        continue
    else:
        break
    
def verify():
    client.messages.create(

        body = f'\nHi {name}! Your OTP verfication code is: {generate_otp}',
        from_ = '+15077097998',
        to = f'{phone_num}',

    )

while True:
    try:
        verify()
        verifier = int(input('An OTP verification code has been sent into your phone number:'))
    except TypeError:
        print('Error')
    if verifier != generate_otp:          
        print('The code that you have entered is incorrect, we have sent another one.')
        continue
    else:
        c.execute("INSERT INTO user_data VALUES(?,?,?)", (name,age,test_number))
        connection.commit()
        print('Account created succesfully')
        break          

#print the user's name, age and phone number


    




