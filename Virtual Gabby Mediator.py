import streamlit as st

# Set page configuration
st.set_page_config(page_title="Virtual Gabby Mediator", layout="wide")

# User Interface Layer
def user_interface_layer():
    st.sidebar.title("Virtual Gabby Mediator")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type='password')
    login_button = st.sidebar.button("Login")

    if login_button:
        st.sidebar.success(f"Welcome, {username}!")

# Communication Layer
def communication_layer():
    st.title("How can I help you?")
    user_input = st.text_area("Please enter what you want to discuss below:", "")
    st.success("Message received!") if user_input else st.info("Awaiting your message...")

# Mediation Layer
def mediation_layer():
    st.title("Let me be your mediator")
    mediation_choice = st.radio("Please select an option:",
                                ["I need more knowledge about men after marriage",
                                 "I need more knowledge about women after marriage",
                                 "I need legal advice",
                                 "I need honeymoon packages"])
    st.write(f"You selected: {mediation_choice}")

# Educational Layer with YouTube Links
def educational_layer_links():
    st.title("Educational Resources")
    st.write("Click on the links below to view educational content:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Video 1"):
            st.video("https://www.youtube.com/watch?v=-65jxGAxMco")
        if st.button("Video 3"):
            st.video("https://www.youtube.com/watch?v=eCLk-2iArYc")
    
    with col2:
        if st.button("Video 2"):
            st.video("https://www.youtube.com/watch?v=dDGs0uT-F1c")
        if st.button("Video 4"):
            st.video("https://www.youtube.com/watch?v=AWkpjGMZFjc")

# Educational Layer with Buttons
def educational_layer_buttons():
    st.title("Additional Educational Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Coursera Courses"):
            st.write("Redirecting to Coursera...")
    
    with col2:
        if st.button("Better Parenting Plan Courses"):
            st.write("Redirecting to Parenting Plan Courses...")

# Main Application
def main():
    # Applying the color schemes to different layers
    st.markdown("""
    <style>
    .sidebar .sidebar-content {background-color: #0e4d92;}
    h1 {color: #0e4d92;}
    .stTextInput>div>div {color: #0e4d92;}
    textarea {background-color: #c3e6cb; color: black;}
    .css-1v0mbdj {background-color: #c3e6cb;}
    .stRadio>div {background-color: #ffa500; color: black;}
    .stButton>button {background-color: #ffa500; color: black;}
    </style>
    """, unsafe_allow_html=True)
    
    user_interface_layer()  # Show the User Interface Layer
    
    if st.sidebar.button("Proceed to Communication Layer"):
        communication_layer()  # Show the Communication Layer
        
        if st.button("Proceed to Mediation Layer"):
            mediation_layer()  # Show the Mediation Layer
            
            if st.button("Proceed to Educational Layer Links"):
                educational_layer_links()  # Show the Educational Layer with YouTube Links
                
                if st.button("Proceed to Educational Layer Buttons"):
                    educational_layer_buttons()  # Show the Educational Layer with buttons

# Run the application
if __name__ == '__main__':
    main()
