import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache
def load_data():
    return pd.read_csv("Dataset .csv")

data = load_data()

def predictive_modeling():

    # Task 1: Predictive Modeling
    st.header("Task 1: Predictive Modeling")

    # # Preparing the data
    # X = data.drop(['Aggregate rating'], axis=1)
    # y = data['Aggregate rating']

    # # Encoding categorical data
    # X = pd.get_dummies(X, drop_first=True)

    # # Splitting the dataset into training and testing sets
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # st.write('Data split into training and testing sets.')

    # # Training and evaluating Linear Regression model
    # lr_model = LinearRegression()
    # lr_model.fit(X_train, y_train)
    # y_pred_lr = lr_model.predict(X_test)

    # # Calculating performance metrics for Linear Regression
    # mse_lr = mean_squared_error(y_test, y_pred_lr)
    # r2_lr = r2_score(y_test, y_pred_lr)

    # st.write('Linear Regression - Mean Squared Error:', mse_lr)
    # st.write('Linear Regression - R2 Score:', r2_lr)

    # # Training and evaluating Decision Tree Regressor
    # dt_model = DecisionTreeRegressor(random_state=42)
    # dt_model.fit(X_train, y_train)
    # y_pred_dt = dt_model.predict(X_test)

    # # Calculating performance metrics for Decision Tree
    # mse_dt = mean_squared_error(y_test, y_pred_dt)
    # r2_dt = r2_score(y_test, y_pred_dt)

    # st.write('Decision Tree - Mean Squared Error:', mse_dt)
    # st.write('Decision Tree - R2 Score:', r2_dt)

    # # Training and evaluating Random Forest Regressor
    # rf_model = RandomForestRegressor(random_state=42)
    # rf_model.fit(X_train, y_train)
    # y_pred_rf = rf_model.predict(X_test)

    # # Calculating performance metrics for Random Forest
    # mse_rf = mean_squared_error(y_test, y_pred_rf)
    # r2_rf = r2_score(y_test, y_pred_rf)

    # st.write('Random Forest - Mean Squared Error:', mse_rf)
    # st.write('Random Forest - R2 Score:', r2_rf)

    st.write('Linear Regression - Mean Squared Error: 42747297.146667674')
    st.write('Linear Regression - R2 Score: -18780864.647762895')
    st.write('Decision Tree - Mean Squared Error: 0.049267399267399266')
    st.write('Decision Tree - R2 Score: 0.9783545517911687')
    st.write('Random Forest - Mean Squared Error: 0.027151717948717888')
    st.write('Random Forest - R2 Score: 0.9880709939355645')


    # Conclusion
    st.header("Conclusion")

    st.write("The Random Forest Regressor model has the lowest Mean Squared Error and the highest R2 Score, indicating it performs the best among the three models in predicting the aggregate rating of a restaurant. The Decision Tree Regressor also shows good performance but slightly less than the Random Forest. The Linear Regression model, however, has significantly worse performance metrics, suggesting it may not be suitable for this particular prediction task.")




    # Task 2: Customer Preference Analysis
    st.header("Task 2: Customer Preference Analysis")

        # Let's start by analyzing the relationship between cuisine type and restaurant ratings.
    # We'll also identify the most popular cuisines based on the number of votes.

    # Extracting relevant columns
    relevant_data = data[['Cuisines', 'Aggregate rating', 'Votes']]

    # Checking for any missing values
    print('Missing values in each column:')
    relevant_data.isnull().sum()

    relevant_data.dropna(subset=['Cuisines'], inplace=True)


    # Splitting the 'Cuisines' column to count each cuisine type separately
    # This is because a restaurant can offer multiple cuisines.
    from collections import Counter

    # Splitting the cuisines and flattening the list
    all_cuisines = relevant_data['Cuisines'].str.split(', ').sum()

    # Counting each cuisine
    cuisine_counts = Counter(all_cuisines)

    # Converting to DataFrame
    cuisine_df = pd.DataFrame(cuisine_counts.items(), columns=['Cuisine', 'Count']).sort_values(by='Count', ascending=False)

    st.write('Most popular cuisines based on the number of votes:')
    st.write(cuisine_df.head(10))

    # we need to expand the 'Cuisines' column so each cuisine type has its own row while keeping the ratings associated.
    expanded_cuisines = relevant_data.assign(Cuisines=relevant_data['Cuisines'].str.split(', ')).explode('Cuisines')

    # Calculating the average rating for each cuisine
    average_ratings = expanded_cuisines.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)

    st.write('Cuisines with the highest average ratings:')
    st.write(average_ratings.head(10))

    # Analysis of Cuisines
    st.header("Analysis of Cuisines")

    st.write("The cuisines with the highest average ratings are diverse, ranging from Sunda and Börek to Taiwanese and Ramen. This suggests that there isn't a single type of cuisine that dominates in terms of higher ratings; rather, quality and customer satisfaction across various cuisines can lead to high ratings.")




    # Task 3: Data Visualization
    st.header("Task 3: Data Visualization")

    # Visualize the distribution of ratings using a histogram
    st.subheader("Distribution of Ratings")
    plt.figure(figsize=(10, 6), facecolor='white')
    sns.histplot(data['Aggregate rating'], bins=20, kde=True, color='skyblue')
    plt.title('Distribution of Aggregate Ratings')
    plt.xlabel('Aggregate Rating')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--')
    plt.show()
    st.pyplot(fig)
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Plot the top 10 cuisines by average rating
    st.subheader("Top 10 Cuisines by Average Rating")
    fig = plt.figure(figsize=(10, 6), facecolor='white')
    average_ratings.head(10).plot(kind='bar', color='orange')
    plt.title('Top 10 Cuisines by Average Rating')
    plt.xlabel('Cuisine')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--')
    plt.show()
    st.pyplot(fig)
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Visualize the relationship between 'Average Cost for two' and 'Aggregate rating'
    st.subheader("Relationship between Average Cost and Aggregate Rating")
    fig = plt.figure(figsize=(10, 6), facecolor='white')
    sns.scatterplot(data=data, x='Average Cost for two', y='Aggregate rating', hue='Price range', palette='coolwarm', alpha=0.6)
    plt.title('Relationship between Average Cost for two and Aggregate Rating')
    plt.xlabel('Average Cost for two')
    plt.ylabel('Aggregate Rating')
    plt.grid(True)
    plt.legend(title='Price Range')
    plt.show()
    st.pyplot(fig)
    st.set_option('deprecation.showPyplotGlobalUse', False)

