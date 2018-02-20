import os
from random import choice as random_choice


def create_tables(student_list, max_seats):
    return [student_list[i::max_seats] for i in range(max_seats)]


student_list = ["Test13", "Test14", "Test15", "Test16", "Test1", "Test2","Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9", "Test10", "Test11", "Test12",]
randomized_list = []
max_seats = 4
tables = 6

while student_list:
    choice = random_choice(student_list)
    student_list.remove(choice)
    randomized_list.append(choice)

final_tables = create_tables(randomized_list, 4)

print(final_tables)

