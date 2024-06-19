students_scores = {'Alex': 98, 'Beth': 13, 'Caroline': 97, 'Dave': 69, 'Eleanor': 83, 'Freddie': 54}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)