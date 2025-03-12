"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)

    limo = Car(100)
    limo.add_fuel(20)

cars = []
c1 = Car("car",180)
c2 = Car("limo",100)
cars.append(c1)
cars.append(c2)

print(f"Car has fuel: {cars[0].fuel}")
print(cars[0])
print(f"Limo has fuel: {cars[1].fuel}")
print(cars[1])

main()