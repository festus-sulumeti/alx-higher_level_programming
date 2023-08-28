#!/usr/bin/python3

   """Printing  an integer with "{:d}".format().

    Args:
        value (int): The integer being printed.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
