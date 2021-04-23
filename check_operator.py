def check_operator(message):
    while True:
        user_input = input(message)
        if user_input == '+' or user_input == '-' or user_input == '*' or user_input == '/':
            return user_input
        else:
            print("Enter the valid Operator")

