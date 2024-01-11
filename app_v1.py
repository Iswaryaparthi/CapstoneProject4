import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset

df = pd.read_csv('airbnb_data_v2.csv')

# Streamlit application
st.title(':rainbow[AirBnB Data Analysis]')

st.subheader(":green[Introduction]")

st.markdown('''Airbnb began in 2008 when two designers who had space to share hosted three travellers looking for a place to stay.
             Now, millions of Hosts and guests have created free Airbnb accounts to enjoy each other's unique view of the world.
             From cozy cottages to elegant penthouses,Hosts are happy to share their places. Whether its a work trip, weekend getaway, family vacation,
             or a longer stay, there are millions of amazing places to visit.''')

st.markdown(''' On the business front, Airbnb for Work has everything needed to do your job on the road,
            from top-rated places and collaborative spaces to team-building Experiences and administrative tools 
            that make managing travel easier than ever.''')

st.subheader(":green[Project views]")

st.markdown('''This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, 
            develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations,
            availability patterns, and location-based trends.''')

st.subheader(':green[Technologies used in this project]')

st.markdown('''Python scripting, MongoDB Atlas, Exporting CSV file, Handling large dataset, Data Preprocessing,
               Exploratory data analysis, Visualization using Plotly, Streamlit Web Application, Dashboard creation
               using PowerBI. ''')

# Sidebar with filters and dropdowns
st.sidebar.header(':green[Data Explorations]')

# Country filter
selected_country = st.sidebar.selectbox('Select Country', ['All'] + df['country'].unique().tolist())

# Property type filter
selected_property_type = st.sidebar.multiselect('Select Property Type(s)', df['property_type'].unique())

# Cancellation policy filter
selected_cancellation_policy = st.sidebar.multiselect('Select Cancellation Policy(ies)', df['cancellation_policy'].unique())

# Apply filters
filtered_df = df.copy()

if selected_country != 'All':
    filtered_df = filtered_df[filtered_df['country'] == selected_country]

if selected_property_type:
    filtered_df = filtered_df[filtered_df['property_type'].isin(selected_property_type)]

if selected_cancellation_policy:
    filtered_df = filtered_df[filtered_df['cancellation_policy'].isin(selected_cancellation_policy)]


st.subheader(':green[Data Visualizations]')

st.markdown('''From here, we will be going to see some insights, data presentations and explorations for the AirBnB dataset
             using  stacked bar chart,bubble chart,donut chart , findings outliers using box plot chart,
             customized bubble charts, horizontal charts and the findings too.''')

# Visualize the distribution of property in stacked bar chart

st.subheader(':violet[Distribution of Property Types in Each Country]')
fig_bar = px.bar(filtered_df, x='country', color='property_type', labels={'property_type': 'Property Type'})
st.plotly_chart(fig_bar)

st.markdown(':red[Findings]')

st.markdown('''Based on the above analysis, the type of the property plays major role in accommodation.
             Mostly, people are tends to stay in Apartment and House due to various factors. 
            Compare to other countries, Condominium stay rises in United States.''')

# Visualize the cancellation policy distribution using a donut chart

st.subheader(':violet[Distribution of Cancellation Policies]')
fig_donut = px.pie(filtered_df, names='cancellation_policy')
st.plotly_chart(fig_donut)

st.markdown(':red[Findings]')

st.markdown('''In all the countries, the people would prefer cancellation policies for accommodation bookings 
               and it would be in moderate,flexible and even strict_14 days with grace period mode.''')

# Visualize the relationship between the number of reviews and the average review scores using a bubble chart

st.subheader(':violet[Number of Reviews vs. Average Review Scores]')
fig_bubble = px.scatter(filtered_df, x='number_of_reviews', y='review_scores', size='number_of_reviews', color='review_scores')
st.plotly_chart(fig_bubble)

st.markdown(':red[Findings]')

st.markdown('''Reviews and ratings are playing the important role in accommodation bookings. 
              If the reviews and ratings are high, the bookings will be high.''')


st.subheader(':violet[Price variations]')

# box plot for outliers

fig = px.box(df, y=["price"])

st.plotly_chart(fig)

st.markdown(':red[Findings]')

st.markdown('''BoxPlot chart helps to find the price variations and their outliers. In this dataset, 
            the price varies  from minimum to maximun of 50k. Here, the maximum price lying
             in between of 0-20k but we can see one outlier which is present in the price of around 50k. 
            So, this is the outlier in this particular dataset. ''')

# Customized bubble chart for reviews and availabilities

st.subheader(':violet[Customized Bubble Chart Visualizations]')

x_column = st.selectbox('Select X-Axis Column', ['number_of_reviews', 'bedrooms', 'accommodates'])
y_column = st.selectbox('Select Y-Axis Column', ['review_scores', 'bathrooms', 'price'])
size_column = st.selectbox('Select Size Column', ['availability_30', 'availability_60', 'availability_90','availability_365'])
color_column = st.selectbox('Select Color Column', ['beds', 'extra_people', 'cleaning_fee'])

fig_custom_bubble = px.scatter(
    filtered_df,
    x=x_column,
    y=y_column,
    size=size_column,
    color=color_column,
    labels={x_column: x_column.capitalize(), y_column: y_column.capitalize()},
    size_max=50,
)

st.plotly_chart(fig_custom_bubble)

st.subheader(':violet[Top Amenities]')

# Preprocess the amenities column
amenities_list = [amenity.strip('{}').replace('"', '') for amenity in df['amenities']]
all_amenities = ', '.join(amenities_list).split(', ')
amenities_counter = Counter(all_amenities)

# Convert Counter to DataFrame for Plotly
amenities_df = pd.DataFrame.from_dict(amenities_counter, orient='index', columns=['Count']).reset_index()
amenities_df.columns = ['Amenity', 'Count']

# Visualize the frequency of each amenity using a horizontal bar chart

fig_amenities = px.bar(
    amenities_df.sort_values(by='Count', ascending=False),
    x='Count',
    y='Amenity',
    orientation='h',    
    labels={'Amenity': 'Amenity', 'Count': 'Count'},
)
st.plotly_chart(fig_amenities)

st.markdown(':red[Findings]')

st.markdown('''All over the world, people would expect some basic amenities while booking the room for stay. 
              In Airbnb, most hotels, apartments provide basic amenities like kitchen, Wi-Fi, TV, dryer, Office setup,
              Parking, Elevators, Microwave, Fire Extinguisher etc.''')

st.markdown(":rainbow[Thank you All!]")