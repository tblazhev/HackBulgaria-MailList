# Imports
from listparser import ListParser

# Globals




# Function


class CommandList():

    """docstring for CommandList"""

    def __init__(self, list_parser):
        self.list_parser = list_parser

    def parse_command(self, command):
        return tuple(command.split(" "))

    def is_command(self, command_tuple, command_string):
        return command_tuple[0] == command_string

    def format_lists(self):
        self.formated_lists = self.list_parser.get_lists()
        self.ready_for_print = []

        for i in range(len(self.formated_lists)):
            self.ready_for_print.append("{0} {1}".format(i, self.formated_lists[i]))
        return self.ready_for_print

    def show_lists(self):
        print("\n".join(self.ready_for_print))



    def show_list(self, list_name):
        return self.list_parser.get_list_data(list_name)

    # def add(self, list_name, entry):
    #     return self.list_parser.add_to_list(list_name, entry):

    # def search(self, email):
    #     return self.list_parser.search_email(email):


    # def trigger_unknown_command():
    #     unknown_command = ["Error: Unknown command!",
    #     "Try one of the following:",
    #     " show_lists",
    #     " show_list [list name]",
    #     " add",
    #     " create",
    #     " search email",
    #     " export",
    #     " exit"]
    #     print("\n".join(unknown_command))

    def create_menu(self):
        self.menu = ["Hello Stranger!", "This is a cutting-edge, console-based mail-list!", "Type help, to see a list of commands."]

    def create_help(self):
        self.help = [
        "Here is a full list of commands: ",
        "",
        "* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
        "* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
        "* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
        "* create <list_name> - Creates a new empty list, with the given name."
        "* search_email <email> - Performs a search into all lists to see if the given email is present . Shows all lists, where the email was found.",
        "* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
        "* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
        "* exit - this will quit the program"]


# Main
def main():
    list_parser = ListParser()
    command_list = CommandList(list_parser)

    print(command_list.create_menu())
    while True:
        command = command_list.parse_command(input("Enter command>"))

        if is_command(command, "help"):
            print(create_help())

        elif is_command(command, "show_lists"):
            CommandList.show_lists()

        elif is_command(command, "show_list", list_name):
            CommandList.show_list(list_name)

        elif is_command(command, "add"):
            CommandList.show_list(list_name)

# elif is_command(command, "create_new_list", list_name):
# CommandList.xxxxxxxxxxx(list_name)

# elif is_command(command, "search_email", search_email_name):
# CommandList.search(search_email)

# elif is_command(command,  merge_lists, list_identifier_1, list_identifier_2):
# CommandList.merge_lists(list_identifier_1, list_identifier_2)

# elif is_command(command, "export" , unique_list_identifier):
# CommandList.export(unique_list_identifier)


        elif is_command(command, "exit"):
            break

        else:
            print(trigger_unknown_command())




# Program run
if __name__ == "__main__":
    main()
