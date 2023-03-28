# Calculates the minimum number of coins required to give a user change

# Modules
from cs50 import get_float

# Main program
def main():

	dollars = getUserInput()
	cents = dollars * 100
	print(getCoins(cents))

# Asks user for change (in dollars)
# and re-prompt for valid input
def getUserInput():
	while True:
		userInput = get_float("Change owed: $")
		if userInput > 0:
			break
	return userInput

# Calculates min. number of coins to give change to user
def getCoins(cents):
	quarters = dimes = nickels = pennies = coins = 0
	while cents > 0:
		if cents >= 25:
			quarters = getQuarters(cents)
			coins += quarters
			cents -= quarters * 25
		elif cents >= 10:
			dimes = getDimes(cents)
			coins += dimes
			cents -= dimes * 10
		elif cents >= 5:
			nickels = getNickels(cents)
			coins += nickels
			cents -= nickels * 5
		elif cents >= 1:
			pennies = getPennies(cents)
			coins += pennies
			cents -= pennies
	return coins

# Calculates min. number of coins per coin type (e.g. quarters, dimes, etc.)
def calculateCoins(cents, coinValue):
	coins = 0
	while (cents - coinValue >= 0):
		coins += 1
		cents -= coinValue
	return coins

# Calculates min. number of quarters
def getQuarters(cents):
	return calculateCoins(cents, 25)

# Calculates min. number of dimes
def getDimes(cents):
	return calculateCoins(cents, 10)

# Calculates min. number of nickels
def getNickels(cents):
	return calculateCoins(cents, 5)

# Calculates min. number of pennies
def getPennies(cents):
	return calculateCoins(cents, 1)


# Runs the program
main()
