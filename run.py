import sys
import signal
from random import randint


def signal_handler(sig, frame):
	print('Bye bye!')
	sys.exit(0)


def question():
	a = randint(10, 99)
	b = randint(10, 99)
	correct_answer = a * b
	prompt = 'Multiply {} and {}\n'.format(a, b)
	passed = False
	while not passed:
		passed = validate_answer(correct_answer, prompt)


def validate_answer(correct_answer, prompt):
	user_answer = input(prompt)
	while True:
		if user_answer.strip().isdigit():
			user_answer = int(user_answer)
			if user_answer == correct_answer:
				print("Good job!")
				break
			else:
				user_answer = input("Wrong! Try again!\n")
		else:
			user_answer = input("Enter correct integer!\n")
	return True


signal.signal(signal.SIGINT, signal_handler)

for x in range(5):
	question()
