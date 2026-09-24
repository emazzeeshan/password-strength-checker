#Password Strength checker
#ABeginner python cyber security project

password = input("Enter your password : ")

if len(password) >= 8:
   print("password has enough characters ")
else:
   print("password is to short ")   

has_uppercase = any(char .isupper() for char in password)
if has_uppercase:
   print("password contains an uppercase letter")
else:
   print("password needs an uppercase letter ")   

has_number = False   
for char in password :
   if char .isdigit():
      has_number = True
if has_number:
   print("password contains a number ")
else:
   print("password needs a number")    

special_characters = "!@#$%^&*"
has_special = False
for char in password:
   if char in special_characters:
      has_special = True
if has_special:
   print("password contains a special character")
else:
   print("password needs a special character")  

score = 0
if len(password) >= 8:
   score += 1
if has_uppercase:
   score += 1   
if has_number:
   score += 1
if has_special:
   score += 1
if score <= 1:
   print("password strength : Weak")   
elif score <= 3:
   print ("password strength : Medium")   
else:
   print("password strength : Strong")






