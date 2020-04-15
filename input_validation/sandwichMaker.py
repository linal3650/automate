#! python3
# sandwichMaker.py -> prompts user for their sandwich preferences

import pyinputplus as pypi

prices = {"wheat": 1.00, 'white': 0.50, 'sourdough': 0.75,
          "chicken": 2.50, "turkey": 2.25, "ham": 2.00, "tofu": 1.50,
          "cheddar": 0.75, "swiss": 0.85, "mozzarella": 1.00,
          "condiments": 1.00
          }

numSandwich = pypi.inputInt('How many sandwiches would you like? \n', greaterThan=1)
totPrice = 0

for i in range(1, numSandwich+1):
    print('Please enter your preferences for Sandwich #{}:'.format(i))
    bread = pypi.inputMenu(['wheat', 'white', 'sourdough'])
    protein = pypi.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
    _cheese = pypi.inputYesNo("Would you like cheese?\n")
    if _cheese.lower() == 'yes':
        cheese = pypi.inputMenu(['cheddar', 'swiss', 'mozzarella'])
        condiments = pypi.inputYesNo("Would you like mayo, mustard, lettuce or tomato?\n")
        if condiments.lower() == 'yes':
            condiments = "condiments"
            print("Total price of Sandwich #{} is ${}\n".format(i, round(prices[bread] + prices[protein] + prices[cheese] + prices[condiments], 2)))
            totPrice = prices[bread] + prices[protein] + prices[cheese] + prices[condiments]
        else:
            print("Total price of Sandwich #{} is ${}\n".format(i, round(prices[bread] + prices[protein] + prices[cheese], 2)))
            totPrice += prices[bread] + prices[protein] + prices[cheese]
    else:
        condiments = pypi.inputYesNo("Would you like mayo, mustard, lettuce or tomato?\n")
        if condiments.lower() == 'yes':
            condiments = "condiments"
            print("Total price of Sandwich #{} is ${}\n".format(i, round(prices[bread] + prices[protein] + prices[condiments], 2)))
            totPrice = prices[bread] + prices[protein] + prices[condiments]
        else:
            print("Total price of Sandwich #{} is ${}\n".format(i, round(prices[bread] + prices[protein], 2)))
            totPrice += prices[bread] + prices[protein]

print("Your total is ${} for the {} sandwiches".format(round(totPrice, 2), numSandwich))
