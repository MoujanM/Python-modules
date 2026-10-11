# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/18 15:59:41 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/23 16:08:14 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def build_dict(arg_lst: list) -> dict:
    """Create inventory dict from list of input."""
    inventory = {}

    for arg in arg_lst:
        name = ""
        quantity = ""
        colon = False

        for char in arg:
            if char == ":":
                colon = True
                continue
            if not colon:
                name += char
            else:
                quantity += char

        if name and quantity:
            inventory[name] = int(quantity)
    return (inventory)


def inventory_system():
    if len(sys.argv) < 2:
        input_dict = {'pixel_sword': 1, 'code_bow': 2, 'health_byte': 1,
                      'quantum_ring': 4}
    elif len(sys.argv) > 2:
        arg_list = sys.argv[1:]
        input_dict = build_dict(arg_list)

    inventory = {
                "Moderate": {},
                "Scarce": {}
                }
    for name, qty in input_dict.items():
        if qty <= 3:
            inventory["Scarce"][name] = qty
        else:
            inventory["Moderate"][name] = qty

    print("=== Inventory System Analysis ===")
    total_count = 0
    for count in input_dict.values():
        total_count += count

    print(f"Total items in inventory: {total_count}")
    print(f"Unique item types: {len(input_dict)}")
    print()

    # sort keys and values list for later use
    keys = []
    for name in input_dict.keys():
        keys += [name]

    values = []
    for value in input_dict.values():
        values += [value]
    values_str = ""
    for i in range(len(values)):
        values_str += str(values[i])
        if i < len(values) - 1:
            values_str += ", "

    n = len(keys)
    for i in range(n):
        max_indx = i
        for j in range(i + 1, n):
            if input_dict[keys[j]] > input_dict[keys[max_indx]]:
                max_indx = j
        keys[i], keys[max_indx] = keys[max_indx], keys[i]

    most = keys[0]
    min_val = input_dict[keys[-1]]
    least = keys[-1]

    origin_order = []
    for k in input_dict.keys():
        origin_order += [k]

    for name in origin_order:
        if input_dict[name] == min_val:
            least = name

    print("=== Current Inventory ===")
    # loop over sorted keys
    for name in keys:
        qty = input_dict[name]
        percentage = (qty / total_count) * 100 if total_count > 0 else 0
        unit_str = "units" if qty > 1 else "unit"
        print(f"{name}: {qty} {unit_str} ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    unit_str = "units" if input_dict[least] > 1 else "unit"
    print(f"Most abundant: {most} ({input_dict[most]} units)")
    print(f"Least abundant: {least} ({input_dict[least]} {unit_str})")

    print("\n=== Item Categories ===")
    for item, value in inventory.items():
        print(f"{item}: {value}")

    print("\n=== Management Suggestions ===")
    restock_lst = []
    for name in origin_order:
        if input_dict[name] <= 1:
            restock_lst += [name]
    restock_str = ", ".join(restock_lst)
    print(f"Restock needed: {restock_str}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {", ".join(keys)}")
    print(f"Dictionary values: {values_str}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in input_dict}")


if __name__ == "__main__":
    inventory_system()
