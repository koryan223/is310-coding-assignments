import pandas as pd
import plotly.express as px
import pycountry

def get_iso_code(country_name):
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except:
        return None

# Load the dataset
data = pd.read_csv('hbs_coffee-coffee.csv')

# Convert data types
data['year'] = data['year'].astype(str)
data['data'] = pd.to_numeric(data['data'], errors='coerce')

# Map country names to ISO codes
data['iso_alpha'] = data['COUNTRY'].apply(get_iso_code)

# Remove rows where iso_alpha is None (meaning no valid ISO code was found)
data = data[data['iso_alpha'].notna()]

# Ensure the data is sorted by year to display correctly in the slider
data = data.sort_values('year')

# Creating the interactive map
fig = px.choropleth(data_frame=data,
                    locations='iso_alpha',
                    color='data',
                    hover_name='COUNTRY',
                    animation_frame='year',
                    color_continuous_scale=px.colors.sequential.Plasma,
                    projection='natural earth',
                    title='Global Coffee Exports Over Time')

# Show the figure
fig.show()
