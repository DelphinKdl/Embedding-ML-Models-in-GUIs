import pickle 
from pathlib import Path

import streamlit_authenticator as stauth

names = ["k teams", "Guest users"]
usernames = ["k.team", "G.User"]
passwords = ["xxxx", "xxxx"]

hashed_passwords = stauth.Hasher(passwords).generate()
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)