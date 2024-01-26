import random
import csv
# Define the quiz questions and options
quiz = [
    {
        'question': 'What is the capital of France?',
        'options': ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
        'correct_answer': 'C'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['A. Jupiter', 'B. Mars', 'C. Venus', 'D. Saturn'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the largest mammal in the world?',
        'options': ['A. Elephant', 'B. Blue Whale', 'C. Giraffe', 'D. Polar Bear'],
        'correct_answer': 'B'
    },
    {
        'question': 'In which year did World War I begin?',
        'options': ['A. 1900', 'B. 1914', 'C. 1923', 'D. 1939'],
        'correct_answer': 'B'
    },
    {
        'question': 'Who wrote "Romeo and Juliet"?',
        'options': ['A. William Shakespeare', 'B. Jane Austen', 'C. Charles Dickens', 'D. Mark Twain'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the capital of Japan?',
        'options': ['A. Tokyo', 'B. Beijing', 'C. Seoul', 'D. Bangkok'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which element has the chemical symbol "O"?',
        'options': ['A. Oxygen', 'B. Gold', 'C. Iron', 'D. Carbon'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the currency of Brazil?',
        'options': ['A. Peso', 'B. Real', 'C. Euro', 'D. Yen'],
        'correct_answer': 'B'
    },
    {
        'question': 'Who painted the Mona Lisa?',
        'options': ['A. Vincent van Gogh', 'B. Pablo Picasso', 'C. Leonardo da Vinci', 'D. Michelangelo'],
        'correct_answer': 'C'
    },
    {
        'question': 'What is the capital of Australia?',
        'options': ['A. Sydney', 'B. Melbourne', 'C. Canberra', 'D. Brisbane'],
        'correct_answer': 'C'
    },
    {
        'question': 'Which country is known as the Land of the Rising Sun?',
        'options': ['A. China', 'B. Japan', 'C. South Korea', 'D. Vietnam'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the largest ocean on Earth?',
        'options': ['A. Atlantic Ocean', 'B. Indian Ocean', 'C. Arctic Ocean', 'D. Pacific Ocean'],
        'correct_answer': 'D'
    },
    {
        'question': 'Who wrote "To Kill a Mockingbird"?',
        'options': ['A. J.K. Rowling', 'B. Harper Lee', 'C. Ernest Hemingway', 'D. George Orwell'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the square root of 81?',
        'options': ['A. 7', 'B. 9', 'C. 8', 'D. 6'],
        'correct_answer': 'B'
    },
    {
        'question': 'Which gas makes up the majority of Earth\'s atmosphere?',
        'options': ['A. Oxygen', 'B. Nitrogen', 'C. Carbon Dioxide', 'D. Hydrogen'],
        'correct_answer': 'B'
    },
    {
        'question': 'Who developed the theory of relativity?',
        'options': ['A. Isaac Newton', 'B. Albert Einstein', 'C. Galileo Galilei', 'D. Stephen Hawking'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the smallest prime number?',
        'options': ['A. 1', 'B. 2', 'C. 3', 'D. 5'],
        'correct_answer': 'B'
    },
    {
        'question': 'In which year did the Titanic sink?',
        'options': ['A. 1912', 'B. 1920', 'C. 1931', 'D. 1945'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who is the author of "1984"?',
        'options': ['A. George Orwell', 'B. Aldous Huxley', 'C. Ray Bradbury', 'D. Jules Verne'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the capital of South Africa?',
        'options': ['A. Johannesburg', 'B. Cape Town', 'C. Pretoria', 'D. Durban'],
        'correct_answer': 'C'
    },
    {
        'question': 'What is the largest desert in the world?',
        'options': ['A. Sahara Desert', 'B. Gobi Desert', 'C. Antarctic Desert', 'D. Arabian Desert'],
        'correct_answer': 'C'
    },
    {
        'question': 'Who painted "Starry Night"?',
        'options': ['A. Pablo Picasso', 'B. Vincent van Gogh', 'C. Claude Monet', 'D. Leonardo da Vinci'],
        'correct_answer': 'B'
    },
    {
        'question': 'Which country is known as the Land of the Midnight Sun?',
        'options': ['A. Sweden', 'B. Norway', 'C. Canada', 'D. Finland'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the capital of Mexico?',
        'options': ['A. Mexico City', 'B. Madrid', 'C. Buenos Aires', 'D. Bogota'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who wrote "The Great Gatsby"?',
        'options': ['A. Ernest Hemingway', 'B. F. Scott Fitzgerald', 'C. Jane Austen', 'D. Charles Dickens'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the chemical symbol for gold?',
        'options': ['A. Au', 'B. Ag', 'C. Fe', 'D. Cu'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who wrote "The Catcher in the Rye"?',
        'options': ['A. J.D. Salinger', 'B. F. Scott Fitzgerald', 'C. Harper Lee', 'D. Ernest Hemingway'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which country is known as the Land of the Thunder Dragon?',
        'options': ['A. Bhutan', 'B. Nepal', 'C. Myanmar', 'D. Laos'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the largest continent by land area?',
        'options': ['A. Asia', 'B. Africa', 'C. North America', 'D. Europe'],
        'correct_answer': 'A'
    },
    {
        'question': 'In which year did the United States declare its independence?',
        'options': ['A. 1776', 'B. 1789', 'C. 1801', 'D. 1750'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who played the character of Jack Dawson in the movie "Titanic"?',
        'options': ['A. Leonardo DiCaprio', 'B. Tom Hanks', 'C. Brad Pitt', 'D. Johnny Depp'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the square root of 100?',
        'options': ['A. 10', 'B. 8', 'C. 12', 'D. 14'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which famous scientist developed the theory of general relativity?',
        'options': ['A. Isaac Newton', 'B. Niels Bohr', 'C. Albert Einstein', 'D. Stephen Hawking'],
        'correct_answer': 'C'
    },
    {
        'question': 'What is the official language of Brazil?',
        'options': ['A. Spanish', 'B. Portuguese', 'C. Italian', 'D. French'],
        'correct_answer': 'B'
    },
    {
        'question': 'Who wrote the play "Romeo and Juliet"?',
        'options': ['A. William Shakespeare', 'B. Jane Austen', 'C. Charles Dickens', 'D. Leo Tolstoy'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which river is the longest in the world?',
        'options': ['A. Amazon River', 'B. Nile River', 'C. Yangtze River', 'D. Mississippi River'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the largest species of big cat?',
        'options': ['A. Lion', 'B. Tiger', 'C. Leopard', 'D. Cheetah'],
        'correct_answer': 'B'
    },
    {
        'question': 'Which planet is known as the "Red Planet"?',
        'options': ['A. Jupiter', 'B. Mars', 'C. Venus', 'D. Saturn'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the chemical symbol for silver?',
        'options': ['A. Ag', 'B. Au', 'C. Fe', 'D. Cu'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who is the author of "The Great Gatsby"?',
        'options': ['A. Ernest Hemingway', 'B. F. Scott Fitzgerald', 'C. Jane Austen', 'D. Mark Twain'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the largest ocean on Earth?',
        'options': ['A. Atlantic Ocean', 'B. Indian Ocean', 'C. Arctic Ocean', 'D. Pacific Ocean'],
        'correct_answer': 'D'
    },
    {
        'question': 'Who is known as the "Father of Computer Science"?',
        'options': ['A. Alan Turing', 'B. Bill Gates', 'C. Steve Jobs', 'D. Tim Berners-Lee'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the capital of South Africa?',
        'options': ['A. Johannesburg', 'B. Cape Town', 'C. Pretoria', 'D. Durban'],
        'correct_answer': 'C'
    },
    {
        'question': 'What is the largest desert in the world?',
        'options': ['A. Sahara Desert', 'B. Gobi Desert', 'C. Antarctic Desert', 'D. Arabian Desert'],
        'correct_answer': 'C'
    },
    {
        'question': 'Who painted "Starry Night"?',
        'options': ['A. Pablo Picasso', 'B. Vincent van Gogh', 'C. Claude Monet', 'D. Leonardo da Vinci'],
        'correct_answer': 'B'
    },
    {
        'question': 'Which country is known as the Land of the Midnight Sun?',
        'options': ['A. Sweden', 'B. Norway', 'C. Canada', 'D. Finland'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the capital of Mexico?',
        'options': ['A. Mexico City', 'B. Madrid', 'C. Buenos Aires', 'D. Bogota'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who wrote "The Great Gatsby"?',
        'options': ['A. Ernest Hemingway', 'B. F. Scott Fitzgerald', 'C. Jane Austen', 'D. Mark Twain'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the chemical symbol for gold?',
        'options': ['A. Au', 'B. Ag', 'C. Fe', 'D. Cu'],
        'correct_answer': 'A'
    },
    {
        'question': 'In which year did the Titanic sink?',
        'options': ['A. 1912', 'B. 1920', 'C. 1931', 'D. 1945'],
        'correct_answer': 'A'
    }

]

# Shuffle the quiz questions to randomize the order

csv_file_path = 'D:/Quiz.csv'  # Specify the path to your desired CSV file

# Write quiz data to CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['question_text', 'option_text', 'is_correct']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write data
    for question in quiz:
        for option in question['options']:
            is_correct = 'True' if option.startswith(
                question['correct_answer']) else 'False'
            writer.writerow({
                'question_text': question['question'],
                'option_text': option,
                'is_correct': is_correct
            })

print(f'CSV file generated successfully: {csv_file_path}')
