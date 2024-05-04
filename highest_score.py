student_scores = input("Input a list of student's scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

""" student_scores.sort()

no_of_scores = 0
for score in student_scores:
    no_of_scores += 1
print(f"The highest score is {student_scores[no_of_scores - 1]}") """

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f'The highest score is {highest_score}')
