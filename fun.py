### 1. Import essential libraries

import os
from dotenv import load_dotenv
import google.generativeai as gen_ai
import streamlit as st
import random

### 2. load our API_key vairable from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

### 3. Set up our AI using the API KEY
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

### 4. Streamlit page settings

st.set_page_config( # Configures our page
    page_title='Chat with Odyssey!',
    page_icon=':chat:',
    layout='centered'
)

# Define a function to translate the roles
def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return 'assistant'
    else:
        return user_role
    
# Initialise chat session with streamlist if it hasn't by default
if 'chat_sesssion' not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    
# Display the Bot's name on the page
st.title("Chat with Odyssey | 🤖")
    
# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        
# Create an input field for the user's message by using a random prompt for the input box
user_prompt_list = ['Chat to Odyssey...', 'Say something...', 'Ask "What is Machine Learning?"', 'Type anything here...', 'Ask Odyssey...', 'Ask "How can I code a CNN in Python?"', 'Ask "What is the meaning of life?"', 'Talk to Odyssey...', 'Ask Odyssey a joke.', 'Ask "What would you do if you were human for a day?"']
random_prompt = random.choice(user_prompt_list) # randomly selects a value from the user_prompt_list to show

user_prompt = st.chat_input(random_prompt)
if user_prompt:
    st.chat_message("user").markdown(user_prompt) # add user's message to chat and display it
    odyssey_response = st.session_state.chat_session.send_message(user_prompt) # Send Odyssey the message and get the response
    with st.chat_message('assistant'):
        st.markdown(odyssey_response.text) # Display Odyssey's Response