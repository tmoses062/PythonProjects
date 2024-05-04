row1 = ["😁","😁","😁"]
row2 = ["😁","😁","😁"]
row3 = ["😁","😁","😁"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row = int(position[0])
column = int(position[1])
# if row == 1:
#     if column == 1:
#         row1[0] = "X"
#     elif column == 2:
#         row1[1] = "X"
#     else:
#         row1[2] = "X"
    
# elif row == 2:
#     if column == 1:
#         row2[0] = "X"
#     elif column == 2:
#         row2[1] = "X"
#     else:
#         row2[2] = "X"
# else:
#     if column == 1:
#         row3[0] = "X"
#     elif column == 2:
#         row3[1] = "X"
#     else
#         row3[2] = "X"

    # OR
    
# selected_row = map[column - 1]
# selected_row[row - 1] = 'X'

    # OR

map[column - 1][row - 1] = 'X'
    
print(f"{row1}\n{row2}\n{row3}")
