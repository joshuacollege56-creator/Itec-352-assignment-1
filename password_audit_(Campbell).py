#asks how many passwrods the user wants to audit 
def get_password_count():
    while True:
        try:
            number = int(input("How many passwords would you like to audit?: "))
            #checks if the number is greater than zero and a actual number
            if number > 0:
                return number
            else:
                print("Please enter a whole number greater than zero.")

        except ValueError:
            print("Please enter a whole number greater than zero.")

#checks the password what values the password has

def evaluate_password(password):
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    #changes the value based on the values given
    for character in password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special = True

    type_total = 0

    if has_uppercase:
        type_total += 1

    if has_lowercase:
        type_total += 1

    if has_digit:
        type_total += 1

    if has_special:
        type_total += 1

    if len(password) >= 12 and type_total == 4:
        return "Strong"
    elif len(password) >= 8 and type_total >= 3:
        return "Moderate"
    else:
        return "Weak"

    #shows number of strong, moderate, and weak passswords.
def display_summary(strong_count, moderate_count, weak_count):
    print()
    print("---------- AUDIT SUMMARY ----------")
    print()
    print("Strong passwords:", strong_count)
    print("Moderate passwords:", moderate_count)
    print("Weak passwords:", weak_count)


def main():
    strong_count = 0
    moderate_count = 0
    weak_count = 0

    password_count = get_password_count()

    for password_number in range(1, password_count + 1):
        password = input("Password " + str(password_number) + ": ")

        rating = evaluate_password(password)

        print("Rating:", rating)

        if rating == "Strong":
            strong_count += 1
        elif rating == "Moderate":
            moderate_count += 1
        else:
            weak_count += 1

    display_summary(strong_count, moderate_count, weak_count)


if __name__ == "__main__":
    main()