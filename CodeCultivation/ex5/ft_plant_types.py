# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 17:19:14 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/05 17:01:54 by mmirdama        ###   ########.fr        #
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

    def get_info(self) -> str:
        """
        Function to access information about any plant's status.
        Returns
        -------
            String containing plant type and attributes
        """
        class_type = self.__class__.__name__
        return f'{self.name} ({class_type}): {self.height}cm, {self.age} days'

    def special_info(self) -> str:
        """Placeholder for child-specific functions"""
        pass


class Flower(Plant):
    """
    Specialized child class of Plants, representing blueprint of Flowers.

    Attributes
    ----------
        name : str
            plant name
        height : int
            height of plant in cm
        age : int
            age of plant in days
        color: str
            speciliazed attribute
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Constructs all necessary attributes for Plant object.
        Calls super() to set up inherited basic features.

        Parameters
        ----------
            name : str
                plant name
            height : int
                height of plant in cm
            age : int
                age of plant in days
            color: str
                speciliazed attribute
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        """Specialised function returns bloom status."""
        return f'{self.name} is blooming beautifully!'

    def get_info(self) -> str:
        """Builds on Plant function to add Flower-specific info."""
        generic_info = super().get_info()
        return f"{generic_info}, {self.color} color"

    def special_info(self) -> str:
        """Plant's generic placeholder is replaced by child info."""
        return self.bloom()


class Tree(Plant):
    """
    Specialized child class of Plants, representing blueprint of Trees.

    Attributes
    ----------
        name : str
            plant name
        height : int
            height of plant in cm
        age : int
            age of plant in days
        trunk_diameter : int
            speciliazed attribute
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """
        Constructs all necessary attributes for Plant object.
        Calls super() to set up inherited basic features.

        Parameters
        ----------
            name : str
                plant name
            height : int
                height of plant in cm
            age : int
                age of plant in days
            trunk_diameter : int
                speciliazed attribute
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        """
        Specialised function that calculates shade area
        and returns str statement.
        """
        shade = 3.14 * ((self.height / 100) ** 2)
        return f'{self.name} provides {shade} square meteres of shade'

    def get_info(self) -> str:
        """Builds on Plant function to add Tree-specific info."""
        generic_info = super().get_info()
        return f"{generic_info}, {self.trunk_diameter}cm diameter"

    def special_info(self) -> str:
        """Plant's generic placeholder is replaced by child info."""
        return self.produce_shade()


class Vegetable(Plant):
    """
    Specialized child class of Plants, representing blueprint of Trees.

    Attributes
    ----------
        name : str
            plant name
        height : int
            height of plant in cm
        age : int
            age of plant in days
        harvest_season : str
            season vegetable can be harvested
        nutritional_value : str
            vegetable's nutritional value
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """
        Constructs all necessary attributes for Plant object.
        Calls super() to set up inherited basic features.

        Parameters
        ----------
            name : str
                plant name
            height : int
                height of plant in cm
            age : int
                age of plant in days
            harvest_season : str
                season vegetable can be harvested
            nutritional_value : str
                vegetable's nutritional value
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition(self) -> str:
        """Specialized function to return nutrition."""
        return f'{self.name} is rich in {self.nutritional_value}'

    def get_info(self) -> str:
        """Builds on Plant function to add Tree-specific info."""
        generic_info = super().get_info()
        return f"{generic_info}, {self.harvest_season} harvest"

    def special_info(self) -> str:
        """Plant's generic placeholder is replaced by child info."""
        return self.get_nutrition()


if __name__ == "__main__":
    plant1 = Flower("Rose", 25, 30, "red")
    plant2 = Tree("Oak", 500, 1825, 50)
    plant3 = Vegetable("Tomato", 80, 90, "summer", "vitamic C")
    my_garden = [plant1, plant2, plant3]
    print("=== Garden Plant Types ===")
    for i in range(3):
        plant = my_garden[i]
        print(plant.get_info())
        print(plant.special_info())
        print()
