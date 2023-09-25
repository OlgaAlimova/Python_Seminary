# Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и
# результаты тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для
# каждого предмета и по оценкам всех предметов вместе взятых.

import csv

class Student:
    def __init__(self, full_name, subjects_csv):
        self._full_name = full_name
        self._subjects = self._load_subjects_from_csv(subjects_csv)

    def _load_subjects_from_csv(self, csv_file):
        subjects = {}
        with open(csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                subject_name = row[0]
                subjects[subject_name] = {'grades': [], 'test_results': []}
        return subjects

    def _validate_full_name(self, value):
        # Проверка ФИО: должно начинаться с заглавной буквы и содержать только буквы и пробелы.
        if not value.istitle() or not value.replace(' ', '').isalpha():
            raise ValueError("ФИО должно начинаться с заглавной буквы и содержать только буквы и пробелы.")
        return value

    def _validate_subject(self, subject):
        if subject not in self._subjects:
            raise ValueError(f"Предмет '{subject}' не существует.")
        return subject

    def _validate_grade(self, grade):
        if grade not in (2, 3, 4, 5):
            raise ValueError("Оценка должна быть от 2 до 5.")
        return grade

    def _validate_test_result(self, result):
        if not (0 <= result <= 100):
            raise ValueError("Результат теста должен быть от 0 до 100.")
        return result

    def add_grade(self, subject, grade):
        subject = self._validate_subject(subject)
        grade = self._validate_grade(grade)
        self._subjects[subject]['grades'].append(grade)

    def add_test_result(self, subject, result):
        subject = self._validate_subject(subject)
        result = self._validate_test_result(result)
        self._subjects[subject]['test_results'].append(result)

    def get_average_grade(self, subject):
        subject = self._validate_subject(subject)
        grades = self._subjects[subject]['grades']
        if not grades:
            return 0
        return sum(grades) / len(grades)

    def get_average_test_result(self, subject):
        subject = self._validate_subject(subject)
        test_results = self._subjects[subject]['test_results']
        if not test_results:
            return 0
        return sum(test_results) / len(test_results)

    def get_overall_average_grade(self):
        all_grades = [grade for subject_data in self._subjects.values() for grade in subject_data['grades']]
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def __get__(self, instance, owner):
        return self._full_name

    def __set__(self, instance, value):
        self._full_name = self._validate_full_name(value)

    full_name = property(__get__, __set__)

# Пример использования
student = Student("Иван Иванович Иванов", "subjects.csv")
student.add_grade("Math", 4)
student.add_test_result("Math", 90)
student.add_grade("History", 5)
student.add_test_result("History", 85)

print(f"Имя студента: {student.full_name}")
print(f"Средний балл по математике: {student.get_average_grade('Math')}")
print(f"Средний балл по всем предметам: {student.get_overall_average_grade()}")
