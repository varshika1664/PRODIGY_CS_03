import string
import getpass

def check_pwd():
    # Prompt requesting a User to type in a password..
    password = getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    # Typed password is crossed referenced against desired characters on at least the existence of one desired character
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count +=1
        else:
            special_count += 1

    # Depending on presence of an existing desired character the strength is then gauged.
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    # depending on results the gathered from the strength ratings, a remark is given to show the user the complexity strength of the password
    if strength == 1:
        remarks = " Poor Password, Improve Password Strength"
    elif strength == 2:
        remarks = "Not a Good Password, Improve Password Strength"
    elif strength == 3:
        remarks = "Good Password, but Not Strong"
    elif strength == 4:
        remarks = " It's a hard password but can be better"
    elif strength == 5:
        remarks = " Very Strong password"

    # statistics of the number of desired characters in the submitted password
    print('Your password has: ')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    # Display of the level of strength of the password from 1 to 5, 1 being very poor and 5 being very strong
    print(f"Password Strength: {strength}")
    print(f"Hint: {remarks}")


# Function requesting a User to test another Password or exit the program
def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice=input('Do you want to enter another pwd (y/n): ')
    else:
        choice=input('Do you want to check pwd strength (y/n): ')

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print('Remember to make strong passwords and do not share them. Stay CYBER SMART!!')
            return exit()
        else:
            print('Invalid, Try Again')
            return ask_pwd()

if __name__ == '__main__':
    print('Welcome to My Password Complexity Checker')
    print('Prodigy Infotech task 03 by: Varshika Srivastava CS Intern')
    ask_pss = ask_pwd()
    while check_pwd:
        check_pwd()
        ask_pss = ask_pwd(True)