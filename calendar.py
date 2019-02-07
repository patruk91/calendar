import upi


def main():
    while True:
        upi.display_schedule()
        upi.display_menu()
        upi.schedule_new_meeting()


if __name__ == '__main__':
    main()
