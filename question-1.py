"""
Question 1
Group Name: DAN/EXT 55
Group Members:
Thuy Chuong Duong - S385201
Kar Keat Koh - S394886
Joshua Joseph Bargamento - S394292
Sihao Cui - S399370
"""
def check_password_strength():
    password = input("Enter your password: ")
    length = len(password)

    has_digit = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    if length > 10 and has_digit and has_upper:
        print("Strong password")

    elif 6 <= length <= 10 and has_digit:
        print("Medium password")

    else:
        print("Weak password")


# Run the program
if __name__ == "__main__":
    check_password_strength()