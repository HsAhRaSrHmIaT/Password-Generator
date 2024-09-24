import streamlit as st

st.title("Password Generator")
st.subheader("Generate a random password")

# Importing the required libraries
import random

length = st.slider("Select the length of the password", min_value=8, max_value=20, value=12, step=1)
# Function to generate a random password
spc_chars = st.number_input("How many special characters do you want in your password?", min_value=0, max_value=5, value=2, step=1)
num_chars = st.number_input("How many numbers do you want in your password?", min_value=0, max_value=5, value=2, step=1)

def generate_password():
    # All possible characters of a password
    numbers = "0123456789"
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()_+/|}{[]~:;?><,."
    password = ""
    for _ in range(length):
        if num_chars + spc_chars > length:
            return 0
        for _ in range(num_chars):
            password += random.choice(numbers)
        for _ in range(spc_chars):
            password += random.choice(special_characters)
        for _ in range(length - num_chars - spc_chars):
            password += random.choice(alphabets)
        password = list(password)
        return "".join(random.sample(password, len(password)))

password = generate_password()
if st.button("Generate Password"):
    if password == 0:
        st.error("Invalid input. Please try again.")
    else:
        st.markdown(f'<div style="border:2px solid;padding:10px;border-radius:10px;">Your random password is: <b>{password}</b></div>',
                    unsafe_allow_html=True)
        st.snow()
