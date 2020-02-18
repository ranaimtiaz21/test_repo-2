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
days = time/60/60/24
print("Days", days)
cost = fuel * 1000
print("Cost: ", cost)
loss = 120000 * days
print("Loss: ", loss)
net = loss + cost
print("Net: ", net)

#Lab 2 Part 1
print("Fuel, Velocity, Duration, Fuel cost, Losses, Value lost")
print(fuel, v, days, cost, loss, net)

#Lab 2 Part 2
fuel_format = format("Fuel", ">15")
v_format = format("Velocity", ">15")
d_format = format("Duration", ">15")
c_format = format("Fuel Cost", ">15")
l_format = format("Losses", ">25")
value_format = format("Value Lost", ">25")
print(fuel_format, v_format, d_format, c_format, l_format, value_format)

fuelFormat = format(int(fuel), ">12,")
fuel_units = format("kg", ">2")
vFormat = format(v, ">11,.2f")
v_units = format("m/s", ">3")
dFormat = format(days, ">10.1f")
d_units = format("days", ">4")
cFormat = format(int(cost), ">11,")
c_units = format("USD", ">3")
lFormat = format(loss, ">21,.0f")
l_units = format("USD", ">3")
valFormat = format(round(net), ">21,")
val_units = format("USD", ">3")
#c_format = format
print(fuelFormat, fuel_units, vFormat, v_units, dFormat, d_units, cFormat, c_units,lFormat, l_units, valFormat, val_units)
