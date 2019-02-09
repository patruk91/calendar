filename = "meetings.txt"


def save_to_file(appointments_data):
    """
    Save information about meetings to the external file.
    :param appointments_data: list of tuples with information about meetings
    (start time, end time, title)
    """
    change_to_str = [[str(element) for element in data] for data in appointments_data]
    with open(filename, "a") as file_object:
        for line in change_to_str:
            file_object.write(",".join(line) + "\n")


def read_from_file():
    """
    Read data about appointments from external file.
    """
    appointments = []
    with open(filename) as file_object:
        for line in file_object:
            appointments.append(tuple(line.rstrip().split(",")))
        appointments = [tuple(int(value) if value.isdigit() else value for value in number) for number in appointments]
        return appointments


def remove_data_from_file(appointments_data):
    """
    Remove desired appointments from external file.
    :param appointments_data: list of tuples with information about meetings
    (start time, end time, title)
    """
    change_to_str = [[str(element) for element in data] for data in appointments_data]
    with open(filename, "w") as file_object:
        for line in change_to_str:
            file_object.write(",".join(line) + "\n")
