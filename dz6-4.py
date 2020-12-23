class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.everage_rate = 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            lecturer.calc_everage_rate()
        else:
            return 'Ошибка'

    def calc_everage_hw_rate(self):
        'Считает среднюю оценку по всем домашним заданиям'
        self.everage_rate = 0
        marks_quantity = 0
        for key in self.grades.values():
            marks_quantity += len(key)
            for marks in key:
                self.everage_rate += marks
        self.everage_rate = round(self.everage_rate / marks_quantity, 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.everage_rate}' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.everage_rate < other.everage_rate
        else:
            return 'Ошибка'

    def __le__(self, other):
        if isinstance(other, Student):
            return self.everage_rate <= other.everage_rate
        else:
            return 'Ошибка'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.everage_rate == other.everage_rate
        else:
            return 'Ошибка'

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.everage_rate != other.everage_rate
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.everage_rate > other.everage_rate
        else:
            return 'Ошибка'

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.everage_rate >= other.everage_rate
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.everage_rate = 0

    def calc_everage_rate(self):
        'Считает среднюю оценку по всем курсам'
        self.everage_rate = 0
        marks_quantity = 0
        for key in self.grades.values():
            marks_quantity += len(key)
            for marks in key:
                self.everage_rate += marks
        self.everage_rate = round(self.everage_rate / marks_quantity, 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.everage_rate}'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.everage_rate < other.everage_rate
        else:
            return 'Ошибка'

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.everage_rate <= other.everage_rate
        else:
            return 'Ошибка'

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.everage_rate == other.everage_rate
        else:
            return 'Ошибка'

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.everage_rate != other.everage_rate
        else:
            return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.everage_rate > other.everage_rate
        else:
            return 'Ошибка'

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.everage_rate >= other.everage_rate
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __str__(self):
        # print('Имя:', ' ', self.name)
        # print('Фамилия:', ' ', self.surname)
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            student.calc_everage_hw_rate()
        else:
            return 'Ошибка'

def calc_everage_stud_rate(students, course):
    'Считает среднюю оценку по всем студентам, которые прошли определенный курс'
    everage_score = 0
    marks_count = 0
    for st in students:
        if isinstance(st, Student) and course in st.grades.keys():
            for marks in st.grades[course]:
                marks_count += 1
                everage_score += marks

    if everage_score == 0:
        return 0

    return round(everage_score / marks_count, 1)


def calc_everage_lect_rate(lecturer, course):
    'Считает среднюю оценку по всем лекторам, которые прошли определенный курс'
    everage_score = 0
    marks_count = 0
    for lt in lecturer:
        if isinstance(lt, Lecturer) and course in lt.grades.keys():
            for marks in lt.grades[course]:
                marks_count += 1
                everage_score += marks

    if everage_score == 0:
        return 0

    return round(everage_score / marks_count, 1)


student1 = Student('Ivan', 'Ladanov', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']

student2 = Student('Elena', 'Ladanova', 'female')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']

lecturer1 = Lecturer('Anton', 'Ivanov')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Java']

lecturer2 = Lecturer('Alex', 'Mitnik')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Java']

reviewer1 = Reviewer('Artem', 'Zabolotnyy')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Java']
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)

reviewer2 = Reviewer('Andrey', 'Andreev')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Java']
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 9)

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 9)

print(f"\n\nСредняя оценка по всем студентам для курса Пайтон {calc_everage_stud_rate([student1, student2],'Python')}")
print(f"Средняя оценка по всем лекторам для курса Пайтон {calc_everage_lect_rate([lecturer1, lecturer2],'Python')}\n\n")

#Тестируем красивый вывод#
print(student1, student2, lecturer1, lecturer2, reviewer1, reviewer2, sep='\n\n')

#Тестируем операции сравнения#
print(f'\nСравниваем лекторов:\nРавно: {lecturer1 == lecturer2}\nНе равно: {lecturer1 != lecturer2}'
      f'\nБольше: {lecturer1 > lecturer2}\n')

print(f'\nСравниваем студентов:\nРавно: {student1 == student2}\nНе равно: {student1 != student2}'
      f'\nБольше или равно: {student1 >= student2}\n')

# new_lecturer = Lecturer('Anton', 'Ivanov')
# new_lecturer.courses_attached += ['Python']
# new_lecturer2 = Lecturer('Artem','Artemov')
# new_lecturer2.courses_attached += ['Java']
# new_lecturer2.everage_rate = 9
# print(f'\nСравниваем лекторов:\nРавно: {new_lecturer == new_lecturer2}\nНе равно: {new_lecturer != new_lecturer2}'
#       f'\nБольше: {new_lecturer > new_lecturer2}\n\n')
#
# new_reviewer = Reviewer('Alex', 'Mitnik')
# print(new_reviewer)
#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# best_student.courses_in_progress += ['Java']
# best_student.courses_in_progress += ['JS']
# best_student.finished_courses += ['HTML']
# best_student.finished_courses += ['Bash']
#
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student)
#
# best_student.rate_lecturer(new_lecturer, 'Python', 10)
# best_student.rate_lecturer(new_lecturer, 'Python', 9)
# best_student.rate_lecturer(new_lecturer, 'Python', 10)
# print(new_lecturer)
#
# print(f'{new_lecturer.grades}')


