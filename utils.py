import requests
import random

def fetch_plant_data(base_url, max_pages):
    water_rates = ['frequent', 'average', 'minimum', 'none']
    """fetches plant data given a base url and the number of pages to request"""
    plants_dict_from_database = {}
    for page in range(1, max_pages + 1):
        paginated_url = f"{base_url}&page={page}"
        response = requests.get(paginated_url)
        data = response.json()

        for plant in data['data']:
            plant_name = plant.get('common_name')
            if plant_name:  # Check if plant_name is not None
                plants_dict_from_database[plant_name.lower()] = {
                        'genus': plant.get('genus', 'Unknown genus'),
                        'species': plant.get('scientific_name', 'Unknown species'),
                        'watering': random.choice(water_rates),
                        'sunlight': plant.get('sunlight', 'full_sun')
                    }
                
    return plants_dict_from_database

def merge_sort(arr, key_func):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]        # Dividing the array elements into 2 halves
        R = arr[mid:]

        merge_sort(L, key_func)  # Sorting the first half
        merge_sort(R, key_func)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if key_func(L[i]) < key_func(R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

def filter_out_list(lst, condition):
    filtered_tasks = []
    for item in lst:
        date = item.scheduled_date
        # Check if the condition is 'month' for monthly tasks
        if condition == 'month' and ' of each month' in date:
            filtered_tasks.append(item)
        # If conditions is a list of strings, it's assumed to be for weekly tasks
        elif date == condition:
            filtered_tasks.append(item)

    return filtered_tasks
