from unittest import TestCase
from encryption import generate_cipher, encrypt


class TestSomething(TestCase):
    def test_for_the_generation_of_a_cipher_from_a_key(self):
        key = 3
        cipher = generate_cipher(key)
        result = ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']
        self.assertEqual(cipher, result)

    def test_for_the_generation_of_a_cipher_from_a_key2(self):
        key = 5
        cipher = generate_cipher(key)
        result = ['V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']
        self.assertEqual(cipher, result)

    def test_for_the_encrypt_form_of_a_plain_test(self):
        plain = 'a'
        key = 3
        result = encrypt(key, plain)
        answer = 'X'
        self.assertEqual(result, answer)

    def test_for_the_encrypt_form_of_a_plain_test3(self):
        plain = 'hello'
        key = 3
        result = encrypt(key, plain)
        answer = 'EBIIL'
        self.assertEqual(result, answer)

    def test_for_the_encrypt_form_of_a_plain_test4(self):
        plain = 'tie'
        key = 3
        result = encrypt(key, plain)
        answer = 'QFB'
        self.assertEqual(result, answer)

    def test_for_the_encrypt_form_of_a_plain_test5(self):
        plain = 'dad'
        key = 3
        result = encrypt(key, plain)
        answer = 'AXA'
        self.assertEqual(result, answer)
