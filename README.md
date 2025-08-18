# Ticket Vending System

This repository contains a simple console code that simulates a ticket vending machine. It has three distinct versions, each with a different level of user interaction and functionality. The application manages the sale of 50 tickets(customizable) and confirms when all seats are full.

-----

### Version 2: Multiple Seat Booking
#### ticket_vending_v2.py

This is the an advanced version. It allows a single user to buy multiple seats in a single transaction. The program asks for the number of seats desired and then books them all under one name. It also includes robust error handling to prevent crashes.

**Features:**

  * Asks the user how many seats they want to purchase.
  * Books multiple seats under a single name.
  * **Input Validation:** Handles non-numeric input and requests for more seats than are available.
  * Provides a single confirmation message for all booked seats, with a singular "seat number is" or plural "seat numbers are" based on the quantity.  
  * Prints a "House Full" message when all seats are sold.  

-----

### Version 1: One-by-One Booking
#### ticket_vending_v1.py

In this version, the user is required to provide a name for each seat. The program books one seat at a time, and the user must enter a name for each of the 50 available seats.

**Features:**

  * Requires a name for each seat.
  * Confirms each seat booking individually with a personalized message.
  * A user can only book one seat per interaction.
  * Prints a "House Full" message when all seats are sold.

-----

### How to Run the Code

1.  **Save the file:** Save the code for any of the versions as a Python file (e.g., `vending_machine_v3.py`).
2.  **Open your terminal:** Navigate to the directory where you saved the file.
3.  **Run the program:** Execute the following command:
    ```
    python vending_machine_v3.py
    ```
    **Use a Code Editor:** You can alternatively use code editors like VSCode, etc. to run the file.

-----
### Future Enhancements/Features

  * Adding a graphical user interface (GUI).
  * Implementing a database to store ticket sales.
  * Adding features like ticket cancellation or refunds, and more!

Feel free to suggest any features. I appreciate your ideas!

### About the Project

This project is a command-line ticket vending system I built in Python to showcase my foundational programming skills. This is the initial command-line version, and I plan to regularly update the repository with new & efficient versions, as I learn and grow. The next major milestone will be developing a Graphical User Interface, transforming the project from a command-line tool into a complete application.


* **Author:**[Abhijith K S](https://github.com/iabhijithks)


* Last Updated on 18/08/2025
