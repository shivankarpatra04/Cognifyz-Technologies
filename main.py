import streamlit as st
from multiapp import MultiApp

# Add the path to your module directory

# Now you can import your module
import home,data,level_1,level_3

main = MultiApp()




# Add all your application here
main.add_app("Home",home.create_cognifyz_homepage)
main.add_app("Dataset", data.analyze_restaurant_dataset)
main.add_app("Level - 1", level_1.analyze_restaurant_data)
main.add_app("Level - 3", level_3.predictive_modeling)
main.run()
