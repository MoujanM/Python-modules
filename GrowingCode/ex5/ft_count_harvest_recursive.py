def ft_count_harvest_recursive(current_day=1, days_max=None):
    if days_max is None:
        days_max = int(input("Days until harvest: "))
    if current_day > days_max:
        print("Harvest time!")
        return
    else:
        print("Day ", current_day)
        ft_count_harvest_recursive(current_day + 1, days_max=days_max)

# ft_count_harvest_recursive()
