

def display_menu():
    """
    Display options for a meeting.
    """
    print("Menu:")
    print("(s) schedule a new meeting"
          "\n(c) cancel an existing meeting"
          "\n(q) quit")


def display_empty_schedule():
    """
    Display schedule for the day.
    """
    print("Your schedule for the day:")
    print("(empty)\n")


def display_schedule(data_meetings):
    """
    Display schedule for the day.
    """
    print("Your schedule for the day:")
    print(data_meetings)
    for data in data_meetings:
        # data == (start time, end time, title meeting)
        print("{} - {} {}" .format(data[1], data[2], data[0]))


def user_choice():
    """
    Ask user what he want to do: organise new, cancel meeting or quit.
    :return: user choice: letter (s,c or q)
    """
    user_option = input("\nYour choice: ")
    return user_option


def schedule_new_meeting():
    """
    Save the new meeting.
    :return: list with data: title, duration and start meeting
    """
    choice = user_choice()
    if choice == "s":
        print("Schedule a new meeting")
        title = get_meet_title()
        duration = get_meet_duration()
        start = get_meet_start_time()
        user_data = (title, int(start), int(duration) + int(start))
        print("Meeting added.\n")
        return user_data


def get_meet_title():
    """
    Ask user about title of meeting.
    :return: String with title.
    """
    meet_title = input("Enter meeting title: ")
    return meet_title


def get_meet_duration():
    """
    Ask user about duration of meeting
    :return: String with duration, number
    """
    while True:
        duration = input("Enter duration in hours (1 or 2): ")
        if check_is_number(duration) and int(duration) < 3:
            break
        else:
            print("Please provide correct number!")
    return duration


def get_meet_start_time():
    """
    Ask user about time start of meeting.
    :return: String with start time, number
    """
    while True:
        start_time = input("Enter start time: ")
        if check_is_number(start_time) and int(start_time) < 24:
            break
        else:
            print("Please provide correct number (1 - 24)!")
    return start_time


def check_is_number(user_data):
    """
    Check if user provided a number for duration and start time
    :param user_data: parametr provided by user
    :return: boolean
    """
    if user_data.isdigit() and int(user_data) > 0:
        return True
    return False
