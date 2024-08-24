#libraries
import streamlit as st

st.set_page_config(
    page_title=" Customer Churn Prediction App!",
    page_icon=" ",
    layout="wide"

)
#style
st.markdown("""
    <style>
    .stMarkdown {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

# title 
st.markdown('<div class=""><h1>🚀 Welcome to Customer Churn Prediction App</h1></div>', unsafe_allow_html=True)

# subtitle 
st.write('<div class""><h3>Experience the power of embedded machine learning in a seamless GUI to predict customer churn</h3></div>', unsafe_allow_html=True)

#  two columns from
st.markdown('<div class="col-container">', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    # contents
    # about app
    st.subheader('About the App')
    st.markdown(""" 
      Welcome to the Customer Churn Prediction Application. This tool is designed to help businesses in the telecommunications industry understand and predict customer churn. By leveraging advanced machine learning models, the application provides insights into customer behavior, identifies at-risk customers, and aids in the development of targeted retention strategies. This Home page serves as an entry point to the various features and functionalities offered by the application.
  
    """)
   # Benefits
    st.subheader(" User Benefits")
    st.markdown("""
    - **Data-driven Decisions**: Make informed decisions backed by data analytics.
    - **Easy Machine Learning**: Utilize powerful machine learning algorithms effortlessly.
    - **Live Demo**: Watch a demo video to see the app in action.
        [Watch Demo Video](#)""")
    # Reach me out
    st.subheader("Need Help?")
    st.markdown("""
        For collaborations, contact me at  delphin.kaduli@gmail.com 
        )
        """)
    st.link_button("Repository on GitHub", "https://github.com/DelphinKdl/Embedding-ML-Models-in-GUIs", type='secondary')
    

with col2:
    # Key Features
    st.subheader("Key Features")
    st.markdown("""
        - **Data Exploration**: Explore the customer churn dataset with detailed column descriptions and filtering options.
        - **Interactive Dashboard**: Analyze customer churn data through interactive visualizations and KPIs.
        - **Customer Churn Prediction**: Predict the likelihood of customer churn with both individual and bulk predictions.
        - **Historical Predictions**: Review logs of past predictions, analyze trends, and assess model performance.
        """)

    # How to Run Application
    st.subheader("How to Run Application")
    st.code("""
        # Activate virtual environment
        GUIenv/scripts/activate
        streamlit run Home.py
        """)
    st.subheader("Machine Learning Integration")
    st.markdown("""
        - **Model Selection**: Choose between advanced models for accurate predictions.
        - **Seamless Integration**: Integrate predictions with a user-friendly interface.
        - **Probability Estimates**: Gain insights into the likelihood of predicted outcomes.
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

    


    

