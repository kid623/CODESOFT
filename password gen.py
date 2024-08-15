import random
import array
max_len =  7
NUMBERS=['0','1','2','3','4','5','6','7','8','9','10']
UPPERCASE_CHAR=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LOWERCASE_CHAR=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
SYMBOLS=['!','@','#','$','%','^','&','*','(',')','_','-','=',',','+','/','.','<','>','/','|','`','~','[',']','{','}','?',';',':']
LIST=NUMBERS + UPPERCASE_CHAR + LOWERCASE_CHAR + SYMBOLS
random_numbers=random.choice(NUMBERS)
random_uppercase=random.choice(UPPERCASE_CHAR)
random_lowercase=random.choice(LOWERCASE_CHAR)
random_symbols=random.choice(SYMBOLS)
temp_pass = random_numbers + random_uppercase + random_lowercase + random_symbols
for id in range(max_len-5):
          temp_pass = temp_pass + random.choice(LIST)
          temp_pass_list = array.array('u',temp_pass)
          random.shuffle(temp_pass_list)
password = ""
for id in temp_pass_list:
    password  = password + id
print("---------------------------Password Generator-----------------------")
print(password)
print("---------------------------Password Generated sucessfully-----------------------")
