#for loop

list = [2,4,6,8,10]
#Denne type kører igennem hver liste element, i dette tilfælde printer den alle tal ud i listen.

for i in list:
    print(i)

#Denne type definerer man hvor mange gange man skal køre igennem noget.
for i in range(10):
    print("i = ", i)

#Her kan man vælge et specifikt index at køre igennem.
for i in range(2,5):
    print(i)

# Print en liste af ulige tal ved at bruge % og en liste.

print("A list of numbers from 0 - 20, finding the uneven numbers")
for i in range(21):
    if i % 2 != 0:
        print("Uneven: ", i)

#Investment Assignment

money = input("How much money do you want to invest?: ")
interest = input("Interest rate: " )
years = input("Over how many years? ")
money = float(money)
years = int(years)

interest = float(interest) * .01

for i in range(years):
    money = money + (money * interest)

print("Investment after {} years: {:.2f} ".format(years,money ))




