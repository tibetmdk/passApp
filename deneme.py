import random
import string

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

create_for_sixteen_none_special()





