from random import randint

print('Welcome To Password Generator')
#upper case password/// 

password = ""
for i in range(10):
    i = chr(randint(65, 90))
    password = str (password) + i
print(password)

#upper and lowercase password
password = ""
for i in range(5):
    i = chr(randint(65, 90))
    for j in range(5):
        j = chr(randint(65, 90)).lower()
    password = str(password) + i + j
print(password)

