from unittest import TestCase
from python_program import duplicate_first_char


class TestSomething(TestCase):
    def test_for_duplicate_of_first_character_to_dollar_sign(self):
        self.assertEqual("resta$t", duplicate_first_char("restart", "$"))

    def test_for_duplicate_of_first_character_to_dollar_sign2(self):
        self.assertEqual("aeropl#ne", duplicate_first_char('aeroplane', '#'))

    def test_for_duplicate_of_first_character_to_a_special_character(self):
        self.assertEqual("shot$$", duplicate_first_char('shotss', '$'))

    def test_for_duplicate_of_first_character_to_a_special_character_2(self):
        self.assertEqual("letter", duplicate_first_char('letter', '$'))
