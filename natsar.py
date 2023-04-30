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
    # add horizontal line
    st.sidebar.markdown("---")
    st.sidebar.write("A python script for extracting telegram data from the bot API and obtaining user data via the Telethon library")
    st.sidebar.write("This is a work in progress")
    st.sidebar.write("Based on my terminal Natsar client: [Repository](https://github.com/synfinner/Natsar)")
    st.sidebar.write("Created with ♥️ by [synfinner](https://twitter.com/synfinner)")

# function for performing the extraction given a bot token
def extractData():
    # add markdown
    st.markdown("Enter your bot token below *(you must escape the colon in the bot token)*:")
    # add a text input for the bot token
    bot_token = st.text_input("token data",label_visibility="collapsed",placeholder="71xxxxxxx2\:BAJxxxxxxxxxe43")
    # if the inputted data is not empty and does not contain a \, return an error
    if bot_token and "\\" not in bot_token:
        st.error("Error: Invalid bot token. You must escape the colon in the bot token.")
        st.error("Erros: Add a \ before the : character in your bot token!! This is a limitation of streamlit.")
    # add a message box to display bot token if bot_token
    if bot_token and "\\" in bot_token:
        # assign the bot token to a variable that removes the \ character
        bot_token2 = bot_token.replace("\\","")
        st.info("Your bot token is: {}".format(bot_token))
        # clear the sidebar and show the bot token
        col1, col2 = st.columns(2)
        with col1:
            st.header("Bot Info:")
            # call the get_bot_info function and assign it to a variable of botInfo
            botInfo = get_bot_info(bot_token2)
            # display the bot info 
            st.markdown(f"**Bot Username:** {botInfo[0]}")
            st.markdown(f"**Bot First Name:** {botInfo[1]}")
            st.markdown(f"**Bot ID:** {botInfo[2]}")
        with col2:
            # call the function to get active users
            st.header("Active Users:")
            botUsers = getUsernames(bot_token2)
            # dynamically display the usernames
            for i in range(len(botUsers)):
                st.markdown(f"**User {i+1}:** {botUsers[i]}")
        with st.container():
            # call function to get file links and display them
            st.header("File Links:")
            # create a bot object
            bot = tg.TelegramBot(bot_token2)
            # call the get_tg_files function and assign it to a variable of fileLinks
            fileLinks = bot.get_tg_files()
            for i in range(len(fileLinks)):
                st.markdown(f"**File {i+1}:** {fileLinks[i]}")

            

if __name__ == "__main__":
    st.set_page_config(
    page_title="Natsar Web",
    page_icon="👋",
)
    # check if there is a natsar.session file. If not, return an error
    try:
        with open('natsar.session', 'r') as f:
            pass
    except FileNotFoundError:
        st.error("Error: natsar.session file not found. Please run the natsar_init.py script first!")
    st.title("Telegram Data Extraction")
    # add horizontal line
    st.markdown("---")
    # call the addSidebarfunction to set up the sidebar
    addSidebar()
    # call the extractData function to perform the extraction
    extractData()