import math

MIN_FUEL = 10000
MAX_FUEL = 20000
CHANGE_FUEL = 1000


def print_header(csv=True):
    if csv:
        print("Fuel, Velocity, Duration, Fuel cost, Losses, Value lost")
    else:
        fuel_format = format("Fuel", ">15")
        v_format = format("Velocity", ">15")
        d_format = format("Duration", ">15")
        c_format = format("Fuel Cost", ">15")
        l_format = format("Losses", ">25")
        value_format = format("Value Lost", ">25")
        print(fuel_format, v_format, d_format, c_format, l_format, value_format)


def print_row(fuel, csv=True):
    dry_weight = 100000
    # fuel = input("What is fuel? ")
    initial_weight = dry_weight + fuel
    distance = 75000000 * 1000
    exhaust_velocity = 10000

    v = exhaust_velocity * (math.log(initial_weight / dry_weight))

    # print("Velocity:", v)

    # part 2
    time = (distance / v)
    days = time / 60 / 60 / 24
    # print("Days", days)
    cost = fuel * 1000
    # print("Cost: ", cost)
    loss = 120000 * days
    # print("Loss: ", loss)
    net = loss + cost
    # print("Net: ", net)
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
    if csv:
        print(fuel, v, days, cost, loss, net)
    else:
        print(fuelFormat, fuel_units, vFormat, v_units, dFormat, d_units, cFormat, c_units, lFormat, l_units, valFormat,
              val_units)


def experiment(exp_fuel, csv):
    if exp_fuel < MAX_FUEL:
        # recursive case
        exp_fuel = exp_fuel + CHANGE_FUEL
        print_row(exp_fuel, csv)
        experiment(exp_fuel, csv)
    else:
        # base case
        return


def get_choice():
    cur = int(input("Enter 1 or 2: "))
    if cur == 1 or cur == 2:
        if cur == 1:
            csv = True
            # print_header(csv)
            # print_row(fuel, csv)
        else:
            csv = False
            # print_header(csv)
            # print_row(fuel, csv)
        return csv
    else:
        print("Invalid! Try again")
        return get_choice()


def main():

    print("How would you like to format the output")
    print("1: CSV")
    print("2: Human Readable")
    csv = get_choice()
    experiment(MIN_FUEL,csv)
    if csv:
        print_header(csv)
        # print_row(fuel, csv)
    else:
        print_header(csv)
        # print_row(fuel, csv)


main()
