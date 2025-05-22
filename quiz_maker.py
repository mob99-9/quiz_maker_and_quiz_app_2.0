import csv

file_name = "data_questions.csv"
question = []
class SaveQuestion:
    def add_to_file(self, user_inputs):
        with open(file_name, "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(user_inputs)

class MakeQuestion:
    def question_maker(self):
        question_set = []
        while True:
            user_question = input("Please enter a question (type exit if none): ")
            if user_question.lower() == "exit":
                exit()
            else:
                question_set.append(user_question)
                for choice in range(0,4):
                    user_choice = input(f"Please enter choice no. {choice + 1}: ")
                    question_set.append(user_choice)
                user_answer = input("Please enter the corret answer (A, B, C, D): ")
                question_set.append(user_answer)
                question.append(question_set)
                add_question = SaveQuestion()
                add_question.add_to_file(question)

main_program = MakeQuestion()

if __name__ == "__main__":
    while True:
        main_program.question_maker()
    else:
        exit