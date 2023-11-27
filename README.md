# My Plant Care Assistant

## Introduction
------------
My Plant Care Assistant is an application that can help manage a person's plant care tasks in a visual, fun, and creative manner. It utilizes an API with common plant names and their care requirements to make suggestions as well as facilitates an interactive and responsive UI for managing your daily, weekly, and monthly tasks!

## How It Works
------------

The application runs as follows: 

1. Adding a plant: The user can create a plant by going to the Add Plant section of the application where they will input the common name or something similar to their desired plant, then they can input a custom name, and let the application know when this plant was last watered. 

2. Schedule Task: User can schedule tasks for their plants after a plant is created. They con choose from Watering, Fertilizing, or Picking and set the task's frequency and time of day. 

3. My Garden: This is a visual representation of all the user's plants. It has a table with what a plant's watering suggestions (if they are in the databse) mean and when a plant's button is clicked, their information will show up in terms of name, plant in databse, last watered, watering suggestion, and all associated tasks as they were inputed. If the button is pressed again, properties will disappear. 

4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. View Task Schedule: Shows Task Schedule in a table and divides task by daily, weekly, and monthly tasks which are all given in chronological order.
   
6. View All Tasks: Shows all tasks ever created with the ability to delete the tasks. Also allows user to sort and filter tasks. 

## Dependencies and Installation
----------------------------
To install the My Plant Care Assistant App, these steps musy be followed:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following commands:
   ```
   pip install streamlit
   ```

3. Optional to obtain your personal API key from the website see, but for purposes of project, one has been provided with minimum tokens, so please be wary of clearing cache and restarting app multiple times since could result in error. 
```

## Usage
-----
To run the app, open your terminal, navigate to the folder in which you have placed this project and type in 'streamlit run app.py'


PlantCareAssistant.py
#### `PlantCareAssistant` Class
- **Purpose**: Manages plant care tasks and plants.
- **Methods**:
  - `__init__(self, plants_dict)`: Initializes the assistant with an empty list of plants and a dictionary containing plant data.
  - `return_all_tasks(self)`: Returns all tasks of all plants.
  - `add_plant(self, plant)`: Adds a plant to the assistant's list.
  - `find_plant(self, plant_name)`: Finds a plant by name.
  - `create_optimized_schedule(self)`: Creates an optimized schedule for all plants using the `OptimizedScheduler`.
  - `sort_tasks(self, sort_by)`: Sorts tasks based on the given criterion (e.g., day of the week, day of the month).

### `Task.py`
#### `Task` Class
- **Purpose**: Represents a task associated with plant care.
- **Attributes**:
  - `task_name`: Name of the task.
  - `scheduled_date`: Scheduled date for the task.
  - `frequency`: Frequency of the task.
  - `time_of_day`: Time of the day for the task.
- **Methods**:
  - `__init__(self, task_name, scheduled_date, frequency, time_of_day)`: Initializes a task.
  - `get_priority(self)`: Determines the priority of a task based on its attributes.
  - `__lt__(self, other)`: Comparison method for sorting tasks based on priority.

### `Plant.py`
#### `Plant` Class
- **Purpose**: Represents a plant, including its tasks and information.
- **Methods**:
  - `__init__(self, name, image_url, date_last_watered, sim_database_plant)`: Initializes a plant with its details.
  - `schedule_task(self, task_name, scheduled_date, task_frequency, task_time_of_day)`: Schedules a new task for the plant.
  - `add_recommended_task(self, rec_task)`: Adds a recommended task to the plant.
  - `clear_recommended_tasks(self)`: Clears the list of recommended tasks.

### `utils.py`
- **`fetch_plant_data(base_url, max_pages)`**: Fetches plant data from a specified URL and pages.
- **`merge_sort(arr, key_func)`**: A merge sort implementation that sorts an array based on a key function.
- **`filter_out_list(lst, condition)`**: Filters a list of items based on a given condition.

### `Trie.py`
#### `Trie` and `TrieNode` Classes
- **Purpose**: Implements a Trie data structure for efficient word search and retrieval.
- **Methods**:
  - `insert(self, word)`: Inserts a word into the Trie.
  - `insert_with_reversed_words(self, name)`: Inserts words in reverse order. (this is used because most of the times plants are structured with an adjective and trie are lookign for prefixes,
  - so it makes it possible to find something like "evergreen oak" because what gets inserted is "oak evergreen" this will get turned back into original
  - later on in program where it is implemented, but also since its own method doesnt disrupt normal trie function if later on it needs ot be used normally
  - `search(self, prefix)`: Searches for words with a given prefix.
  - `_get_words_from_node(self, node, prefix)`: Helper method to retrieve words from a node.
  - `build_plant_trie(plant_names)`: Builds a Trie from plant names.

### `app.py`
- **Purpose**: Main Streamlit application file.
- **Functionality**:
  - Initializes and configures the Streamlit UI.
  - Implements the UI logic for various options like "Add Plant", "Schedule Task", "My Garden", "View Task Schedule", and "View All Tasks".
  - Add Plant tab
  - adds a plant and required a name, a plant that's similar to it, an image url and the date it was last watered
  - Schedule Task
  - requires the user to choose a task out fo the three that are given, choose the frequency of it, and time of day
  - My Garden
  - shows all plants in a "garden" with a column set up, each plant has a button that can be clicked to show info on plant
  - also shows what different watering suggestions mean that user can use to change their tasks (right now can only delete and create new ones)
  - View Task Schedule
  - this shows tasks divided into a schedule by daily, weekly, and monthly tasks which are shown in order through the optimized scehduler object that
  - sorts them in order through using a queue, this queue format can be used later on for implementing some type of "complete"
  - View All Tasks
  - shows all tasks and allows user to filter and sort what they want to see
  - can also delete tasks

### `optimizedScheduler.py`
#### `OptimizedScheduler` Class
- **Purpose**: Manages and prioritizes tasks using a queue.
- **Methods**:
  - `__init__(self, plants)`: Initializes the scheduler with a list of plants.
  - `generate_schedule(self)`: Generates a schedule by prioritizing tasks.

Each file and class is focused on a specific aspect of the plant care assistant application, working together to manage plants, tasks, and scheduling within the Streamlit UI.
