# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 16:46:27 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/13 17:12:14 by mmirdama        ###   ########.fr        #
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
    def __init__(self, message="Not enough water in the tank!") -> None:
        super().__init__(message)


class GardenManager:

    @staticmethod
    def add_plants(plant: str) -> None:
        err_msg = "Plant name cannot be empty!"
        if plant == "":
            raise GardenError(err_msg)
        print(f'Added {plant} successfully')

    @staticmethod
    def water_plants(plant_list: list) -> None:
        print("Opening watering system")
        err_msg = "Error: Cannot water None - invalid plant!"
        try:
            for plant in plant_list:
                print(f"Watering {plant} - success")
                if plant is None:
                    raise WaterError(err_msg)
        except WaterError as e:
            print(f'{e}')
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant_name: str, water_level: int,
                           sunlight_hours: int):
        if plant_name == "":
            msg = "Plant name cannot be empty!"
            raise GardenError(msg)
        elif water_level < 1:
            msg = f"Water level {water_level} is too low (min 1)"
            raise WaterError(msg)
        elif water_level > 10:
            msg = f"Water level {water_level} is too high (max 10)"
            raise WaterError(msg)
        elif sunlight_hours < 2:
            msg = f"Sunlight hours {sunlight_hours} is too low (min 2)"
            raise GardenError(msg)
        elif sunlight_hours > 12:
            msg = f"Sunlight hours {sunlight_hours} is too high (max 12)"
            raise GardenError(msg)
        else:
            print(
                f"{plant_name}: healthy (water: {water_level},"
                f" sun: {sunlight_hours})")


def test_garden_management():
    print("=== Garden Management System ===", end='\n\n')
    plant_list = ["tomato", "lettuce", ""]
    print("Adding plants to garden...")
    try:
        for plant in plant_list:
            GardenManager.add_plants(plant)
    except GardenError as e:
        print(f"Error adding plant: {e}")
    print()
    print("Watering plants...")
    GardenManager.water_plants(["tomato", "lettuce"])
    print()
    print("Checking plant health...")
    health_check = [
        ("tomato", 5, 8),
        ("lettuce", 15, 7)
    ]
    for plant in health_check:
        try:
            GardenManager.check_plant_health(*plant)
        except GardenError as e:
            print(f"Error checking {plant[0]}: {e}")
    print()
    print("Testing error recovery...")
    try:
        raise WaterError
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
