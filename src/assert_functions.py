from colorama import init

init()
from colorama import Fore, Style


def assert_equals_bool(message, expected, computed):
    if expected == computed:
        print_ok(message)
    else:
        print_error(message + " Expected " + str(expected) + " but found " + str(computed))


def assert_equals_arr(message, expected, computed):
    if expected == computed:
        print_ok(message)
    else:
        print_error(message + " Expected "
                    + str(expected) + " but found " + str(computed))


def assert_equals_int(message, expected, computed):
    if expected == computed:
        print_ok(message)
    else:
        print_error(message + " Expected " + str(expected) + " but found " + str(computed))


def assert_equals_arr_twod(message, expected, computed):
    if len(expected) != len(computed):
        print_error(message + " Expected has length " + str(len(expected))
                    + " but computed has " + str(len(computed)))
        return

    for i in range(len(computed)):
        for j in range(len(computed[i])):
            if computed[i][j] != expected[i][j]:
                print_error("\tElement in row " + str(i) + " and column " + str(j) + " of expected is " + str(
                    expected[i][j]) + " in computed is " + str(computed[i][j]))
                return
    print_ok(message)


def assert_equals_str(message, expected, computed):
    if expected == computed:
        print_ok(message)
    else:
        print_error(message + " Expected " + str(expected) + " but found " + str(computed))


# Colorize
ANSI_RESET = Style.RESET_ALL
ANSI_RED = Fore.RED
ANSI_GREEN = Fore.GREEN
ANSI_BLUE = Fore.BLUE


def print_info(message):
    print(ANSI_BLUE + message + ANSI_RESET)


def print_ok(message):
    print(ANSI_GREEN + "OK: " + message + ANSI_RESET)


def print_error(message):
    print(ANSI_RED + "ERROR: " + message + ANSI_RESET)


def print_bar():
    print("-----------------------------------------------------")



