student_heights = input("Input a list of student's height ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
no_of_students = 0

for height in student_heights:
    total_height = int(total_height + height)
    no_of_students = int(no_of_students + 1)
print(total_height)
print(no_of_students)

average_height = total_height / no_of_students
print(f"The average height is {average_height}")
