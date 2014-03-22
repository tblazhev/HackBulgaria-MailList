import os
from glob import glob


class ListParser():
    """docstring for ListParser"""
    def __init__(self):
        self.__script_path = os.path.dirname(os.path.realpath(__file__))
        self.__lists_dir_path = self.__script_path + "/lists"
        self.__common_path = self.__lists_dir_path + "/list_"
        self.__glob_path = self.__common_path + "*"

    """ Getters and Setters """
    def get_script_path(self):
        return self.__script_path

    def get_lists_dir_path(self):
        return self.__lists_dir_path

    def set_lists_dir_path(self, path):
        self.__lists_dir_path = path

    def get_common_path(self):
        return self.__common_path

    def set_common_path(self, path):
        self.__common_path = path

    def get_glob_path(self):
        return self.__glob_path

    def set_glob_path(self, path):
        self.__glob_path = path

    def spaces_to_underscores(self, string):
        return string.replace(" ", "_")

    """ API functions """
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
            lists.append(f.replace(self.__common_path, ""))
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

    def add_to_list(self, list_name, name, email):
        file_path = self.__common_path + list_name
        try:
            f = open(file_path, "r")
        except IOError:
            return False
        contents = f.read()
        f.close()

        if email in contents:
            return False

        users = contents.split("\n")
        new_entry = name + " - " + email
        users.append(new_entry)
        if '' in users:
            users.remove('')
        users = "\n".join(users)

        f = open(file_path, "w")
        f.seek(0)
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

    def update_subscriber(self, list_name, old_name, old_email, new_name, new_email):
        list_data = self.get_list_data(list_name)
        old_entry = old_name + " - " + old_email
        index = False
        for i, entry in enumerate(list_data):
            if entry == old_entry:
                index = i
                break
        if not index:
            return False
        list_data[index] = new_name + " - " + new_email

        file_path = self.__common_path + list_name
        try:
            f = open(file_path, "w")
        except IOError:
            return False
        f.write("\n".join(list_data))
        f.close()
        return True

    def update_list(self, list_name, new_list_name):
        old_name = self.__common_path + list_name
        new_name = self.__common_path + new_list_name
        if os.path.isfile(new_name):
            return False
        try:
            os.rename(old_name, new_name)
        except OSError:
            return False
        return True

    def remove_subscriber(self, list_name, name, email):
        users = self.get_list_data(list_name)
        if not users:
            return False
        to_remove = "{} - {}".format(name, email)
        if to_remove not in users:
            return False
        users.remove(to_remove)
        try:
            f = open(self.__common_path + list_name, "w")
        except IOError:
            return False
        users = "\n".join(users)
        f.write(users)
        f.close()
        return True

    # def merge_lists(self, list_name_1, list_name_2, new_list_name):
    #     users1 = self.get_list_data(list_name_1)
    #     users2 = self.get_list_data(list_name_2)
    #     new_list_users = list(set(users1) | set(users2))
    #     new_list_users.sort()
    #     try:
    #         f = open(self.__common_path + new_list_name, "w")
    #     except IOError:
    #         return False
    #     print(new_list_users)
    #     new_list_users = "\n".join(new_list_users)
    #     f.write(new_list_users)
    #     f.close()
    #     return True
