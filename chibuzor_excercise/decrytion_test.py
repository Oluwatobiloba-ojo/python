from unittest import TestCase
from decryption import decrypt


class TestSomething(TestCase):
    def test_for_the_decryption_of_an_encrypted_letter(self):
        letter = 'x'
        key = 3
        result = decrypt(letter, key)
        answer = "A"
        self.assertEqual(answer, result)

    def test_for_the_decryption_of_an_encrypted_letter2(self):
        letter = 'ebiil'
        key = 3
        result = decrypt(letter, key)
        answer = 'HELLO'
        self.assertEqual(answer, result)

    def test_for_the_decryption_of_an_encrypted_letter3(self):
        letter = 'AXA'
        key = 3
        result = decrypt(letter, key)
        answer = 'DAD'
        self.assertEqual(answer, result)
