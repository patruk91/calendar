import upi


def main():
    meetings = []
    while True:
        if meetings == []:
            upi.display_empty_schedule()
        else:
            upi.display_schedule(meetings)
        upi.display_menu()
        meetings.append(upi.schedule_new_meeting())


if __name__ == '__main__':
    main()
