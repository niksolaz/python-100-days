# high score exercise
student_scores = input("Input a list of student scores: ").split() # split string into list exemple: 78 65 89 86 55 91 64 89
for n in range(0, len(student_scores)):  # 0, 1, 2, 3, 4, 5, 6, 7
    student_scores[n] = int(student_scores[n]) # convert string to integer

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
