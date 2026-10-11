# DataDeck 🎮
DataDeck is a comprehensive library designed to aid in the development of games while implementing robust Object-Oriented Programming (OOP) practices. This library provides a foundation for creating modular, scalable, and maintainable game architectures.

## 📂 Project Structure
```bash
DataDeck/
├── src/
│   ├── main.py
│   ├── game/
│   │   ├── __init__.py
│   │   ├── game_engine.py
│   │   └── player.py
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── helpers.py
├── tests/
│   └── test_game.py
├── README.md
└── requirements.txt
```


## OOP Concepts with Examples
This project employs several core concepts of OOP to create modular and reusable code.

### Classes and Objects

```python
class Player:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f'Player: {self.name}'
```
### Inheritance
```python
class SportsPlayer(Player):
    def __init__(self, name, sport):
        super().__init__(name)
        self.sport = sport

    def display(self):
        return f'Sports Player: {self.name}, Sport: {self.sport}'
```

### Polymorphism

```python
def display_player(player):
    # Works for both Player and SportsPlayer instances
    print(player.display())
```

## Game Implementation Details

The game module contains the main functionalities required for game development.
Game Engine: This is where the core logic of the game resides, managing the game loop and entities.
Player Management: Involves creating and managing players, each with their own attributes and capabilities.


### Examples Walkthrough

Here is an example of how to use DataDeck in your script:
```pyhton
from src.game.player import Player

# Create a new player
player1 = Player('Alice')
print(player1.display())  # Output: Player: Alice
```

#### Design Patterns

The project makes use of several industry-standard design patterns:
Singleton: Ensures a single instance of the game engine.
Factory: Streamlines object creation for game entities.
Observer: Manages events and notifications between components.
