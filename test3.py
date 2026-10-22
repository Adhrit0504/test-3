
grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}


total_score = 0
for score in grades.values():
    total_score += score

average_score = total_score / len(grades)
print(f"Class Average: {average_score:.2f}")


top_scorer = max(grades, key=grades.get)
bottom_scorer = min(grades, key=grades.get)

print(f"Top Scorer: {top_scorer} with {grades[top_scorer]}")
print(f"Bottom Scorer: {bottom_scorer} with {grades[bottom_scorer]}")


search_name = input("Enter student name to search: ")
student_score = grades.get(search_name)

if student_score is not None:
    print(f"{search_name}'s grade is {student_score}.")
else:
    print(f"Sorry, '{search_name}' was not found in the grade book.")