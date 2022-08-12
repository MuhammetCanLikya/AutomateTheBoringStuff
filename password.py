passwordFile=open("SecretPasswordFile.txt")
secretPassword=passwordFile.read()
print("Enter your password")
typepPassword=input()
if typepPassword == secretPassword:
    print("access acceptted")
    if typepPassword == "123456":
        print("only idiots try this password")
    else:
        print("Access denied")