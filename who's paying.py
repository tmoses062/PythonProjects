import random

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
namesAsCSV = input("Give me everybody's names, separated by a comma. ")
names = namesAsCSV.split(", ")

#print(names)
x = len(names)

# randomchoice = random.randint(0, x - 1)
# payer = names(randomchoice)
# print(f"{payer} is going to pay the bill. ")  OR

payer = names[random.randint(0, x - 1)]
print(f"{payer} is going to pay the bill. ")