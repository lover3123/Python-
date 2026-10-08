# Ch8 | 29/40 | Step 2: Create the Quiz File and Shuffle the Question Order [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

   --snip--

   # Generate 35 quiz files.
   for quizNum in range(35):
       # Create the quiz and answer key files.
     quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
     answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

       # Write out the header for the quiz.
     quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
       quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
       quizFile.write('\n\n')

       # Shuffle the order of the states.
       states = list(capitals.keys())
     random.shuffle(states)

       # TODO: Loop through all 50 states, making a question for each.
