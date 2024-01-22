import streamlit as st
import pickle

# Adding a red-colored title
title_html = """
<h1 style="color: red;">Smart Predictive Modeling for Rental Property Prices</h1>
"""
st.markdown(title_html, unsafe_allow_html=True)

# Sidebar with input fields
type = st.sidebar.selectbox('type', [None, 'BHK1', 'BHK2', 'BHK3', 'BHK4', 'BHK4PLUS'])
type_dict = {'RK1': 0, "BHK1": 1, "BHK2": 2, "BHK3": 3, "BHK4": 4, "BHK4PLUS": 5}

facing = st.sidebar.selectbox('facing', [None, 'N', 'E', 'W', 'S', 'NE', 'NW', 'SE', 'SW'])
facing_dict = {'N': 1, "E": 2, "W": 3, "S": 4, "NE": 5, "NW": 6, "SE": 7, "SW": 8}

lease_type = st.sidebar.selectbox('lease_type', [None, 'ANYONE', 'FAMILY', 'BACHELOR', 'COMPANY'])
lease_type_dict = {'BACHELOR': 1, "FAMILY": 2, "COMPANY": 3, "ANYONE": 4}

parking = st.sidebar.selectbox('parking', [None, 'BOTH', 'TWO_WHEELER', 'NONE', 'FOUR_WHEELER'])
parking_dict = {'NONE': 0, "TWO_WHEELER": 1, "FOUR_WHEELER": 2, "BOTH": 3}

water_supply = st.sidebar.selectbox("water_supply", [None, 'CORPORATION', 'CORP_BORE', 'BOREWELL'])
water_supply_dict = {'CORPORATION': 1, "CORP_BORE": 2, "BOREWELL": 3}

building_type = st.sidebar.selectbox("building_type", [None, 'AP', 'IH', 'IF', 'GC'])
building_type_dict = {'AP': 1, "IH": 2, "IF": 3, "GC": 4}

furnishing = st.sidebar.selectbox('furnishing', [None, 'SEMI_FURNISHED', 'FULLY_FURNISHED', 'NOT_FURNISHED'])
furnishing_dict = {'NOT_FURNISHED': 0, "SEMI_FURNISHED": 1, "FULLY_FURNISHED": 2}

gym = st.sidebar.checkbox('Gym')
lift = st.sidebar.checkbox('Lift')
negotiable = st.sidebar.checkbox('Negotiable')
property_size = st.sidebar.number_input('Property Size', min_value=0)
property_age = st.sidebar.number_input('Property Age', min_value=0)
bathroom = st.sidebar.number_input('Number of Bathrooms', min_value=0)
balconies = st.sidebar.number_input('Number of Balconies', min_value=0)
floor = st.sidebar.number_input('floor', min_value=0)
total_floor = st.sidebar.number_input('total_floor', min_value=0)
cup_board = st.sidebar.number_input('cup_board', min_value=0)

activation_day = st.sidebar.number_input('Activation Day', min_value=1, max_value=31)
activation_month = st.sidebar.number_input('Activation Month', min_value=1, max_value=12)
activation_year = st.sidebar.number_input('Activation Year', min_value=1900, max_value=2100)
latitude = st.sidebar.number_input('Latitude')
longitude = st.sidebar.number_input('Longitude')

swimming_pool = st.sidebar.checkbox('Swimming Pool')
internet = st.sidebar.checkbox('Internet')
ac = st.sidebar.checkbox('AC')
club = st.sidebar.checkbox('Club')
intercom = st.sidebar.checkbox('Intercom')
cpa = st.sidebar.checkbox('CPA')
fs = st.sidebar.checkbox('FS')
servant = st.sidebar.checkbox('Servant')
security = st.sidebar.checkbox('Security')
sc = st.sidebar.checkbox('SC')
gp = st.sidebar.checkbox('GP')
park = st.sidebar.checkbox('Park')
rwh = st.sidebar.checkbox('RWH')
stp = st.sidebar.checkbox('STP')
hk = st.sidebar.checkbox('HK')
pb = st.sidebar.checkbox('PB')
vp = st.sidebar.checkbox('VP')
no_of_amenities = st.sidebar.number_input('Number of Amenities', min_value=0)

# Continue adding input fields for other features

data = [type, lease_type, parking, water_supply, building_type, furnishing]
if None not in data and st.button('Predict'):
    features = [
        type_dict[type], lease_type_dict[lease_type], parking_dict[parking],
        water_supply_dict[water_supply], building_type_dict[building_type], furnishing_dict[furnishing],
        gym, lift, negotiable, property_size, property_age, bathroom, balconies, floor, total_floor, cup_board,
        activation_day, activation_month, activation_year, latitude, longitude,
        facing_dict[facing],  # Use the dictionary to map facing to a numerical value
        swimming_pool, internet, ac, club, intercom, cpa, fs, servant, security,
        sc, gp, park, rwh, stp, hk, pb, vp, no_of_amenities
    ]
    model = pickle.load(open('houserent.pkl', 'rb'))
    predict = model.predict([features])[0]
    st.title(f'Your Predicted Rent: Rs {predict:.2f}')

