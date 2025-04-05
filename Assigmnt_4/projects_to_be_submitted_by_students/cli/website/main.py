import streamlit as st

# Page Configuration
st.set_page_config(page_title="My Streamlit Website", page_icon="🌐", layout="centered")

# Sidebar Navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    st.title("Welcome to My Streamlit Website 🎉")
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, *{name}*! Welcome to my website.")

elif page == "About":
    st.title("About This Website")
    st.write("This is a simple website built using *Streamlit* in Python. 🚀")
    st.write("Features:")
    st.markdown("- Dynamic user input ✨\n- Sidebar navigation 📌\n- Simple and interactive UI 🖥")

# Footer
st.markdown("---")
st.write("Made with ❤ using Streamlit")