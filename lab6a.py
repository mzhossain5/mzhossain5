#!/usr/bin/env python3
# Author ID: mzhossain5

class Student:

    def __init__(self, name, number):
        # Ensure that the student number is always stored as a string
        self.name = name
        self.number = str(number)
        self.courses = {}

    def displayStudent(self):
        """Return a formatted string containing the student's name and number."""
        return f'Student Name: {self.name}\nStudent Number: {self.number}'

    def addGrade(self, course, grade):
        """Add or update the grade for a specific course."""
        self.courses[course] = grade

    def displayGPA(self):
        """Calculate and return the student's GPA as a formatted string."""
        if not self.courses:
            return f'GPA of student {self.name} is 0.0'
        total = sum(self.courses.values())
        gpa = total / len(self.courses)
        return f'GPA of student {self.name} is {gpa:.1f}'

    def displayCourses(self):
        """Return a list of courses with grades greater than 0.0."""
        return [course for course, grade in self.courses.items() if grade > 0.0]

if __name__ == '__main__':
    # Create and test the Student class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Output for student1
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Output for student2
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())

