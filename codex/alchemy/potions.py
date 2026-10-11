
def healing_potion() -> str:
    from .elements import create_fire, create_water
    recipe = f"{create_fire()} and {create_water()}"

    return f"Healing potion brewed with {recipe}"

def strength_potion() -> str:
    from .elements import create_earth, create_fire
    recipe = f"{create_earth()} and {create_fire()}"

    return f"Strength potion brewerd with {recipe}"

def invisibility_potion() -> str:
    from .elements import create_air, create_water
    recipe = f"{create_air()} and {create_water()}"

    return f"Invisibility potion brewed with {recipe}"

def wisdom_potion() -> str:
    import elements
    fire = elements.create_fire()
    air = elements.create_air()
    earth = elements.create_earth()
    water = elements.create_water()

    recipe = f"{fire}, {water}, {air}, {earth}"

    return f"Wisdom potion brewed with all elements: {recipe}"


