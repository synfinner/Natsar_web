#!/usr/bin/env python3

# streamlit script for natsar, a python script for extracting telegram data from the bot API
# and obtaining user data via the Telethon library

# import stremlit for the base app
import streamlit as st
from modules import ntelegram as tg

def get_bot_info(bot_token):
    # create a TelegramBot object from the ntelegram module
    bot = tg.TelegramBot(bot_token)
    # send a request to the getMe endpoint
    response = bot.send_request("getMe")
    # return the response
    return response

def getUsernames(bot_token):
    bot = tg.TelegramBot(bot_token)
    response = bot.send_request('getUpdates')
    # return the response
    return response

def addSidebar():
    # add a sidebar to the app
    st.sidebar.title("Natsar")
    st.sidebar.write("A python script for extracting telegram data from the bot API and obtaining user data via the Telethon library")
    st.sidebar.write("This is a work in progress")
    st.sidebar.write("Based on my terminal Natsar client: [Repository](https://github.com/synfinner/Natsar)")
    st.sidebar.write("Created with ♥️ by [synfinner](https://twitter.com/synfinner)")

# function for the content of first app page
def content():
    st.title("Natsar Web")
    # add horizontal line
    st.markdown("---")
    st.markdown("""
## What is Natsar?
Natsar is a python script for extracting telegram data from the bot API and obtaining user data via the Telethon library. This is a work in progress and is based on my terminal Natsar client

## How to use
If you didn't already, run the `natsar_init.py` script to create a `natsar.session` file. This is required for API usage. Alternatively, you can use the Bot Info page without a session file or client keys, as it only requires an obtained bot token.
    """)

# main function
if __name__ == "__main__":
    # set the page config
    st.set_page_config(
    page_title="Natsar Web",
    page_icon="❤️",
)
    # check if there is a natsar.session file. If not, return an error
    try:
        with open('natsar.session', 'r') as f:
            pass
    except FileNotFoundError:
        st.error("Error: natsar.session file not found. Please run the natsar_init.py script first!")
    addSidebar()
    content()
    