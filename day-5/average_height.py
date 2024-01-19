# average height exercise
list_of_height = [180, 124, 165, 173, 189, 169, 146]

total_height = 0

for height in list_of_height:
    total_height += height

print(f"Total height is {total_height}")

number_of_students = 0

for student in list_of_height:
    number_of_students += 1

print(f"Number of students is {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"Average height is {average_height}")