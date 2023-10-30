# DAY-2-DAY Home Assistant


#### Description:
Welcome to the Day-2-Day Home Assistant, a program designed to simplify your daily routine. This project aims to provide a user-friendly interface for managing tasks, organizing shopping lists, and staying updated on the current weather. In this README, we'll delve into the project's structure, functionalities, and design choices.


### Project Structure:

- **main.py:**
  - This is the main script that orchestrates the entire Day-2-Day Home Assistant. It contains the `main()` function, which serves as the entry point. The function initializes the program, loads user data, and presents the user with a menu to choose from various features:
    * *(1) A To-Do List that allows you to create a list of tasks for your day. You can later edit this list to add more tasks or print it for your convenience.* *
    * *(2) A Grocery List that allows you to create a shopping list for your visit to the supermarket. It prompts you to register any number of items and their respective quantities, and also warns you if a certain item is already on the list. Later, you can access the complete list.* *
    * *(3) A weather report that uses the location registered in your first login to return the temperature and the current weather condition to you.* *

- **user.csv:**
  - The `user.csv` file stores user information, such as the user's name and location. This information is essential for personalizing the weather report feature based on the user's location.

- **to_do_list.txt:**
  - This file is dedicated to storing the user's to-do list. The `to_do_list()` function in `main.py` allows users to create, edit, and read their to-do lists.

- **grocery_list.csv:**
  - The `grocery_list.csv` file stores the user's grocery list, including items and their respective quantities. The `grocery_list()` function in `main.py` enables users to manage their shopping lists seamlessly.


### Design Choices:

- **Console-Based Interface:**
  - The project utilizes a console-based interface to ensure simplicity and accessibility. This design choice allows users to interact with the Day-2-Day Home Assistant without the need for a complex graphical user interface.

- **Data Storage:**
  - User data, including name and location, is stored in a CSV file (`user.csv`). Task and grocery lists are stored in text and CSV files (`to_do_list.txt` and `grocery_list.csv`, respectively). This file-based storage approach was chosen for its simplicity and ease of implementation.

- **Real-time Weather API:**
  - The weather report feature fetches real-time weather information using the WeatherAPI. This decision was made to provide users with accurate and up-to-date weather details based on their specified location.


### Usage:

   - Run `program.py` to launch the Day-2-Day Home Assistant.
   - Follow on-screen prompts to provide your name and location on the first use.
   - Choose from the menu options to manage your to-do list, grocery list, or check the weather.

Feel free to explore the features of the Day-2-Day Home Assistant and integrate it into your daily routine. If you have any questions or suggestions, we'd love to hear from you!
