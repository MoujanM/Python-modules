# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_cooordinate_system.py                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 19:14:12 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/23 14:38:37 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import math


def calculate_distance(p1: tuple, p2: tuple) -> float:
    distance = math.sqrt(
        ((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2)
        + ((p2[2] - p1[2])**2))
    return distance


def parse_strin(coord_str: str) -> tuple:
    coords = coord_str.split(",")
    return tuple(int(p) for p in coords)


def coordinate_system():
    print("=== Game Coordinate System ===", end='\n\n')

    # initial coordinate creation demo
    if len(sys.argv) == 4:
        # list of nums given
        pos_lst = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
    elif len(sys.argv) == 2 and sys.argv[1][0]:
        pos_lst = parse_strin(sys.argv[1])
    else:
        # revert to default nums for demo
        pos_lst = (10, 20, 5)
    pos_created = tuple(pos_lst)
    print(f"Position created: {pos_created}")

    origin_pos = (0, 0, 0)
    distance = calculate_distance(pos_created, origin_pos)
    print(f"Distance between {origin_pos} and {pos_created}: {distance:.2f}")
    print()

    # parsing demo
    pos = "3,4,0"
    print(f"Parsing coordinates: {pos}")
    parsed = parse_strin(pos)
    print(f"Parsed position: {parsed}")
    distance = calculate_distance(parsed, origin_pos)
    print(f"Distance between {origin_pos} and {parsed}: {distance:.1f}")
    print()

    # error handling demo
    invalid_pos = "abc,def,ghi"
    print(f"Parsing invalid coordinates: {invalid_pos}")
    try:
        parse_strin(invalid_pos)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
    print()

    # unpacking demo
    print("Unpacking demonstation:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    coordinate_system()
