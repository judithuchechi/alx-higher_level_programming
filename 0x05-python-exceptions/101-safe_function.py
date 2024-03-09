#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    Execute a function safely, handling exceptions.

    Parameters:
    - fct: The function to be executed.
    - *args: Variable number of arguments to pass to the function.

    Returns:
    - The result of the function execution if successful, or an error message if an exception occurs.
    """
    try:
        result = fct(*args)
        return result
    except Exception as error:
            print("Exception: {}".format(error), file=sys.stderr)
