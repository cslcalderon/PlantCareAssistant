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