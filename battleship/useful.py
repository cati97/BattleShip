import os  # for os.system("clear") - clearing the screen


def clear():
    os.system('clear')  # works only when run in the terminal


#  input validation
def validate_letter(letter):
    valid_letters = ["A", "B", "C", "D", "E", "F", "G"]

    while letter.upper() not in valid_letters:
        print("Incorrect input! Try again(letter A-G)")
        letter = input("Letter: ")
        if letter not in valid_letters:
            continue
        else:
            return letter
    else:
        return letter


def validate_number(number):  # a string 9
    while True:
        try:
            number = int(number)
        except ValueError:
            print("Input is not a number! Try again(number 1-7)")
            number = input("Number: ")
            continue
        else:  # we go here if try statement is a success
            while number not in range(1, 8):  # 1-7
                print("Try again in range 1-7 !")
                number = input("Number: ")  # 2
                number = int(number)
                if number not in range(1, 8):
                    continue
                else:
                    break
            else:
                break
        break

    return number


def validate_direction(direction):
    valid_directions = ['H', 'V']
    direction = direction.upper()
    while direction not in valid_directions:
        print("Invalid direction! Try again.")
        direction = input("Horizontally(h) or Vertically (v): ")
        if direction not in valid_directions:
            continue
        else:
            return direction
    else:
        return direction


def validate_amount_ships(amount):
    while True:
        try:
            amount = int(amount)
        except ValueError:
            print("Input is not a number! Try again")
            amount = input("Please choose the amount of ships from 2 to 5: ")
            continue
        else:  # we go here if try statement is a success
            while amount not in range(2, 6):  # 2-5
                print("Try again in range 2-5 !")
                amount = input("Please choose the amount of ships from 2 to 5: ")
                amount = int(amount)
                if amount not in range(2, 6):
                    continue
                else:
                    break
            else:
                break
        break

    return amount

