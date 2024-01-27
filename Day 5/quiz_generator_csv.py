import pandas as pd
import random

# Load quiz questions from the CSV file
file_path = 'D:/UniqueQuiz1.csv'  # Adjust the file path accordingly
df = pd.read_csv(file_path)

# Convert the DataFrame to a list of dictionaries
quiz = df.to_dict(orient='records')


def label_options(options):
    return [f"{chr(65 + i)}. {option}" for i, option in enumerate(options)]


# Shuffle the quiz questions to randomize the order
score = 0

# Repeat the quiz for each execution
while True:
    # Shuffle the quiz questions to randomize the order
    random.shuffle(quiz)

    # Randomly select 5 questions
    selected_questions = quiz[:5]

    # Ask each question and check the user's answer
    for question in selected_questions:
        print(question['Question'])
        # Label options as A, B, C, D
        labeled_options = label_options(
            [question['Option A'], question['Option B'], question['Option C'], question['Option D']])
        for option in labeled_options:
            print(option)

        user_answer = input(
            "Enter the correct option letter (A, B, C, or D): ").upper()

        # Extract the correct option letter from the full option text
        correct_option = [key for key, value in question.items(
        ) if value == question['Correct Option']][0]
        correct_letter = correct_option.split()[-1]

        if user_answer == correct_letter:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {option}.\n")

    if score >= 3:  # Adjust the passing score as needed
        print("Congratulations! You have successfully passed the test")
        print(f"Your final score is: {score}/{len(selected_questions)}")
    else:
        print("You have failed to pass the test")
        print(f"Your final score is: {score}/{len(selected_questions)}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
    else:
        score = 0  # Reset score for a new game
