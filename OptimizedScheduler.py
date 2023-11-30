import queue

class OptimizedScheduler:
    """Manages and prioritizes tasks in a queue."""
    def __init__(self, plants):
        """Initializes the scheduler with an empty task queue."""
        self.plants = plants
        self.task_queue = queue.PriorityQueue()

    def generate_schedule(self):
        """generates schedule with queue"""
        for plant in self.plants:
            for task in plant.tasks:
                self.task_queue.put(task)

        schedule = []
        while not self.task_queue.empty():
            task = self.task_queue.get()
            schedule.append(task)
        return schedule
