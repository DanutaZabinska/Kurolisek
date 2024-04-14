def give_me_name():
    # Ask user for name
    user_name = input("Enter your name: ")
    return user_name


def give_me_age():
    # Ask user for age
    user_age = input("Enter your age: ")
    return user_age


given_name = give_me_name()
given_age = give_me_age()


# Print data from user
def print_user_info(name, age):
    print("Hello {}!".format(name), "you are {}".format(age))


print_user_info(given_name, given_age)