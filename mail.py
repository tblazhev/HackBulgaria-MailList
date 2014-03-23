# Imports
from listparser import ListParser

# Globals

# Function


class CommandList():

    """docstring for CommandList"""

    def __init__(self, list_parser):
        self.list_parser = list_parser
        self.all_lists = self.list_parser.get_lists()

    def parse_command(self, command):
        return tuple(command.split(" "))

    def is_command(self, command_tuple, command_string):
        return command_tuple[0] == command_string

    def format_lists(self):
        self.all_lists = self.list_parser.get_lists()
        self.return_lists = []

        index = 1
        for i in self.all_lists:
            self.return_lists.append("[{}] {}".format(index, i))
            index += 1
        return self.return_lists

    def show_lists(self):
        return "\n".join(self.format_lists())

    def create(self, list_name):
        self.list_parser.create_list(list_name)

    def add(self, list_id):
        list_name = self.all_lists[int(list_id) - 1]
        name = input("name>")
        email = input("email>")
        print("{} was added to {}".format(name, list_name))
        self.list_parser.add_to_list(list_name, name, email)

    def show_list(self, list_id):
        list_name = self.all_lists[int(list_id) - 1]

        self.format_lst = self.list_parser.get_list_data(list_name)
        self.return_lst = []
        for i in range(len(self.format_lst)):
            self.return_lst.append("[{}] {}".format(i, self.format_lst[i]))

        return "\n".join(self.return_lst)

    def search_email(self, list, email):
        output = []
        index = 1
        for list in self.all_lists:
            if self.list_parser.search_email(list, email) is True:
                output.append("[{}] {}".format(index, list))
                index += 1

        if len(output) == 0:
            output.append(
                "<{}> was not found in the current mailing lists.".format(email))
        return "\n".join(output)

    def update_subscriber(self, list_id, subs_id):

        list_name = self.all_lists[int(list_id) - 1]
        ListNames = self.list_parser.get_list_data(list_name)

        return ListNames

# # can provide *old_entry == NameEmail1

#         SubscriberID = int(subs_id) - 1
#         NameEmail1 = ListNames[SubscriberID]
#         NameEmail2 = NameEmail1.split(" - ")
#         old_name = NameEmail2[0]
#         old_email = NameEmail2[1]

#         print("Updating: {}".format(NameEmail1))
#         print("Pres enter if you want the field to remain the same")

#         new_name = input("enter new name>")
#         new_email = input("enter new email>")

#         if (int(list_id) - 1) > len(self.all_lists):
#             return "List with unique identifier <{}> was not found.".format(list_id)

#         elif (SubscriberID - 1) > len(ListNames):
#             return "Subscriber with identifider <{}> was not found in the list <{}>".format(subs_id, list_name)

#         if len(new_name) == 0:
#             print("Subscriber updated: {} - {}".format(old_name, new_email))

#             return self.list_parser.update_subscriber(list_name, old_name, old_email, old_name, new_email)

#         elif len(new_email) == 0:
#             print("Subscriber updated: {} - {}".format(new_name, old_email))

#             return self.list_parser.update_subscriber(list_name, old_name, old_email, new_name, old_email)

#         else:
#             print("Subscriber updated: {} - {}".format(new_name, new_email))

#             return self.list_parser.update_subscriber(list_name, old_name, old_email, new_name, new_email)

    def update_lists(self, list_id, new_name):

        list_name = self.all_lists[int(list_id) - 1]
        print("Updated <{}> to <{}>.".format(list_name, new_name))
        return self.list_parser.update_list(list_name, new_name)

    def remove_subscriber(self, list_id, subs_id):

        list_name = self.all_lists[int(list_id) - 1]
        ListNames = self.list_parser.get_list_data(list_name)
        SubscriberID = int(subs_id) - 1
        NameEmail1 = ListNames[SubscriberID]
        NameEmail2 = NameEmail1.split(" - ")
        name = NameEmail2[0]
        email = NameEmail2[1]

        if (int(list_id) - 1) > len(self.all_lists):
            return "List with unique identifier <{}> was not found.".format(list_id)

        elif (SubscriberID - 1) > len(ListNames):
            return "Subscriber with identifider <{}> was not found in the list <{}>".format(subs_id, list_name)

        else:
            print("<{}> was removed from the list <{}>".format(name, list_name))
            return self.list_parser.remove_subscriber(list_name, name, email)

    def create_menu(self):

        menu = [
            "Hello Stranger!", "This is a cutting-edge, console-based mail-list!",
            "Type help, to see a list of commands."]
        return "\n".join(menu)

    def create_help(self):

        HelpMenu = [
            "Here is a full list of commands: ",
            "",
            "* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
          "* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
           "* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
           "* update_subs <unique_list_identifier> <unique_name_identifier> - updates the information for the given subscriber in the given list",
           "* remove_subscriber <unique_list_identifier> <unique_name_identifier> - Removes the given subscriber from the given list",
           "* create <list_name> - Creates a new empty list, with the given name.",
           "* update <unique_list_identifier>  <new_list_name> - Updates the given list with a new name.",
           "* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.",
           "* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
           "* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
           "* exit - this will quit the program",
           ""]
        return "\n".join(HelpMenu)
