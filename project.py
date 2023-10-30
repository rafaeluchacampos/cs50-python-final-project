import os
import time
import requests
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    figlet.setFont(font="speed")
    print(figlet.renderText("DAY-2-DAY HOME ASSISTANT"))
    time.sleep(3)
    clearscreen()

    user = "user.csv"
    user_data = load_data(user)

    if not user_data:
        print("Welcome to the Day-2-Day Home Assistant")
        user_data = new_user()
        user_data = load_data(user)
        print(f"Welcome, {user_data['Name']}!\n")
        time.sleep(1)
        clearscreen()
    else:
        print(f"Welcome back, {user_data['Name']}!\n")
        time.sleep(2)
    while True:
        print("######## MENU ############################")
        print("#                                        #")
        print("# (1) To-Do List    |  (3) Weather Today #")
        print("# (2) Grocery List  |  (4)               #")
        print("#                                        #")
        print("##########################################\n\n")
        menu = input("Acess option or (e) Exit: ").lower()
        time.sleep(1)
        if menu == "e":
            break
        elif menu == "1":
            clearscreen()
            to_do_list()
        elif menu == "2":
            clearscreen()
            grocery_list()
        elif menu == "3":
            clearscreen()
            weather_today()
        else:
            print("Please select a valid option")
            time.sleep(1)
            clearscreen()
            pass


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def new_user():
    name = input("What's your name? ")
    location = input("Where are you located? ")

    with open("user.csv", 'w') as f:
        f.write(f"Name : {name}\n")
        f.write(f"Location : {location}\n")


def load_data(user):
    data = {}
    if os.path.exists(user):
        with open("user.csv", 'r') as f:
            lines = f.readlines()
            for line in lines:
                key, value = line.strip().split(' : ')
                data[key] = value
    return data


def to_do_list():
        print("#### TO DO LIST ################")
        print("#                              #")
        print("# (1) Create new list          #")
        print("# (2) Edit list                #")
        print("# (3) Read list                #")
        print("#                              #")
        print("################################\n\n")
        option = input("Acess option or (e) Exit: ").lower()

        if option == "1":
            clearscreen()
            new_list = []
            print("##### New To Do List ######\n\n")
            print("Enter new tasks or press (CLTR+D) to exit\n\n")

            try:
                while True:
                    new_task = input(">> ")
                    new_list.append(new_task)
            except EOFError:
                with open("to_do_list.txt", 'w') as f:
                    for item in new_list:
                        f.write(item + "\n")
                clearscreen()
                return

        elif option == "2":
            clearscreen()
            print("##### To Do List ######\n")
            with open("to_do_list.txt", 'r') as f:
                to_do_list = f.readlines()
                for item in to_do_list:
                    print(item)
            print("Enter new tasks or press (CLTR+D) to exit\n\n")
            new_list = []
            try:
                while True:
                    new_task = input(">> ")
                    new_list.append(new_task)
            except EOFError:
                with open("to_do_list.txt", 'a') as f:
                    for item in new_list:
                        f.write(item + "\n")
                clearscreen()
                return

        elif option == "3":
            clearscreen()
            time.sleep(1)
            print("##### To Do List #######\n\n")
            with open("to_do_list.txt", 'r') as f:
                to_do_list = f.readlines()
            for item in to_do_list:
                print(item)
                time.sleep(1)
            print("\n\n")
            input("Press Enter to exit")
            clearscreen()

        elif option == "e":
            return
        else:
            print("Select a valid option")


def grocery_list():
    print("#### GROCERY LIST ##############")
    print("#                              #")
    print("# (1) Create new list          #")
    print("# (2) Edit list                #")
    print("# (3) Read list                #")
    print("#                              #")
    print("################################\n\n")
    option = input("Access option or (e) Exit: ").lower()

    if option == "1":
        clearscreen()
        grocery_items = []
        print("##### Grocery List ######\n\n")

        while True:
            try:
                item = input("What do you need to buy? ")
                quantity = input("Quantity: ")
                grocery_items.append({"item": item, "quantity": quantity})
                add_another_item = input("Want to add another item (y/n)? ").lower()
                while add_another_item not in ("y", "n"):
                    add_another_item = input("Invalid input. Want to add another item (y/n)? ").lower()
                if add_another_item == "n":
                    break
            finally:
                with open("grocery_list.csv", 'w') as f:
                    for grocery_item in grocery_items:
                        f.write(f"{grocery_item['quantity']}: {grocery_item['item']}\n")
                    clearscreen()

    elif option == "2":
        clearscreen()
        print("##### Grocery List ######\n\n")
        grocery_items = []
        try:
            with open("grocery_list.csv", 'r') as f:
                check = f.readlines()
            while True:
                item = input("What do you need to buy? ")
                if any(item in line for line in check):
                    print("Item already on the list!")
                    continue
                quantity = input("Quantity: ")
                grocery_items.append({"item": item, "quantity": quantity})
                add_another_item = input("Want to add another item (y/n)? ").lower()
                while add_another_item not in ("y", "n"):
                    add_another_item = input("Invalid input. Want to add another item (y/n)? ").lower()
                if add_another_item == "n":
                    break
        finally:
            with open("grocery_list.csv", 'a') as f:
                for grocery_item in grocery_items:
                    f.write(f"{grocery_item['quantity']}: {grocery_item['item']}\n")
                clearscreen()

    elif option == "3":
        clearscreen()
        time.sleep(1)
        print("##### Grocery List #######\n\n")
        with open("grocery_list.csv", 'r') as f:
            groceries = f.readlines()
        for grocery in groceries:
            print(grocery, end="")
        print("\n\n")
        input("Press Enter to exit")
        clearscreen()

    elif option == "e":
        return
    else:
        print("Select a valid option")


def weather_today():
    clearscreen()
    user = "user.csv"
    user_data = load_data(user)
    user_location = user_data['Location']
    print(user_location)
    url = "http://api.weatherapi.com/v1/current.json?key=9fa62cb2bc3643bab49192638230309&q="+user_location+"&aqi=no"

    response = requests.get(url)
    weather = response.json()

    temp = weather.get("current").get("temp_c")
    condition = weather.get("current").get("condition").get("text")

    print(f"Right now in {user_data['Location']} is {temp} degrees")
    print(f"The weather outside is {condition}")

    input("Press Enter to exit")
    clearscreen()


if __name__ == "__main__":
    main()
