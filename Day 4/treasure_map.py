# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Convert the user input to row and column indices
row_index = int(position[0]) - 1
column_index = int(position[1]) - 1

# Mark the spot with 'X'
map[row_index][column_index] = '❌'

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
