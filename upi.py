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


def display_schedule_with_data(data_appointment):
    """
    Display schedule for the day.
    """
    print("Your schedule for the day:")
    for data in data_appointment:
        # data == (start time, end time, title meeting)
        print("{} - {} {}" .format(data[0], data[1], data[2]))


def user_choice():
    """
    Ask user what he want to do: organise new, cancel meeting or quit.
    :return: user choice: letter (s,c or q)
    """
    user_option = input("\nYour choice: ")
    return user_option


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
            print("ERROR: Number is not 1 or 2!")
    return duration


def get_meet_start_time(appointments_data, duration):
    """
    Ask user about time start of meeting.
    :return: String with start time, number
    """
    while True:
        start_time = input("Enter start time: ")
        if check_is_number(start_time) and 8 <= int(start_time) < 18 and int(start_time) + int(duration) <= 18:
            if duration != 0 and check_if_overlap(appointments_data, start_time, duration):
                print("ERROR: Meeting overlaps with existing meeting!")
            else:
                break
        else:
            print("ERROR: Meeting is outside of your working hours (8 to 18)!")
    return start_time



