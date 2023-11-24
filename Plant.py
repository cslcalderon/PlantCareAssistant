from Task import Task

class Plant:
    """Represents a plant, including its tasks and information."""
    def __init__(self, name, image_url, date_last_watered, sim_database_plant):
        """Initializes a Plant with its details."""
        self.name = name
        self.image_url = image_url
        self.date_last_watered = date_last_watered
        self.sim_database_plant = sim_database_plant
        self.tasks = []
        self.recommended_tasks = []

    def schedule_task(self, task_name, scheduled_date, task_frequency, task_time_of_day):
        """Schedules a new task for the plant."""
        new_task = Task(task_name, scheduled_date, task_frequency, task_time_of_day)
        self.tasks.append(new_task)

    def modify_task(self, task_name, new_date, new_frequency, new_time_of_day):
        """Modifies an existing task based on the given parameters."""
        for task in self.tasks:
            if task.task_name == task_name:
                task.scheduled_date = new_date
                task.frequency = new_frequency
                task.time_of_day = new_time_of_day
                return True  # Task found and modified
        return False  # Task not found
