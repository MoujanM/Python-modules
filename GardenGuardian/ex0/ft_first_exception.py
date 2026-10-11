# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 16:45:04 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/13 16:45:17 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
        if temp > 40:
            print(f"Error: {temp}˚C is too hot for plants (max 40˚C)")
        elif temp < 0:
            print(f"Error: {temp}˚C is cold hot for plants (min 0˚C)")
        else:
            print(f"Temperature {temp}˚C is perfect for plants!")
            return temp
    except ValueError:
        # triggers when int() fails
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_input = ["25", "abc", "100", "-50"]
    for i in test_input:
        print(f"Testing temperature: {i}")
        check_temperature(i)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
