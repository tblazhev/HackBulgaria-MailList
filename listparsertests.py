import unittest
from listparser import ListParser
import os
from glob import glob


class ListParserTest(unittest.TestCase):
    """docstring for ListParserTest"""
    def setUp(self):
        self.list_parser = ListParser()
        self.script_path = os.path.dirname(os.path.realpath(__file__))

        self.lists_dir_path = self.script_path + "/lists_test"
        self.common_path = self.lists_dir_path + "/list_"
        self.lists_glob_path = self.common_path + "*"

        self.list_parser.set_lists_dir_path(self.lists_dir_path)
        self.list_parser.set_common_path(self.common_path)
        self.list_parser.set_glob_path(self.lists_glob_path)

        try:
            os.mkdir(self.lists_dir_path)
        except OSError:
            pass

        self.test_list_name = "test_list"
        self.test_list_path = self.lists_dir_path + "/list_" + self.test_list_name

    def test_init(self):
        self.assertEqual(self.script_path, self.list_parser.get_script_path())
        self.assertEqual(self.lists_dir_path, self.list_parser.get_lists_dir_path())
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

    def test_get_non_existing_list_data(self):
        self.assertTrue(not self.list_parser.get_list_data(self.test_list_name))

    def test_add_to_list(self):
        self.list_parser.create_list(self.test_list_name)
        name = "Tedi"
        email = "tedi@hackbulgaria.com"
        self.assertTrue(self.list_parser.add_to_list(self.test_list_name, name, email))
        name = "Adrian"
        email = "adrian@hackbulgaria.com"
        self.assertTrue(self.list_parser.add_to_list(self.test_list_name, name, email))

        expected = "Tedi - tedi@hackbulgaria.com\nAdrian - adrian@hackbulgaria.com"
        f = open(self.common_path + self.test_list_name, "r")
        contents = f.read()
        f.close()
        self.assertEqual(expected, contents)

    def test_add_existing_item(self):
        self.list_parser.create_list(self.test_list_name)
        name = "Tedi"
        email = "tedi@hackbulgaria.com"
        self.assertTrue(self.list_parser.add_to_list(self.test_list_name, name, email))
        self.assertTrue(not self.list_parser.add_to_list(self.test_list_name, name, email))

    def test_add_to_nonexisting_list(self):
        name = "Tedi"
        email = "tedi@hackbulgaria.com"
        self.assertTrue(not self.list_parser.add_to_list(self.test_list_name, name, email))

    def test_search_email(self):
        self.list_parser.create_list(self.test_list_name)
        name = "Tedi"
        email = "tedi@hackbulgaria.com"
        self.list_parser.add_to_list(self.test_list_name, name, email)
        self.assertTrue(self.list_parser.search_email("tedi@hackbulgaria.com"))

    def test_search_non_existing_email(self):
        self.list_parser.create_list(self.test_list_name)
        name = "Tedi"
        email = "tedi@hackbulgaria.com"
        self.list_parser.add_to_list(self.test_list_name, name, email)
        self.assertTrue(not self.list_parser.search_email("Gosho2@hackbulgaria.com"))

    def test_update_subscriber(self):
        self.list_parser.create_list(self.test_list_name)
        name = "Tedi"
        email = "tedi@hackbulgaria.com"
        self.list_parser.add_to_list(self.test_list_name, name, email)
        name = "Tedi2"
        email = "tedi2@hackbulgaria.com"
        self.list_parser.add_to_list(self.test_list_name, name, email)
        name = "Tedi3"
        email = "tedi3@hackbulgaria.com"
        self.list_parser.add_to_list(self.test_list_name, name, email)

        new_name = 'Tedi4'
        new_email = 'tedi4@hackbulgaria.com'
        res = self.list_parser.update_subscriber(self.test_list_name, name, email, new_name, new_email)
        self.assertTrue(res)

        entry1 = 'Tedi - tedi@hackbulgaria.com'
        entry2 = 'Tedi2 - tedi2@hackbulgaria.com'
        entry3 = 'Tedi4 - tedi4@hackbulgaria.com'
        expected = [entry1, entry2, entry3]
        users = self.list_parser.get_list_data(self.test_list_name)
        self.assertEqual(expected, users)

    def test_remove_subscriber(self):
        self.list_parser.create_list(self.test_list_name)
        self.list_parser.add_to_list(self.test_list_name, "Tedi", "tedi@hackbulgaria.com")
        self.list_parser.add_to_list(self.test_list_name, "Tedi2", "tedi2@hackbulgaria.com")
        self.assertTrue(self.list_parser.remove_subscriber(self.test_list_name, "Tedi2", "tedi2@hackbulgaria.com"))
        subscribers = self.list_parser.get_list_data(self.test_list_name)
        self.assertTrue("Tedi2 - tedi2@hackbulgaria.com" not in subscribers)

    def test_remove_nonexisting_subscriber(self):
        self.list_parser.create_list(self.test_list_name)
        self.list_parser.add_to_list(self.test_list_name, "Tedi", "tedi@hackbulgaria.com")
        self.list_parser.add_to_list(self.test_list_name, "Tedi2", "tedi2@hackbulgaria.com")
        self.assertTrue(not self.list_parser.remove_subscriber(self.test_list_name, "Tedi22", "tedi22@hackbulgaria.com"))

    def test_update_nonexisting_subscriber(self):
        self.list_parser.create_list(self.test_list_name)
        name = "Tedi"
        email = "tedi@hackbulgaria.com"
        self.list_parser.add_to_list(self.test_list_name, name, email)
        name = "Tedi2"
        email = "tedi2@hackbulgaria.com"
        self.list_parser.add_to_list(self.test_list_name, name, email)
        name = "Tedi3"
        email = "tedi3@hackbulgaria.com"
        self.list_parser.add_to_list(self.test_list_name, name, email)

        new_name = 'Tedi4'
        new_email = 'tedi4@hackbulgaria.com'
        res = self.list_parser.update_subscriber(self.test_list_name, name, "fakemail@fake", new_name, new_email)
        self.assertTrue(not res)

    def test_update_list_name(self):
        self.list_parser.create_list(self.test_list_name)
        self.assertTrue(self.list_parser.update_list(self.test_list_name, "new_name"))
        self.assertTrue(not self.list_parser.create_list("new_name"))
        self.assertTrue(self.list_parser.create_list(self.test_list_name))

    def test_update_nonexisting_list_name(self):
        self.list_parser.create_list(self.test_list_name)
        self.assertTrue(not self.list_parser.update_list("does not exist", "new_name"))

    def test_update_list_name_to_name_that_already_exists(self):
        self.list_parser.create_list(self.test_list_name)
        self.list_parser.create_list("new_name")
        self.assertTrue(not self.list_parser.update_list(self.test_list_name, "new_name"))

    # def test_merge_lists(self):
    #     self.list_parser.create_list("list1")
    #     self.list_parser.create_list("list2")
    #     self.list_parser.add_to_list("list1", "Tedi", "tedi@hackbulgaria.com")
    #     self.list_parser.add_to_list("list1", "Tedi2", "tedi2@hackbulgaria.com")
    #     self.list_parser.add_to_list("list2", "Tedi2", "tedi2@hackbulgaria.com")
    #     self.list_parser.add_to_list("list2", "Tedi3", "tedi3@hackbulgaria.com")

    #     self.assertTrue(self.list_parser.merge_lists("list1", "list2", "list3"))
    #     expected_users = ["Tedi - tedi@hackbulgaria.com", "Tedi2 - tedi2@hackbulgaria.com", "tedi3@hackbulgaria.com"]
    #     users = self.list_parser.get_list_data("list3")
    #     print(users)
    #     self.assertEqual(expected_users, users)

    def tearDown(self):
        files = glob(self.lists_glob_path)
        for f in files:
            try:
                os.remove(f)
            except OSError:
                pass
        try:
            os.rmdir(self.lists_dir_path)
        except OSError:
            pass

if __name__ == '__main__':
    unittest.main()
