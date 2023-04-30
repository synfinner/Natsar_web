#!/usr/bin/env python3

import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from telethon import TelegramClient, events, sync


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
telegram_app_id = os.getenv("TELEGRAM_APP_ID")
telegram_app_hash = os.getenv("TELEGRAM_APP_HASH")

#class to send a request to the telegram bot api based on user supplied endpoint
class TelegramBot:
    # function to initialize the class
    def __init__(self, token):
        # set the token
        self.token = token
    
    def extract_profile_data(self, profile):
        # send a request to the profile link and get the response
        profile = requests.get(profile).text
        # get the profile data
        profile_desc = profile.split('og:description" content="')[1].split('"')[0]
        # get the profile title from og:title
        profile_title = profile.split('og:title" content="')[1].split('"')[0]
        # print tab delimited profile data
        return profile_desc, profile_title
        
    # function to remove duplicates from a list
    def remove_duplicates(self, users):
        # create an empty list
        new_users = []
        # loop through the list
        for i in users:
            # if the user is not in the new list, append it
            if i not in new_users:
                new_users.append(i)
        # return the new list
        return new_users
    
    def remove_file_duplicates(self, files):
        # create an empty list
        new_files = []
        # loop through the list
        for i in files:
            # if the user is not in the new list, append it
            if i not in new_files:
                new_files.append(i)
        # return the new list
        return new_files

    # function to send a request to the telegram bot api
    def send_request(self, endpoint):
        # send a request to the telegram bot api
        response = requests.get('https://api.telegram.org/bot{}/{}'.format(self.token, endpoint))
        # if the response is not 200, raise an exception
        if response.status_code != 200:
            raise Exception('Error: {}'.format(response.text))
        if endpoint == 'getMe':
            # Try to return the bot username, first name, username, and id
            try:
                return response.json()['result']['username'], response.json()['result']['first_name'],\
                    response.json()['result']['id']
            except KeyError:
                raise Exception('Error: {}'.format(response.text))
        elif endpoint == 'getUpdates':
            # append the user id and username to a list
            users = []
            for i in response.json()['result']:
                try:
                    users.append((i['message']['from']['id'], i['message']['from']['username']))
                except KeyError:
                    pass
            # call a function to remove duplicates
            users = self.remove_duplicates(users)
            return users
    def get_tg_files(self):
            # get the telegram bot updates
            response = requests.get('https://api.telegram.org/bot{}/getUpdates'.format(self.token))
            # for each update, get the file id if it exists
            files = []
            for i in response.json()['result']:
                try:
                    files.append(i['message']['reply_to_message']['document']['file_id'])
                except KeyError:
                    pass
            # for each update, get the file id if it exists
            for i in response.json()['result']:
                try:
                    files.append(i['message']['document']['file_id'])
                except KeyError:
                    pass
            # call the remove_file_duplicates function to remove duplicate ids
            files = self.remove_file_duplicates(files)
            # for each file id, send a request to the telegram bot api to get the file path and store it in a list
            file_paths = []
            for i in files:
                response = requests.get('https://api.telegram.org/bot{}/getFile?file_id={}'.format(self.token, i))
                file_paths.append(response.json()['result']['file_path'])
            # return the file paths
            return file_paths

# class to resolve a telegram username and get data
class TelegramUser:
    # function to initialize the class
    def __init__(self, username):
        # set the username
        self.username = username

    # function to resolve a telegram username
    def resolv_user(self):
        # setup telegram session
        client = TelegramClient('natsar', telegram_app_id, telegram_app_hash)
        client.start()
        # Use telegram client to get user info with get_entity
        resolvedData = client.get_entity(self.username)
        # Disconnect the client and return the user info
        client.disconnect()
        return resolvedData