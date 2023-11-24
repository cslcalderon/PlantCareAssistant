import datetime
from Task import Task
MAX_TASKS_PER_DAY = 7

class AdaptiveScheduler:
    def __init__(self, plants, plants_dict):
        self.plants = plants
        self.plants_dict = plants_dict

    def get_watering_frequency(self, plant):
        print(plant.name, "-", plant.sim_database_plant)
        return self.plants_dict.get(plant.sim_database_plant, {}).get('watering', 'unknown')

    def schedule_tasks(self):
        scheduled_tasks = []
        task_dates = {}

        for plant in self.plants:
            watering_freq = self.get_watering_frequency(plant)
            print()
            print("this is watering freq")
            print(watering_freq)
            
            interval = self.determine_interval(watering_freq)
            print(interval)
            
            if interval > 0:
                self.schedule_known_plant_tasks(plant, interval, scheduled_tasks, task_dates)
            else:
                self.schedule_unknown_plant_tasks(plant, scheduled_tasks, task_dates)
        print(scheduled_tasks)
        return scheduled_tasks

    def schedule_known_plant_tasks(self, plant, interval, scheduled_tasks, task_dates):
        next_watering_date = datetime.date.today()
        while next_watering_date < datetime.date.today() + datetime.timedelta(days=30):
            next_watering_date = self.adjust_date_if_crowded(next_watering_date, task_dates)
            task_description = f"Watering {plant.name}"
            task = Task(task_description, next_watering_date, "Once", "Morning")
            scheduled_tasks.append(task)
            task_dates[next_watering_date] = task_dates.get(next_watering_date, 0) + 1
            next_watering_date += datetime.timedelta(days=interval)

    def schedule_unknown_plant_tasks(self, plant, scheduled_tasks, task_dates):
        for task in plant.tasks:
            scheduled_date = self.adjust_date_if_crowded(task.scheduled_date, task_dates)
            if scheduled_date != task.scheduled_date:
                plant.modify_task(task.task_name, scheduled_date, task.frequency, task.time_of_day)
            scheduled_tasks.append(task)
            task_dates[scheduled_date] = task_dates.get(scheduled_date, 0) + 1

    def adjust_date_if_crowded(self, date, task_dates):
        while task_dates.get(date, 0) > MAX_TASKS_PER_DAY:
            date += datetime.timedelta(days=1)
        return date

    def determine_interval(self, watering_freq):
        # Logic for determining the interval
        if watering_freq == "frequent":
            return 1
        elif watering_freq == "average":
            return 3
        elif watering_freq == "minimum":
            return 30 
        else:
            return -1
