# -*- coding: utf-8 -*-

# if python < 3
from __future__ import division 


# Task from http://www.cyberforum.ru/python/thread1719415.html

groupmates = [
    {
        "name": "StudentOne",
        "group": "111",
        "age": 21,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "StudenTwo",
        "group": "111",
        "age": 22,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "StudentThree",
        "group": "111",
        "age": 23,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "StudentFour",
        "group": "111",
        "age": 24,
        "marks": [5, 5, 5, 4, 5]
    }
]


def pass_gpa(students, gpa):
    """
    Функция возвращет список студентов,
    прошедших средний балл (gpa)
    """
    
    pass_students = []
    
    for student in students:
        if (sum(student['marks']) / len(student['marks'])) > gpa:
            pass_students.append(student)
            
    return pass_students
    

print("name\t\tgroup\tage\tmarks")

for student in pass_gpa(groupmates, 4):    
    print("%s\t%s\t%s\t%s" % (student['name'], 
                              student['group'], 
                              student['age'], 
                              student['marks']))




