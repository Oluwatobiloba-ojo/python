from unittest import TestCase
from student_collection_age_and_name import student_age


class TestSomething(TestCase):
    def test_for_student_age(self):
        name = "Dike"
        age = 33
        age_result = student_age(name)
        self.assertEqual(age, age_result)

    def test_for_student_age_existing_in_the_list(self):
        name = 'OPE'
        age = 25
        age_result = student_age(name)
        self.assertEqual(age, age_result)

    def test_for_the_addition_of_the_name_which_is_not_in_a_dictionary(self):
        name = 'Sikiru'
        age = 45
        age_result = student_age(name, age)
        self.assertEqual(age, age_result)

    def test_for_the_addition_of_name_in_a_dictionary(self):
        name = 'Melody'
        age = 20
        age_result = student_age(name)
        self.assertEqual(age, age_result)

    def test_for_the_output_of_the_name(self):
        name = 'Rashidat'
        age = 50
        age_result = student_age(name, age)
        self.assertEqual(age, age_result)
