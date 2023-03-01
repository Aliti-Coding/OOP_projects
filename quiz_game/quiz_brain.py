#TODO: asking the question
#TODO: checking if the answer was correct
#TODO: checking if were the end of the quiz


class QuizBrain:
    """quizbrain is depended on question model.
    we use the question_bank list as a parameter to get the quizbrain working
    """

    #create a constructor
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0
    #a checker if there are questions left for the while loop
    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    # Method to get the next question and store user answer            
    def next_question(self):
        current_question = self.questions_list[self.question_number] #accessing current question
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        # print(current_question.answer)
    
    # Method to check if the answear is correct or false
    def check_answer(self, user_answer, correct_answer):
        # print(user_answer)
        # print(correct_answer)
        if user_answer.lowmer() == correct_answer.lower():
            print(correct_answer)
            print(f"you got it right!")
            self.score += 1 
        else:
            print("that was wrong.")
        print(f"the correct answer was: {correct_answer}")
        print(f"your current score is : {self.score}/{self.question_number}")
