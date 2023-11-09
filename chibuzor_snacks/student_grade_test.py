from unittest import TestCase
from student_grade_function import position, total_of_scores, highest_scoring_student, highest_score, \
    lower_student_score, lower_score, number_of_passes, number_of_failure, checks_the_greatest_numbers_of_pass, \
    checks_the_greatest_subject_pass, check_for_the_greatest_score_in_a_2D_list, check_for_the_greatest_student, \
    check_for_the_lowest_score_in_a_2D_list, check_for_the_subject_with_highest_score, check_for_the_lowest, \
    check_for_the_overall_highest_score, check_for_the_overall_lowest_score


class TestSomething(TestCase):
    def test_position_of_a_score(self):
        total = [99, 78, 50, 67, 24, 90]
        result = [1, 3, 5, 4, 6, 2]
        self.assertEqual(result, position(total))

    def test_position_of_a_score2(self):
        total = [122, 150, 560, 300]
        result = [4, 3, 1, 2]
        self.assertEqual(position(total), result)

    def test_positions(self):
        total = [50, 70, 60, 40]
        result = [3, 1, 2, 4]
        self.assertEqual(result, position(total))

    def test_positional(self):
        total = [100, 150, 140, 190, 99]
        result = [4, 2, 3, 1, 5]
        self.assertEqual(position(total), result)

    def test_sum_of_a_list(self):
        numbers = [45, 56, 78, 89]
        result = 268
        self.assertEqual(result, total_of_scores(numbers))

    def test_for_the_highest_scoring_student(self):
        grades = [67, 98, 93, 78]
        result = 2
        self.assertEqual(result, highest_scoring_student(grades))

    def test_for_highest_scoring_in_a_subject(self):
        scores = [67, 98, 93, 78]
        result = 98
        self.assertEqual(result, highest_score(scores))

    def test_for_lower_score(self):
        grades = [67, 98, 93, 78]
        result = 67
        self.assertEqual(result, lower_score(grades))

    def test_for_lower_scoring_student(self):
        grades = [67, 98, 93, 78]
        result = 1
        self.assertEqual(result, lower_student_score(grades))

    def test_for_lower_scoring_student2(self):
        grades = [98, 93, 78, 67]
        student = 4
        self.assertEqual(student, lower_student_score(grades))

    def test_for_number_of_passes_in_a_score(self):
        grades = [67, 98, 93, 78]
        self.assertEqual(4, number_of_passes(grades))

    def test_for_number_of_passes(self):
        grades = [21, 62, 34, 83]
        self.assertEqual(number_of_passes(grades), 2)

    def test_for_the_number_of_failures(self):
        grades = [67, 98, 93, 78]
        self.assertEqual(number_of_failure(grades), 0)

    def test_for_the_number_of_fail(self):
        grades = [21, 62, 34, 83]
        self.assertEqual(number_of_failure(grades), 2)

    def test_for_greatest_number_of_passes(self):
        grades = [21, 62, 34, 83]
        gradesB = [67, 98, 93, 78]
        gradeC = [49, 56, 27, 66]
        list_of_passes = [number_of_passes(grades), number_of_passes(gradesB), number_of_passes(gradeC)]
        self.assertEqual(checks_the_greatest_numbers_of_pass(list_of_passes), number_of_passes(gradesB))

    def test_for_the_subject_with_greatest_passes(self):
        grades = [21, 62, 34, 83]
        gradesB = [67, 98, 93, 78]
        gradeC = [49, 56, 27, 66]
        lists_of_subject_passes = [number_of_passes(grades), number_of_passes(gradesB), number_of_passes(gradeC)]
        self.assertEqual(checks_the_greatest_subject_pass(lists_of_subject_passes), 1)

    def test_for_the_greatest_number_of_failures(self):
        grades = [21, 62, 54, 83]
        gradesB = [67, 98, 93, 78]
        gradeC = [49, 56, 27, 66]
        lists_of_subject_failures = [number_of_failure(grades), number_of_failure(gradesB), number_of_failure(gradeC)]
        self.assertEqual(checks_the_greatest_numbers_of_pass(lists_of_subject_failures), number_of_failure(gradeC))

    def test_for_the_greatest_in_a_2D_list(self):
        grades = [[21, 62, 54, 83], [67, 98, 93, 78], [49, 56, 27, 66]]
        result = 98
        self.assertEqual(check_for_the_greatest_score_in_a_2D_list(grades), result)

    def test_for_the_student_who_scored_highest_score(self):
        grades = [[21, 62, 54, 83], [67, 98, 93, 78]]
        result = 2
        self.assertEqual(check_for_the_greatest_student(grades), result)

    def test_for_the_subject_with_highest_scores_and_the_score_and_row(self):
        grades = [[21, 62, 54, 83],
                  [98, 67, 93, 78]]
        result = [1, 2, 98]
        self.assertEqual(check_for_the_subject_with_highest_score(grades, 4), result)

    def test_for_the_column_which_have_highest_score_and_the_score_and_row(self):
        grades = [[34, 56, 78, 99],
                  [67, 78, 89, 100]]
        self.assertEqual(check_for_the_subject_with_highest_score(grades, 4), [4, 2, 100])

    def test_for_the_the_lowest_score_in_a_2D_list(self):
        grades = [[21, 62, 54, 83], [67, 98, 93, 78]]
        result = 21
        self.assertEqual(check_for_the_lowest_score_in_a_2D_list(grades), result)

    def test_for_the_lowest_score_and_return_the_row_column_and_score(self):
        grades = [[88, 76, 78, 99],
                  [67, 78, 89, 100]]
        self.assertEqual(check_for_the_lowest(grades, 4), [1, 2, 67])
    def test_for_the_highest_score_and_return_the_student_and_score(self):
        total_grades = [137, 216, 154, 227]
        self.assertEqual(check_for_the_overall_highest_score(total_grades), [4, 227])

    def test_for_the_lowest_score_and_return_the_student_and_score(self):
        total_grades = [137, 216, 154, 227]
        self.assertEqual(check_for_the_overall_lowest_score(total_grades), [1, 137])
