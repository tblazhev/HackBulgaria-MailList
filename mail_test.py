# Imports
import unittest
from mail import CommandList
from listparser import ListParser
# from os import


# Test

class test_mail(unittest.TestCase):

    """Testing the unit"""

    def setUp(self):
        self.list_parser = ListParser()
        self.command_list = CommandList(self.list_parser)

    def test_parse_command(self):
        self.assertEqual(('hello', 'world'),
                         self.command_list.parse_command("hello world"))

    def test_is_command(self):
        self.assertTrue(
            True, self.command_list.is_command(('hello', 'world'), "hello"))


# Program Run
if __name__ == '__main__':
    unittest.main()
