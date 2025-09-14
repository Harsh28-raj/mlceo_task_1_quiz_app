class Question:
    def __init__(self, questext, options, corranswer):
        self.questext = questext
        self.options = options
        self.corranswer = corranswer

    def checkanswer(self, useranswer):
        return useranswer == self.corranswer

    def getscore(self, useranswer):
        if self.checkanswer(useranswer):
            return 1
        else :
            return 0



class EasyQuestion(Question):
    def getscore(self, useranswer):
        if self.checkanswer(useranswer):
            return 2
        else:
            return -1



class HardQuestion(Question):
    def getscore(self, useranswer):
        if self.checkanswer(useranswer):
            return 4
        else:
            return -2


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.correctscore = 0

    def start(self):
        for i in range(len(self.questions)):
            question = self.questions[i]
            print(f"\n Qno.{i+1}: {question.questext}")
            for option in question.options:
                print(option)

            useranswer = input("Your answer : ").lower()

            score = question.getscore(useranswer)
            self.correctscore += score

            if score > 0:
                print(f"Correct! Current Score {score} . \n Total:- {self.correctscore}\n")
            elif score < 0:
                print(f"Wrong! Current Penalty Score {score}.\n Total:- {self.correctscore}\n")
            else:
                print(f"Wrong!  Current Score {score} \n Total:- {self.correctscore}\n")

        print(f" Quiz Over! Final Score:  {self.correctscore}/8")
        a = self.correctscore / 8
        per = a * 100
        print(f"Percentage :- {per:.2f}%")
        if per<0:
            print("Very bad _ _")
            print("          _  ")
            print("         ___  ")
        elif per>=0 and per<50:
            print("Well tried () ()")
            print("             -")
            print("            ___")
        else:
            print("Excellent")



q1 = EasyQuestion("What is the capital of France?",
                  ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"], "c")

q2 = HardQuestion("Who developed the Python language?",
                  ["a) James Gosling", "b) Guido van Rossum", "c) Dennis Ritchie", "d) Bjarne Stroustrup"], "b")

q3 = EasyQuestion("What is 2 + 2?",
                  ["a) 3", "b) 4", "c) 5", "d) 22"], "b")

questions = [q1, q2, q3]


quiz = Quiz(questions)
quiz.start()
