import random

capitals = {'Andhra Pradesh': 'Hyderabad', 'Arunachal Pradesh': 'Itanagar', 'Assam': 'Dispur', 'Bihar': 'Patna',
            'Chhattisgarh': 'Raipur', 'Goa': 'Panji', 'Gujarat': 'Gandhinagar', 'Haryana': 'Chandigarh',
            'Himachal Pradesh': 'Shimla', 'Jammu and Kashmir': 'Srinagar', 'Jarkhand': 'Ranchi',
            'Karnataka': 'Bengaluru',
            'Kerala': 'Thiruvananthapuram', 'Madhya Pradesh': 'Bhopal', 'Maharashtra': 'Mumbai', 'Manipur': 'Imphal',
            'Meghalaya': 'Shillong', 'Mizoram': 'Aizawl', 'Nagaland': 'Kohima', 'Odisha': 'Bhubaneswar',
            'Punjab': 'Chandigarh',
            'Rajasthan': 'Jaipur', 'Sikkim': 'Gangtok', 'Tamil Nadu': 'Chennai', 'Telangana': 'Hyderabad',
            'Tripura': 'Agartala', 'Uttar Pradesh': 'Lucknow', 'Uttarakhand': 'Dehradun', 'West Bengal': 'Kolkata'}
quiznum = 0
for quiznum in range(35):
    quizFile = open('C:\\Users\\Admin\\Documents\\Python practice\\Automate\\CapitalsQuiz%s.txt' % (quiznum + 1), 'w')
    answerKeyFile = open(
        'C:\\Users\\Admin\\Documents\\Python practice\\Automate\\CapitalsQuiz_Answer%s.txt' % (quiznum + 1), 'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiznum + 1))
    quizFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(29):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write('%s. What is the capital of %s? \n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s.%s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
