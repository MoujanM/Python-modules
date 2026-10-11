# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 16:45:21 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/13 16:45:22 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def garden_operations(operation: str, data=None) -> None:
    """
    'Engine' Function that takes given data and does
    transformation based on operation specified.
    """
    if operation == "get_int":
        res = int(data)
    elif operation == "divide":
        res = 100 / data
    elif operation == "file":
        res = open(data, 'r')
        res.close()
    elif operation == "find_value":
        res = {}[data]
    return res


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    test_tasks = [
        (ValueError, "ValueError", "get_int", "abc"),
        (ZeroDivisionError, "ZeroDivisionError", "divide", 0),
        (FileNotFoundError, "FileNotFoundError", "file", "missing.txt"),
        (KeyError, "KeyError", "find_value", "missing_plant")
    ]
    for task in test_tasks:
        error_type, label, operation, data = task
        print(f"Testing {label}...")
        try:
            garden_operations(operation, data)
        except error_type as e:
            print(f"Caught {label}: {e}", end='\n\n')
    print("Testing multiple errors together...")
    try:
        garden_operations("get_int", "Oo0ps")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but the program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
