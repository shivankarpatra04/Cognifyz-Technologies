import streamlit as st
import pandas as pd

def analyze_restaurant_dataset():
    st.title("Restaurant Dataset Analysis")

    # Load the dataset
    dataset = pd.read_csv('Dataset .csv')

    # Link external CSS file
    st.markdown('<link rel="stylesheet" href="styles.css">', unsafe_allow_html=True)

    # Display the first few rows to understand its structure
    st.subheader("First Few Rows of the Dataset")
    st.dataframe(dataset.head())

    # Summarize the dataset
    st.subheader("Dataset Summary")
    st.write("Number of rows:", dataset.shape[0])
    st.write("Number of columns:", dataset.shape[1])
    st.write("Data types:", dataset.dtypes)

    # Display notable features and key details
    st.subheader("Key Details about the Dataset")

    st.write("""
    - **Geographical Information:** It provides detailed location data, including city, address, locality, and precise geographical coordinates, which could be useful for spatial analysis.
    - **Restaurant Details:** Beyond basic identification, it includes specifics like cuisines offered, average cost, and currency, which can help analyze the restaurant market in different regions.
    - **Service Features:** Information on table booking, online delivery, and current delivery status can offer insights into the service aspects of these restaurants.
    - **Ratings:** The dataset includes aggregate ratings and rating colors, which could be used to perform sentiment analysis or evaluate customer satisfaction across different locales or cuisines.
    """)

if __name__ == "__main__":
    analyze_restaurant_dataset()
