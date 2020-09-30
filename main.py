import functions

while True:
    choice = input("0 - Log in Twitter. \n"
                   "1 - Get Trends\n"
                   "2 - Send Tweet\n"
                   "99 - Exit\n")

    if choice == "0":
        functions.Login()

    elif choice == "1":
        functions.Trends()

    elif choice == "2":
        functions.SendTweet()

    elif choice == "99":
        break

    else:
        print("Invalid!")