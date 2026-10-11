# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 13:57:49 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/05 15:29:28 by mmirdama        ###   ########.fr        #
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
    def __init__(self, name: str, height: int, age: int) -> None:
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

    def grow_tall(self) -> None:
        """Function to simulate plant growth"""
        self.height += 1

    def grow_old(self) -> None:
        """Function to simulate plant aging"""
        self.age += 1

    def get_info(self) -> tuple:
        """
        Function to access information about current plant status.
        Returns
        -------
            tuple containing plant attributes
        """
        return (self.name, self.height, self.age)


if __name__ == "__main__":
    """Simulate growth of a plant over a week"""
    my_plant = Plant("Rose", 25, 30)
    plant_info = my_plant.get_info()
    print("=== Day 1 ===")
    print(f'{plant_info[0]}: {plant_info[1]}cm, {plant_info[2]} days old')
    h1 = plant_info[1]
    i = 1
    for i in range(1, 7):
        my_plant.grow_tall()
        my_plant.grow_old()
        i += 1
    new_info = my_plant.get_info()
    h2 = new_info[1]
    print('=== Day 7 ===')
    print(f'{new_info[0]}: {new_info[1]}cm, {new_info[2]} days old')
    print(f'Growth this week: +{h2 - h1}cm')
