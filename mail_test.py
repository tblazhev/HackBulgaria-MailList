# Imports
import unittest
from mail import CommandList
# from os import


# Test

class test_mail(unittest.TestCase):

    """Testing the unit"""

    def test_parse_command(self):
        self.assertEqual(('hello', 'world'),
                         CommandList.parse_command("hello world"))

    def is_command(self):
        self.assertEqual(
            'hello', CommandList.is_command(('hello', 'world'), "hello"))

    # def test_show_list(self)
    #      self.assertEqual( ,CommandList.show_list())


# Program Run
if __name__ == '__main__':
    unittest.main()
