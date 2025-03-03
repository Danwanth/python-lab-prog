class Question:
    def __init__(self, question_text, is_multiple_choice, options=None, correct_option=None):
        self.question_text = question_text
        self.is_multiple_choice = is_multiple_choice
        self.options = options if options else []
        self.correct_option = correct_option

    def check_answer(self, answer):
        if self.is_multiple_choice:
            return answer == self.correct_option
        else:
            return answer.strip().lower() == self.options[0].strip().lower()


class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def conduct_quiz(self, student):
        student.score = 0
        print(f"Starting quiz for {student.name}...\n")

        for i, question in enumerate(self.questions):
            print(f"Question {i + 1}: {question.question_text}")

            if question.is_multiple_choice:
                for j, option in enumerate(question.options):
                    print(f"{j + 1}. {option}")
                answer = int(input("Your answer (1-{}): ".format(len(question.options)))) - 1
            else:
                answer = input("Your answer: ")

            if question.check_answer(answer if question.is_multiple_choice else answer):
                student.score += 1

    def display_score(self, student):
        print(f"\n{student.name}'s score: {student.score}/{len(self.questions)}")


class Student:
    def __init__(self, name):
        self.name = name
        self.score = 0


def main():
    quiz = Quiz()

    # Adding questions to the quiz
    while True:
        question_text = input("Enter question text (or 'done' to finish): ")
        if question_text.lower() == 'done':
            break

        is_multiple_choice = input("Is this a multiple-choice question? (yes/no): ").strip().lower() == 'yes'
        options = []
        correct_option = None

        if is_multiple_choice:
            num_options = int(input("Enter number of options: "))
            for i in range(num_options):
                option = input(f"Enter option {i + 1}: ")
                options.append(option)
            correct_option = int(input("Enter the correct option number (1-{}): ".format(num_options))) - 1

        question = Question(question_text, is_multiple_choice, options, correct_option)
        quiz.add_question(question)

    # Conducting the quiz for students
    while True:
        student_name = input("Enter student name (or 'done' to finish): ")
        if student_name.lower() == 'done':
            break

        student = Student(student_name)
        quiz.conduct_quiz(student)
        quiz.display_score(student)


if __name__ == "__main__":
    main()
