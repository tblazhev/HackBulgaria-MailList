import os
from glob import glob


class ListParser():
    """docstring for ListParser"""
    def __init__(self):
        self.__script_path = os.path.dirname(os.path.realpath(__file__))
        self.__lists_dir_path = self.__script_path + "/lists"
        self.__common_path = self.__lists_dir_path + "/list_"
        self.__glob_path = self.__lists_dir_path + "/list_*"

    def get_script_path(self):
        return self.__script_path

    def get_lists_dir_path(self):
        return self.__lists_dir_path

    def get_common_path(self):
        return self.__common_path

    def get_glob_path(self):
        return self.__glob_path

    def spaces_to_underscores(self, string):
        return string.replace(" ", "_")

    def create_list(self, list_name):
        list_name = self.spaces_to_underscores(list_name)
        file_path = self.__lists_dir_path + "/list_" + list_name
        try:
            f = open(file_path, "x")
            f.close()
        except IOError:
            return False
        return True

    def get_lists(self):
        files = glob(self.__glob_path)
        lists = []
        for f in files:
            lists.append(f.replace(self.__glob_path[:-1], ""))
        lists.sort()
        return lists

    def get_list_data(self, list_name):
        file_path = self.__common_path + list_name
        try:
            f = open(file_path, "r")
        except IOError:
            return False
        contents = f.read()
        f.close()
        users = contents.split("\n")
        return users

    def add_to_list(self, list_name, entry):
        file_path = self.__common_path + list_name
        try:
            f = open(file_path, "r+")
        except IOError:
            return False
        contents = f.read()
        users = contents.split("\n")
        users.extend(entry)
        users.remove('')
        users = "\n".join(users)
        f.write(users)
        f.close()
        return True

    def search_email(self, email):
        lists = self.get_lists()
        for list_name in lists:
            users = self.get_list_data(list_name)
            for user in users:
                if email in user:
                    return True
        return False
