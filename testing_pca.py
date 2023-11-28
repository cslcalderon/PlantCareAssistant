""""Unit test for PlantCareAssistant
Project By: Sofia Calderon and Melanie Velazquez"""

import unittest
from Task import Task
from Plant import Plant
from OptimizedScheduler import OptimizedScheduler
from Trie import Trie

class TestTask(unittest.TestCase):

    def test_task_initialization(self):
        task = Task("🚰 Water", "Tuesday", "Once a week", "Morning")
        self.assertEqual(task.task_name, "🚰 Water")
        self.assertEqual(task.scheduled_date, "Tuesday")
        self.assertEqual(task.frequency, "average")
        self.assertEqual(task.time_of_day, "Morning")

    def test_get_priority_weekly(self):
        task = Task("🧃 Fertilize", "Friday", "Once a week", "Afternoon")
        self.assertEqual(task.get_priority(), (5, 1))

    def test_get_priority_monthly(self):
        task = Task("🤲 Pick", "15 of each month", "Once a month", "Evening")
        self.assertEqual(task.get_priority(), (15, 2))


class TestPlant(unittest.TestCase):
    def test_plant_initialization(self):
        plant = Plant("Rose", "http://example.com/rose.jpg", "2023-01-01", "RoseDB")
        self.assertEqual(plant.name, "Rose")
        self.assertEqual(plant.image_url, "http://example.com/rose.jpg")
        self.assertEqual(plant.date_last_watered, "2023-01-01")
        self.assertEqual(plant.sim_database_plant, "RoseDB")
        self.assertEqual(plant.tasks, [])
        self.assertEqual(plant.recommended_tasks, [])

    def test_schedule_task(self):
        plant = Plant("Cactus", "http://example.com/cactus.jpg", "2023-02-01", "CactusDB")
        plant.schedule_task("Watering", "Tuesday", "Once a week", "Morning")
        self.assertEqual(len(plant.tasks), 1)
        self.assertEqual(plant.tasks[0].task_name, "Watering")
        self.assertEqual(plant.tasks[0].scheduled_date, "Tuesday")

    def test_change_watering_date(self):
        plant = Plant("Orchid", "http://example.com/orchid.jpg", "2023-03-01", "OrchidDB")
        plant.change_watering_date("2023-03-15")
        self.assertEqual(plant.date_last_watered, "2023-03-15")

class TestOptimizedScheduler(unittest.TestCase):
    def test_scheduler_initialization(self):
        plants = [Plant("Aloe", "url1", "2023-04-01", "AloeDB"), Plant("Basil", "url2", "2023-04-02", "BasilDB")]
        scheduler = OptimizedScheduler(plants)
        self.assertEqual(scheduler.plants, plants)
        self.assertTrue(scheduler.task_queue.empty())

    def test_generate_schedule_no_tasks(self):
        plants = [Plant("Cactus", "url3", "2023-04-03", "CactusDB")]
        scheduler = OptimizedScheduler(plants)
        schedule = scheduler.generate_schedule()
        self.assertEqual(schedule, [])

    def test_generate_schedule_with_tasks(self):
        plant1 = Plant("Daisy", "url4", "2023-04-04", "DaisyDB")
        plant1.schedule_task("Watering", "Monday", "Once a week", "Morning")
        plant2 = Plant("Eucalyptus", "url5", "2023-04-05", "EucalyptusDB")
        plant2.schedule_task("Fertilizing", "Tuesday", "Once a week", "Afternoon")
        plants = [plant1, plant2]
        scheduler = OptimizedScheduler(plants)
        schedule = scheduler.generate_schedule()
        self.assertEqual(len(schedule), 2)
        self.assertIsInstance(schedule[0], Task)
        self.assertIsInstance(schedule[1], Task)

class TestTrie(unittest.TestCase):
    def test_insert(self):
        trie = Trie()
        trie.insert("plant")
        node = trie.root
        for char in "plant":
            self.assertIn(char, node.children)
            node = node.children[char]
        self.assertTrue(node.is_end_of_word)

    def test_search(self):
        trie = Trie()
        trie.insert("tree")
        trie.insert("trie")
        result = trie.search("tr")
        self.assertIn("tree", result)
        self.assertIn("trie", result)






    

if __name__ == '__main__':
    unittest.main()

