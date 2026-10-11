# Code Cultivation: Object-Oriented Programming

## Python Module 01

This module is dedicated to mastering **Object-Oriented Programming (OOP)** concepts through progressively challenging exercises. Each exercise builds upon the previous one, introducing new OOP principles while reinforcing foundational concepts.

## Module Overview

This module focuses on developing a deep understanding of OOP principles in Python, starting with basic class definitions and advancing to complex inheritance hierarchies, polymorphism, and advanced design patterns. Each exercise includes a `__main__` test function that demonstrates the concepts in action.

## OOP Concepts Summary Table

| Concept | Description | Introduced in Exercise |
|---------|-------------|------------------------|
| **Classes** | Blueprints for objects | 1 |
| **Objects** | Instances of classes | 1 |
| **Instance Variables** | Data unique to each object | 1 |
| **Instance Methods** | Functions that operate on objects | 1 |
| **Constructor (`__init__`)** | Special method for initialization | 1 |
| **Encapsulation** | Data hiding and controlled access | 2 |
| **Private Attributes** | Attributes hidden from outside access | 2 |
| **Properties** | Controlled attribute access via decorators | 2 |
| **Inheritance** | Creating classes from other classes | 3 |
| **Method Overriding** | Redefining parent methods in child | 3 |
| **super()** | Accessing parent class methods | 3 |
| **Polymorphism** | Objects responding to the same interface differently | 4 |
| **Abstract Classes** | Classes that define an interface | 4 |
| **Class Methods** | Methods that operate on the class itself | 5 |
| **Static Methods** | Methods that don't require instance or class | 5 |
| **Magic Methods** | Special methods like `__str__()`, `__eq__()` | 5 |
| **Operator Overloading** | Customizing built-in operators for classes | 5 |
| **Composition** | Objects containing other objects | 6 |
| **Mixins** | Classes providing reusable functionality | 6 |
| **Design Patterns** | Proven solutions for common problems | 7 |

## Progressive Exercise Structure

### Exercise 1: Introduction to Classes and Objects
- Basic class definition and instantiation
- Instance variables and methods
- The `__init__()` constructor
- Using `self` parameter

### Exercise 2: Encapsulation and Data Hiding
- Private attributes (name mangling with `__` prefix)
- Protected attributes (single `_` prefix convention)
- Getter and setter methods (`@property` decorator)
- Importance of encapsulation

### Exercise 3: Inheritance and Method Overriding
- Single and multiple inheritance
- Parent and child classes
- Method overriding
- The `super()` function
- Method Resolution Order (MRO)

### Exercise 4: Polymorphism and Abstract Classes
- Polymorphism (method overloading and overriding)
- Abstract base classes (ABC)
- Abstract methods and properties
- Interface design with ABC
- Duck typing in Python

### Exercise 5: Class Methods, Static Methods, and Magic Methods
- Class methods (`@classmethod`)
- Static methods (`@staticmethod`)
- Magic methods (`__str__()`, `__repr__()`, `__eq__()`, etc.)
- Operator overloading
- Special methods for customization

### Exercise 6: Composition and Mixins
- Composition (has-a relationships)
- Aggregation vs. composition
- Mixin classes
- Combining inheritance and composition
- Choosing composition over inheritance

### Exercise 7: Design Patterns and Real-World Applications
- Singleton pattern
- Factory pattern
- Observer pattern
- Decorator pattern
- Real-world OOP design


## Testing
Each exercise file contains a `if __name__ == "__main__":` block that:
- Demonstrates the key OOP concepts
- Shows practical usage patterns
- Can be run independently to verify understanding
- Serves as a reference for best practices

Run any exercise with:
```bash
python exercise_X.py
```
