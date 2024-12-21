'''

Gear Transformation Power Calculation
In the One Piece universe, Monkey D. Luffy can activate different "Gear" transformations, each amplifying his base power in unique ways. The total power is calculated using the following formula:

total_power = base_power * (gear_level ** 2)
Write a function called calculate_power that takes as input Luffy's base_power and the gear_level, and computes his total power during that transformation.

'''
def total_power(base_power, gear_level ):
    '''The total power is calculated using the following formula:'''
    total_power = base_power * (gear_level ** 2)
    return total_power

print('The total power is : ', total_power(1000,2))