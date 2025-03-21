# Streamlit app for the Further project

import streamlit as st
from agent import FurtherAgent
import time
import json

# Initialize the agent
agent = FurtherAgent()

# Set page title and configure
st.set_page_config(
    page_title="ACME Senior Living - Chat Assistant", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)
st.title("ACME Senior Living - Chat Assistant")

# Add a sidebar with information about the app
with st.sidebar:
    st.header("About this app")
    st.write("""
    This is a demo of a conversational AI assistant for ACME Senior Living.
    It can answer questions about the community, pricing, amenities, and help schedule tours.
    """)
    st.divider()
    st.subheader("Technical Details")
    st.write("Powered by OpenRouter and Gemini 2.0 Flash")
    
    # Debugging section
    st.divider()
    st.subheader("Debug Information")
    if "last_thinking" in st.session_state:
        with st.expander("Last Thinking Process"):
            st.text(st.session_state.last_thinking)
    
    # Add a reset button
    if st.button("Reset Conversation"):
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "assistant", 
            "content": "Hi, this is ACME Senior Living. My name is Sophie. How may I help you today?"
        })
        if "last_thinking" in st.session_state:
            del st.session_state.last_thinking
        st.rerun()

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add a welcome message
    st.session_state.messages.append({
        "role": "assistant", 
        "content": "Hi, this is ACME Senior Living. My name is Sophie. How may I help you today?"
    })

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response in chat container
    with st.chat_message("assistant"):
        # Add a placeholder for the streaming effect
        message_placeholder = st.empty()
        full_response = ""
        
        # Show thinking indicator
        with st.spinner("Sophie is typing..."):
            try:
                # Get response from the agent - now returns a dictionary with message and metadata
                agent_response = agent.respond(st.session_state.messages)
                
                # Extract message and thinking from the response
                response = agent_response["message"]
                
                # Store thinking in session state for debugging if available
                if "thinking" in agent_response and agent_response["thinking"]:
                    st.session_state.last_thinking = agent_response["thinking"]
                
            except Exception as e:
                response = f"I'm sorry, but I encountered an error: {str(e)}"
        
        # Simulate streaming effect
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.02)
            message_placeholder.markdown(full_response + "▌")
        
        # Display the full response
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

