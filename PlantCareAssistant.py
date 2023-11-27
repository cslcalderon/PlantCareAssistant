from OptimizedScheduler import OptimizedScheduler

class PlantCareAssistant:
    """Assists in managing plant care tasks."""
    def __init__(self, plants_dict):
        """Initializes with an empty list of plants."""
        self.plants = []
        self.plants_dict = plants_dict
    
    def return_all_tasks(self):
        """returns all tasks of all plants"""
        all_tasks = []
        for plant in self.plants:
            for task in plant.tasks:
                all_tasks.append(task)
        # print("returned")
        # print(all_tasks)
        return all_tasks

    def add_plant(self, plant):
        """Adds a plant to the assistant's list."""
        self.plants.append(plant)

    def remove_plant(self, plant):
        """Removes a plant from the plant care assistnat plant list"""
        self.plants.remove(plant)

    def find_plant(self, plant_name):
        """Finds a plant from the plant list"""
        for plant in self.plants:
            if plant.name == plant_name:
                return plant
        
    def create_optimized_schedule(self):
        """Creates an optimized schedule for all plants. """
        scheduler = OptimizedScheduler(self.plants)
        return scheduler.generate_schedule()

    # def sort_tasks(self, sort_by):
    #     tasks = self.return_all_tasks()
    #     if sort_by == "Day of the Week":
    #         return merge_sort(tasks, lambda x: x.scheduled_date)
    #     elif sort_by == "Day of Month":
    #         return merge_sort(tasks, lambda x: int(x.scheduled_date.split()[0]))
    #     else:
    #         return tasks
    