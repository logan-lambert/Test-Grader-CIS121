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
from Test import Test
import os

if __name__ == "__main__":
    test_result_dir = input("Enter a name for the test result file: ") + ".txt"
    _ = input("Press enter to start")
 
    student_tests: list[Test] = []
    scores: list[int] = []

    # Loops througn tests folder and reads each file
    for file in os.listdir("./"):
        if not file.startswith("answer_key") and file.endswith(".txt"):
            test_content = read_txt_file(file)
            test = Test(test_content[0], test_content[1:])
            student_tests.append(test)
    
    # Reads answer key file
    answer_key = read_txt_file("answer_key.txt")

    # Grades individual tests and records results into graded_info list
    for test in student_tests:
        test.grade(answer_key)
        scores.append(test.return_score())
    
    class_average = class_average_calc(scores)
    
    # Writes test results to specified file
    write_scores(test_result_dir, student_tests, class_average)

    print(f"Results posted successfully in {test_result_dir}")
