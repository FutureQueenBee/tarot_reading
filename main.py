# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# https://www.guru99.com/learn-python-main-function-with-examples-understand-main.html
# 78 cards in all

import csv
import random
from random import shuffle

def main():
	
	user_name = raw_input("What is your name?")

	tarot_tsv_file = open("tarot-deck.tsv", "r")
	# Open tsv Tarot deck file
	tarot_deck_dict = {}

	with open("tarot-deck-file-001.tsv") as tsv:
		for line in csv.reader(tsv, dialect="excel-tab"):
			tarot_deck_dict[line[0]] = line[1:] 
	# Creates dictionary of Tarot deck: {'15': ['Ace of Swords', 'Raw power, victory, break-throughs, mental clarity', 'http://www.tarotlore.com/tarot-cards/ace-of-swords/']}
	
	left_deck = random.sample(xrange(78),39)

	print(left_deck)
	
	cards = range(1,79)
	
	right_deck = []
	for card in cards:
		if card not in left_deck:
			right_deck.append(card)
	shuffle(right_deck)

	deck_selection = raw_input("The deck is cut! Select either the Left deck or the Right deck by typing 'RIGHT' or 'LEFT'")
	
	final_five = []
	final_five_dict = {}
	if deck_selection == "RIGHT":
		for i in range(1,6):
			random_card = random.choice(right_deck)
			if random_card not in final_five:
				final_five.append(random_card)
				final_five_dict[str(i)] = random_card
	elif deck_selection == "LEFT":
		for i in range(1,6):
			random_card = random.choice(left_deck)
			if random_card not in final_five:
				final_five.append(random_card)
				final_five_dict[str(i)] = random_card

	final_selection = raw_input("Select three numbers from 1 through 5, separated by commas.").split(',')

	print(final_selection)
	print(final_five_dict)

	tarot_reading = []
	for n in final_selection:
		tarot_reading.append(tarot_deck_dict[str(final_five_dict[n])])

	print(tarot_reading)
	return tarot_reading
		
if __name__ == "__main__":
	main()
	print("Main executed")
