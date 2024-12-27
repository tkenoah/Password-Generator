import random
import string
from graphics import *

def password(min_length, letters_only=False, numbers=False, special=False):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation

    check = ""
    if letters_only:
        check = letters
    else:
        check = letters
        if numbers:
            check += digits
        if special:
            check += special_char

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(check)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special_char:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special:
            meets_criteria = meets_criteria and has_special

    return pwd

#One button function
def createButton(win, p1, p2, label):
    button = Rectangle(p1, p2)
    button.setFill("green")
    button.draw(win)
    text = Text(button.getCenter(), label)
    text.draw(win)
    return button

def isButtonClicked(button, point):
    return button.getP1().getX() < point.getX() < button.getP2().getX() and \
           button.getP1().getY() < point.getY() < button.getP2().getY()

def toggleButton(button, state):
    if state:
        button.setFill("lightgreen")
    else:
        button.setFill("red")  

def main():
    win = GraphWin("Password Generator", 600, 500)

    numbers_button = createButton(win, Point(50, 250), Point(150, 300), "Numbers")
    special_button = createButton(win, Point(200, 250), Point(300, 300), "Special")
    normal_button = createButton(win, Point(350, 250), Point(450, 300), "Normal")
    generate_button = createButton(win, Point(200, 350), Point(300, 400), "Generate")
    exit_button = createButton(win, Point(450, 400), Point(550, 450), "Exit")

    output_box = Text(Point(300, 150), "Your password will appear here")
    output_box.setTextColor("white")
    output_box.setSize(16)  
    output_box.draw(win)

    allow_numbers = False
    allow_special = False
    letters_only = True

    toggleButton(numbers_button, allow_numbers)
    toggleButton(special_button, allow_special)
    toggleButton(normal_button, letters_only)

    while True:
        click_point = win.getMouse()  

        if isButtonClicked(numbers_button, click_point):
            allow_numbers = not allow_numbers
            toggleButton(numbers_button, allow_numbers)
            if allow_numbers:  # If Numbers is enabled, Letters turns off
                letters_only = False
                toggleButton(normal_button, letters_only)

        elif isButtonClicked(special_button, click_point):
            allow_special = not allow_special
            toggleButton(special_button, allow_special)
            if allow_special:  # If Special is enabled, Letters turns off
                letters_only = False
                toggleButton(normal_button, letters_only)

        elif isButtonClicked(normal_button, click_point):
            letters_only = not letters_only
            toggleButton(normal_button, letters_only)
            if letters_only:  # If Letters is enabled, Numbers and Special turn off
                allow_numbers = False
                allow_special = False
                toggleButton(numbers_button, allow_numbers)
                toggleButton(special_button, allow_special)

        elif isButtonClicked(generate_button, click_point):
            min_length = 8 
            pwd = password(min_length, letters_only, allow_numbers, allow_special)
            output_box.setText(f"Generated Password: {pwd}")

        elif isButtonClicked(exit_button, click_point):
            win.close()
            break

main()