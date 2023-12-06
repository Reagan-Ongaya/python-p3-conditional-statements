#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    password_input = get_password_input()
    if (username.lower() == "admin" or username.upper() == "ADMIN") and password == "12345":
        return "Access granted"

    else:
        "Access denied"

def get_password_input():
    return input("Enter password: ")

def hows_the_weather(temperature):
    # your code here
    if temperature <= 35 :
        print( "It's brisk out there!")
        return "It's brisk out there!"
    
    elif 40>= temperature <= 65:
        print("It's a little chilly out there!")

    elif temperature > 85:
        print("It's to dang hot out there!")

    else:
        print("It's perfect out there!")


def fizzbuzz(number):
    # your code here
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print( number)
            


def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 != 0:  
            print(num1 / num2)
        else:
            print("Error: Division by zero!")
            return None
    else:
        print("Invalid operation!")
        return None

