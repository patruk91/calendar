data_meetings = []


def display_menu():
    """
    Display options for a meeting.
    """
    print("Menu:")
    print("(s) schedule a new meeting"
          "\n(c) cancel an existing meeting"
          "\n(q) quit")


def display_schedule():
    print("Your schedule for the day:")
    if data_meetings == []:
        print("(empty)\n")
    else:
        print(data_meetings)


def user_choice():
    user_option = input("\nYour choice: ")
    return user_option


def schedule_new_meeting():
    choice = user_choice()
    if choice == "s":
        print("Schedule a new meeting")
        title = get_meet_title()
        duration = get_meet_duration()
        start = get_meet_start_time()
        data_meetings.extend((title, duration, start))
        print("Meeting added.\n")
        return data_meetings


def get_meet_title():
    meet_title = input("Enter meeting title: ")
    return meet_title


def get_meet_duration():
    while True:
        duration = input("Enter duration in hours (1 or 2): ")
        if check_is_number(duration):
            break
        else:
            print("Please provide correct number!")
    return duration


def get_meet_start_time():
    start_time = input("Enter start time: ")
    return start_time


def check_is_number(user_data):
    if user_data.isdigit() and int(user_data) > 0:
        return True
    return False
