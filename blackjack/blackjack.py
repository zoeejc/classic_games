#!/usr/bin/env python3

import sys
import random as r
import os

# items in list
# when item chosen, remove from list
# do different things based on input
# twist, stick, split
# A is default 11, if you go over 21 it changes to 1

os.system('clear')

cards = {"1": 1,
		 "2": 2,
		 "3": 3,
		 "4": 4,
		 "5": 5,
		 "6": 6,
		 "7": 7,
		 "8": 8,
		 "9": 9,
		 "10": 10,
		 "J": 10,
		 "Q": 10,
		 "K": 10,
		 "A": 11}

my_cards = []
dealer_cards = []

print(">>> Welcome to blackjack, type 'play' to play, or 'rules' to see the rules!")

start = input()

if start == "rules":
	rule = open('rules.txt', 'r')
	print('\n' + rule.read())
	start = input()

if start == "play":

	os.system('clear')

	print(">>> Here are your cards!")

	mycard1 = r.choice(list(cards.keys()))
	mycard2 = r.choice(list(cards.keys()))
	print(mycard1, mycard2)

	my_cards.append(mycard1)
	my_cards.append(mycard2)

	total = cards[mycard1] + cards[mycard2]
	print(f">>> Your total is {total}")

	print(">>> What would you like to do: twist, split or stick?")

	prompt = input()

	while prompt != "stick":

		if prompt == "twist":
			next = r.choice(list(cards.keys()))
			my_cards.append(next)
			total += cards[next]
			print(f">>> Your next card is {next}, your total is now {total}!")

			if total > 21 and ("A" in my_cards):
				total -= 10
				my_cards.remove("A")
				print(f">>> You went bust, but you had an ace!! Total is now {total}!")

			elif total > 21:
				print(">>> Oh no!! You went bust!!!")
				break

			elif total == 21:
				print(">>> You Win!!")
				break

			elif total <= 21 and (len(my_cards) == 5):
				print(">>> You got a 5 card trick!! Congrats!!")
				break

			prompt = input()

		elif prompt == "split":
			if mycard1 == mycard2:
				print(f"Starting with first card: {mycard1}.")
				print(">>> What would you like to do: twist or stick?")
				next = r.choice(list(cards.keys()))
				my_cards.append(next)
				total += cards[next]
				print(f">>> Your next card is {next}, your total is now {total}!")

				if total > 21 and ("A" in my_cards):
					total -= 10
					my_cards.remove("A")
					print(f">>> You went bust, but you had an ace!! Total is now {total}!")

				elif total > 21:
					print(">>> Oh no!! You went bust!!!")
					break

				elif total == 21:
					print(">>> You Win!!")

				elif total <= 21 and (len(my_cards) == 5):
					print(">>> You got a 5 card trick!! Congrats!!")

			else:
				print(">>> Can't split!! Both of your cards must be the same to split!")

			prompt = input()

#	if prompt == "stick":
#		dcard1 = r.choice(list(cards.keys()))
#		dcard2 = r.choice(list(cards.keys()))
#		print(f"The dealer's cards are: {dcard1} {dcard2}")
