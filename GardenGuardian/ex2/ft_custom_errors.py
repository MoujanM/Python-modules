# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_custom_errors.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 16:45:29 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/13 16:45:30 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, plant: str) -> None:
        message = f"The {plant} plant is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, water: str) -> None:
        message = "Not enough water in the tank!"
        super().__init__(message)


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===", end='\n\n')
    tests = [
        (PlantError, "PlantError", "tomato"),
        (WaterError, "WaterError", "water"),
        ]
    for test in tests:
        error_type, label, inputs = test
        print(f"Testing {label}...")
        try:
            raise error_type(inputs)
        except error_type as e:
            print(f"Caught {label}: {e}", end='\n\n')
    problems = [PlantError("tomato"), WaterError("water")]
    print("Testing catching all garden errors...")
    for problem in problems:
        try:
            raise problem
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
