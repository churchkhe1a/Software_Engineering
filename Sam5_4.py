def fix_grades(grades):
 new_grades = []
 for grade in grades:
  if grade == 2:
   continue
  elif grade == 3:
   new_grades.append(4)
  else:
   new_grades.append(grade)
 return new_grades

grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print(f"Обновленный список оценок 1: {fix_grades(grades1)}")
print(f"Обновленный список оценок 2: {fix_grades(grades2)}")
print(f"Обновленный список оценок 3: {fix_grades(grades3)}")
