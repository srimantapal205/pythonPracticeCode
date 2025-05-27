"""

Gear Transformation Power Calculation
In the One Piece universe, Monkey D. Luffy can activate different "Gear" transformations, each amplifying his base power in unique ways. The total power is calculated using the following formula:

total_power = base_power * (gear_level ** 2)
Write a function called calculate_power that takes as input Luffy's base_power and the gear_level, and computes his total power during that transformation.
"""
def calculate_power(base_power, gear_level ):
    '''The total power is calculated using the following formula:'''
    total_power = base_power * (gear_level ** 2)
    return total_power

print('The total power is : ', calculate_power(1000,2))

"""

The Straw Hat Pirates have a list of islands they plan to visit.

On each island, they aim to collect different types of Poneglyph rubbings.

Write a function called collect_poneglyph_types that takes as input a dictionary where the keys are island names and the values are lists of Poneglyph types available on each island.

For each island, print a message:

"On [island], the crew collected the following Poneglyphs: [types]."
where [types] is a comma-separated string of Poneglyph types.

Keep a cumulative set of all unique Poneglyph types collected.

After the loop, print the total unique Poneglyph types collected:

"Total unique Poneglyph types collected: [total]"
Return the set of unique Poneglyph types collected.

Test the function with the following input:

islands = {
    'Wano': ['Road Poneglyph', 'Historical Poneglyph'],
    'Zou': ['Road Poneglyph'],
    'Alabasta': ['Historical Poneglyph']
}

"""

def collect_poneglyph_types(island):
    unique_poneglyphs =  set()
    for island, types in island.items():
        types_str = ', '.join(types)
        print(f"On {island}, the crew collected the following Poneglyphs: {types_str}.")
        unique_poneglyphs.update(types)
    total_unique = len(unique_poneglyphs)
    print(f"Total unique Poneglyph types collected: {total_unique}")
    return unique_poneglyphs
    
islands = {
    'Wano': ['Road Poneglyph', 'Historical Poneglyph'],
    'Zou': ['Road Poneglyph'],
    'Alabasta': ['Historical Poneglyph']
}

collect_poneglyph_types(islands)


"""

Devil Fruit User Class
In One Piece, characters who consume a Devil Fruit gain special powers.

Task: Create a class called DevilFruitUser with the following specifications:

An attribute name (string) to store the user's name.

A private attribute __devil_fruit (string) to store the name of the Devil Fruit.

A method reveal_fruit() that returns the name of the Devil Fruit.

A method use_power() that prints:

"[name] uses the power of the [devil_fruit]!"

"""

class DevilFruitUser:
    def __init__(self, name, devil_fruit):
        self.name = name
        self.__devil_fruit = devil_fruit
        
    def reveal_fruit(self):
        return self.__devil_fruit
        
    def use_power(self):
     devil_fruit_name =  self.reveal_fruit()
     print(f"{self.name} uses the power of the {devil_fruit_name}!") 
     
    
name = "Nico Robin"
devil_fruit = "Hana Hana no Mi"

user =    DevilFruitUser(name, devil_fruit)

print(user.name)

fruit_name = user.reveal_fruit()
print(fruit_name)

user.use_power()

        