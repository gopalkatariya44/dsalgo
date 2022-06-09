while True:
    email  = input("Enter Email : ")
#     if(len(email) < 6):
#         print("password more than 6 char")
    # if("@" not in email):
    #     print("your email not contain @")
    if(email.count("@") == 1):
        print("your email more then one @")
        