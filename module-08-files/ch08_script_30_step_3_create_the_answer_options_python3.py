"""Chapter 8: Reading and Writing Files
Section: Step 3: Create the Answer Options
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter8
Type: book script/example
PPT map: Syllabus Ch8: files
File: ch08_script_30_step_3_create_the_answer_options_python3.py (30 of 40 in this chapter)
"""

   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

   --snip--

       # Loop through all 50 states, making a question for each.
       for questionNum in range(50):

           # Get right and wrong answers.
         correctAnswer = capitals[states[questionNum]]
         wrongAnswers = list(capitals.values())
         del wrongAnswers[wrongAnswers.index(correctAnswer)]
         wrongAnswers = random.sample(wrongAnswers, 3)
         answerOptions = wrongAnswers + [correctAnswer]
         random.shuffle(answerOptions)

           # TODO: Write the question and answer options to the quiz file.

           # TODO: Write the answer key to a file.
