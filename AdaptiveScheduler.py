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
                scheduled_tasks.append(self.schedule_known_plant_tasks(plant, watering_freq, interval, scheduled_tasks, task_dates))
            else:
                self.schedule_unknown_plant_tasks(plant, scheduled_tasks, task_dates)
        print(scheduled_tasks)
        return scheduled_tasks

    def schedule_known_plant_tasks(self, plant, watering_freq, interval, scheduled_tasks, task_dates):
        plant.clear_recommended_tasks()
        new_tasks = []
        rec_date = 'Monday'
        rec_frequency = 'frequent'
        rec_day_of_time = 'Morning'

        changedTask = False

        print(plant.sim_database_plant)
        print(self.plants_dict.get(plant.sim_database_plant, {}).get('watering'))
        print(interval)
        
        if plant.tasks:
            for task in plant.tasks:
                if task.frequency != watering_freq:
                    rec_frequency = watering_freq
                    changedTask = True 
                rec_task = Task(task.task_name, rec_date, rec_frequency, rec_day_of_time)
                plant.add_recommended_task(rec_task)
                new_tasks.append(rec_task)
        print(new_tasks)

        return new_tasks      

    def schedule_unknown_plant_tasks(self, plant, scheduled_tasks, task_dates):
        pass

    def adjust_date_if_crowded(self, date, task_dates):
        while task_dates.get(date, 0) > MAX_TASKS_PER_DAY:
            date += datetime.timedelta(days=1)
        return date

    def determine_interval(self, watering_freq):
        # Logic for determining the interval
        if watering_freq == "frequent":
            return 2
        elif watering_freq == "average":
            return 7
        elif watering_freq == "minimum":
            return 30 
        else:
            return -1
