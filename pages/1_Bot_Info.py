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
    st.sidebar.markdown("**Bot token:** *(escape the colon in the bot token)*:")
    # add a text input for the bot token to the sidebar and assign it as a global variable
    global bot_token
    bot_token = st.sidebar.text_input("token datas",label_visibility="collapsed",placeholder="71xxxxxxx4\:BAJxxxxxxxxxe43")

# function for performing the extraction given a bot token
def extractData():
    # add a text input for the bot token
    # if the inputted data is not empty and does not contain a \, return an error
    if bot_token and "\\" not in bot_token:
        st.error("Error: Invalid bot token. You must escape the colon in the bot token.")
        st.error("Error: Add a \ before the : character in your bot token!! This is a limitation of streamlit.")
    # add a message box to display bot token if bot_token
    if bot_token and "\\" in bot_token:
        # assign the bot token to a variable that removes the \ character
        bot_token2 = bot_token.replace("\\","")
        st.info("Entered Bot Token: {}".format(bot_token))
        # create a column container for the displayed information
        telegram_columns = st.container()
        # set the height of the container to 100px and add a scroll bar
        telegram_columns.markdown("<style>div.css-1l02zno{height: 100px; overflow-y: scroll;}</style>",
    unsafe_allow_html=True,
        )
        with telegram_columns:
            # Setup the columns for data display
            col1, col2 = st.columns(2)
            with col1:
                st.header("Bot Info:")
                st.divider()
                # add a spinner to indicate that the bot info is being retrieved
                with st.spinner("Retrieving bot info..."):
                    # call the get_bot_info function and assign it to a variable of botInfo
                    botInfo = get_bot_info(bot_token2)
                    # display the bot info 
                    st.markdown(f"**Bot Username:** {botInfo[0]}")
                    st.markdown(f"**Bot First Name:** {botInfo[1]}")
                    st.markdown(f"**Bot ID:** {botInfo[2]}")
            with col2:
                # call the function to get active users
                st.header("Active Users:")
                st.divider()
                # add a spinner to indicate that the active users are being retrieved
                with st.spinner("Retrieving active users..."):
                    try:
                        botUsers = getUsernames(bot_token2)
                    except Exception as e:
                        st.exception(e)
                    # dynamically display the usernames
                    if len(botUsers) == 0:
                        st.markdown("**No active users found**")
                    for i in range(len(botUsers)):
                        st.markdown(f"**User {i+1}:** {botUsers[i]}")
        # create a container for the file links outside of the columns
        with st.container():
            # call function to get file links and display them
            st.header("File Links:")
            st.divider()
            with st.spinner("Retrieving file links..."):
                # create a bot object
                try:
                    bot = tg.TelegramBot(bot_token2)
                except Exception as e:
                    st.exception(e)
                # call the get_tg_files function and assign it to a variable of fileLinks
                fileLinks = bot.get_tg_files()
                if len(fileLinks) == 0:
                    st.markdown("**No file links found**")
                for i in range(len(fileLinks)):
                    st.markdown(f"**File {i+1}:** {fileLinks[i]} -- [Download](https://api.telegram.org/file/bot{bot_token2}/{fileLinks[i]})")

# main function
if __name__ == "__main__":
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