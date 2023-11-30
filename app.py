# Import Streamlit and other necessary standard libraries
import streamlit as st
# Import custom modules
from PlantCareAssistant import PlantCareAssistant
from utils import fetch_plant_data
from Trie import build_plant_trie
from drop_down_options import deal_with_option


BASE_URL = 'https://perenual.com/api/species-list?key=sk-7nhl6560db5f5bed93100&edible=1'
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
options = ["🪴 Add Plant", "📝 Schedule Task", "👩‍🌾 My Garden", "🗓️ View Task Schedule", "📒 View All Tasks"]
option = st.sidebar.selectbox("Choose an Option:", options)


deal_with_option(option, plant_trie, plants_dict)