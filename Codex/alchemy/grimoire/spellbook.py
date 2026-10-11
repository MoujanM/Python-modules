
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    val_str = validate_ingredients(ingredients)
    if "IN" in val_str:
        return f"Spell rejected: {spell_name} ({val_str})"
    else:
        return f"Spell recorded: {spell_name} ({val_str})"
