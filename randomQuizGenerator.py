#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
# Nicholas Ivey 3/16/2016
import random, os
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 
'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

			#TODO: follow the 'generating random quiz files' project in the textbook to fill in this file.
			#TODO: however, make the following modificatiosn to the instructions on the textbook:
			#       1. instead of making 35 quiz versions, you'll only make 5 quiz versions
			#       2. instead of creating quiz and answer files in the current working directory, create a folder titled 'quizzes' and another folder titled 'answers'.
			#       3. place the randomly-generated quizzes in the 'quizzes' directory.
			#       4. plaec the corresponding answers in the 'answers' directory.

os.makedirs(os.path.join('./answers'), exist_ok=True) 
os.makedirs(os.path.join('./quizzes'), exist_ok=True) 
for quizNum in range(5):

		quizFile = open('./quizzes/capitalsquiz%s.txt' % (quizNum+1), 'w') #creates or opens quiz txt file
		answerKeyFile = open('./answers/capitalsquiz_answers%s.txt' % (quizNum+1), 'w') #creates or opens answers txt file

		quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n') #TOP OF QUIZ FILE
		quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum+1))
		quizFile.write('\n\n')

		#Change order of states 
		states = list(capitals.keys())
		random.shuffle(states)

		for questionNum in range(50):
			correctAnswer = capitals[states[questionNum]] # assigns correct answer 
			wrongAnswers = list(capitals.values()) #creates a list of all wrong answers 
			del wrongAnswers[wrongAnswers.index(correctAnswer)] #removes correct answer from incorrect list
			wrongAnswers = random.sample(wrongAnswers, 3) # chooses 3 random wrong answers 
			answerOptions = wrongAnswers + [correctAnswer] #creates options 1-4
			random.shuffle(answerOptions) # shuffles options

			quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum])) #writes question

			for i in range(4):
				quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i])) #writes out chooses
				quizFile.write('\n')

			answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)])) #writes out answer in key 

		print('Generated quiz and answers')
quizFile.close() # closes files
answerKeyFile.close()

