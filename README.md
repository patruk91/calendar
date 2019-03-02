# calendar

In this exercise, you will be writing a console program that manages a meeting schedule. 
The exercise is divided into milestones. You should complete a milestone (and make sure your program works!) 
before moving to the next milestone.

### Structure
Your program should use multiple modules:

- calendar.py: main program
- ui.py: printing data, asking user for input
- storage.py: saving and loading files (after you implement it)
You should not use any global variables. If you need to store state (for example, a list of meetings), you will
need to pass it to the functions that need it.

## Program features

### Milestone 1: Schedule and cancel
- The program should allow you to schedule 1-hour or 2-hour meetings. The meeting times should be at full hour
(like 9:00). The meetings have a title.
- It should be possible to cancel a meeting.
- Make sure user input is validated! The program should keep asking until the user enters the right data.

### Milestone 2: Validate meeting time
- The meetings should be between 8 and 18. It should not be possible to schedule a meeting outside these hours.
- It should not be possible to schedule a meeting that overlaps with existing meeting

### Milestone 3: Save and load
- Now, make the program store the schedule in a file (meetings.txt). The program should load the data on start,
and store it when the schedule is updated.

Milestone 4: More features
- It should be possible to edit a meeting (change title, duration, or time). Make sure to check if the new meeting
time is validated.
- The program should display the total meeting duration (how many hours of meetings).
- There should be a "compact meetings" feature that moves meetings to earliest possible time (starting from 8).
For instance, if we have a schedule like this:
