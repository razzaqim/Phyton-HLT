
def password_strengh(password):
    """ This function returns the strengh of a password as strong, medium or weak"""
    if (len(password) >=10) and count_lowercase >=2 and count_uppercase  >=2 and count_special >=2:
        return ("This password is strong")
    elif(len(password) >=8) and count_lowercase >=1 and count_uppercase >=1 and count_special >=1:
        return ("This password is medium") 
    else:
        return("This password is weak")

count_lowercase=0
count_uppercase=0
count_special=0

password = input("Type a password: ")
password_confirm = input("Confirm your password: ")

for i in password:
      if(i.islower()):
            count_lowercase += 1
      elif(i.isupper()):
            count_uppercase += 1 
      elif(i == "!" or '"'or "£" or "$" or "%" or "^" or "&" or "*" or "(" or ")" or "{" or "}", "[" or "]" or "~" or "-" or "_" or "+" or "=" or "<" or ">" or "," or "."or "/" or "?"):
            count_special += 1 


if password != password_confirm:
    print("Error - your password is incorrect")
elif password == password_confirm:
    print(password_strengh(password))