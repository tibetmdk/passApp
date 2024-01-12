import math
import random
import string

def login_page():
    print("""
===============================
|   welcome to S P C(V1.0)    |
===============================
    -----------------------------------------------------------      
                    Please Login to Program
    -----------------------------------------------------------

""")

def welcome_page():
    print("""
===============================
|   welcome to S P C(V1.0)    |
===============================
    -----------------------------------------------------------     
*****if you get more info about S P C(V1.0) please enter "/h"*****
    -----------------------------------------------------------

""")

def get_info():
    print("""
          ===============Basic Implementations==================

          *If you want 8 character password please enter /spc --create 8 

          *If you want 12 character password please enter /spc --create 12

          *If you want 16 character password please enter /spc --create 16
          
          ================Extra Implementations=================

          *If you want 8 character password with non-special characters(&,+,%,${,}) /spc --create -w -sp 8

          *If you want 12 character password with non-special characters(&,+,%,${,}) /spc --create -w -sp 12

          *If you want 16 character password with non-special characters(&,+,%,${,}) /spc --create -w -sp 16
          
          """)

def send_to_file():
    pass

def create_for_eight():
    numbers = string.digits

    symbols = string.punctuation

    lower_cases = string.ascii_lowercase

    upper_cases = string.ascii_uppercase

    all_characters = [numbers,symbols,lower_cases,upper_cases]

    psswrd = ""

    for j in range(4):
        for i in range(2):
            psswrd += all_characters[j][random.randint(0,9)]



    psswrd = list(psswrd)
    random.shuffle(psswrd)

    psswrd_final = ""

    for i in psswrd:
        psswrd_final += i
    print(psswrd_final)

def create_for_eight_none_special():
    numbers = string.digits

    lower_cases = string.ascii_lowercase

    upper_cases = string.ascii_uppercase

    all_characters = [numbers,lower_cases,upper_cases]

    psswrd = ""

    for j in range(3):
        for i in range(3):
            psswrd += all_characters[j][random.randint(0,9)]



    psswrd = list(psswrd)
    random.shuffle(psswrd)

    psswrd_final = ""

    for i in psswrd[:8]:
        psswrd_final += i
    print(psswrd_final)

  

def create_for_twelve():
    numbers = string.digits

    symbols = string.punctuation

    lower_cases = string.ascii_lowercase

    upper_cases = string.ascii_uppercase

    all_characters = [numbers,symbols,lower_cases,upper_cases]

    psswrd = ""

    for j in range(4):
        for i in range(3):
            psswrd += all_characters[j][random.randint(0,9)]

    psswrd = list(psswrd)
    random.shuffle(psswrd)

    psswrd_final = ""

    for i in psswrd:
        psswrd_final += i
    print(psswrd_final)

def create_for_twelve_none_special():
    numbers = string.digits

    lower_cases = string.ascii_lowercase

    upper_cases = string.ascii_uppercase

    all_characters = [numbers,lower_cases,upper_cases]

    psswrd = ""

    for j in range(3):
        for i in range(4):
            psswrd += all_characters[j][random.randint(0,9)]



    psswrd = list(psswrd)
    random.shuffle(psswrd)

    psswrd_final = ""

    for i in psswrd:
        psswrd_final += i
    print(psswrd_final)
    

def create_for_sixteen():
    numbers = string.digits

    symbols = string.punctuation

    lower_cases = string.ascii_lowercase

    upper_cases = string.ascii_uppercase

    all_characters = [numbers,symbols,lower_cases,upper_cases]

    psswrd = ""

    for j in range(4):
        for i in range(4):
            psswrd += all_characters[j][random.randint(0,9)]

    psswrd = list(psswrd)
    random.shuffle(psswrd)

    psswrd_final = ""

    for i in psswrd:
        psswrd_final += i
    print(psswrd_final)

def create_for_sixteen_none_special():
    numbers = string.digits

    lower_cases = string.ascii_lowercase

    upper_cases = string.ascii_uppercase

    all_characters = [numbers,lower_cases,upper_cases]

    psswrd = ""

    for j in range(3):
        for i in range(6):
            psswrd += all_characters[j][random.randint(0,9)]



    psswrd = list(psswrd)
    random.shuffle(psswrd)

    psswrd_final = ""

    for i in psswrd[:16]:
        psswrd_final += i
    print(psswrd_final)
    

user_name = "a"
user_pasword = "b"

login_status = False


if __name__ == "__main__":
    login_page()
    while not login_status:
        username = input('Please enter username:')
        password = input('Please enter password:')
        
        if username != user_name and password == user_pasword:
            print("Your user name is wrong!")

        elif username == user_name and password != user_pasword:
            print("Your password is wrong!")
        
        elif username != user_name and password != user_pasword:
            print("Both is wrong!")
        
        else:
            welcome_page()
            login_status = True
        select = input(':')


        if select == '/h':
            get_info()

        elif select == "/spc --create 8":
            print("Şifreniz aşağıda hazır durumda...")
            create_for_eight()

        elif select == "/spc --create -w -sp 8":
            create_for_eight_none_special()

        elif select == "/spc --create 12":
            print("Şifreniz aşağıda hazır durumda...")
            create_for_twelve()

        elif select == "/spc --create -w -sp 12":
            print("Şifreniz aşağıda hazır durumda...")
            create_for_twelve_none_special()

        elif select == "/spc --create 16":
            print("Şifreniz aşağıda hazır durumda...")
            create_for_sixteen()

        elif select == "/spc --create -w -sp 16":
            print("Şifreniz aşağıda hazır durumda...")
            create_for_sixteen_none_special()

        else:
            print("A wrong keystroke")

















