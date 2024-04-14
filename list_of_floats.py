
list_of_floats = [2.2, 4.4, 5.5, 7.7]


def average(list_f):
    return sum(list_f) / len(list_f)


average(list_of_floats)
average_from_list = average(list_of_floats)


def print_average(ave):
    print("The average of list containing{}".format(list_of_floats), "is {}".format(ave))


print_average(average_from_list)