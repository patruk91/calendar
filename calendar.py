import upi


def main():
    meetings = []
    while True:
        if meetings == []:
            upi.display_empty_schedule()
        else:
            upi.display_schedule(meetings)
        upi.display_menu()
        choice = upi.user_choice()
        if choice == "s":
            meetings.append(upi.schedule_meeting())
        elif choice == "c":
            upi.cancel_meeting(meetings)


if __name__ == '__main__':
    main()
