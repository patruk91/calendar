import upi


def schedule_meeting(appointments_data):
    """
    Ask user for new appointment and save it.
    :return: list with data: title, start meeting, end meeting
    """
    print("Schedule a new meeting")
    title = upi.get_meet_title()
    duration = upi.get_meet_duration()
    start_time = int(upi.get_meet_start_time(appointments_data, duration))
    end_time = int(duration) + int(start_time)
    user_data_appointment = (start_time, end_time, title)
    print("Meeting added.\n")
    return user_data_appointment


def cancel_meeting(appointments_data):
    print("Cancel an existing meeting")
    start_meetings = [start_time[0] for start_time in appointments_data]
    duration = 0
    while True:
        cancel_time = int(upi.get_meet_start_time(appointments_data, duration))
        if cancel_time not in start_meetings:
            print("ERROR: There is no meeting starting at that time!")
        else:
            indice_of_cancel_meet = start_meetings.index(cancel_time)
            del appointments_data[indice_of_cancel_meet]
            return appointments_data


def check_is_number(user_data):
    """
    Check if user provided a number for duration and start time
    :param user_data: parametr provided by user
    :return: boolean
    """
    if user_data.isdigit() and int(user_data) > 0:
        return True
    return False


def check_if_overlap(appointments_data, start_time, duration):
    """
    Check if meeting hours are overlapping.
    :param appointments_data: list of tuples with information about meetings
    (start time, end time, title)
    :param start_time: number, hour when meeting starts
    :param duration: number, duration of the meeting
    :return: boolean True if they overlap
    """
    meet_time = [(int(start_end[0]), int(start_end[1])) for start_end in appointments_data]
    busy_hours = []

    for time_ in meet_time:
        if time_[1] - time_[0] == 2:
            busy_hours.append(time_[0])
            busy_hours.append(time_[0] + 1)
        else:
            busy_hours.append(time_[0])
    if int(start_time) in busy_hours or int(start_time) + int(duration) -1 in busy_hours:
        return True
    return False
