# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 16:52:09 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/05 16:54:31 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class SecurePlant:
    """
    Secure class for plants; protects and encapsulate sensitive data.

    Attributes
    ----------
        name : str
            plant name
        height : int
            height of plant in cm (must be +)
        age : int
            age of plant in days (must be + and possible)
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Constructs all attributes for SecurePlant, incl. encapsulated
        age and height values.

        Attributes
        ----------
            name: str
                plant name
            height: int
                plant height in cm - must be positive through validation
            age: int
                plant age in days - must be positive through validation
        Notes
        -----
        Sets __height and __age to 0, and calls setters to safely guard against
        invalid values.
        """
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """
        Function to provide controlled way to modify plant height.
        Checks if entered data is valid (> 0) and
        prints error message when invalid values attempted.
        """
        if height >= 0:
            self.__height = height
            print(f'Height updated: {height}cm [OK]')
        else:
            print(f'Invalid operation attempted: height {height}cm [REJECTED]')
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """
        Function to provide controlled way to modify plant age.
        Checks if entered data is valid (> 0) and
        prints error message when invalid values attempted.
        """
        if age >= 0:
            self.__age = age
            print(f'Age updated: {age} days [OK]')
        else:
            print(f'Invalid operation attempted: age {age}days [REJECTED]')
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        """Safe way to access plant height through encapsulation."""
        return self.__height

    def get_age(self) -> int:
        """Safe way to access plant height through encapsulation."""
        return self.__age


if __name__ == "__main__":
    plant = SecurePlant("Rose", 10, 5)
    print("=== Garden Security System ===")
    print(f'Plant created: {plant.name}')
    plant.set_height(25)
    plant.set_age(30)

    # plant.set_height(-5)
    for h in range(-5, -6, -1):
        plant.set_height(h)

    info = f'({plant.get_height()}cm, {plant.get_age()} days)'

    print(f'Current plant: {plant.name} {info}')
