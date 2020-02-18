#Knight Lab

import math
dry_weight = 100000
fuel = input("What is fuel? " )
fuel = int(fuel)
initial_weight = dry_weight + fuel
distance = 75000000 * 1000
exhaust_velocity = 10000

v = exhaust_velocity * (math.log(initial_weight/dry_weight))

print("Velocity:", v)

#part 2
time = (distance/v)
days = time/60/24
print("Days", days)
cost = fuel * 11000
print("Cost: ", cost)
loss = 120000 * days
print("Loss: ", loss)
net = loss + cost
print("Net: ", net)
