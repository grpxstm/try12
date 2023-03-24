import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Rishwin","Aashish","Midhun","Prince"]
usernames = ["rishwin","aashish","midhun","prince"]
passwords = ["rishwin123","aashish123","midhun123","prince123"]

hashed_passwords = stauth.Hasher(passwords).generate()
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
	pickle.dump(hashed_passwords,file)
