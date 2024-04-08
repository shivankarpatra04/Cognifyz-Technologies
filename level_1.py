import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static


def analyze_restaurant_data():
    st.title("Restaurant Dataset Analysis")

    # Reading the dataset from a CSV file using pandas
    data = pd.read_csv('Dataset .csv')

    

    # Task 1: Data Exploration and Preprocessing

    # Retrieving the dimensions of the dataset (number of rows, number of columns)
    st.subheader("Data Dimensions")
    st.write("Number of rows:", data.shape[0])
    st.write("Number of columns:", data.shape[1])

    # Checking for missing values in each column of the dataset
    st.subheader("Missing Values")
    st.write(data.isnull().sum())

    # Filling missing values in the 'Cuisines' column with a specific string ('Not Available')
    specific_string = 'Not Available'
    data['Cuisines'].fillna(specific_string, inplace=True)

    # Convert the 'Aggregate rating' column to numeric type
    is_numeric = pd.to_numeric(data['Aggregate rating'], errors='coerce').notnull().all()

    # Displaying whether the 'Aggregate rating' column contains numeric values
    if is_numeric:
        st.write("'Aggregate rating' column contains numeric values.")
    else:
        st.write("'Aggregate rating' column contains non-numeric values.")

    # Visualizing the distribution of 'Aggregate rating' using a histogram
    st.subheader("Distribution of Aggregate Rating")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(data['Aggregate rating'], bins=20, color='orange')
    ax.set_title('Distribution of Aggregate Rating')
    ax.set_xlabel('Aggregate Rating')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Overview
    st.markdown("### Overview")
    st.write("Class imbalance refers to an unequal distribution of classes in a classification dataset. In this case, it refers to the unequal distribution of ratings in the 'Aggregate rating' column.")

    # Analysis Details
    st.markdown("### Analysis Details")
    st.write("- **Class '0.0'**: 2148 samples")
    st.write("- **Classes '1.8' to '4.9'**: Varies from 1 to 274 samples")

    # Observations
    st.markdown("### Observations")
    st.write("From the class distribution, it's evident that the majority class is '0.0', with 2148 samples. The remaining rating values have fewer samples, with some having as few as 1 sample (e.g., class '1.8'). This indicates a significant class imbalance, where the majority class dominates the dataset, and the minority classes are underrepresented.")

    # Task 2: Descriptive Analysis

    data.describe()

    
    
    st.subheader("Distribution of Country Codes")

    # Counting the occurrences of each country code
    country_counts = data['Country Code'].value_counts()

    # Plotting the distribution of country codes
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Country Code', data=data, order=country_counts.index)
    plt.title('Distribution of Country Codes')
    plt.xlabel('Country Code')
    plt.ylabel('Number of Restaurants')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Display the plot
    st.pyplot()

    
    
    st.subheader("Distribution of Cities")

    # Counting the occurrences of each city
    city_counts = data['City'].value_counts()

    # Plotting the top 20 cities with the highest number of restaurants
    plt.figure(figsize=(14, 8))
    city_counts.head(20).plot(kind='bar', color='skyblue')
    plt.title('Top 20 Cities with the Highest Number of Restaurants')
    plt.xlabel('City')
    plt.ylabel('Number of Restaurants')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Display the plot
    st.pyplot()

   
   
    st.subheader("Distribution of Cuisines")

    # Extracting individual cuisines and their counts
    cuisine_counts = data['Cuisines'].str.split(', ', expand=True).stack().value_counts()

    # Plotting the top 20 cuisines
    plt.figure(figsize=(14, 8))
    cuisine_counts.head(20).plot(kind='bar', color='orange')
    plt.title('Top 20 Cuisines')
    plt.xlabel('Cuisine')
    plt.ylabel('Number of Restaurants')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Display the plot
    st.pyplot()

    st.subheader("Analysis Highlights")

    st.markdown("In the analysis, it was discovered that **North Indian cuisine** reigns supreme among restaurants, boasting a staggering count of **3960 establishments**. Moreover, the bustling city of **New Delhi** emerged as the ultimate hub for food enthusiasts, with a remarkable **5473 dining establishments**.")

    # Task 3: Geospatial Analysis

    # Create a map centered around the mean latitude and longitude of the restaurant locations
    st.subheader("Geospatial Analysis")
    map_center = [data['Latitude'].mean(), data['Longitude'].mean()]
    map_restaurants = folium.Map(location=map_center, zoom_start=5)

    # Create a MarkerCluster object for clustering markers
    marker_cluster = MarkerCluster().add_to(map_restaurants)

    # Add markers for each restaurant location
    for idx, row in data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['Restaurant Name']
        ).add_to(marker_cluster)

    # Display the map
    folium_static(map_restaurants)

    st.subheader("Correlation Between Location and Rating")

    # Create a scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='Longitude', y='Latitude', hue='Aggregate rating', data=data, palette='viridis', alpha=0.7, ax=ax)
    ax.set_title('Correlation Between Location and Rating')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.legend(title='Rating')

    # Display the plot
    st.pyplot(fig)


    st.subheader("Correlation Coefficient Calculation")

    # Calculate the correlation coefficient
    correlation_coefficient = data[['Latitude', 'Longitude', 'Aggregate rating']].corr().loc['Aggregate rating', ['Latitude', 'Longitude']]

    # Display the results
    st.write("Correlation Coefficient between Latitude and Rating:", correlation_coefficient['Latitude'])
    st.write("Correlation Coefficient between Longitude and Rating:", correlation_coefficient['Longitude'])

    # Interpretation
    st.markdown("""
    - A coefficient close to 1 indicates a strong positive correlation, meaning that as one variable (latitude or longitude) increases, the other tends to increase as well.
    - A coefficient close to -1 indicates a strong negative correlation, meaning that as one variable increases, the other tends to decrease.
    - A coefficient close to 0 indicates no linear correlation between the variables.
    """)

    st.subheader("Interpreting Correlation Coefficients")

    st.markdown("""
    1. **Correlation Coefficient between Latitude and Rating:**
       - The correlation coefficient between latitude and rating is close to zero (0.0005), indicating a very weak positive correlation.
       - This suggests that there is almost no linear relationship between the latitude of restaurant locations and their ratings.

    2. **Correlation Coefficient between Longitude and Rating:**
       - The correlation coefficient between longitude and rating is approximately -0.1168, indicating a weak negative correlation.
       - This suggests that there is a slight negative linear relationship between the longitude of restaurant locations and their ratings.
       - However, the magnitude of this correlation is quite small, indicating that the impact of longitude on restaurant ratings is not very strong.

    Overall, based on these correlation coefficients, it seems that the geographical location (latitude and longitude) of restaurants has minimal influence on their ratings. Other factors such as food quality, service, ambiance, and pricing may play a more significant role in determining the ratings of restaurants.
    """)

if __name__ == "__main__":
    analyze_restaurant_data()
