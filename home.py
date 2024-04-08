import streamlit as st

def create_cognifyz_homepage():
    st.title("Cognifyz Technologies Internship Program")

    st.write("""
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    .container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
    }
    h1, h2, h3 {
        color: #333;
    }
    img {
        max-width: 100%;
        height: auto;
    }
    </style>
    """, unsafe_allow_html=True)

    st.write("""
    <div class="container">
        <h2>Cognifyz - Where Data Meets Intelligence</h2>
        <p>Cognifyz Technologies is a leading technology company specializing in data science, AI, ML, and data analytics tools. We offer internship programs to enhance skills and knowledge in these areas.</p>
        <h3>About Us</h3>
        <p>Cognifyz Technologies focuses on delivering innovative and cutting-edge solutions to meet the evolving needs of businesses. We provide training programs and deliver impactful projects and solutions.</p>
        <!-- Add more content here -->
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    ### Internship Program
    Welcome to our exciting Data Science internship program! This program offers an engaging and rewarding experience where you can choose from different levels and tasks to complete.
    """)

    st.write("""
    ### Submission Guidelines
    During your internship tenure, it is important to keep in mind the following points:
    - Create a professional video showcasing your internship projects and achievements.
    - Host the video on LinkedIn and tag Cognifyz Technologies.
    - Submission form will be shared later.
    - Use relevant hashtags like #cognifyz #cognifyzTech #cognifyzTechnologies.
    """)

    st.write("""
    ### Task List
    Welcome to our exciting Data Science internship program! To complete this internship, you will have the chance to choose any 2 of 3 levels: Level 1, Level 2, or Level 3. We've designed these levels to cater to your convenience and ensure an engaging and rewarding experience. Additionally, the successful completion of Level 3 ( any 2 task out of 4) will further enhance your chances of receiving a stipend.
    """)
    
    st.write("""
    ### Level 1 Tasks (Completed)
    - Task 1: Data Exploration and Preprocessing
    - Task 2: Descriptive Analysis
    - Task 3: Geospatial Analysis
    """)
    
    st.write("""
    ### Level 2 Tasks
    - Task 1: Price Range Analysis
    - Task 2: Feature Engineering
    - Task 3: Predictive Modeling
    """)
    
    st.write("""
    ### Level 3 Tasks (Completed)
    - Task 1: Predictive Modeling
    - Task 2: Customer Preference Analysis
    - Task 3: Data Visualization
    """)
    
    st.write("""
    ### How to Contact Us?
    To find out more information, please contact us at [contact@cognifyz.com](mailto:contact@cognifyz.com), or visit our website [www.cognifyz.com](https://www.cognifyz.com).
    """)
    
    

if __name__ == "__main__":
    create_cognifyz_homepage()
