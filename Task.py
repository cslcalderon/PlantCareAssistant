
FREQUENCIES = {"Once a week": "average", "Multiple times a week": "frequent", "Once a month": "minimum"}
class Task:
    """
    Represents a task associated with plant care, such as watering or fertilizing.
    Attributes:
        task_name (str): Name of the task.
        date (str): Date for the task.
        frequency (str): Frequency of the task.
        time_of_day (str): Time of the day for the task.
    """
    def __init__(self, task_name, scheduled_date, frequency, time_of_day):
        """initializes task"""
        self.task_name = task_name
        self.scheduled_date = scheduled_date
        self.frequency = FREQUENCIES.get(frequency)
        self.time_of_day = time_of_day

    def get_priority(self):
        """Determines the priority of a task based on its frequency, scheduled_date, and time of day."""
        # Assign numerical values for priority calculation
        day_priority = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 0}
        time_of_day_priority = {"Morning": 0, "Afternoon": 1, "Evening": 2}
        month_day_priority = 31  # Default for monthly tasks

        # Check if the task is scheduled by day of the week or date of the month
        if self.frequency in ["average", "frequent"]:
            day = day_priority.get(self.scheduled_date, 8)  # Handle special cases or errors
        else:  # "Once a month"
            # Extract the day of the month from the scheduled_date (e.g., "9 of each month")
            try:
                day = int(self.scheduled_date.split(' ')[0])
            except ValueError:
                day = month_day_priority  # Default if parsing fails

        time = time_of_day_priority[self.time_of_day]

        return day, time

    def __lt__(self, other):
        """comparison method"""
        return self.get_priority() < other.get_priority()
    