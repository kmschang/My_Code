from random import randint

print ("Game Rule: \nIf you want heads, type heads.\nIf you want tails, type tails.\nIf you want to leave, type end.\n")

while True:

	while True:

		answer = input("Heads or Tails?\n:")
		lower = answer.lower()


		if lower == "heads":
			newanswer = "heads"
			break

		elif lower == "tails":
			newanswer = "tails"
			break

		elif answer == "end":
			newanswer = 'end'
			break

		else:
			print ("Try again please?")

	number = randint(0,101)
	key = number %2

	if newanswer == 'end':
		print ("Your game has been stopped!")
		break

	elif key == 1 and newanswer == "heads":
		print ("It was Heads. You Won!")

	elif key == 1 and newanswer != "heads":
		print ("It was Heads. You Lost!")

	elif key == 0 and newanswer == "tails":
		print ("It was tails. You Won!")

	elif key == 0 and newanswer != "tails":
		print ("It was tails. You Lost!")

	else:
		print ("There was an error. Please Restart.")

	gameend = input("Do you want to play again? (y or n)")

	if gameend == "n":
		break
