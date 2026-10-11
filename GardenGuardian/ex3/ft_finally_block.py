# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_finally_block.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 16:45:35 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/13 16:46:09 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    err_msg = "Error: Cannot water None - invalid plant!"
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(err_msg)
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    clean_plant_list = ["tomato", "lettuce", "carrots"]
    error_plant_list = ["tomato", None, "beans"]
    tests = [clean_plant_list, error_plant_list]

    print("=== Garden Watering System ===", end='\n\n')
    for test in tests:
        print("Testing normal watering..." if test is clean_plant_list
              else "Testing with error...")
        try:
            water_plants(test)
        except ValueError as e:
            print(f"{e}")
        finally:
            if test is clean_plant_list:
                print("Watering completed successfully!", end='\n\n')
            else:
                print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
