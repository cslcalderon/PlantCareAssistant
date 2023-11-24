from OptimizedScheduler import OptimizedScheduler
from AdaptiveScheduler import AdaptiveScheduler

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
            all_tasks.append(plant.tasks)

    def add_plant(self, plant):
        """Adds a plant to the assistant's list."""
        self.plants.append(plant)

    def find_plant(self, plant_name):
        """Finds a plant by name. """
        for plant in self.plants:
            if plant.name == plant_name:
                return plant
            
    def create_optimized_schedule(self):
        """Creates an optimized schedule for all plants. """
        scheduler = OptimizedScheduler(self.plants)
        return scheduler.generate_schedule()
    
    def create_adaptive_schedule(self):
        """Creates an optimized schedule for all plants."""
        scheduler = AdaptiveScheduler(self.plants, self.plants_dict)
        return scheduler.schedule_tasks()