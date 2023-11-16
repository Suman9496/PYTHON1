import random


def run_quiz(questions):
    score = 0

    for question, options, correct_option in questions:
        print(question)

        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        user_answer = int(input("Enter your answer (1-{}): ".format(len(options))))

        if user_answer == correct_option:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_option}: {options[correct_option - 1]}\n")

    print("Quiz completed. Your score is {}/{}".format(score, len(questions)))


# Example quiz questions with Indian names (question, options, correct_option)
indian_quiz_questions = [
    ("What is the capital of India?", ["Delhi", "Mumbai", "Kolkata", "Chennai"], 1),
    ("Which river is considered the holiest in Hinduism?", ["Ganga", "Yamuna", "Brahmaputra", "Sarasvati"], 1),
    ("Who is known as the 'Father of the Nation' in India?",
     ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "Subhas Chandra Bose"], 1),
    ("Which festival is known as the 'Festival of Lights'?", ["Diwali", "Holi", "Navratri", "Eid"], 1),
]

# Run the Indian-themed quiz
run_quiz(indian_quiz_questions)
