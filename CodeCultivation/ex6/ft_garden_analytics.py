# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/05 14:54:52 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/05 14:54:54 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class GardenManager:
    """The Boss: handles and holds all gardens' data."""

    total_gardens_managed = 0

    def __init__(self) -> None:
        """Class initiates a garden dict {owner:garden}"""
        self.gardens = {}
        

    def add_garden(self, owner: str) -> None:
        """Add to Manager's records"""
        if owner not in self.gardens:
            self.gardens[owner] = []
            GardenManager.total_gardens_managed += 1

    def add_plant(self, owner: str, new_plant: "Plant") -> None:
        """Function to add new plant to a specific garden."""
        self.gardens[owner].append(new_plant)
        print (f"Added {new_plant.name} to {owner}'s garden.")
    
    def help_grow(self, owner: str) -> None:
        """"
        Function to grow all plants in garden simultaenously.
        Output used in report construction. 
        """
        if owner in self.gardens:
            print(f'{owner} is helping all plants grow ...')
            plants = self.gardens[owner]
            count = GardenManager.GardenStats.counter_help(plants)
            for i in range(count):
                plants[i].grow()
                print (f'{plants[i].name} grew 1cm')
    
    def get_owner_score(self, owner: str) -> int:
        """Return score of a particular owner's gardens."""
        plants = self.gardens[owner]
        score = GardenManager.GardenStats.get_score(plants)
        return score

    @classmethod
    def create_garden_network(cls, owners: list) -> "GardenManager":
        """Initiate Manager for all gardens."""
        manager = cls()
        count = GardenManager.GardenStats.counter_help(owners)
        for i in range(count):
            manager.add_garden(owners[i])
        return manager


    def get_garden_report(self, owner: str) -> None:
        """Gets calculations from GardenStats and displays in organized way."""
        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.gardens[owner]:
            print(plant.report_status())
        print()
        plant_count = GardenManager.GardenStats.counter_help(self.gardens[owner])
        print(f"Plants added: {plant_count}, Total growth: {plant_count}cm")
        types = GardenManager.GardenStats.count_types(self.gardens[owner])
        print(f"Plant types: {types["reg"]} regular, ", end="")
        print(f"{types["flow"]} flowering, ", end="")
        print(f"{types["prize"]} prize flowers")
        print()
        validation = GardenManager.GardenStats.height_validation(self.gardens[owner])
        print(f"Height validation test: {validation}")
        
    
    class GardenStats:
        """Child class to handle statistical calculations."""

        @staticmethod
        def counter_help(my_list: list) -> int:
            """Because len() is not authorized."""
            count = 0
            for _ in my_list:
                count += 1
            return count

        @staticmethod
        def count_types(plants: list) -> dict[str, int]:
            """
            Nested helper function to get plant-type stats.

            Attributes
            ----------
                plants : list
                    list of all plants in a garden
            
            Returns
            -------
                dictionary with plant : count format
            """
            types = {"reg" : 0, "flow" : 0, "prize" : 0}
            for p in plants:
                if p.__class__.__name__ == "PrizeFlower":
                    types["prize"] += 1
                elif p.__class__.__name__ == "FloweringPlant":
                    types["flow"] += 1
                else:
                    types["reg"] += 1
            return types

        @staticmethod
        def height_validation(plants: list) -> bool:
            """Utility function to validate all heights > 0."""
            count = GardenManager.GardenStats.counter_help(plants)
            for i in range(count):
                if plants[i].get_height() <= 0:
                    return False
            return True

        @staticmethod
        def get_score(plants: list) -> int:
            """Utility function to calculate a garden's score."""
            plant_count = GardenManager.GardenStats.counter_help(plants)
            score = 0
            for i in range(plant_count):
                score += 10
                score += plants[i].get_height()
                if plants[i].__class__.__name__ == "PrizeFlower":
                    score += plants[i].points
            return score

class Plant:
    """
    Parent class.
    Attributes
    ----------
        name : str
            plant name
        height : int
            height of plant in cm
        age : int
            age of plant in days
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Constructs all necessary attributes for Plant object."""
        self.name = name
        if height > 0:
            self.__height = height
        if age > 0 and age < 5000:
            self.__age = age
    
    def report_status(self) -> str:
        """Function to streamline report creation."""
        return f"- {self.name}: {self.get_height()}cm"

    def grow(self) -> None:
        """Function to simulate plant growth"""
        self.__height += 1

    def get_height(self) -> int:
        """Function to access height safely."""
        return self.__height
    
class FloweringPlant(Plant):
    """
    Child class of Plant.

    Attributes
    ----------
        name : str
            plant name
        height : int
            height of plant in cm
        age : int
            age of plant in days
        color: str
            speciliazed attribute
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Constructs all necessary attributes for Plant object.
        Calls super() to set up inherited basic features.
        """
        super().__init__(name, height, age)
        self.color = color

    def report_status(self) -> str:
        """
        Function to streamline report creation.
        Calls super() to add specific info to base info.
        """
        base_info = super().report_status()
        return f"{base_info}, {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
    """
    Grandchild of Plant.

    Attributes
    ----------
    name : str
            plant name
        height : int
            height of plant in cm
        age : int
            age of plant in days
        color : str
            specialized attribute
        points : int
            count of prize points
    """
    def __init__(self, name: str, height: int, age: int,
                 color: str, points: int) -> None:
        """
        Constructs all necessary attributes for Plant object.
        Calls super() to set up inherited basic features.
        """
        super().__init__(name, height, age, color)
        self.points = points

    def report_status(self) -> str:
        """
        Function to streamline report creation.
        Calls super() to add specific info to base info.
        """
        base_info = super().report_status()
        return f'{base_info}, Prize points: {self.points}'


if __name__ == "__main__":
    print(f'=== Garden Management System Demo ===')
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    p1 = Plant("Oak Tree", 100, 280)
    p2 = FloweringPlant("Rose", 25, 45, "red")
    p3 = PrizeFlower("Sunflower", 50, 60, "yellow", 10)
    p4 = PrizeFlower("Magic", 32, 50, "blue", 50)
    gardens.add_plant("Bob", p4)
    for plant in [p1, p2, p3]:
        gardens.add_plant("Alice", plant)
    print()
    gardens.help_grow("Alice")
    print()
    # print alice's garden report
    gardens.get_garden_report("Alice")
    # print additional info about garden network
    a_score = gardens.get_owner_score("Alice")
    b_score = gardens.get_owner_score("Bob")
    print(f"Garden scores - Alice: {a_score}, Bob: {b_score}")
    print(f"Total gardens managed: {gardens.total_gardens_managed}")