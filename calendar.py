import upi
import storage
import handlers


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
    while True:
        appointments_data = storage.read_from_file()
        handle_day_schedule(appointments_data)
        upi.display_menu()
        choice = upi.user_choice()
        if choice == "s":
            appointments_data.append(handlers.schedule_meeting(appointments_data))
            storage.save_to_file(appointments_data)
        elif choice == "c":
            if appointments_data == []:
                print("ERROR: No meeting to cancel!\n")
            else:
                updated_appointments = handlers.cancel_meeting(appointments_data)
                storage.remove_data_from_file(updated_appointments)
        elif choice == "e":
            handlers.edit_meeting(appointments_data)
        elif choice == "d":
            upi.display_total_meeting_duration(appointments_data)
        elif choice == "m":
            handlers.compact_meetings(appointments_data)
        else:
            break


if __name__ == '__main__':
    main()
