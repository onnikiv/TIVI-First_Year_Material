
while True:
    user_id = str(input("Anna tunnus: \n")).upper()
    if user_id == "PYTHON":
        user_password = str(input("Anna salasana: \n")).upper()
        if user_password == "RULES":
            print("Tervetuloa")
            break
    else:
        print("jou")




#user_password = str(input("Anna salasana: \n"))
#user_password = "rules".upper()