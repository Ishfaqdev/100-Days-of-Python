import pandas as pd

# Replace 'D:/Quiz1.csv' with the actual file path
file_path = 'D:/Quiz1.csv'

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Assuming 'Question' is the column with questions
df_unique = df.drop_duplicates(subset='Question')

# Save the result to a new CSV file
# Replace 'D:/UniqueQuiz1.csv' with the desired file name and path
df_unique.to_csv('D:/UniqueQuiz1.csv', index=False)
