import streamlit as st

# User Interface Layer
def user_interface():
    st.sidebar.title("Virtual Gabby Mediator")
    st.sidebar.text_input("Username")
    st.sidebar.text_input("Password", type="password")
    st.sidebar.button("Login")

# Communication Layer
def communication_layer():
    st.markdown("<h2 style='color: lightgreen;'>How can I help you?</h2>", unsafe_allow_html=True)
    st.text_area("Enter your request here:")

# Mediation Layer
def mediation_layer():
    st.markdown("<h2 style='color: #FFD700;'>Let me be your mediator</h2>", unsafe_allow_html=True)
    options = [
        "I need more knowledge about men after marriage",
        "I need more knowledge about women after marriage",
        "I need legal advice",
        "I need honeymoon packages"
    ]
    for option in options:
        st.button(option)

# Educational Layer
def educational_layer():
    st.markdown("<h2 style='color: orange;'>Educational Resources</h2>", unsafe_allow_html=True)
    links = {
        "Video 1": "https://www.youtube.com/watch?v=-65jxGAxMco",
        "Video 2": "https://www.youtube.com/watch?v=dDGs0uT-F1c",
        "Video 3": "https://www.youtube.com/watch?v=eCLk-2iArYc",
        "Video 4": "https://www.youtube.com/watch?v=AWkpjGMZFjc"
    }
    for name, url in links.items():
        st.markdown(f"[{name}]({url})", unsafe_allow_html=True)

# Additional Educational Layer
def additional_educational_layer():
    st.markdown("<h2 style='color: yellow;'>Additional Courses</h2>", unsafe_allow_html=True)
    st.button("Coursera Courses")
    st.button("Better parenting plan courses")

# Navigation
page_names = ["User Interface", "Communication", "Mediation", "Educational", "Additional Educational"]
page_funcs = [user_interface, communication_layer, mediation_layer, educational_layer, additional_educational_layer]

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", page_names)

page_funcs[page_names.index(selection)]()