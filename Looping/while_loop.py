import random

#Assignment - Find the right number!

#Random nummer i mellem 1 og 50
rand_num = random.randrange(1,51)

i = 1
print("Random number: ", rand_num)
#Kører igennem et while loop indtil i == rand_num
while (i != rand_num):
    print(i)
    i += 1

print("Found the random number : ", rand_num)

#Christmas tree while loop

tree_height = input("Hvor højt skal træet være? ")
tree_height = int(tree_height)

spaces = tree_height - 1

hashes = 1

stump_spaces = tree_height - 1

while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")

    for i in range(hashes):
        print('#', end="")

    print()

    spaces -= 1
    hashes += 2
    tree_height -= 1

for i in range(stump_spaces):
    print(' ', end="")

print("#")


