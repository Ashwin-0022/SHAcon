print("  ____  _   _    _                    ")
print(" / ___|| | | |  / \   ___ ___  _ __   ")
print(" \___ \| |_| | / _ \ / __/ _ \| '_ \  ")
print("  ___) |  _  |/ ___ \ (_| (_) | | | | ")
print(" |____/|_| |_/_/   \_\___\___/|_| |_| ")
print("                                      ")

import hashlib
print("0 = Hasher\n1 = Dictionary Attack\n-1 = exit")
select = int(input("Select an option: "))

if select==0:
    print("\r")
    print("\r")
    print("---Hasher---")
    print("\r")
    print("0 = sha/all\n1 = sha1\n2 = sha224\n3 = sha256\n4 = sha384\n5 = sha512\n-1 = exit\n")

    str = str(input("text:"))
    user = int(input("Enter an option: "))


    if user==0:
        result = hashlib.sha1(str.encode())
        print("SHA1: ")
        print(result.hexdigest())
        print("\r")

        result = hashlib.sha224(str.encode())
        print("SHA224: ")
        print(result.hexdigest())
        print("\r")

        result = hashlib.sha256(str.encode())
        print("SHA256: ")
        print(result.hexdigest())
        print("\r")

        result = hashlib.sha384(str.encode())
        print("SHA384: ")
        print(result.hexdigest())
        print("\r")

        result = hashlib.sha512(str.encode())
        print("SHA512: ")
        print(result.hexdigest())
        print("\r")

    elif user==1:
        result = hashlib.sha1(str.encode())
        print("SHA1: ")
        print(result.hexdigest())
        print("\r")

    elif user==2:
        result = hashlib.sha224(str.encode())
        print("SHA224: ")
        print(result.hexdigest())
        print("\r")

    elif user==3:
        result = hashlib.sha256(str.encode())
        print("SHA256: ")
        print(result.hexdigest())
        print("\r")

    elif user==4:
        result = hashlib.sha384(str.encode())
        print("SHA384: ")
        print(result.hexdigest())
        print("\r")

    elif user==5:
        result = hashlib.sha512(str.encode())
        print("SHA512: ")
        print(result.hexdigest())
        print("\r")

    elif user==-1:
        exit()

elif select==1:
    print("\r")
    print("\r")
    print("---Dictionary Attack---")
    print("\r")
    hash = str(input("hash: "))

    file = open("passfile.txt", "r")
    data = file.read()
    pwd = data.split("\n")
    for i in pwd:
        result = hashlib.sha1(i.encode())
        s1 = result.hexdigest()
        result = hashlib.sha224(i.encode())
        s2 = result.hexdigest()
        result = hashlib.sha256(i.encode())
        s3 = result.hexdigest()
        result = hashlib.sha384(i.encode())
        s4 = result.hexdigest()
        result = hashlib.sha512(i.encode())
        s5 = result.hexdigest()

        
        if s1==hash:
            print("possible password is[SHA1]: ",i)
        elif s2==hash:
            print("possible password is[SHA224]: ",i)
        elif s3==hash:
            print("possible password is[SHA256]: ",i)
        elif s4==hash:
            print("possible password is[SHA384]: ",i)
        elif s5==hash:
            print("possible password is[SHA512]: ",i)


