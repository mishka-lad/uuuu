grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
def sortByAlphabet(students):
    return students [0]
students.sort()
print(students)
import statistics
result = [statistics.mean(k) for k in grades]
print(result)
students_grades = dict(zip(students, result))
print(students_grades)