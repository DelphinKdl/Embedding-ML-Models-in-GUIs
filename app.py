import streamlit as st
import yaml
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import Hasher
import Data, Predict, History, Dashboard

# Configure page
st.set_page_config(page_title= "Customer Churn Prediction App!", page_icon="bar_chart:", layout="wide")


def main():
    # Load yaml configuration file
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    # Pre-hash all plain text passwords
    Hasher.hash_passwords(config["credentials"])

    authenticator = stauth.Authenticate(
                                        config["credentials"],
                                        config["cookie"]["name"],
                                        config["cookie"]["key"],
                                        config["cookie"]["expiry_days"],
                                        config["pre-authorized"],
                                        auto_hash = False
                                        )

    # Add authentication widget
    authenticator.login("sidebar", "login")
    

    # Set conditional statements
    if st.session_state["authentication_status"] is None:
        st.sidebar.info("Please enter username and password to access pages")
        st.sidebar.code(
                """
                TestCredentials:
                Username: test_user
                Password: passcode
                """
                )
    left, center, right = st.columns([1,10,1])
    with center:
        st.markdown("<h1 style='> Customer Churn Prediction App!</h1>", unsafe_allow_html=True)
        st.image("./image/login.png")
    
    if st.session_state["authentication_status"] is False:
        st.sidebar.error("Username/Password is incorrect !!! Try again.")

    if st.session_state["authentication_status"]:
        if "page" not in st.session_state:
            st.session_state["page"] = "Home page"

        st.sidebar.info(f"####welcome, *{st.session_state['name']}*!!")
        authenticator.logout(location = "sidebar")

        #menu
        st.sidebar.title("Navigation")
        st.session_state["page"] = st.sidebar.selectbox("Select page", options = ["Home","Data","Dashboard","Predicts","History"])
        
        if st.session_state["page"] == "Home":
            Home.show_Home()
        elif st.session_state["page"] == "Data":
            Data.show_Data()
        elif st.session_state["page"] == "Dashboard":
            Dashboard.show_Dashboard()
        elif st.session_state["page"] == "Predicts":
            Predict.show_Predictions()


if __name__ == "__main__":
    main()