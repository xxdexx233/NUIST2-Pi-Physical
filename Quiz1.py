import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#NUISTvQuiz Game in Python
def quiz():
	print("Welcome to the Animal Quiz!")
	print("Answer the following questions:")

#Questions and Answers
	questions = [
		"1.What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat",
		"2.Which bird can fly backwards?: a. Cuckoo, b. Eagle, c. Hummingbird",
		"3.WHat is the only mammal capable of flight?: a. Bat, b. Squirrel, c. Dolphin"
	]
	answers = [
		"Blue Whale",
		"HummingBird",
		"Bat"
	]
	score = 0

# Ask questions
	for i in range(len(questions)):
		user_answer = input(questions[i]).strip.lower()
		if user_answer == answer[i]:
			print("Correct!")
			score += 1
			GPIO.setup(18,GPIO.OUT)
			GPIO.output(18,GPIO,HIGH)
			time.sleep(1)
			GPIO.output(18,GPIO.LOW)
		else:
			print("Incorrect!")
			GPIO.setup(23,GPIO.OUT)
                        GPIO.output(23,GPIO,HIGH)
                        time.sleep(1)
                        GPIO.output(23,GPIO.LOW)

#Provide final score
	print("\nQuiz completed!")
	print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
quiz()
