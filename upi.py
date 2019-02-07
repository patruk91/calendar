def display_menu():
    """
    Display options for an organise meeting.
    :return: user choice: organise new meeting, cancel, or quit from program
    """
    print("Menu:")
    print("\n(s) schedule a new meeting"
          "\n(c) cancel an existing meeting"
          "\n(q) quit")

    user_choice = input("Your choice: ")
    return user_choice
