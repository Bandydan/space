from body import body
from fuelmod import fuel
from engine import engine
from random import choice
from math import log

choice_made = int(raw_input("1 for random, 2 for custom: ").strip())

ship = {}

if (1 == choice_made):
    ship['engine'] = engine[choice(engine.keys())]
    ship['fuel'] = fuel[choice(fuel.keys())]
    ship['body'] = body[choice(body.keys())]

total_mass = ship['engine']['weight'] + \
    ship['fuel']['weight'] * ship['body']['tank'] + \
    ship['body']['weight']

total_end_mass = total_mass - ship['fuel']['weight']


# print total_mass

acceleration = ship['fuel']['impulse'] \
    * log(float(total_mass) / float(total_end_mass))

# print log(float(total_mass) / float(total_end_mass))
# exit()

flight_force = acceleration * total_mass
gravity_force = 9.8 * total_mass

flight = True if flight_force > gravity_force else False


print flight

print flight_force, gravity_force
