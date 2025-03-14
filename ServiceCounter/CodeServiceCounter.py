# Project: Service Counter
# Author: Nathan Sayphrarath
# Email: nsayphrarath2709522@woonsocketschools.com
# Date: 3-12-2025
# Description: I'm making an app for the WACTC Garage

import time, os


Cost = 0
tax = 0
grandTotal = 0
isShopping = True

while isShopping is True:

    print("Welcome to the WACTC Garage!")  # Welcome
    print()

    name = input("What is your name?:")  # Asking name
    print()
    time.sleep(1)
    print(f"Hello {name}!")
    print()

    make_Model = input("What is the make and model of your vehicle?: ")  # Asking the make and model

    mileage = input("Okay so what is the mileage on your car?:")  # Asking for mileage
    print()
    time.sleep(1)

    service = input("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Great! So here is a list of our available services:

    1.Oil Change and tire Rotation:

    A.$79.99 for oil and filter change
    B.$30.00 for standard tyres
    C.$45.00 for 4WD or Truck tyres

    2.Brake Pads and Front End Alignment:

    D.$120 for the package

    3.Broken Glass Repair:

    E.$69.99 for a large window
    F.$39.99 for a small window

    4. Dent Removal:

    G.$5 per small dent
    H.$10 per large dent 

    PLEASE make sure you use the numbers and letters to choose what you want.

    (Ex. If you want a Broken glass repair for a large window, you would put 3E.)

    What would you like?:
    """)

    if service == "1A":
        Cost = Cost + 79.99
        tax = Cost * 0.1  # Assumaing tax is 10%
        grandTotal = Cost + tax
    elif service == "1B":
        Cost = Cost + 30
        tax = Cost * 0.1
        grandTotal = Cost + tax
    elif service == "1C":
        Cost = Cost + 45
        tax = Cost * 0.1
        grandTotal = Cost + tax
    elif service == "2D":
        Cost = Cost + 120
        tax = Cost * 0.1
        grandTotal = Cost + tax
    elif service == "3E":
        Cost = Cost + 69.99
        tax = Cost * 0.1
        grandTotal = Cost + tax
    elif service == "3F":
        Cost = Cost + 39.99
        tax = Cost * 0.1
        grandTotal = Cost + tax
    elif service == "4G":
        time.sleep(1)
        smallDents = int(input("How many small dents would you like to remove?:"))
        Cost = Cost + smallDents * 5
        tax = Cost * 0.1
        grandTotal = Cost + tax
    elif service == "4H":
        time.sleep(1)
        largeDents = int(input("How many large dents would you like to remove:"))
        Cost = Cost + largeDents * 10
        tax = Cost * 0.1
        grandTotal = Cost + tax
    else:
        print("Wrong Input")




    time.sleep(3)

    print()
    
    print("""
    ==================================
    Customer Invoice
    ==================================
    """)
    print(f"Customer Name:{name}")
    print("Location: WACTC Garage")
    print()
    print("Items Purchased")
    print("---------------------------------")
    print(f"Item:{service}")
    print(f"Price:{Cost}")
    print("---------------------------------")
    print(f"Subtotal:{Cost}")
    print(f"Tax:{tax}")
    print(f"Grand Total:{grandTotal}")
    print("==================================")
    print("THANK YOU FOR YOUR BUSINESS")
    isShopping = False














