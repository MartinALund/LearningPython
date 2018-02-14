#Float

#Opret en variabel som castes til en float
your_float = float(input("Enter a float: "))

#Afrund float til 2 decimaler ved at {:.2f} - Alt der bliver placeret ind i {} skal afrundes med .2 og man angiver f fordi det er en float
print("Round to 2 decimals: {:.2f} ".format(your_float))

#Floats er upræcise, dette ville man tro giver 0 men det giver faktisk et meget lille tal
i = 0.1 + 0.1 + 0.1 - 0.3
print(i)

i = .11111111111111111111111111111111
j = .00000000000000010000000000000001
print("Floats er mest præcise før 16 digits, efter det bliver de meget upræcise")
print("Answer : {:.32}".format(i + j))