from python_oop.model.Person import Person
from python_oop.model.Dice import Dice
import random
import numpy as np

'''person = Person("Martin",26,"188")
person.print_person()
person.name = "JensLyn"
person.print_person()'''


def main():
    dices = []
    amount_of_dice = 6

    for i in range(amount_of_dice):
        dice = Dice(i + 1, random.randint(1, 6))
        dices.append(dice)

    for dice in dices:
        print("{} terning viser {}".format(dice.id, dice.value))


if __name__ == "__main__":
    main()








