def func1():
    """this function is used to (log/write) food and exercise on customer file"""
    try:
        import datetime
        shomoi = datetime.datetime.now()

        print("\n1 = Harry\n2 = Rohan\n3 = Hammad")
        client_number = int(input("client number : "))

        # -------------------harry--------------------------------------------
        if client_number == 1:
            print("\n1 = food\n2 = exercise")
            food_exercise = int(input("what you want to lock : "))

            if food_exercise == 1:
                f = open("harryfood.txt", "a")
                write_food = input("\nwrite about food : \n")
                f.write(f"\n{shomoi} :   {write_food}")
                f.close()
                print("you have successfully write this on harry's food", "(", write_food, ")\n")

            elif food_exercise == 2:
                f = open("harryexercise.txt", "a")
                write_exercise = input("\nwrite about exercise : ")
                f.write(f"\n{shomoi} :   {write_exercise}")
                f.close()
                print("you have successfully write this on harry's food", "(", write_exercise, ")\n")

            else:
                print("your input is wrong!\n")

        # ------------------------------rohan-------------------------------------
        elif client_number == 2:
            print("\n1 = food\n2 = exercise")
            food_exercise = int(input("what you want to lock : "))

            if food_exercise == 1:
                f = open("rohanfood.txt", "a")
                write_food = input("\nwrite about food : ")
                f.write(f"\n{shomoi} :   {write_food}")
                f.close()
                print("you have successfully write this on harry's food", "(", write_food, ")\n")

            elif food_exercise == 2:
                f = open("rohanexercise.txt", "a")
                write_exercise = input("\nwrite about exercise : ")
                f.write(f"\n{shomoi} :   {write_exercise}")
                f.close()
                print("you have successfully write this on harry's food", "(", write_exercise, ")\n")
            else:
                print("your input is wrong!")

        # -----------------------------hammad-------------------------------------------
        elif client_number == 3:
            print("\n1 = food\n2 = exercise")
            food_exercise = int(input("what you want to lock : "))

            if food_exercise == 1:
                f = open("hammadfood.txt", "a")
                write_food = input("\nwrite about food : ")
                f.write(f"\n{shomoi} :   {write_food}")
                f.close()
                print("you have successfully write this on harry's food", "(", write_food, ")\n")

            elif food_exercise == 2:
                f = open("hammadexercise.txt", "a")
                write_exercise = input("\nwrite about exercise : ")
                f.write(f"\n{shomoi} :   {write_exercise}")
                f.close()
                print("you have successfully write this on harry's food", "(", write_exercise, ")\n")
            else:
                print("your input is wrong!\n")

        else:
            print("your input is wrong!\n")  # func1 code end here

    except Exception as e:
        print(e)


def func2():
    """this function is used to (retrieve / see) the food and exercise"""
    try:
        print("\n1 = Harry\n2 = Rohan\n3 = Hammad")
        client_number = int(input("client number : "))

        # ----------------------------harry--------------------------------
        if client_number == 1:
            print("\n1 = food\n2 = exercise")
            food_exercise = int(input("what you want to see : "))

            if food_exercise == 1:
                f = open("harryfood.txt")
                print(f.read())
                f.close()

            elif food_exercise == 2:
                f = open("harryexercise.txt")
                print(f.read())
                f.close()

            else:
                print("your input is wrong!\n")

            # ------------------------------rohan---------------------------------
        elif client_number == 2:
            print("\n1 = food\n2 = exercise")
            food_exercise = int(input("what you want to see : "))

            if food_exercise == 1:
                f = open("rohanfood.txt")
                print(f.read())
                f.close()

            elif food_exercise == 2:
                f = open("rohanexercise.txt")
                print(f.read())
                f.close()

            else:
                print("your input is wrong!\n")

            # --------------------------------hammad----------------------------------------
        elif client_number == 3:
            print("\n1 = food\n2 = exercise")
            food_exercise = int(input("what you want to see : "))

            if food_exercise == 1:
                f = open("hammadfood.txt")
                print(f.read())
                f.close()

            elif food_exercise == 2:
                f = open("hammadexercise.txt")
                print(f.read())
                f.close()

            else:
                print("your input is wrong!\n")

        else:
            print("your input is wrong!\n")

    except Exception as e:
        print(e)


# --------------main code start here-------------------------
while True:
    try:
        print("\n1 = log\n2 = retrive")
        inp1 = int(input("what you want to do : "))
        if inp1 == 1:
            func1()
        elif inp1 == 2:
            func2()
        else:
            print("your input is wrong!")
    except Exception as k:
        print(k)
