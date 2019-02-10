import handlers


def display_menu():
    """
    Display options for a meeting.
    """
    print("\nMenu:")
    print("(s) schedule a new meeting"
          "\n(c) cancel an existing meeting"
          "\n(d) show total meeting duration"
          "\n(e) edit an existing meeting"
          "\n(m) compact meetings"
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
    max_meet_duration = 3
    while True:
        duration = input("Enter duration in hours (1 or 2): ")
        if handlers.check_is_number(duration) and int(duration) < max_meet_duration:
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
        if handlers.handle_border_conditions_for_time(appointments_data, start_time, duration):
            break

    return start_time


def display_total_meeting_duration(appointments_data):
    """
    Display total meeting duration.
    :param appointments_data: list of list(with data: start meeting, end meeting, title)
    """
    print("Display the total meeting duration:")
    hours = sum([abs(start_end[1] - start_end[0]) for start_end in appointments_data])
    print("Appointments time: {} hours\n" .format(hours))
