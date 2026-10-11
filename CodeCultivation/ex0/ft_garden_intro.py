# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/02 13:56:28 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/05 14:59:23 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def plant_info(name: str, height: int, age: int) -> None:
    """Function to display information for a plant"""
    print("=== Welcome to My Garden ===")
    print(f'Plant: {name}')
    print(f'Height: {height}cm')
    print(f'Age: {age} days')
    print("=== End of Program ===")


if __name__ == "__main__":
    name = "Rose"
    height = 25
    age = 30
    plant_info(name, height, age)
