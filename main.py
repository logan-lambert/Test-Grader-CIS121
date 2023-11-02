"""
Test Grader Project

Written By:
Logan Lambert
Shawn Perkins
Sophonias Aregawi
10/31/2023

This program reads through a folder of student tests,
it then calculates the grade for each student compared
to the answer key file. Finally, it writes class average
and student scores to a separate file specified by user.
"""

from functions import *
import os

if __name__ == "__main__":
    test_result_dir = input("Enter a name for the test result file: ") + ".txt"
    _ = input("Press enter to start")
 
    student_tests = []
    graded_info = []

    # Loops througn tests folder and reads each file
    for file in os.listdir("./tests"):
        if file.endswith(".txt"):
            test = read_txt_file(f"./tests/{file}")
            student_tests.append(test)
    
    # Reads answer key file
    answer_key = read_txt_file("answer_key.txt")

    # Grades individual tests and records results into graded_info list
    for test in student_tests:
        graded_test = grader(test, answer_key)
        graded_info.append(graded_test)
    
    class_average = class_average_calc(graded_info)

    # Writes test results to specified file
    write_scores(test_result_dir, graded_info, class_average)

    print(f"Results posted successfully in {test_result_dir}")
