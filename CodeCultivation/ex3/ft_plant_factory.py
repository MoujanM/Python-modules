# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 16:01:36 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/05 15:50:44 by mmirdama        ###   ########.fr        #
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
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    my_garden = [Plant(*data) for data in plant_data]
    for i in range(5):
        info = my_garden[i].get_info()
        print(f'Created: {info[0]} ({info[1]}cm, {info[2]}days)')
