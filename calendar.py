import upi


def handle_day_schedule(appointments):
    """
    Display a day schedule, depend if we have already some appointments.
    :param appointments: list with (start time, end time, title) of meeting
    """
    if appointments == []:
        upi.display_empty_schedule()
    else:
        upi.display_schedule_with_data(appointments)


def main():
    appointments_data = []
    while True:
        print(appointments_data)
        print(upi.read_from_file())
        appointments_data = upi.read_from_file()
        handle_day_schedule(appointments_data)
        upi.display_menu()
        choice = upi.user_choice()
        if choice == "s":
            appointments_data.append(upi.schedule_meeting(appointments_data))
        elif choice == "c":
            upi.cancel_meeting(appointments_data)
        elif choice == "f":
            upi.save_to_file(appointments_data)
        else:
            break


if __name__ == '__main__':
    main()
