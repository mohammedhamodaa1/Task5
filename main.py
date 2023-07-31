user_name = input('your name: ')
user_age = input("your age: ")
user_street = input("your street:")
user_city = input("your city:")
user_country = input("your country: ")

msg = f'''
"Name:  {user_name}"
"Age: {user_age}" 
"Adress   {user_street},  {user_city},  {user_country}"
'''
print(msg)
####################
user_age = int(user_age) - 5
msg1 = f'''
      "Hello {user_name} Your age is {user_age} Years Old , Your Address is {user_street}, {user_city}, {user_country}.
      "
'''
print(msg1)
####################
print(type(user_name))
print(type(user_age))
print(type(user_street))
print(type(user_city))
print(type(user_country))

##########
msg2 = f'''
    "Hello '{user_name}', How Are You? \ """ Your Age Is "{user_age}"" + And Your Country Is: {user_country}

'''
print(msg2)
###############
msg3 = f'''
    "Hello '{user_name}', How Are You? \

    """ Your Age Is "{user_age}"" + And
    Your City Is: {user_city}

'''
print(msg3)

####################

name = 'Doaa Reem'
print(name[:1])
print(name[2:3])
print(name[-1:])

print(name[6:9:])
print(name[:4:])
print(name[2:7:])
print(name[-1:-5:-1])
print(name[:4:2], name[5:7])

name2 = "$&$&Mohammed$&$&"
print(name2.strip('$&'))

msg6 = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg6.replace('%', 'love'))
