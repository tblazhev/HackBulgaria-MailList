import unittest
from listparser import ListParser
import os
from glob import glob


class ListParserTest(unittest.TestCase):
    """docstring for ListParserTest"""
    def setUp(self):
        self.list_parser = ListParser()
        self.script_path = os.path.dirname(os.path.realpath(__file__))
        self.lists_dir_path = self.script_path + "/lists"
        self.lists_glob_path = self.lists_dir_path + "/list_*"
        self.test_list_name = "test_list"
        self.test_list_path = self.lists_dir_path + "/list_" + self.test_list_name

    def test_init(self):
        self.assertEqual(self.script_path, self.list_parser.get_script_path())
        self.assertEqual(self.lists_dir_path, self.list_parser.get_lists_path())
        self.assertEqual(self.lists_glob_path, self.list_parser.get_glob_path())

    def test_spaces_to_underscores(self):
        filename = "filename with spaces"
        new_filename = self.list_parser.spaces_to_underscores(filename)
        new_filename_check = "filename_with_spaces"
        self.assertEqual(new_filename_check, new_filename)

    def test_create_list(self):
        self.assertTrue(self.list_parser.create_list(self.test_list_name))
        files = glob(self.lists_glob_path)
        self.assertTrue(self.test_list_path in files)

    def test_create_existing_list(self):
        self.list_parser.create_list(self.test_list_name)
        self.assertTrue(not self.list_parser.create_list(self.test_list_name))

    def test_create_list_with_spaces(self):
        list_with_spaces = "name with spaces"
        list_with_spaces_path = self.lists_dir_path + "/list_name_with_spaces"
        self.list_parser.create_list(list_with_spaces)
        files = glob(self.lists_glob_path)
        self.assertTrue(list_with_spaces_path in files)

    def test_get_lists(self):
        self.list_parser.create_list("testlist1")
        self.list_parser.create_list("testlist2")
        self.list_parser.create_list("testlist3")
        lists = ["testlist1", "testlist2", "testlist3"]
        self.assertEqual(lists, self.list_parser.get_lists())

    def test_get_list_data(self):
        self.list_parser.create_list(self.test_list_name)
        f = open(self.test_list_path, "w")
        contents = "Tedi - tedi@hackbulgaria.com\nAdrian - adrian@hackbulgaria.com"
        f.write(contents)
        f.close()
        users = contents.split("\n")
        self.assertEqual(users, self.list_parser.get_list_data(self.test_list_name))

    def test_get_non_existing_list(self):
        self.assertTrue(not self.list_parser.get_list_data(self.test_list_name))

    def test_add_to_list(self):
        self.list_parser.create_list(self.test_list_name)
        new_entry = ["Gosho - Gosho@hackbulgaria.com"]
        self.assertTrue(self.list_parser.add_to_list(self.test_list_name, new_entry))
        users = self.list_parser.get_list_data(self.test_list_name)
        self.assertEqual(new_entry, users)

    def test_add_to_nonexisting_list(self):
        new_entry = ["Gosho - Gosho@hackbulgaria.com"]
        self.assertTrue(not self.list_parser.add_to_list(self.test_list_name, new_entry))

    def tearDown(self):
        files = glob(self.lists_glob_path)
        for f in files:
            try:
                os.remove(f)
            except OSError:
                pass

if __name__ == '__main__':
    unittest.main()
