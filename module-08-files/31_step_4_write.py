# Ch8 | 31/40 | Step 4: Write Content to the Quiz and Answer Key Files [script]
# Automate 1e by Al Sweigart (CC-BY-NC-SA) - https://automatetheboringstuff.com/1e/chapter8

   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

   --snip--
       # Loop through all 50 states, making a question for each.
       for questionNum in range(50):
           --snip--

           # Write the question and the answer options to the quiz file.
           quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,
               states[questionNum]))
         for i in range(4):
             quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
           quizFile.write('\n')

           # Write the answer key to a file.
         answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
              answerOptions.index(correctAnswer)]))
       quizFile.close()
       answerKeyFile.close()
