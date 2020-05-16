
name = input(“Enter your name: “)
for i in name:
if i.isalpha() is False:
   raise NameError(“Invalid Name”)
 elif len(name) >10 : 
 print(name + “ is a long name”)
  else:
  print(name)



email = input(“what is you email address: “)
  if “@“ not in email :
    raise NameError(“email must contain @ and .”)

  elif “.” not in email :
    raise NameError(“email must contain @ and .”)
  
else:
    print(email)




 age = int(input(“what is your age: “))
     if age <18 :
       print(“sorry you\'re still a minor at age” + str(age))
   else: 
       print(age)

    


   Number = int(input(“your phone number: 0”))
       print(“0” + str(Number))
   

