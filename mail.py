#Imports
from listparser import ListParser

#Globals


#Function

class CommandList():
    """docstring for CommandList"""

    def __init__(self, arg):
        self.arg = arg


    def parse_command(self, command):
        return tuple(self, command.split(" "))

    def is_command(self, command_tuple, command_string):
        return self.command_tuple[0] == self.command_string

    def show_list(self):
        return ListParser.show_list()




    def trigger_unknown_command():
        unknown_command = ["Error: Unknown command!",
        "Try one of the following:",
        " show_lists",
        " show_list [list name]",
        " add",
        " create",
        " search email",
        " export",
        " exit"]

        print("\n".join(unknown_command))



#Main
# def main():
#
#     print(create_menu())

#     while True:
#         command = parse_command(input("Enter command>"))

#         if is_command(command, "help"):
#             print(create_help())


#         elif is_command(command, "show_list"):
#             print(create_language_list(conn))

#         elif is_command(command, "start"):
#             trigger_start(conn, command)
#         elif is_command(command, "answer"):
#             trigger_answer(conn, command)
#         elif is_command(command, "finish"):
#             break
#         else:
#             print(trigger_unknown_command())

    conn.close()


#Program run
if __name__ == "__main__":
    main()
