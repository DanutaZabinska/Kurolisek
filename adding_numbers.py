def give_first_number():
    # Ask user for first number
    first_number = int(input("Enter first integer number: "))
    return first_number


def give_second_number():
    # Ask user for second number
    second_number = int(input("Enter second integer number: "))
    return second_number


given_first = give_first_number()
given_second = give_second_number()


# Add to numbers and print numbers with their sum
def print_sum_and_user_numbers(first, second):
    sum = first + second
    print("Hello! you enter {}".format(first), "and {}".format(second), "so the sum is {}".format(sum))


print_sum_and_user_numbers(given_first, given_second)