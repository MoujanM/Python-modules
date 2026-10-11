# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 13:57:08 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/05 15:16:08 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """
    Class representing blueprint of all plants.

    Attributes
    ----------
    name : str
        plant name
    height : int
        height of plant in cm
    age : int
        age of plant in days
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Constructs all necessary attributes for Plant object.

        Parameters
        ----------
        name : str
            plant name
        height : int
            height of plant in cm
        age : int
            age of plant in days
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    my_garden = [plant1, plant2, plant3]

    print("=== Garden Plant Registry ===")
    for plant in my_garden:
        print(f'{plant.name}: {plant.height}cm, {plant.age} days old')
    print("=== End of Program ===")
