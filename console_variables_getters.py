error_variable = "\nPodałeś niewłaściwą wartość, wpisz ją ponownie.\n"

def get_float_value(input_question):
    while True:
        try:
            x = float(input(input_question))
            return x
        except ValueError:
            print(error_variable)


def get_int_value(input_question):
    while True:
        try:
            x = int(input(input_question))
            return x
        except ValueError:
            print(error_variable)


def get_str_value(input_question):
    x = input(input_question).lower()
    return x
