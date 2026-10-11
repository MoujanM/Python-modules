
def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]

    words = ingredients.split(" ")

    if not words or any(word not in valid_elements for word in words):
        validation = "INVALID"
    else:
        validation = "VALID"

    return f"{ingredients} - {validation}"

