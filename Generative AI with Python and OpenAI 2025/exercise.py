'''

Gear Transformation Power Calculation
In the One Piece universe, Monkey D. Luffy can activate different "Gear" transformations, each amplifying his base power in unique ways. The total power is calculated using the following formula:

total_power = base_power * (gear_level ** 2)
Write a function called calculate_power that takes as input Luffy's base_power and the gear_level, and computes his total power during that transformation.

'''
def calculate_power(base_power, gear_level ):
    '''The total power is calculated using the following formula:'''
    total_power = base_power * (gear_level ** 2)
    return total_power

print('The total power is : ', total_power(1000,2))

'''

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

'''

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