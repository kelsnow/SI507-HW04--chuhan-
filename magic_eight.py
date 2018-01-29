import random

def ask():
	ask = input("What is your question?(Enter quit if you want to stop)")
	return ask

answers_list = ["It is certain", 
				  "It is decidedly so", 
				  "Without a doubt", 
				  "Yes definitely",
				  "You may rely on it",
				  "As I see it, yes",
				  "Most likely",
				  "Outlook good",
				  "Yes",
				  "Signs point to yes",
				  "Reply hazy try again",
				  "Ask again later",
				  "Better not tell you now",
				  "Cannot predict now",
				  "Concentrate and ask again",
				  "Don't count on it",
				  "My reply is no",
				  "My sources say no",
				  "Outlook not so good",
				  "Very doubtful" ]

final_answer = random.choice(answers_list)



	# question = ask()
	# if question.lower() == "quit":
	# 	stop = True
	# else:
	# 	if question[-1] != "?":
	# 		print("I'm sorry, I can only answer questions.")
	# 	else:
	# 		print (final_answer)
	
	
while True:
	question = ask()
	if question.lower() !="quit":
		if question[-1] != "?":
			print("I'm sorry, I can only answer questions.")
		else:
			print (final_answer)
	else:
		break

