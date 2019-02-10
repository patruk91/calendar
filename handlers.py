import upi
import storage


def schedule_meeting(appointments_data):
    """
    Ask user for new appointment and save it.
    :return: list with data: start meeting, end meeting, title
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
    """
    Cancel an existing meeting.
    :param appointments_data: list of list(with data: start meeting, end meeting, title)
    :return: list of list: updated appointments_data
    """
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


def display_total_meeting_duration(appointments_data):
    print("Display the total meeting duration:")
    hours = sum([abs(start_end[1] - start_end[0]) for start_end in appointments_data])
    print("Appointments time: {} hours\n" .format(hours))


def edit_meeting(appointments_data):
    """
    Edit an existing meeting.
    :param appointments_data: list of list(with data: start meeting, end meeting, title)
    :return:
    """
    print("Edit an existing meeting")
    chosen_meet = get_correct_meet_title(appointments_data)
    appointment_to_edit = get_correct_appointment(appointments_data, chosen_meet)
    indice_of_meet = get_indice_meet_to_edit(appointments_data, chosen_meet)

    print("\nWhat do you want to change?:")
    print("a) time"
          "\nb) duration"
          "\nc) title")
    user_change = input("Your choice: ")

    if user_change == "a":
        update_by_time(appointments_data, appointment_to_edit, indice_of_meet)
    elif user_change == "b":
        update_by_duration(appointments_data, appointment_to_edit)
    elif user_change == "c":
        update_by_title(appointments_data, appointment_to_edit, indice_of_meet)
    else:
        print("ERROR: Not available option!\n")


def update_by_title(appointments_data, appointment_to_edit, indice_of_meet):
    """
    Edit an existing meeting by title and save to file.
    :param appointments_data: list of list(with data: start meeting, end meeting, title)
    :param appointment_to_edit: list: list to edit with data: start meeting, end meeting, title
    :param indice_of_meet:index in appointments_data, to edit this record
    :return: save data to file
    """
    title = upi.get_meet_title()
    appointment_to_edit[2] = title
    appointments_data[indice_of_meet] = appointment_to_edit
    storage.save_to_file(appointments_data)


def update_by_duration(appointments_data, appointment_to_edit):
    """
    Edit an existing meeting by duration and save to file.
    :param appointments_data: list of list(with data: start meeting, end meeting, title)
    :param appointment_to_edit: list: list to edit with data: start meeting, end meeting, title
    :return: save data to file
    """
    appointments_data = [rec for rec in appointments_data if rec != tuple(appointment_to_edit)]
    while True:
        duration = int(upi.get_meet_duration())
        start_time = str(appointment_to_edit[0])
        if upi.handle_border_conditions_for_time(appointments_data, start_time, duration):
            appointment_to_edit[1] = appointment_to_edit[0] + duration
            appointments_data.append(appointment_to_edit)
            storage.save_to_file(appointments_data)
            break


def get_correct_meet_title(appointments_data):
    """
    Ask user until he don't pickup correct appointment title.
    :param appointments_data: list of list(with data: start meeting, end meeting, title)
    :return: string: title of meeting to edit
    """
    while True:
        chosen_meet = input("Enter the title of meeting, which you want to change:")
        meet_titles = [title[2] for title in appointments_data]
        if chosen_meet in meet_titles:
            return chosen_meet
        else:
            print("ERROR: There is no meeting title in appointments!")


def update_by_time(appointments_data, appointment_to_edit, indice_of_meet):
    """
    Edit an existing meeting by time and save to file.
    :param appointments_data: list of list(with data: start meeting, end meeting, title)
    :param appointment_to_edit: list: list to edit with data: start meeting, end meeting, title
    :param indice_of_meet: index in appointments_data, to edit this record
    :return: save data to file
    """
    duration = abs(int(appointment_to_edit[0]) - appointment_to_edit[1])
    new_time = upi.get_meet_start_time(appointments_data, duration)
    if new_time:
        appointment_to_edit[0] = int(new_time)
        appointment_to_edit[1] = appointment_to_edit[0] + duration
        appointments_data[indice_of_meet] = appointment_to_edit
        storage.save_to_file(appointments_data)


def get_correct_appointment(appointments_data, chosen_meet):
    """
    Find correct record (appointment) to edit.
    :param appointments_data: list of list(with data: start meeting, end meeting, title)
    :param chosen_meet: string: title of meeting to edit
    :return: list: list to edit with data: start meeting, end meeting, title
    """
    indice_of_meet = get_indice_meet_to_edit(appointments_data, chosen_meet)
    appointment_to_edit = list(appointments_data[indice_of_meet])
    upi.display_schedule_with_data([appointment_to_edit])
    return appointment_to_edit


def get_indice_meet_to_edit(appointments_data, chosen_meet):
    """
    Find correct index in appointments_data, to edit this record
    :param appointments_data: list of list(with data: start meeting, end meeting, title)
    :param chosen_meet: string: title of meeting to edit
    :return: number: index of meeting to edit
    """
    indice_of_meet = [indice for indice in range(len(appointments_data))
                      if chosen_meet == appointments_data[indice][2]]
    return indice_of_meet[0]


def check_is_number(user_data):
    """
    Check if user provided a number for duration and start time
    :param user_data: parameter provided by user
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

    if int(start_time) in busy_hours or int(start_time) + int(duration) - 1 in busy_hours:
        return True
    return False
