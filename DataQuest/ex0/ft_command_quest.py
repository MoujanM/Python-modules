# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_command_quest.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 19:10:42 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/23 14:32:22 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def command_quest():
    print("=== Command Quest ===")
    name = sys.argv[0]
    n = len(sys.argv)
    if n == 1:
        print("No arguments provided")
        print(f"Progam name: {name}")
        print(f"Total arguments: {n}")
    elif n > 1:
        print(f"Progam name: {name}")
        print(f"Arguments received: {n - 1}")
        for i in range(1, n):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {n}")


if __name__ == "__main__":
    command_quest()
