#Imports
from listparser import ListParser
from mail import CommandList

#Globals


#Function


# Main
def main():
    list_parser = ListParser()
    command_list = CommandList(list_parser)

    print(command_list.create_menu())

    while True:
        # unparsed_command =
        # print(unparsed_command)
        command = command_list.parse_command(input("Enter command>"))

        if command_list.is_command(command, "help"):
            print(command_list.create_help())

        elif command_list.is_command(command, "show_lists"):
            print(command_list.show_lists())

        elif command_list.is_command(command, "show_list"):
            print(command_list.show_list(command[1]))

        elif command_list.is_command(command, "add"):
            command_list.add(command[1])

        elif command_list.is_command(command, "create"):
            command_list.create(command[1])

        elif command_list.is_command(command, "search_email"):
            print(command_list.search_email(command[1]))

# elif command_list.is_command(command,  merge_lists, list_identifier_1, list_identifier_2):
# command_lis.merge_lists(list_identifier_1, list_identifier_2)

# elif command_list.is_command(command, "export" , unique_list_identifier):
# command_lis.export(unique_list_identifier)

        elif command_list.is_command(command, "exit"):
            break

        else:
            print(command_list.trigger_unknown_command())


# Program run
if __name__ == "__main__":
    main()
