## Introduction
The project "Cultural Brews: A Digital Exploration of Coffee's Influence Across Time and Space" aims to unravel the complex narrative of coffee's cultural and economic impacts across various societies throughout history. Coffee is not just a popular beverage but a significant cultural marker that has influenced social practices, political movements, and economic conditions globally. This research is driven by the goal to understand how coffee transitioned from a simple agricultural product to a central element in social interactions and economic structures.

The relevance of this study lies in its potential to enhance our understanding of cultural commodities and their broader societal impacts, using coffee as a primary example. By employing digital humanities methods, this project seeks to demonstrate the power of computational tools in cultural studies, offering new insights into historical data and trends that traditional methods might overlook.
***

## Literature Review
The scholarly exploration of coffee's role in society spans several disciplines, reflecting its multifaceted influence. Historical texts often depict coffee as a catalyst for social interaction and intellectual discourse, particularly in the context of the Enlightenment and various revolutionary movements. In "The Role of Coffee in the Enlightenment Revolution," it is argued that coffee houses in 18th-century Europe served as hubs for intellectual exchange that significantly contributed to the era's groundbreaking philosophical and scientific progress (chocolate class).

Similarly, Eddy Gilpin in "Café Liberté: The Role of the Coffeehouse in the French Revolution" discusses how Parisian coffeehouses became centers for political debate and grassroots organizing during the French Revolution. These establishments provided a space where revolutionary ideas were disseminated and discussed, playing a crucial role in shaping the political landscape of the time (The Alexandrian).

Moreover, the economic implications of coffee are highlighted in various market analyses, such as the ICO Coffee Market report, which details fluctuations in coffee prices and their impact on global trade(Coffee Market Report). This economic perspective underscores the importance of coffee in global markets and its role in the economies of developing countries, often referred to as third-world countries.

These diverse scholarly perspectives provide a foundational understanding of coffee's historical and cultural significance. This project builds upon these studies by applying digital humanities tools to further dissect and visualize coffee's impact across different times and spaces, aiming to offer a more nuanced understanding of its global significance.
***

## Data Collection & Curation
The data collection and curation process for the project involved an extensive exploration of both historical and contemporary sources to compile a comprehensive dataset on coffee's influence throughout history.

**Primary Data Sources**
1. HBS Coffee Dataset: The foundational dataset for this project was sourced from the Harvard Business Review's "hbs coffee.xlsx." This dataset provides detailed records on coffee production, trade, and consumption statistics over several decades. It includes data on coffee prices, production volumes, and export-import statistics across major coffee-producing countries. This quantitative data forms the backbone of the analysis, allowing for a detailed examination of trends and patterns in the coffee market.

2. Historical Texts and Records: To understand the cultural and historical context of coffee, a variety of historical sources were digitized. These included advertisements, coffee house records, and literary mentions of coffee. These texts offer insights into the social and economic roles of coffee in various societies.

**Secondary Data Sources:**
1. NPR Article An article from NPR: provided a visual representation of the historical distribution of coffee cultivation. This secondary source supplemented the primary data by offering a geospatial perspective on the spread of coffee culture across the globe.


2. Coffee Market Reports: Recent market reports, such as the Coffee Market Report March 2024, were used to understand current trends in the coffee industry. These reports offer up-to-date information on coffee prices, market demand, and the economic impact of coffee on different regions.

3. Scholarly Articles on Coffee Houses: Historical analyses, such as those discussing the role of coffee houses during the Enlightenment and French Revolution, were crucial in understanding the social impact of coffee. These sources provided qualitative data that helped frame the discussion around coffee's role in fostering intellectual and political activities.
***

## Data Curation Process:
- Digitization and Text Extraction: Historical texts and records were digitized using OCR (Optical Character Recognition) technology. This process involved converting scanned images of documents into machine-readable text, which was then cleaned and prepared for analysis.
  
- Data Cleaning and Standardization: The data extracted from various sources, especially historical texts, required extensive cleaning and standardization. This involved correcting OCR errors, standardizing date formats, and resolving inconsistencies in measurement units.

- Named Entity Recognition (NER): To extract specific information related to coffee, such as types of coffee, locations, and historical figures associated with coffee, NER techniques were applied to the text data. This allowed for the automated identification and categorization of relevant entities.

- Integration and Harmonization: Data from different sources were integrated into a single dataset. This involved harmonizing fields such as geographic locations and time periods to ensure consistency across the dataset. The integrated dataset was then structured to support various types of analysis, including temporal trends and spatial distributions.

- Documentation and Metadata Creation: To ensure the reproducibility of the research and to aid future researchers, comprehensive documentation of the data sources, curation processes, and analysis methods was created. Metadata describing the data fields, sources, and curation steps were also developed.
***

##Data Visualization
```
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
```
**Explanation:**
This will show the export of copy in each part of the world from 1900 to 2010

save as html and embbed it
