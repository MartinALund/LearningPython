import random
import numpy as np

def main():
    int_dice = []
    amount_of_dice = 6

    for i in range(amount_of_dice):
        int_dice.append(random.randint(1, 6))

    print(int_dice)
    print("Average value: ", np.average(int_dice))
    print("Max value: ", np.max(int_dice))
    print("Min value: ", np.min(int_dice))


if __name__ == '__main__':
    main()