# Import Streamlit and other necessary standard libraries
from datetime import datetime
import streamlit as st
# Import custom modules
from PlantCareAssistant import PlantCareAssistant
from Plant import Plant
from utils import fetch_plant_data
from Trie import build_plant_trie

# Initial setup
# https://perenual.com/api/species-list?key=sk-7nhl6560db5f5bed93100&edible=1

BASE_URL = 'https://trefle.io/api/v1/plants?token=WoVOkNUumu6SWX9B5B9ZTjn3A_M6Bi8apCyfFSXBKoM'
MAX_PAGES = 1

@st.cache_data
def cached_fetch_plant_data(url, pages):
    return fetch_plant_data(url, pages)

plants_dict = cached_fetch_plant_data(BASE_URL, MAX_PAGES)


all_plant_names = list(plants_dict.keys())
print(all_plant_names)
plant_trie = build_plant_trie(all_plant_names)

# Create app    
if 'pca' not in st.session_state:
    st.session_state.pca = PlantCareAssistant(plants_dict)
    
# Streamlit UI
st.title("🪴 My Plant Care Assistant 📝")

# Sidebar for options
options = ["🪴 Add Plant", "📝 Schedule Task", "👩‍🌾 My Garden", "📑 View All Tasks", "📈 Optimized Schedule"]
option = st.sidebar.selectbox("Choose an Option:", options)

if option == "🪴 Add Plant":
    #using plant database to find plant more similar, so then we can use this to 
    #give suggestions with optimized scheduler

    st.write("If you see a plant that matches your plant or is similar enough to it, please click on the respective button.")
    user_plant_input = st.text_input("Enter the type of plant you are interested in (e.g., 'mint')")
    if user_plant_input:
        # Reverse the order of words in the user's input for searching
        reversed_query_words = user_plant_input.lower().split()[::-1]
        search_query = ' '.join(reversed_query_words)
        print(search_query)

        # Perform the search using the Trie
        similar_plants_keys = plant_trie.search(search_query)
        similar_plants = [' '.join(key.split()[::-1]) for key in similar_plants_keys]


        if similar_plants:
            st.write("Similar plants:")
            for plant_name in similar_plants:
                if st.button(plant_name):
                    st.session_state.plant_in_database = plant_name
                    st.write(f"You selected {plant_name}")
        else:
            st.write("No similar plants found.")
            st.session_state.plant_in_database = None

    plant_name = st.text_input("Enter plant name")
    plant_image_url = st.text_input("Enter plant image URL")
    last_watered = st.date_input("Last watered date")

    # Adding a Plant
    if st.button("Add Plant"):
        if plant_name and plant_image_url:
            database_plant = st.session_state.get('plant_in_database')
            plant = Plant(plant_name, plant_image_url, last_watered, database_plant)
            st.session_state.pca.add_plant(plant)
            st.success("Plant added successfully")
        else:
            st.error("Please enter both plant name and image URL")


if 'selected_task' not in st.session_state:
    st.session_state['selected_task'] = None

if option == "📝 Schedule Task":
    # Extract plant names for the selectbox
    plant_names = [plant.name for plant in st.session_state.pca.plants]
    plant_name = st.selectbox("Select plant", plant_names)


    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🚰 Water"):
            st.session_state['selected_task'] = "🚰 Water"
    with col2:
        if st.button("🧃 Fertilize"):
            st.session_state['selected_task'] = "🧃 Fertilize"
    with col3:
        if st.button("🤲 Pick"):
            st.session_state['selected_task'] = "🤲 Pick"
    # with col4:
    #     if st.button("🔄 Custom"):
    #         st.session_state['selected_task'] = st.text_input("Enter custom task")

    # Display selected task
    if st.session_state['selected_task']:
        st.write("Selected task:", st.session_state['selected_task'])

    # Frequency and Timing Inputs
    # Frequency Input
    frequency = st.selectbox("Select frequency", ["Once a week", "Multiple times a week", "Once a month"])
    day_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    time_of_day = st.radio("Select time of day", ["Morning", "Afternoon", "Evening"])

    multiple_days = False
    # Conditional Input based on Frequency
    if frequency == "Once a week":
        day_of_week = st.selectbox("Select day of the week", day_options)
        date = day_of_week
    elif frequency == "Multiple times a week":
        days_of_week = st.multiselect("Select which days of the week", day_options, default=day_options[:2])
        date = ", ".join(days_of_week)
        multiple_days = True
    else:
        day_of_month = st.selectbox("Select day of the month", list(range(1, 31)))
        date = f"{day_of_month} of each month"

    # Add Task Button
    if st.button("Add Task"):
        if st.session_state['selected_task']:
            plant_to_add_task = st.session_state.pca.find_plant(plant_name)
            if plant_to_add_task:
                if multiple_days:
                    for day in days_of_week:
                        plant_to_add_task.schedule_task(st.session_state['selected_task'], day, frequency, time_of_day)
                else:
                    plant_to_add_task.schedule_task(st.session_state['selected_task'], date, frequency, time_of_day)

                st.success(f"Task '{st.session_state['selected_task']}' scheduled for {plant_name} on {date} at {time_of_day}")
            else:
                st.error("Plant not found.")
        else:
            st.error("Please select a task to add.")

if option == "👩‍🌾 My Garden":
    st.header("👩‍🌾 My Garden")
    COLS_PER_ROW = 4
    
    # Change here: Use list comprehension to get plant names from Plant objects
    plant_names = [plant.name for plant in st.session_state.pca.plants]
    
    # Store the selected plant in the session state
    if 'selected_plant' not in st.session_state:
        st.session_state['selected_plant'] = None

    for i in range(0, len(plant_names), COLS_PER_ROW):
        cols = st.columns(COLS_PER_ROW)
        for j in range(COLS_PER_ROW):
            if i + j < len(plant_names):
                plant_name = plant_names[i + j]
                # Find the Plant object for the given plant_name
                plant = st.session_state.pca.find_plant(plant_name)
                with cols[j]:
                    # Toggle button to make image clickable and toggleable
                    if st.button(plant_name, key=plant_name):
                        # Toggle the selected plant
                        if st.session_state['selected_plant'] == plant_name:
                            # Deselect if the same plant is clicked again
                            st.session_state['selected_plant'] = None
                        else:
                            # Select the new plant
                            st.session_state['selected_plant'] = plant_name
                    st.image(plant.image_url, caption=plant_name, width=150)

    # Display details of selected plant
    if st.session_state['selected_plant']:
        selected_plant = st.session_state.pca.find_plant(st.session_state['selected_plant'])
        if selected_plant:
            st.write(f"Details for {selected_plant.name}:")
            st.write(f"Last Watered: {selected_plant.date_last_watered}")
            st.write(f"Plant in Database: {selected_plant.sim_database_plant}")
      
            for task in selected_plant.tasks:
                st.write(f"Task: {task.task_name} - Date: {task.scheduled_date} - Time of Day: {task.time_of_day}")

        else:
            st.error("Selected plant not found.")

if option == "📑 View All Tasks":
    today = datetime.today()
    day_of_week = today.strftime("%A")  # E.g., "Monday"
    day_of_month = today.day
    print(today.day)

    st.write("Here is your optimized schedule and suggested changes.")

    # Initialize the scheduler and add tasks
    optimized_schedule = st.session_state.pca.create_optimized_schedule()

    # Initialize separate lists for each frequency type
    daily_tasks = []
    weekly_tasks = []
    monthly_tasks = []

    # Filter tasks based on frequency
    for task in optimized_schedule:
        task_data = {
            "Task": task.task_name, 
            "Plant": [p.name for p in st.session_state.pca.plants if task in p.tasks][0], 
            "Date": task.scheduled_date, 
            "Time of Day": task.time_of_day
        }


        if task.scheduled_date == day_of_week or task.scheduled_date.split()[0] == str(day_of_month):
            daily_tasks.append(task_data)
        elif task.frequency == "Once a week":
            weekly_tasks.append(task_data)
        elif task.frequency == "Multiple times a week":
            weekly_tasks.append(task_data)
        elif task.frequency == "Once a month":
            monthly_tasks.append(task_data)

    # Display Daily Tasks in a table
    if daily_tasks:
        st.subheader("Daily Tasks")
        st.table(daily_tasks)
    else:
        st.write("No daily tasks scheduled.")

    # Display Weekly Tasks in a table
    if weekly_tasks:
        st.subheader("Weekly Tasks")
        st.table(weekly_tasks)
    else:
        st.write("No weekly tasks scheduled.")

    # Display Monthly Tasks in a table
    if monthly_tasks:
        st.subheader("Monthly Tasks")
        st.table(monthly_tasks)
    else:
        st.write("No monthly tasks scheduled.")

if option == "📈 Optimized Schedule":
    st.write('working on it')

    today = datetime.today()
    day_of_week = today.strftime("%A")  # E.g., "Monday"
    day_of_month = today.day
    adaptive_schedule  = st. session_state.pca.create_adaptive_schedule()
    print(adaptive_schedule)

    st.write("Here is your optimized schedule and suggested changes.")

    daily_tasks = []
    weekly_tasks = []
    monthly_tasks = []

    # Filter tasks based on frequency
    for task in adaptive_schedule:
        task_data = {
            "Task": task.task_name, 
            "Plant": [p.name for p in st.session_state.pca.plants if task in p.tasks][0], 
            "Date": task.scheduled_date, 
            "Time of Day": task.time_of_day
        }

        if task.scheduled_date == day_of_week or task.scheduled_date == day_of_month:
            daily_tasks.append(task_data)
        elif task.frequency == "Once a week":
            weekly_tasks.append(task_data)
        elif task.frequency == "Multiple times a week":
            weekly_tasks.append(task_data)
        elif task.frequency == "Once a month":
            monthly_tasks.append(task_data)

    # Display Daily Tasks in a table
    if daily_tasks:
        st.subheader("Daily Tasks")
        st.table(daily_tasks)
    else:
        st.write("No daily tasks scheduled.")

    # Display Weekly Tasks in a table
    if weekly_tasks:
        st.subheader("Weekly Tasks")
        st.table(weekly_tasks)
    else:
        st.write("No weekly tasks scheduled.")

    # Display Monthly Tasks in a table
    if monthly_tasks:
        st.subheader("Monthly Tasks")
        st.table(monthly_tasks)
    else:
        st.write("No monthly tasks scheduled.")
    