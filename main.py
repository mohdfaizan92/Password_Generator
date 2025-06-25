import random
import string

platform = input("enter the name of platform : ")
length = int(input("enter the length of your password : "))
character=string.ascii_letters+string.digits+string.punctuation
password = ''.join(random.choice(character)for i in range(length))
print("Generated password for ",platform,": ",password)

file=open("pswd.txt","a")
file.write("platform: "+platform + ", password: "+password+ "\n")
file.close()
print("password saved to pswd.txt file")