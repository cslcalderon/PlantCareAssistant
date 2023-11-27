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

    def change_watering_date(self, new_watering_last_water):
        """Changes watering date with updated date that is given"""
        self.date_last_watered = new_watering_last_water

    # def add_recommended_task(self, rec_task):
    #     """Modifies an existing task based on the given parameters."""
    #     self.recommended_tasks.append(rec_task)
    
    # def clear_recommended_tasks(self):
    #     self.recommended_tasks = []

    

